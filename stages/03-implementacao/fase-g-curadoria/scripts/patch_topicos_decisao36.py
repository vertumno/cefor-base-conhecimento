#!/usr/bin/env python3
"""Fase G — patch da Decisão 36: acrescenta os 6 tópicos novos aos artigos.

Aplica as ADIÇÕES de tópicos decididas na revisão editorial de 2026-06-10
sobre `ajustes-editoriais.json` (zera o déficit de cardinalidade <2 sem
remover nenhum tópico já atribuído). Reaplicar com consolidar + aplicar.

Uso: python patch_topicos_decisao36.py AJUSTES.json
"""

import json
import sys

ADICOES = {
    # Gamificação e Engajamento
    "3338": ["Gamificação e Engajamento", "Sala Virtual"],
    "3339": ["Gamificação e Engajamento"],
    "3430": ["Gamificação e Engajamento"],
    "3431": ["Gamificação e Engajamento"],
    "3432": ["Gamificação e Engajamento"],
    "3450": ["Gamificação e Engajamento"],
    "3451": ["Gamificação e Engajamento"],
    # Comunicação e Interação
    "3340": ["Comunicação e Interação"],
    "3376": ["Comunicação e Interação"],
    "3382": ["Comunicação e Interação"],
    "3399": ["Comunicação e Interação"],
    "3420": ["Comunicação e Interação"],
    "3421": ["Comunicação e Interação"],
    "3436": ["Comunicação e Interação"],
    "3448": ["Comunicação e Interação"],
    # Ferramentas Externas + Produção de Conteúdo (ferramentas de autoria)
    "3342": ["Ferramentas Externas", "Produção de Conteúdo"],
    "3345": ["Ferramentas Externas", "Produção de Conteúdo"],
    "3372": ["Ferramentas Externas", "Produção de Conteúdo"],
    "3373": ["Ferramentas Externas", "Produção de Conteúdo"],
    "3374": ["Ferramentas Externas", "Produção de Conteúdo"],
    "3379": ["Ferramentas Externas", "Produção de Conteúdo"],
    "3413": ["Ferramentas Externas", "Produção de Conteúdo", "Comunicação e Interação"],
    "3423": ["Ferramentas Externas", "Produção de Conteúdo"],
    "3439": ["Ferramentas Externas", "Produção de Conteúdo"],
    "3435": ["Ferramentas Externas", "Procedimentos Institucionais"],
    # Produção de Conteúdo
    "3397": ["Produção de Conteúdo"],
    "3398": ["Produção de Conteúdo"],
    "3425": ["Produção de Conteúdo"],
    "3438": ["Produção de Conteúdo"],
    "3443": ["Produção de Conteúdo"],
    "3452": ["Produção de Conteúdo"],
    "3453": ["Produção de Conteúdo"],
    "3457": ["Produção de Conteúdo"],
    "3458": ["Produção de Conteúdo"],
    "3460": ["Produção de Conteúdo"],
    # Procedimentos Institucionais
    "3343": ["Procedimentos Institucionais"],
    "3380": ["Procedimentos Institucionais"],
    "3392": ["Procedimentos Institucionais"],
    "3409": ["Procedimentos Institucionais"],
    "3414": ["Procedimentos Institucionais"],
    "3428": ["Procedimentos Institucionais"],
    "3454": ["Procedimentos Institucionais", "Direitos Autorais e Segurança"],
    # Atividades e Recursos (guias e operação de atividades/recursos)
    "3344": ["Atividades e Recursos"],
    "3346": ["Atividades e Recursos"],
    "3358": ["Atividades e Recursos"],
    "3359": ["Atividades e Recursos"],
    "3361": ["Atividades e Recursos"],
    "3364": ["Atividades e Recursos"],
    "3375": ["Atividades e Recursos"],
    "3377": ["Atividades e Recursos"],
    "3378": ["Atividades e Recursos", "Produção de Conteúdo"],
    "3390": ["Atividades e Recursos"],
    "3393": ["Atividades e Recursos"],
    "3394": ["Atividades e Recursos"],
    "3395": ["Atividades e Recursos"],
    "3396": ["Atividades e Recursos", "Produção de Conteúdo"],
    "3401": ["Atividades e Recursos"],
    "3402": ["Atividades e Recursos"],
    "3403": ["Atividades e Recursos", "Produção de Conteúdo"],
    "3404": ["Atividades e Recursos", "Sala Virtual"],
    "3405": ["Atividades e Recursos", "Sala Virtual"],
    "3406": ["Atividades e Recursos"],
    "3407": ["Atividades e Recursos", "Comunicação e Interação"],
    "3437": ["Atividades e Recursos"],
    "3471": ["Atividades e Recursos"],
    "3472": ["Atividades e Recursos", "Produção de Conteúdo"],
    # Combinações só com tópicos pré-existentes (déficit resolvido sem termo novo)
    "3356": ["Configuração de Curso"],
    "3360": ["Sala Virtual"],
    "3365": ["Configuração de Curso"],
    "3367": ["Banco de Questões"],
    "3368": ["Configuração de Curso"],
    "3385": ["Configuração de Curso"],
    "3388": ["Configuração de Curso"],
    "3412": ["Inclusão e Desenho Universal"],
}


def main() -> None:
    caminho = sys.argv[1]
    with open(caminho, encoding="utf-8") as f:
        ajustes = json.load(f)

    alterados = 0
    for wp_id, novos in ADICOES.items():
        art = ajustes["artigos"].get(wp_id)
        if art is None or "topicos" not in art:
            sys.exit(f"artigo {wp_id} ausente ou sem campo topicos no ajustes")
        for t in novos:
            if t not in art["topicos"]:
                art["topicos"].append(t)
        if len(art["topicos"]) > 4:
            sys.exit(f"artigo {wp_id} estourou o máximo de 4 tópicos: {art['topicos']}")
        alterados += 1

    ajustes["_meta"]["regras"].append(
        "2026-06-10 — Decisão 36 aplicada via patch_topicos_decisao36.py: "
        "+6 tópicos no vocabulário; adições nos artigos em déficit."
    )

    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(ajustes, f, ensure_ascii=False, indent=1)

    print(f"{alterados} artigos atualizados com os tópicos da Decisão 36.")


if __name__ == "__main__":
    main()
