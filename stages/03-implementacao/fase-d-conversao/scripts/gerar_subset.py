# -*- coding: utf-8 -*-
"""
Gera um WXR reduzido com apenas os artigos cujos post_id forem passados, mantendo
o cabecalho do channel (autores, termos) e o rodape. Preserva CDATA — trabalha no
texto bruto, sem reserializar.

Uso:
    python gerar_subset.py <wxr_completo> <wxr_subset> <id1> <id2> ...
    python gerar_subset.py <wxr_completo> <wxr_subset> --map-to=cgte_base <id1> ...

--map-to troca o post_type dos artigos (mapeamento kbe_knowledgebase -> cgte_base
da Fase E), necessario para que o DESTINO-LOCAL exiba os posts no admin.
"""
import sys, re

RE_ITEM = re.compile(r"[ \t]*<item>.*?</item>\s*", re.DOTALL)
RE_PID = re.compile(r"<wp:post_id>(\d+)</wp:post_id>")


def main(entrada, saida, ids, map_to=None, strip_terms=False):
    ids = set(ids)
    raw = open(entrada, "rb").read()
    idx = raw.find(b"<?xml")
    text = raw[idx:].decode("utf-8")

    primeiro = text.find("<item>")
    header = text[:primeiro]
    # rodape: tudo apos o ultimo </item>
    ultimo = text.rfind("</item>") + len("</item>")
    rodape = text[ultimo:]

    if strip_terms:
        # remove definicoes de taxonomia da base antiga (irrelevantes p/ teste de corpo;
        # poluiriam o banco com termos orfaos). Mantem wp:author.
        antes = len(header)
        for tag in ("wp:term", "wp:category", "wp:tag"):
            header = re.sub(rf"[ \t]*<{tag}>.*?</{tag}>\s*", "", header, flags=re.DOTALL)
        print(f"  header: removidas definicoes de termos ({antes-len(header)} bytes)")

    mantidos = []
    autores_usados = set()
    for m in RE_ITEM.finditer(text):
        item = m.group(0)
        pid = RE_PID.search(item)
        if pid and pid.group(1) in ids:
            if map_to:
                item = item.replace(
                    "<wp:post_type><![CDATA[kbe_knowledgebase]]></wp:post_type>",
                    f"<wp:post_type><![CDATA[{map_to}]]></wp:post_type>")
            for cr in re.findall(r"<dc:creator><!\[CDATA\[(.*?)\]\]></dc:creator>", item):
                autores_usados.add(cr)
            mantidos.append(item)

    # poda os wp:author do header para so os referenciados pelos artigos mantidos
    def manter_autor(m):
        login = re.search(r"<wp:author_login><!\[CDATA\[(.*?)\]\]>", m.group(0))
        return m.group(0) if (login and login.group(1) in autores_usados) else ""
    header, n_autor = re.subn(r"[ \t]*<wp:author>.*?</wp:author>\s*", manter_autor,
                              header, flags=re.DOTALL)
    print(f"  header: autores mantidos = {sorted(autores_usados)}")

    out = header + "".join(mantidos) + rodape
    with open(saida, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(out)
    print(f"Subset com {len(mantidos)} artigos salvo em: {saida}")
    for it in mantidos:
        t = re.search(r"<title>(.*?)</title>", it, re.DOTALL)
        p = RE_PID.search(it)
        print(f"  #{p.group(1)} {t.group(1)[:60] if t else ''}")


if __name__ == "__main__":
    args = sys.argv[3:]
    map_to = None
    strip_terms = False
    rest = []
    for a in args:
        if a.startswith("--map-to="):
            map_to = a.split("=", 1)[1]
        elif a == "--strip-terms":
            strip_terms = True
        else:
            rest.append(a)
    main(sys.argv[1], sys.argv[2], rest, map_to, strip_terms)
