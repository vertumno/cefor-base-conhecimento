#!/usr/bin/env python3
"""
Fase C — Extrator de arquivos .wpress (All-in-One WP Migration).

O .wpress é um container sequencial simples (não é TAR nem ZIP — por isso o
7-Zip não abre). Cada entrada tem um cabeçalho de 4377 bytes:

    offset    0, 255  bytes : nome do arquivo (null-padded)
    offset  255,  14  bytes : tamanho do conteúdo em bytes (string decimal)
    offset  269,  12  bytes : mtime unix (string decimal)
    offset  281, 4096 bytes : diretório (caminho relativo, null-padded)

Seguido do conteúdo cru do arquivo. O fim do container é um cabeçalho
inteiramente zerado (4377 bytes \x00).

Uso:
    python extrair_wpress.py ARQUIVO.wpress --listar
    python extrair_wpress.py ARQUIVO.wpress -o PASTA_DESTINO [--somente uploads]

Só stdlib. Referência do formato: plugin servmask/all-in-one-wp-migration
(lib/vendor/servmask/archiver).
"""

import argparse
import os
import sys
from collections import Counter
from pathlib import Path, PurePosixPath

TAM_NOME = 255
TAM_TAMANHO = 14
TAM_MTIME = 12
TAM_DIR = 4096
TAM_CABECALHO = TAM_NOME + TAM_TAMANHO + TAM_MTIME + TAM_DIR  # 4377
CABECALHO_FIM = b"\x00" * TAM_CABECALHO


def _campo(buf: bytes, inicio: int, tamanho: int) -> str:
    return buf[inicio : inicio + tamanho].split(b"\x00", 1)[0].decode("utf-8", "replace")


def iterar_entradas(caminho: Path):
    """Gera (caminho_relativo: PurePosixPath, tamanho: int, mtime: int, offset_conteudo: int)."""
    with open(caminho, "rb") as f:
        while True:
            cab = f.read(TAM_CABECALHO)
            if len(cab) < TAM_CABECALHO or cab == CABECALHO_FIM:
                return
            nome = _campo(cab, 0, TAM_NOME)
            tamanho = int(_campo(cab, TAM_NOME, TAM_TAMANHO) or "0")
            mtime = int(_campo(cab, TAM_NOME + TAM_TAMANHO, TAM_MTIME) or "0")
            diretorio = _campo(cab, TAM_NOME + TAM_TAMANHO + TAM_MTIME, TAM_DIR)
            # O .wpress grava o separador do SO de origem; normaliza para POSIX.
            relativo = PurePosixPath(diretorio.replace("\\", "/")) / nome if diretorio else PurePosixPath(nome)
            yield relativo, tamanho, mtime, f.tell()
            f.seek(tamanho, os.SEEK_CUR)


def caminho_seguro(destino: Path, relativo: PurePosixPath) -> Path:
    """Resolve o caminho de saída impedindo travessia (.., absoluto, drive)."""
    partes = [p for p in relativo.parts if p not in ("..", "/", "") and ":" not in p]
    alvo = destino.joinpath(*partes)
    if not alvo.resolve().is_relative_to(destino.resolve()):
        raise ValueError(f"caminho suspeito no container: {relativo}")
    return alvo


def listar(arquivo: Path) -> None:
    total = 0
    bytes_total = 0
    por_topo = Counter()
    bytes_topo = Counter()
    for relativo, tamanho, _mtime, _off in iterar_entradas(arquivo):
        total += 1
        bytes_total += tamanho
        topo = relativo.parts[0] if len(relativo.parts) > 1 else "(raiz)"
        por_topo[topo] += 1
        bytes_topo[topo] += tamanho
    print(f"{total} arquivos, {bytes_total / 1024 / 1024:.1f} MiB\n")
    print(f"{'pasta de topo':<30}{'arquivos':>10}{'MiB':>12}")
    for topo, qtd in por_topo.most_common():
        print(f"{topo:<30}{qtd:>10}{bytes_topo[topo] / 1024 / 1024:>12.1f}")


def extrair(arquivo: Path, destino: Path, somente: str | None) -> None:
    destino.mkdir(parents=True, exist_ok=True)
    extraidos = 0
    pulados = 0
    bytes_extraidos = 0
    with open(arquivo, "rb") as f:
        for relativo, tamanho, mtime, offset in iterar_entradas(arquivo):
            if somente and not str(relativo).startswith(somente):
                pulados += 1
                continue
            alvo = caminho_seguro(destino, relativo)
            alvo.parent.mkdir(parents=True, exist_ok=True)
            f.seek(offset)
            restante = tamanho
            with open(alvo, "wb") as saida:
                while restante > 0:
                    bloco = f.read(min(1024 * 1024, restante))
                    if not bloco:
                        raise EOFError(f"container truncado em {relativo}")
                    saida.write(bloco)
                    restante -= len(bloco)
            if mtime:
                os.utime(alvo, (mtime, mtime))
            extraidos += 1
            bytes_extraidos += tamanho
            if extraidos % 100 == 0:
                print(f"  ... {extraidos} arquivos ({bytes_extraidos / 1024 / 1024:.0f} MiB)", flush=True)
    print(f"\nExtraídos: {extraidos} arquivos ({bytes_extraidos / 1024 / 1024:.1f} MiB) em {destino}")
    if somente:
        print(f"Pulados (fora de '{somente}'): {pulados}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Extrai arquivos .wpress (All-in-One WP Migration).")
    parser.add_argument("wpress", type=Path, help="caminho do arquivo .wpress")
    parser.add_argument("-o", "--destino", type=Path, help="pasta de saída da extração")
    parser.add_argument("--somente", help="extrai só entradas cujo caminho começa com este prefixo (ex.: uploads)")
    parser.add_argument("--listar", action="store_true", help="só lista o sumário por pasta de topo, sem extrair")
    args = parser.parse_args()

    if not args.wpress.is_file():
        print(f"arquivo não encontrado: {args.wpress}", file=sys.stderr)
        return 1
    if args.listar:
        listar(args.wpress)
        return 0
    if not args.destino:
        parser.error("--destino é obrigatório para extrair (ou use --listar)")
    extrair(args.wpress, args.destino, args.somente)
    return 0


if __name__ == "__main__":
    sys.exit(main())
