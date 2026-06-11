#!/usr/bin/env python3
"""
Fase C — QA da extração: cruza os anexos do WXR com a pasta uploads extraída.

Confere que toda URL de attachment (<wp:attachment_url>) e toda URL
wp-content/uploads referenciada nos corpos dos artigos existe como arquivo
na pasta extraída.

Uso:
    python verificar_uploads.py WXR.xml PASTA_EXTRAIDA/uploads
"""

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

# Exclui ']' para não engolir o terminador ']]>' quando a URL fecha um CDATA.
PADRAO_UPLOADS = re.compile(r"https?://[^\s\"'<>\]]+?/wp-content/uploads/([^\s\"'<>?#\]]+)")


def relativos_de(texto: str) -> set[str]:
    return {unquote(m.group(1)) for m in PADRAO_UPLOADS.finditer(texto)}


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 1
    wxr = Path(sys.argv[1])
    uploads = Path(sys.argv[2])

    raw = wxr.read_bytes()
    raw = raw[raw.find(b"<?xml") :]  # o WXR tem linhas em branco antes da declaração
    texto = raw.decode("utf-8", "replace")

    anexos = set()
    for m in re.finditer(r"<wp:attachment_url>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</wp:attachment_url>", texto):
        caminho = urlparse(m.group(1)).path
        marca = "/wp-content/uploads/"
        if marca in caminho:
            anexos.add(unquote(caminho.split(marca, 1)[1]))

    citados = relativos_de(texto)

    def conferir(nome: str, conjunto: set[str]) -> int:
        faltando = sorted(r for r in conjunto if not (uploads / r).is_file())
        print(f"{nome}: {len(conjunto)} URLs, {len(conjunto) - len(faltando)} encontradas, {len(faltando)} faltando")
        for r in faltando[:30]:
            print(f"  FALTA  {r}")
        if len(faltando) > 30:
            print(f"  ... e mais {len(faltando) - 30}")
        return len(faltando)

    problemas = conferir("attachments do WXR", anexos)
    problemas += conferir("uploads citados em corpos/metas", citados)
    print("\nOK — mídia extraída cobre o WXR." if problemas == 0 else f"\n{problemas} arquivos faltando.")
    return 0 if problemas == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
