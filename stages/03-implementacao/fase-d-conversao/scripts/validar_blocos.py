# -*- coding: utf-8 -*-
"""
Validacao a seco (sem tocar o banco) do block markup gerado.

Checa, para o corpo de cada kbe_knowledgebase do WXR:
  1. Gramatica: cada `<!-- wp:NAME -->` tem seu `<!-- /wp:NAME -->` na ordem certa
     (pilha balanceada; sem delimitador orfao).
  2. Atributos: o JSON apos o nome do bloco parseia.
  3. HTML: o conteudo de cada bloco e bem-formado (tags balanceadas).

NAO valida a semantica `isValid` de cada bloco core (isso o editor faz ao abrir) —
valida o que e deterministico e garante import sem markup quebrado.

Uso: python validar_blocos.py <wxr>
"""
import sys, re, json
from html.parser import HTMLParser
from xml.etree import ElementTree as ET

NS = {"wp": "http://wordpress.org/export/1.2/",
      "content": "http://purl.org/rss/1.0/modules/content/"}

RE_BLOCO = re.compile(r"<!--\s*(/?)wp:([a-z][a-z0-9-]*)\s*(\{.*?\})?\s*(/?)-->", re.DOTALL)
VOID = {"img", "br", "hr", "input", "meta", "link", "source", "area", "col", "embed", "wbr"}


def carregar(path):
    raw = open(path, "rb").read()
    root = ET.fromstring(raw[raw.find(b"<?xml"):])
    arts = []
    for it in root.find("channel").findall("item"):
        if it.findtext("wp:post_type", "", NS) != "kbe_knowledgebase":
            continue
        arts.append((it.findtext("wp:post_id", "", NS),
                     it.findtext("title", "") or "",
                     it.findtext("content:encoded", "", NS) or ""))
    return arts


def validar_gramatica(content):
    erros = []
    pilha = []
    for m in RE_BLOCO.finditer(content):
        fechamento, nome, attrs, selfclose = m.group(1), m.group(2), m.group(3), m.group(4)
        if selfclose:           # <!-- wp:x /--> bloco void, nao empilha
            continue
        if fechamento:          # <!-- /wp:x -->
            if not pilha:
                erros.append(f"fechamento orfao wp:{nome}")
            elif pilha[-1] != nome:
                erros.append(f"esperava /wp:{pilha[-1]}, veio /wp:{nome}")
                pilha.pop()
            else:
                pilha.pop()
        else:                   # abertura
            pilha.append(nome)
    if pilha:
        erros.append(f"blocos sem fechamento: {pilha}")
    return erros


def validar_json(content):
    erros = []
    for m in RE_BLOCO.finditer(content):
        attrs = m.group(3)
        if attrs:
            try:
                json.loads(attrs)
            except Exception as e:
                erros.append(f"JSON invalido em wp:{m.group(2)}: {e}")
    return erros


class HTMLChecker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.pilha = []
        self.erros = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.pilha.append(tag)

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if tag in self.pilha:
            # fecha ate o tag (tolera fechamentos implicitos como <li>/<p>)
            while self.pilha and self.pilha[-1] != tag:
                self.pilha.pop()
            if self.pilha:
                self.pilha.pop()
        # endtag sem abertura: ignora (tolerante)


# blocos cujo conteudo o Gutenberg NAO valida (renderiza cru) — pular na checagem HTML
RE_HTML_CRU = re.compile(
    r"<!--\s*wp:(html|freeform)\s*-->.*?<!--\s*/wp:\1\s*-->", re.DOTALL)

RE_PARA_BLOCO = re.compile(
    r"<!--\s*wp:paragraph(\s+\{.*?\})?\s*-->\s*(.*?)\s*<!--\s*/wp:paragraph\s*-->",
    re.DOTALL)
RE_HEAD_BLOCO = re.compile(
    r"<!--\s*wp:heading(\s+\{.*?\})?\s*-->\s*(.*?)\s*<!--\s*/wp:heading\s*-->",
    re.DOTALL)


def validar_tag_externa(content):
    """O Gutenberg compara a tag EXTERNA de wp:paragraph/wp:heading com o que
    save() geraria: atributos legados (style/class/id/align/data-*) marcam o
    bloco como invalido no editor. Conteudo interno (rich text) faz round-trip
    e nao precisa ser checado. Classe de bug encontrada em 2026-06-11 (25/139)."""
    erros = []
    sem_cru = RE_HTML_CRU.sub("", content)
    for m in RE_PARA_BLOCO.finditer(sem_cru):
        attrs_json, body = m.group(1) or "", m.group(2)
        abre = re.match(r"<p(\s[^>]*)?>", body)
        if not abre:
            erros.append(f"wp:paragraph sem <p> de abertura: {body[:50]!r}")
            continue
        extra = abre.group(1)
        if extra:
            al = re.fullmatch(r'\sclass="has-text-align-(\w+)"', extra)
            if not (al and f'"align":"{al.group(1)}"' in attrs_json):
                erros.append(f"wp:paragraph com atributos na tag externa: {abre.group(0)[:70]!r}")
    for m in RE_HEAD_BLOCO.finditer(sem_cru):
        abre = re.match(r"<h[1-6](\s[^>]*)?>", m.group(2))
        if abre and abre.group(1):
            resto = re.sub(r'\s(class="wp-block-heading[^"]*"|id="[^"]*")', "", abre.group(1))
            if resto.strip():
                erros.append(f"wp:heading com atributos na tag externa: {abre.group(0)[:70]!r}")
    return erros


def validar_html(content):
    # remove blocos de HTML cru (nao validados pelo Gutenberg) e os comentarios de bloco
    content = RE_HTML_CRU.sub("", content)
    html_only = RE_BLOCO.sub("", content)
    c = HTMLChecker()
    try:
        c.feed(html_only)
        c.close()
    except Exception as e:
        return [f"parse HTML falhou: {e}"]
    # tags estruturais que NAO podem ficar abertas
    estruturais = [t for t in c.pilha if t in
                   ("p", "ul", "ol", "li", "figure", "blockquote", "table",
                    "h1", "h2", "h3", "h4", "h5", "h6", "div", "pre")]
    if estruturais:
        return [f"tags estruturais nao fechadas: {estruturais}"]
    return []


def main(path):
    arts = carregar(path)
    total_erros = 0
    artigos_com_erro = 0
    for pid, tit, content in arts:
        erros = []
        erros += validar_gramatica(content)
        erros += validar_json(content)
        erros += validar_html(content)
        erros += validar_tag_externa(content)
        if erros:
            artigos_com_erro += 1
            total_erros += len(erros)
            print(f"#{pid} {tit[:55]}")
            for e in erros:
                print(f"    - {e}")
    print()
    print(f"Artigos validados: {len(arts)}")
    print(f"Artigos com problema: {artigos_com_erro}")
    print(f"Total de problemas: {total_erros}")
    if artigos_com_erro == 0:
        print("\nOK — gramatica balanceada, JSON valido e HTML bem-formado em todos.")


if __name__ == "__main__":
    main(sys.argv[1])
