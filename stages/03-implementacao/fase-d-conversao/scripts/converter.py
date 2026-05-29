# -*- coding: utf-8 -*-
"""
Conversor SiteOrigin -> Gutenberg (Fase D do roadmap de migracao).

DESCOBERTA (2026-05-29): o corpo dos 139 artigos NAO usa SiteOrigin — e HTML
classico TinyMCE com paragrafos implicitos. Este conversor transforma esse HTML
em block markup Gutenberg (blocos core), de minima friccao, sem reescrita.

Pipeline:
    post_content (HTML classico)
      -> normalizar shortcodes ([caption], [embed], [display-posts], [libras])
      -> wpautop (inserir <p> em paragrafos implicitos)
      -> tokenizar elementos de nivel superior
      -> mapear cada elemento para um bloco Gutenberg
      -> serializar block markup

Uso como modulo:
    from converter import html_para_blocos
    blocos = html_para_blocos(post_content)
"""
import re
from html.parser import HTMLParser

# ---------------------------------------------------------------------------
# 1. wpautop — porta pragmatica da funcao do WordPress (formatting.php)
# ---------------------------------------------------------------------------

# Tags de nivel de bloco que NAO devem ser envolvidas em <p>.
BLOCKS = ("table|thead|tfoot|caption|col|colgroup|tbody|tr|td|th|div|dl|dd|dt|"
          "ul|ol|li|pre|form|map|area|address|math|style|p|h1|h2|h3|h4|h5|h6|"
          "fieldset|legend|section|article|aside|hgroup|header|footer|nav|"
          "figure|figcaption|details|menu|summary|blockquote|option|object|"
          "audio|video|embed|script|noscript|select|hr|iframe")


def wpautop(pee, br=True):
    """Replica o comportamento essencial de wpautop() do WordPress."""
    if pee.strip() == "":
        return ""
    pee = pee + "\n"

    # protege conteudo de <pre>
    pre_tags = {}
    if "<pre" in pee:
        parts = pee.split("</pre>")
        last = parts.pop()
        out = ""
        for i, part in enumerate(parts):
            start = part.find("<pre")
            if start == -1:
                out += part
                continue
            name = f"<pre wp-pre-tag-{i}></pre>"
            pre_tags[name] = part[start:] + "</pre>"
            out += part[:start] + name
        pee = out + last

    pee = re.sub(r"<br\s*/?>\s*<br\s*/?>", "\n\n", pee)
    # adiciona quebras duplas ao redor de blocos
    pee = re.sub(r"(<(?:" + BLOCKS + r")(?: [^>]*)?>)", r"\n\n\1", pee)
    pee = re.sub(r"(</(?:" + BLOCKS + r")>)", r"\1\n\n", pee)
    pee = pee.replace("\r\n", "\n").replace("\r", "\n")

    # <option>/<object> nao devem quebrar — simplificado, ignoramos aqui.
    pee = re.sub(r"\n\n+", "\n\n", pee)

    # divide em paragrafos
    pees = re.split(r"\n\s*\n", pee)
    pee = ""
    for tinkle in pees:
        if tinkle.strip():
            pee += "<p>" + tinkle.strip("\n") + "</p>\n"

    # remove <p> vazios
    pee = re.sub(r"<p>\s*</p>", "", pee)
    # nao envolver blocos em <p>: tira <p> antes de tag de bloco de abertura
    pee = re.sub(r"<p>\s*(</?(?:" + BLOCKS + r")[^>]*>)", r"\1", pee)
    pee = re.sub(r"(</?(?:" + BLOCKS + r")[^>]*>)\s*</p>", r"\1", pee)

    if br:
        # converte \n simples dentro de paragrafos em <br>
        def _autobr(m):
            return m.group(0).replace("\n", "<br />\n")
        # so dentro de <p>...</p>
        def repl(m):
            inner = m.group(1)
            inner = inner.replace("\n", "<br />\n")
            return "<p>" + inner + "</p>"
        pee = re.sub(r"<p>(.*?)</p>", repl, pee, flags=re.DOTALL)

    # remove <br> imediatamente antes de fechamento de bloco
    pee = re.sub(r"<br />\s*(</?(?:" + BLOCKS + r")[^>]*>)", r"\1", pee)

    # restaura <pre>
    for name, original in pre_tags.items():
        pee = pee.replace(name, original)

    return pee.strip()


# ---------------------------------------------------------------------------
# 2. Normalizacao de shortcodes
# ---------------------------------------------------------------------------

RE_CAPTION = re.compile(
    r"\[caption[^\]]*\](.*?)\[/caption\]", re.DOTALL | re.IGNORECASE)
RE_EMBED = re.compile(
    r"\[embed[^\]]*\]\s*(.*?)\s*\[/embed\]", re.DOTALL | re.IGNORECASE)
RE_SC_AUTONOMO = re.compile(r"\[(display-posts|libras)([^\]]*)\]", re.IGNORECASE)

# Placeholder atomico: caractere de controle que o wpautop nao fragmenta.
PH_OPEN, PH_CLOSE = chr(1), chr(2)
RE_PLACEHOLDER = re.compile(PH_OPEN + r"(\d+)" + PH_CLOSE)


def normalizar_shortcodes(html, store):
    """Troca shortcodes por placeholders atomicos; o bloco final fica em `store`.

    Cada placeholder vira um paragrafo isolado pos-wpautop e e expandido no fim
    para o bloco Gutenberg correto (wp:image / wp:embed / wp:shortcode).
    """
    def _guardar(bloco):
        idx = len(store)
        store.append(bloco)
        return f"\n\n{PH_OPEN}{idx}{PH_CLOSE}\n\n"

    def cap(m):
        inner = m.group(1).strip()
        img_m = re.search(r"<img[^>]*>", inner, re.IGNORECASE)
        img = img_m.group(0) if img_m else ""
        legenda = inner[img_m.end():].strip() if img_m else inner
        return _guardar(_converter_imagem(img, legenda or None))
    html = RE_CAPTION.sub(cap, html)

    def emb(m):
        url = m.group(1).strip()
        return _guardar(_bloco_embed(url))
    html = RE_EMBED.sub(emb, html)

    def sc(m):
        return _guardar(_block("shortcode", m.group(0)))
    html = RE_SC_AUTONOMO.sub(sc, html)
    return html


# ---------------------------------------------------------------------------
# 3. Tokenizador de nivel superior
# ---------------------------------------------------------------------------

VOID = {"img", "br", "hr", "input", "meta", "link", "source", "area", "col", "embed"}


class TopLevelTokenizer(HTMLParser):
    """Quebra HTML em fragmentos de nivel superior (depth 0)."""

    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tokens = []          # lista de (tipo, conteudo)
        self.depth = 0
        self.buffer = ""
        self.current_tag = None

    def _flush_text(self, text):
        if self.depth == 0:
            # texto solto no topo
            if text.strip():
                self.tokens.append(("text", text))
        else:
            self.buffer += text

    def handle_starttag(self, tag, attrs):
        full = self.get_starttag_text()
        if self.depth == 0:
            self.current_tag = tag
            self.buffer = full
            if tag in VOID:
                self.tokens.append(("el", self.buffer, tag))
                self.buffer = ""
                self.current_tag = None
            else:
                self.depth = 1
        else:
            self.buffer += full
            if tag not in VOID:
                self.depth += 1

    def handle_startendtag(self, tag, attrs):
        full = self.get_starttag_text()
        if self.depth == 0:
            self.tokens.append(("el", full, tag))
        else:
            self.buffer += full

    def handle_endtag(self, tag):
        if self.depth == 0:
            return  # fechamento orfao no topo — ignora
        self.buffer += f"</{tag}>"
        self.depth -= 1
        if self.depth == 0:
            self.tokens.append(("el", self.buffer, self.current_tag))
            self.buffer = ""
            self.current_tag = None

    def handle_data(self, data):
        self._flush_text(data)

    def handle_entityref(self, name):
        self._flush_text(f"&{name};")

    def handle_charref(self, name):
        self._flush_text(f"&#{name};")

    def handle_comment(self, data):
        if self.depth > 0:
            self.buffer += f"<!--{data}-->"


def tokenizar(html):
    p = TopLevelTokenizer()
    p.feed(html)
    p.close()
    return p.tokens


# ---------------------------------------------------------------------------
# 4. Mapeamento elemento -> block markup
# ---------------------------------------------------------------------------

def _block(name, html_inner, attrs=None):
    attr_json = ""
    if attrs:
        import json
        attr_json = " " + json.dumps(attrs, separators=(",", ":"), ensure_ascii=False)
    return f"<!-- wp:{name}{attr_json} -->\n{html_inner}\n<!-- /wp:{name} -->"


def _converter_lista(el_html, ordered):
    """Converte <ul>/<ol> para wp:list com wp:list-item aninhados (WP 6.8).

    Listas aninhadas ou malformadas caem em wp:html (sempre valido) — o Gutenberg
    nao valida wp:html, evitando bloco semantico quebrado. Curadoria refina (DP-7).
    """
    inner = re.sub(r"^\s*<[ou]l[^>]*>|</[ou]l>\s*$", "", el_html.strip(),
                   flags=re.IGNORECASE)
    # aninhamento -> fallback seguro
    if re.search(r"<(ul|ol)\b", inner, re.IGNORECASE):
        return _block("html", el_html.strip())
    itens = re.findall(r"<li[^>]*>(.*?)</li>", inner, re.DOTALL | re.IGNORECASE)
    # se a extracao nao bate com o numero de <li> de abertura, ha malformacao
    if len(itens) != len(re.findall(r"<li\b", inner, re.IGNORECASE)):
        return _block("html", el_html.strip())
    li_blocks = []
    for it in itens:
        # remove <p>/</p> orfaos dentro do item (lixo do editor legado)
        it = re.sub(r"</?p\b[^>]*>", "", it).strip()
        li_blocks.append(f"<!-- wp:list-item -->\n<li>{it}</li>\n<!-- /wp:list-item -->")
    tag = "ol" if ordered else "ul"
    cls = ' class="wp-block-list"'
    inner_blocks = "\n".join(li_blocks)
    attrs = {"ordered": True} if ordered else None
    body = f"<{tag}{cls}>\n{inner_blocks}\n</{tag}>"
    return _block("list", body, attrs)


def _converter_imagem(img_html, caption=None):
    # extrai id da classe wp-image-NNN se houver
    m = re.search(r"wp-image-(\d+)", img_html)
    attrs = {}
    if m:
        attrs["id"] = int(m.group(1))
    attrs["sizeSlug"] = "full"
    fig_inner = img_html
    if caption:
        fig_inner += f"<figcaption class=\"wp-element-caption\">{caption}</figcaption>"
    body = f'<figure class="wp-block-image size-full">{fig_inner}</figure>'
    return _block("image", body, attrs)


def _converter_embed_youtube(url):
    attrs = {
        "url": url, "type": "video", "providerNameSlug": "youtube",
        "responsive": True,
        "className": "wp-embed-aspect-16-9 wp-has-aspect-ratio",
    }
    body = ('<figure class="wp-block-embed is-type-video is-provider-youtube '
            'wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio">'
            '<div class="wp-block-embed__wrapper">\n' + url +
            '\n</div></figure>')
    return _block("embed", body, attrs)


RE_YT = re.compile(r"(?:youtube\.com/(?:embed/|watch\?v=)|youtu\.be/)([\w-]+)")


def _bloco_embed(url):
    """Decide entre embed YouTube e embed generico a partir da URL."""
    m = RE_YT.search(url)
    if m:
        return _converter_embed_youtube(f"https://www.youtube.com/watch?v={m.group(1)}")
    return _block("embed", url + "\n", {"url": url})


def _iframe_para_bloco(el_html):
    src = re.search(r'src="([^"]+)"', el_html)
    if src and "youtube" in src.group(1):
        return _bloco_embed(src.group(1))
    # outros iframes -> wp:html
    return _block("html", el_html)


# tags de bloco que, se presentes dentro de um <div>, impedem trata-lo como paragrafo
RE_BLOCO_INTERNO = re.compile(
    r"<(div|p|h[1-6]|ul|ol|table|figure|blockquote|pre|hr|iframe|section|article)\b",
    re.IGNORECASE)


def _converter_div(html):
    """<div> de conteudo inline vira paragrafo; <div><img> vira imagem.

    Artigos recentes usam <div> por paragrafo no lugar de <p>. Sem isto cairiam
    no fallback wp:html (nao-editaveis na curadoria).
    """
    inner = re.sub(r"^\s*<div[^>]*>|</div>\s*$", "", html.strip(),
                   flags=re.IGNORECASE).strip()
    if not inner:
        return None
    # div que e essencialmente uma unica imagem
    if re.fullmatch(r"<img[^>]*>", inner, re.IGNORECASE):
        return _converter_imagem(inner)
    # div sem blocos aninhados -> paragrafo (placeholders \x01..\x02 sao resolvidos depois)
    if not RE_BLOCO_INTERNO.search(inner) and "<img" not in inner.lower():
        return _block("paragraph", f"<p>{inner}</p>")
    # tem estrutura interna -> fallback seguro
    return _block("html", html.strip())


def elemento_para_bloco(token):
    tipo = token[0]
    if tipo == "text":
        texto = token[1].strip()
        if not texto:
            return None
        return _block("paragraph", f"<p>{texto}</p>")

    html = token[1]
    tag = token[2].lower()

    # marcadores de embed/shortcode podem aparecer como texto — tratados antes.
    if tag in ("p",):
        inner = html.strip()
        # paragrafo que e so um marcador __EMBED__ ou __SHORTCODE__
        return _block("paragraph", inner)
    if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
        level = int(tag[1])
        attrs = None if level == 2 else {"level": level}
        return _block("heading", html.strip(), attrs)
    if tag == "ul":
        return _converter_lista(html, ordered=False)
    if tag == "ol":
        return _converter_lista(html, ordered=True)
    if tag == "img":
        return _converter_imagem(html.strip())
    if tag == "div":
        return _converter_div(html)
    if tag == "figure":
        return _block("html", html.strip())
    if tag == "iframe":
        return _iframe_para_bloco(html)
    if tag == "hr":
        return _block("separator",
                      '<hr class="wp-block-separator has-alpha-channel-opacity"/>')
    if tag == "blockquote":
        inner = re.sub(r"^\s*<blockquote[^>]*>|</blockquote>\s*$", "", html.strip(),
                       flags=re.IGNORECASE)
        body = f'<blockquote class="wp-block-quote">{inner}</blockquote>'
        return _block("quote", body)
    if tag == "li":
        # <li> orfao no topo (lista malformada no legado) -> html seguro
        return _block("html", html.strip())
    if tag == "pre":
        return _block("preformatted", html.strip())
    if tag == "table":
        body = f'<figure class="wp-block-table">{html.strip()}</figure>'
        return _block("table", body)
    # fallback
    return _block("html", html.strip())


# ---------------------------------------------------------------------------
# 5. Pipeline completo
# ---------------------------------------------------------------------------

def _resolver_placeholders(texto, store):
    """Expande os placeholders atomicos pelos blocos guardados em `store`.

    O placeholder, isolado pos-wpautop, vira `<!-- wp:paragraph --><p>PH</p>...`;
    trocamos o paragrafo inteiro pelo bloco real (imagem/embed/shortcode).
    """
    def envolto(m):
        return store[int(m.group(1))]
    # paragrafo que contem APENAS o placeholder
    texto = re.sub(
        r"<!-- wp:paragraph -->\s*<p>\s*" + PH_OPEN + r"(\d+)" + PH_CLOSE +
        r"\s*</p>\s*<!-- /wp:paragraph -->",
        envolto, texto)
    # qualquer placeholder remanescente (ex.: dentro de outro bloco)
    texto = RE_PLACEHOLDER.sub(envolto, texto)
    return texto


def _prelimpeza(html):
    """Remove lixo do HTML legado que o TinyMCE tolerava e o Gutenberg rejeita."""
    html = re.sub(r"</\s*br\s*>", "", html)        # </br> nao existe
    html = re.sub(r"<\s*br\s*>", "<br/>", html)     # <br> -> <br/>
    return html


def html_para_blocos(post_content):
    if not post_content or not post_content.strip():
        return ""
    store = []
    post_content = _prelimpeza(post_content)
    etapa = normalizar_shortcodes(post_content, store)
    etapa = wpautop(etapa, br=False)
    tokens = tokenizar(etapa)
    blocos = []
    for tk in tokens:
        b = elemento_para_bloco(tk)
        if b:
            blocos.append(b)
    saida = "\n\n".join(blocos)
    saida = _resolver_placeholders(saida, store)
    return saida


if __name__ == "__main__":
    import sys
    exemplo = sys.stdin.read()
    print(html_para_blocos(exemplo))
