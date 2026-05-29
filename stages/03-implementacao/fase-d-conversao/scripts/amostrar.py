# -*- coding: utf-8 -*-
"""Extrai amostras de post_content de artigos para inspecao manual."""
import sys, re
from xml.etree import ElementTree as ET

NS = {"wp": "http://wordpress.org/export/1.2/",
      "content": "http://purl.org/rss/1.0/modules/content/"}


def carregar_root(path):
    with open(path, "rb") as fh:
        raw = fh.read()
    idx = raw.find(b"<?xml")
    if idx > 0:
        raw = raw[idx:]
    return ET.fromstring(raw)


def main(path, needle=None, n=2):
    root = carregar_root(path)
    channel = root.find("channel")
    arts = []
    for item in channel.findall("item"):
        if item.findtext("wp:post_type", "", NS) != "kbe_knowledgebase":
            continue
        c = item.findtext("content:encoded", "", NS) or ""
        t = item.findtext("title", "") or ""
        arts.append((t, c))
    if needle:
        arts = [a for a in arts if needle in a[1]]
    for t, c in arts[:n]:
        print("=" * 80)
        print("TITULO:", t)
        print("-" * 80)
        print(c[:3000])
        print()


if __name__ == "__main__":
    path = sys.argv[1]
    needle = sys.argv[2] if len(sys.argv) > 2 else None
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 2
    main(path, needle, n)
