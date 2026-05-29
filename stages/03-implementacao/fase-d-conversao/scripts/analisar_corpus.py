# -*- coding: utf-8 -*-
"""
Analisa o WXR da base antiga e caracteriza o corpo dos 139 artigos kbe_knowledgebase.
Objetivo (Fase D): descobrir o que realmente vive no post_content antes de projetar
o conversor SiteOrigin -> Gutenberg.

Uso:
    python analisar_corpus.py "<caminho do .xml>"
"""
import sys
import re
import html
from collections import Counter
from xml.etree import ElementTree as ET

NS = {
    "wp": "http://wordpress.org/export/1.2/",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "excerpt": "http://wordpress.org/export/1.2/excerpt/",
    "dc": "http://purl.org/dc/elements/1.1/",
}


def carregar_root(path):
    """Le o WXR tolerando lixo (linhas em branco / BOM) antes da declaracao <?xml."""
    with open(path, "rb") as fh:
        raw = fh.read()
    # remove BOM e qualquer coisa antes da declaracao xml
    idx = raw.find(b"<?xml")
    if idx > 0:
        raw = raw[idx:]
    return ET.fromstring(raw)


def main(path):
    root = carregar_root(path)
    channel = root.find("channel")

    artigos = []
    for item in channel.findall("item"):
        ptype = item.findtext("wp:post_type", default="", namespaces=NS)
        if ptype != "kbe_knowledgebase":
            continue
        title = item.findtext("title", default="") or ""
        status = item.findtext("wp:status", default="", namespaces=NS)
        post_id = item.findtext("wp:post_id", default="", namespaces=NS)
        content = item.findtext("content:encoded", default="", namespaces=NS) or ""
        # postmeta
        metas = {}
        for pm in item.findall("wp:postmeta", NS):
            k = pm.findtext("wp:meta_key", default="", namespaces=NS)
            v = pm.findtext("wp:meta_value", default="", namespaces=NS) or ""
            metas[k] = v
        artigos.append({
            "id": post_id, "title": title, "status": status,
            "content": content, "metas": metas,
        })

    print(f"Total kbe_knowledgebase: {len(artigos)}\n")

    # status
    st = Counter(a["status"] for a in artigos)
    print("== Status ==")
    for k, v in st.most_common():
        print(f"  {k:20} {v}")
    print()

    # SiteOrigin / panels_data
    com_panels = [a for a in artigos if a["metas"].get("panels_data")]
    com_so_shortcode = [a for a in artigos if "siteorigin_widget" in a["content"]]
    print("== SiteOrigin ==")
    print(f"  com postmeta panels_data: {len(com_panels)}")
    print(f"  com shortcode siteorigin_widget no content: {len(com_so_shortcode)}")
    print()

    # tamanho do content
    vazios = [a for a in artigos if not a["content"].strip()]
    print(f"== Corpo vazio: {len(vazios)} ==")
    if vazios:
        for a in vazios[:10]:
            print(f"   #{a['id']} [{a['status']}] {a['title'][:60]}")
    print()

    # tags HTML usadas
    tag_counter = Counter()
    for a in artigos:
        for m in re.finditer(r"<\s*([a-zA-Z][a-zA-Z0-9]*)", a["content"]):
            tag_counter[m.group(1).lower()] += 1
    print("== Tags HTML no corpo (top 30) ==")
    for k, v in tag_counter.most_common(30):
        print(f"  {k:14} {v}")
    print()

    # shortcodes reais [foo ...] no content (exclui entidades e links)
    sc_counter = Counter()
    for a in artigos:
        # shortcodes: [palavra ...] ou [palavra]
        for m in re.finditer(r"\[/?([a-zA-Z][a-zA-Z0-9_-]*)[\s\]]", a["content"]):
            sc_counter[m.group(1).lower()] += 1
    print("== Possiveis shortcodes no corpo (top 30) ==")
    for k, v in sc_counter.most_common(30):
        print(f"  {k:24} {v}")
    print()

    # presenca de blocos Gutenberg ja
    com_gutenberg = [a for a in artigos if "<!-- wp:" in a["content"]]
    print(f"== Ja em blocos Gutenberg (<!-- wp:): {len(com_gutenberg)} ==\n")

    # imagens
    com_img = [a for a in artigos if "<img" in a["content"]]
    com_iframe = [a for a in artigos if "<iframe" in a["content"]]
    print(f"== Midia embutida ==")
    print(f"  com <img>: {len(com_img)}")
    print(f"  com <iframe>: {len(com_iframe)}")
    print()


if __name__ == "__main__":
    main(sys.argv[1])
