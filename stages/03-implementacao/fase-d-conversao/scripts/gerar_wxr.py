# -*- coding: utf-8 -*-
"""
Gera o WXR convertido (Fase D): substitui o post_content dos 139 kbe_knowledgebase
pelo block markup Gutenberg, preservando CDATA e TODA a estrutura do export
(attachments, termos, postmeta, autores). Faz substituicao textual cirurgica —
nao reserializa via ElementTree, que destruiria CDATA e a ordem dos namespaces.

Uso:
    python gerar_wxr.py <wxr_entrada> <wxr_saida> [relatorio.md]
"""
import sys, re
from collections import Counter
from converter import html_para_blocos

RE_ITEM = re.compile(r"<item>.*?</item>", re.DOTALL)
RE_CONTENT = re.compile(
    r"(<content:encoded><!\[CDATA\[)(.*?)(\]\]></content:encoded>)", re.DOTALL)
RE_TITLE = re.compile(r"<title>(.*?)</title>", re.DOTALL)
RE_PID = re.compile(r"<wp:post_id>(\d+)</wp:post_id>")


def main(entrada, saida, relatorio=None):
    raw = open(entrada, "rb").read()
    idx = raw.find(b"<?xml")
    prefixo = raw[:idx] if idx > 0 else b""  # lixo antes da declaracao (descartado)
    text = raw[idx:].decode("utf-8")

    stats = {"convertidos": 0, "blocos": Counter(), "fallback": [], "vazios": 0}

    def repl_item(m):
        item = m.group(0)
        if "<![CDATA[kbe_knowledgebase]]>" not in item:
            return item
        cm = RE_CONTENT.search(item)
        if not cm:
            return item
        original = cm.group(2)
        convertido = html_para_blocos(original)
        if not convertido.strip():
            stats["vazios"] += 1
        # seguranca CDATA: quebra qualquer ]]> embutido
        convertido_cdata = convertido.replace("]]>", "]]]]><![CDATA[>")
        stats["convertidos"] += 1
        stats["blocos"].update(re.findall(r"<!-- wp:([a-z-]+)", convertido))
        if "<!-- wp:html" in convertido:
            pid = RE_PID.search(item)
            tit = RE_TITLE.search(item)
            stats["fallback"].append((
                pid.group(1) if pid else "?",
                (tit.group(1) if tit else "").strip(),
                convertido.count("<!-- wp:html"),
            ))
        novo = cm.group(1) + convertido_cdata + cm.group(3)
        return item[:cm.start()] + novo + item[cm.end():]

    out = RE_ITEM.sub(repl_item, text)
    with open(saida, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(out)

    print(f"Artigos convertidos: {stats['convertidos']}")
    print(f"Corpos vazios apos conversao: {stats['vazios']}")
    print(f"WXR salvo em: {saida}")

    if relatorio:
        escrever_relatorio(relatorio, stats, entrada, saida)
        print(f"Relatorio salvo em: {relatorio}")


def escrever_relatorio(path, stats, entrada, saida):
    import os
    linhas = []
    linhas.append("# Relatório de conversão — Fase D (SiteOrigin → Gutenberg)\n")
    linhas.append("> Gerado automaticamente por `scripts/gerar_wxr.py`.\n")
    linhas.append("## Resumo\n")
    linhas.append(f"- **Entrada:** `{os.path.basename(entrada)}`")
    linhas.append(f"- **Saída:** `{os.path.basename(saida)}`")
    linhas.append(f"- **Artigos convertidos:** {stats['convertidos']}")
    linhas.append(f"- **Corpos vazios após conversão:** {stats['vazios']}")
    linhas.append("")
    linhas.append("## Distribuição de blocos gerados\n")
    linhas.append("| Bloco | Ocorrências |")
    linhas.append("|---|---|")
    for k, v in stats["blocos"].most_common():
        linhas.append(f"| `wp:{k}` | {v} |")
    linhas.append("")
    linhas.append("## Artigos com fallback `wp:html` (revisar na curadoria — Fase G)\n")
    linhas.append("Conteúdo estrutural (callouts estilizados, listas aninhadas/malformadas) "
                  "preservado como HTML editável. Renderiza correto; a curadoria converte "
                  "em blocos editoriais quando for revisar.\n")
    linhas.append("| post_id | Título | Ocorrências |")
    linhas.append("|---|---|---|")
    for pid, tit, n in sorted(stats["fallback"], key=lambda x: -x[2]):
        linhas.append(f"| {pid} | {tit[:70]} | {n} |")
    linhas.append("")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(linhas))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
