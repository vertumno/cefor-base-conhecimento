# -*- coding: utf-8 -*-
"""Testa o conversor contra artigos reais do WXR."""
import sys
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
        arts.append((it.findtext("title", "") or "",
                     it.findtext("content:encoded", "", NS) or ""))
    return arts


def main(path, needle=None, n=1):
    arts = carregar(path)
    if needle:
        arts = [a for a in arts if needle in a[1]]
    for t, c in arts[:n]:
        print("#" * 80)
        print("ARTIGO:", t)
        print("#" * 80)
        out = html_para_blocos(c)
        print(out)
        print()


if __name__ == "__main__":
    path = sys.argv[1]
    needle = sys.argv[2] if len(sys.argv) > 2 else None
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    main(path, needle, n)
