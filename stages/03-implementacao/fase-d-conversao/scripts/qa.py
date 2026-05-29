# -*- coding: utf-8 -*-
"""Varredura de qualidade: converte os 139 e mede a distribuicao de blocos."""
import sys, re
from collections import Counter
from xml.etree import ElementTree as ET
from converter import html_para_blocos

NS = {"wp": "http://wordpress.org/export/1.2/",
      "content": "http://purl.org/rss/1.0/modules/content/"}


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


def main(path):
    arts = carregar(path)
    bloco_counter = Counter()
    html_fallback = []   # artigos com wp:html (revisar)
    orfaos = []          # placeholders nao resolvidos
    sem_blocos = []
    for pid, t, c in arts:
        out = html_para_blocos(c)
        tipos = re.findall(r"<!-- wp:([a-z-]+)", out)
        bloco_counter.update(tipos)
        if "wp:html" in out:
            n = out.count("<!-- wp:html")
            html_fallback.append((pid, t, n))
        if "\x01" in out or "\x02" in out:
            orfaos.append((pid, t))
        if not tipos:
            sem_blocos.append((pid, t))

    print(f"Artigos processados: {len(arts)}\n")
    print("== Distribuicao de blocos gerados ==")
    for k, v in bloco_counter.most_common():
        print(f"  wp:{k:14} {v}")
    print()
    print(f"== Artigos com fallback wp:html: {len(html_fallback)} ==")
    for pid, t, n in sorted(html_fallback, key=lambda x: -x[2])[:25]:
        print(f"  #{pid} ({n}x) {t[:60]}")
    print()
    print(f"== Placeholders orfaos: {len(orfaos)} ==")
    for pid, t in orfaos:
        print(f"  #{pid} {t[:60]}")
    print()
    print(f"== Artigos sem nenhum bloco: {len(sem_blocos)} ==")
    for pid, t in sem_blocos:
        print(f"  #{pid} {t[:60]}")


if __name__ == "__main__":
    main(sys.argv[1])
