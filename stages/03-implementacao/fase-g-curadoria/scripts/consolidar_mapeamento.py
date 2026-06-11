#!/usr/bin/env python3
"""Fase G — consolida esqueleto + ajustes editoriais no mapeamento canônico.

Valida contra os vocabulários fechados (taxonomia.md §3-§5) e produz
`mapeamento-curadoria.json`, o insumo único do `aplicar_curadoria.php`.

Uso:
  python consolidar_mapeamento.py ESQUELETO.json AJUSTES.json SAIDA.json
"""

import json
import sys

TIPOS = {"Tutorial", "Referência", "Conceitual", "Solução de Problema", "Recurso"}
CATEGORIAS = {"ferramentas", "gestao-moodle", "pedagogia", "acessibilidade", "conduta", "identidade"}
TOPICOS = {
    "Questionário", "Banco de Questões", "Tarefa", "Fórum", "Livro de Notas",
    "H5P", "Rótulo", "Webconferência", "Vídeo", "Áudio e Podcast", "Livro Digital",
    "Configuração de Curso", "Matrícula e Inscrição", "Backup e Restauração",
    "Moodle Codes", "Sala Virtual", "IA Generativa", "GPT Customizado",
    "Libras", "Audiodescrição", "Inclusão e Desenho Universal",
    "Planejamento e Design Educacional", "Padrão Visual", "MOOC",
    "Direitos Autorais e Segurança",
    # Decisão 36 (2026-06-10) — ampliação para 31
    "Atividades e Recursos", "Gamificação e Engajamento", "Comunicação e Interação",
    "Produção de Conteúdo", "Ferramentas Externas", "Procedimentos Institucionais",
}


def main() -> None:
    esq_path, aj_path, saida = sys.argv[1:4]
    with open(esq_path, encoding="utf-8") as f:
        esqueleto = json.load(f)
    with open(aj_path, encoding="utf-8") as f:
        ajustes = json.load(f)

    erros, deficit, nao_classificar, sem_subtitulo = [], [], [], []
    artigos_finais = []

    for art in esqueleto["artigos"]:
        wp_id = str(art["wp_id"])
        aj = ajustes["artigos"].get(wp_id, {})

        final = {
            "wp_id": art["wp_id"],
            "slug": art["slug"],
            "titulo": art["titulo"],
            "status": art["status"],
            "id_inventario": art["id_inventario"],
        }

        if aj.get("acao") == "nao-classificar":
            final["acao"] = "nao-classificar"
            final["nota"] = aj.get("nota", "")
            nao_classificar.append(f'{wp_id} {art["titulo"]}')
            artigos_finais.append(final)
            continue

        final["tipo"] = aj.get("tipo", art["tipo"])
        final["categoria"] = aj.get("categoria", art["categoria"])
        final["topicos"] = aj.get("topicos", art["topicos"])
        final["subtitulo"] = aj.get("subtitulo", art.get("subtitulo", ""))
        final["trilhas"] = art["trilhas"]

        if final["tipo"] not in TIPOS:
            erros.append(f'{wp_id}: tipo inválido {final["tipo"]!r}')
        if final["categoria"] not in CATEGORIAS:
            erros.append(f'{wp_id}: categoria inválida {final["categoria"]!r}')
        for t in final["topicos"]:
            if t not in TOPICOS:
                erros.append(f"{wp_id}: tópico inválido {t!r}")
        if len(final["topicos"]) > 4:
            erros.append(f'{wp_id}: {len(final["topicos"])} tópicos (máx. 4)')
        if len(final["topicos"]) < 2:
            deficit.append(f'{wp_id} ({len(final["topicos"])}) {art["titulo"]}')
        # subtítulo vazio é legítimo quando o ajuste o define explicitamente
        # (decisão de Marcos 2026-06-11: sem subtítulo no legado, deixar vazio)
        if final["subtitulo"] == "" and aj.get("subtitulo") == "":
            sem_subtitulo.append(f'{wp_id} {art["titulo"]}')
        else:
            palavras = len(final["subtitulo"].split())
            if not 8 <= palavras <= 27:  # tolerância de ±2 sobre a regra 10-25
                erros.append(f"{wp_id}: subtítulo com {palavras} palavras")

        artigos_finais.append(final)

    if erros:
        print("ERROS DE VALIDAÇÃO:")
        print("\n".join(" - " + e for e in erros))
        sys.exit(1)

    trilhas = {}
    for sigla, t in esqueleto["trilhas"].items():
        ed = ajustes["trilhas_editorial"].get(sigla, {})
        trilhas[sigla] = {**t, **ed}

    resultado = {
        "_meta": {
            "documento": "Fase G — mapeamento de curadoria CANÔNICO (esqueleto + ajustes editoriais)",
            "consumidor": "scripts/aplicar_curadoria.php",
            "validacao_pendente": "Elton + Juliana (taxonomia) · Rute + Juliana (trilhas)",
        },
        "trilhas": trilhas,
        "percurso_v1": {**esqueleto["percurso_v1"], **ajustes["percurso_editorial"]},
        "artigos": artigos_finais,
    }
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=1)

    classificados = [a for a in artigos_finais if "tipo" in a]
    print(f"{len(artigos_finais)} artigos consolidados: {len(classificados)} classificados, {len(nao_classificar)} não classificados.")
    print("\nNão classificados (utilitários / fora-da-base):")
    print("\n".join(" - " + n for n in nao_classificar))
    print(f"\nDéficit de tópicos (<2, exigem curadoria fina — taxonomia.md §5): {len(deficit)}")
    print("\n".join(" - " + d for d in deficit))
    if sem_subtitulo:
        print(f"\nSem subtítulo (vazio explícito nos ajustes): {len(sem_subtitulo)}")
        print("\n".join(" - " + s for s in sem_subtitulo))


if __name__ == "__main__":
    main()
