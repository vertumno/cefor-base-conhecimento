#!/usr/bin/env python3
"""Fase G — gera o ESQUELETO do mapeamento de curadoria dos artigos.

Cruza três fontes:
  1. Inventário da base antiga (categoria/tipo/temas/percursos antigos por artigo).
  2. Tabelas de correspondência antigo→novo (taxonomia.md §7, codificadas aqui).
  3. Mapa de trilhas/percursos (trilhas-percursos-mapa.md, codificado aqui por id).

Saída: JSON de revisão com sugestão de categoria/tipo/tópicos por artigo +
vínculos de trilha. A palavra final é EDITORIAL — o esqueleto marca com
`revisar: true` tudo o que foi decidido por heurística fraca. O arquivo
canônico (mapeamento-curadoria.json) é o esqueleto após a revisão editorial.

Uso:
  python gerar_esqueleto_mapeamento.py INVENTARIO.json ARTIGOS_WP.json SAIDA.json
"""

import json
import re
import sys
import unicodedata

# ---------------------------------------------------------------- helpers


def sem_acento(s: str) -> str:
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()


def norm(s: str) -> str:
    return sem_acento((s or "").lower())


# ------------------------------------------------- taxonomia.md §7.2 (tipos)

TIPO_ANTIGO_NOVO = {
    "tutorial": "Tutorial",
    "tutorial/avaliacao": "Tutorial",
    "referencia moodle": "Referência",
    "template/code": "Referência",
    "institucional/padrao visual": "Referência",
    "conceitual": "Conceitual",
    "ferramenta externa": "Recurso",
    "ferramenta/gpt": "Recurso",
    "evento/divulgacao": None,  # fora da base (taxonomia.md §7.2)
    "outros": None,  # reclassificar editorialmente
}

# -------------------------------------- categoria: regras por palavra-chave
# Ordem importa: a primeira regra que casar (no título + temas) decide.
# Fontes: taxonomia.md §4 (domínios) e trilhas-percursos-mapa.md §2 (filtro).

REGRAS_CATEGORIA = [
    ("acessibilidade", r"libras|audiodescri|acessib|vlibras|tempo ampliado|videobook"),
    ("conduta", r"direito autoral|direitos autorais|netiqueta|seguranca|plagio|lgpd"),
    ("identidade", r"padrao visual|mooc|relicefor|livro digital|e-?book|identidade visual|template"),
    (
        "ferramentas",
        r"h5p|rotulo|webconfer|conferencia web|video|audio|podcast|youtube|canva|padlet|"
        r"powtoon|gpt|chatgpt|aplicativo|mobile|questionario|prova|banco de questoes|"
        r"tarefa|forum|glossario|wiki|escolha|base de dados|levelup|level up|"
        r"barra de progresso|emblema|badge|safe exam|gamifica|ferramenta",
    ),
    (
        "gestao-moodle",
        r"sala virtual|livro de notas|notas|backup|restaura|matricula|inscri|usuario|"
        r"acesso|visitante|moodle codes?|sistema academico|importa|secoes|semanas|"
        r"checklist|curso|navega|painel|perfil|senha|relatorio",
    ),
    (
        "pedagogia",
        r"planejamento|design educacional|mapa de atividades|bloom|rubrica|pedagog|"
        r"metodologia|aprendizagem|avaliacao formativa",
    ),
]

CATEGORIA_ANTIGA_NOVA = {
    # diretas (taxonomia.md §7.1) — usadas quando nenhuma regra de keyword casa
    "recurso educacional": "ferramentas",
    "ferramentas de autoria": "ferramentas",
    "ferramentas de comunicacao": "ferramentas",
    "tecnologias educacionais": "pedagogia",
    "conhecimentos pedagogicos": "pedagogia",
    "aspectos pedagogicos": "pedagogia",
    "procedimentos de comunicacao": "conduta",
    "procedimento de tecnologia da informacao": "conduta",
    "procedimento administrativo": "conduta",
    "processos": "conduta",
    "livros digitais (e-book)": "identidade",
    "mooc": "identidade",
    "ambiente virtual de aprendizagem": "gestao-moodle",
    "ambiente virtual": "gestao-moodle",
    "moodle": "gestao-moodle",
    "moodle x sistema academico": "gestao-moodle",
}

# ------------------------------------------------ tópicos (25, casing fixo)
# termo preferido -> regex sobre titulo+temas (sinônimos do vocabulário +
# variações observadas nas 82 tags antigas)

REGRAS_TOPICO = {
    "Questionário": r"questionario|quiz|prova",
    "Banco de Questões": r"banco de quest|sorteio|categoria de quest",
    "Tarefa": r"\btarefa",
    "Fórum": r"\bforum",
    "Livro de Notas": r"livro de notas|notas|media|recupera",
    "H5P": r"h5p",
    "Rótulo": r"rotulo",
    "Webconferência": r"webconfer|conferencia web|rnp",
    "Vídeo": r"video|youtube",
    "Áudio e Podcast": r"audio|podcast",
    "Livro Digital": r"livro digital|e-?book|relicefor",
    "Configuração de Curso": r"configura|secoes|semanas|data de inicio|checklist|importa",
    "Matrícula e Inscrição": r"matricula|inscri|cadastro",
    "Backup e Restauração": r"backup|restaura",
    "Moodle Codes": r"moodle codes?|\bcodigo|\bhtml\b|\bcss\b",
    "Sala Virtual": r"sala virtual|sala de aula virtual",
    "IA Generativa": r"\bia\b|inteligencia artificial|gpt|chatgpt|generativ",
    "GPT Customizado": r"gpt",
    "Libras": r"libras|vlibras|videobook",
    "Audiodescrição": r"audiodescri",
    "Inclusão e Desenho Universal": r"inclusao|desenho universal|tempo ampliado|acessib",
    "Planejamento e Design Educacional": r"planejamento|design educacional|mapa de atividades|bloom|rubrica",
    "Padrão Visual": r"padrao visual|identidade visual",
    "MOOC": r"mooc",
    "Direitos Autorais e Segurança": r"direito|netiqueta|seguranca|senha|safe exam|plagio",
}

# --------------------------- trilhas-percursos-mapa.md §3/§4 (por id de inventário)

TRILHAS = {
    "T1": {
        "titulo": "Da sala vazia ao primeiro dia de aula",
        "categoria": "gestao-moodle",
        "firme": True,
        "artigos": [129, 82, 56, 89, 111, 66],
        "ancora": 129,
    },
    "T2": {
        "titulo": "Avaliação online de ponta a ponta",
        "categoria": "gestao-moodle",
        "firme": True,
        "artigos": [127, 125, 120, 121, 116, 107, 122, 119, 123, 124, 108, 118, 106, 104, 103, 34, 126],
        "ancora": 127,
    },
    "T3": {
        "titulo": "Do Livro de Notas ao Sistema Acadêmico",
        "categoria": "gestao-moodle",
        "firme": True,
        "artigos": [85, 57, 16, 113, 47],
        "ancora": 85,
    },
    "T4": {
        "titulo": "Conteúdo interativo com H5P, do básico ao avançado",
        "categoria": "ferramentas",
        "firme": True,
        "artigos": [17, 18, 19],
        "ancora": 17,
    },
    "T5": {
        "titulo": "Aulas ao vivo por Webconferência",
        "categoria": "ferramentas",
        "firme": True,
        "artigos": [53, 54, 27, 58],
        "ancora": 53,
    },
    "T6": {
        "titulo": "Acompanhamento e gamificação do progresso",
        "categoria": "ferramentas",
        "firme": True,
        "artigos": [44, 43, 45],
        "ancora": None,
    },
    "T7": {
        "titulo": "Avaliação acessível para todos os estudantes",
        "categoria": "acessibilidade",
        "firme": True,
        "artigos": [15, 2, 26],
        "ancora": 15,
    },
    "T8": {
        "titulo": "Conteúdo em Libras no AVA, do vídeo ao termo técnico",
        "categoria": "acessibilidade",
        "firme": True,
        "artigos": [35, 62, 14],
        "ancora": None,
    },
    "T9": {
        "titulo": "Avaliações com IA generativa",
        "categoria": "pedagogia",
        "firme": True,
        "artigos": [5, 8, 6],
        "ancora": 5,
    },
    "T10": {
        "titulo": "Administração da sala virtual ao longo do curso",
        "categoria": "gestao-moodle",
        "firme": False,  # candidata — confirmar com Rute
        "artigos": [92, 86, 63, 59, 48, 87],
        "ancora": None,
    },
}

PERCURSO_V1 = {
    "titulo": "Dominando o Moodle",
    "trilhas": ["T1", "T2", "T3"],  # T10 entra se confirmada
    "complementares": [93, 130],  # certificados · mapa de atividades
}

# fora da base (trilhas-percursos-mapa.md §5 — remover/arquivar)
FORA_DA_BASE = {1, 20, 64, 10, 11, 12}

# ---------------------------------------------------------------- main


def main() -> None:
    inv_path, wp_path, saida = sys.argv[1:4]
    with open(inv_path, encoding="utf-8") as f:
        inventario = {a["slug"]: a for a in json.load(f)["artigos"]}
    with open(wp_path, encoding="utf-8") as f:
        artigos_wp = json.load(f)

    trilha_por_id = {}
    for sigla, t in TRILHAS.items():
        for pos, id_inv in enumerate(t["artigos"], start=1):
            trilha_por_id.setdefault(id_inv, []).append(
                {"trilha": sigla, "posicao": pos}
            )

    saida_artigos = []
    for wp in artigos_wp:
        antigo = inventario.get(wp["slug_legado"])
        registro = {
            "wp_id": wp["wp_id"],
            "titulo": wp["titulo"],
            "status": wp["status"],
            "slug": wp["slug"],
            "id_inventario": antigo["id"] if antigo else None,
            "antigo": {
                "categoria": antigo["categoria"] if antigo else None,
                "tipo": antigo["tipo"] if antigo else None,
                "temas": antigo["temas"] if antigo else [],
            },
            "tipo": None,
            "categoria": None,
            "topicos": [],
            "trilhas": trilha_por_id.get(antigo["id"], []) if antigo else [],
            "fora_da_base": bool(antigo and antigo["id"] in FORA_DA_BASE),
            "revisar": [],
            "subtitulo": "",
            "snippet": wp["snippet"][:240],
        }

        texto = norm(wp["titulo"])
        if antigo:
            texto += " " + " ".join(norm(t) for t in antigo["temas"])

        # tipo
        if antigo:
            registro["tipo"] = TIPO_ANTIGO_NOVO.get(norm(antigo["tipo"]))
        if not registro["tipo"]:
            registro["revisar"].append("tipo")

        # categoria: keyword primeiro; correspondência direta como fallback
        for cat, padrao in REGRAS_CATEGORIA:
            if re.search(padrao, texto):
                registro["categoria"] = cat
                break
        if not registro["categoria"] and antigo:
            registro["categoria"] = CATEGORIA_ANTIGA_NOVA.get(norm(antigo["categoria"]))
        if not registro["categoria"]:
            registro["revisar"].append("categoria")

        # tópicos por keyword (2 a 4; excedente corta, falta marca revisão)
        topicos = [t for t, padrao in REGRAS_TOPICO.items() if re.search(padrao, texto)]
        registro["topicos"] = topicos[:4]
        if len(topicos) < 2:
            registro["revisar"].append("topicos")
        elif len(topicos) > 4:
            registro["revisar"].append("topicos_excedentes:" + ",".join(topicos[4:]))

        registro["revisar"].append("subtitulo")
        saida_artigos.append(registro)

    resultado = {
        "_meta": {
            "fonte_antiga": "data/base-antiga/base-conhecimento-cefor-inventario.json",
            "regras": "taxonomia.md §7 + trilhas-percursos-mapa.md §2-§5",
            "nota": "ESQUELETO — campos em `revisar` exigem decisão editorial. "
            "O canônico é mapeamento-curadoria.json (este arquivo revisado).",
        },
        "trilhas": TRILHAS,
        "percurso_v1": PERCURSO_V1,
        "artigos": saida_artigos,
    }
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=1)

    n = len(saida_artigos)
    pend = {c: sum(1 for a in saida_artigos if c in a["revisar"]) for c in ("tipo", "categoria", "topicos")}
    print(f"{n} artigos. Pendências de revisão: {pend}")


if __name__ == "__main__":
    main()
