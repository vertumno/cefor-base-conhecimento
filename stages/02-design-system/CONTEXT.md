# Fase 2 -- Design System

Definir a linguagem visual completa da base: tokens, componentes, comportamento responsivo, acessibilidade, experiencia de leitura. Os 6 pilares do DS sao interdependentes e devem ser trabalhados juntos.

## Inputs

| Source | File/Location | Section/Scope | Why |
|---|---|---|---|
| Pilares do sistema | `../../_config/pilares.md` | Pilares 1, 2, 5, 6, 8, 9 | Escopo dos pilares de design |
| Design System escopo | `../01-fundacoes/references/design-system-escopo.md` | Full file | Camadas, componentes, padroes |
| Decisoes visuais | `../../_config/decisoes.md` | Decisoes 6-8 (tipografia, fundo, modo escuro) | Direcoes visuais aprovadas |
| Biblioteca de Padroes | `../01-fundacoes/output/contentsystem.md` | §A.4 (Biblioteca de Padrões de Conteúdo) | Quais componentes o CS exige |
| Modelos Mentais | `../01-fundacoes/output/contentsystem.md` | §A.7 (Modelos Mentais do Público) | Informam UX |
| Relatorio comparativo | `../00-benchmarking/output/relatorio-comparativo.md` | Secao 4 (Recomendacoes por Oculos) | Referencias visuais |

## Process

1. Definir Design Tokens (paleta claro/escuro, tipografia, espacamento, sombras, breakpoints)
2. Definir Sistema de Leitura (coluna, line-height, progresso, tempo de leitura, indice)
3. Mapear Componentes em Atomic Design (atomos, moleculas, organismos, templates)
4. Definir comportamento de acessibilidade por componente (contraste, ARIA, teclado)
5. Definir comportamento responsivo por componente
6. Definir interacoes (feedback, curtir, compartilhar, copiar, salvar)
7. ✅ Criar layouts de pagina — os **9 tipos** da arquitetura de informacao: inicio, artigo, categoria, trilha + listagem, percurso + listagem, topico, busca
8. ✅ Produzir prototipos de alta fidelidade (9 paginas em `drafts/prototipos-paginas/base-*.html`, casca compartilhada `shell.css/js` + `a11y.css/js`)

## Checkpoints

| After Step | Agent Presents | Human Decides |
|---|---|---|
| Step 1 | Tokens visuais (cores, fontes, espacamento) | Elton + Juliana validam identidade visual |
| Step 3 | Catalogo de componentes mapeados | Elton confirma viabilidade tecnica no WP |
| Step 7 | Layouts de pagina (9 tipos) | ✅ Validado por Elton (2026-06-07) — categoria=hero claro+chip · trilhas=grid+filtro · busca=unificada |

## Outputs

> **Decisao de escopo (Elton, 2026-05-21):** a Fase 2 consolida tudo em UM arquivo canonico, `output/design.md`, em vez de desmembrar nos 5 documentos separados originalmente previstos. Razao: o schema `design.md` (google-labs-code) ja e fonte unica de verdade (tokens + componentes + regras); fragmentar recria problema de sincronizacao e vai contra o fluxo design-first. Os drafts HTML (`kit-visual.html`, exploracoes) seguem como apoio visual.

| Artifact | Location | Format | Status |
|---|---|---|---|
| **Design System (canonico)** | `output/design.md` | Markdown + frontmatter de tokens (schema google-labs-code/design.md) | ✅ v1.0 (2026-05-21) |
| Kit Visual (style guide vivo) | `drafts/kit-visual.html` | HTML interativo (toggles claro/escuro/contraste/dislexia) | ✅ fonte dos tokens |
| Prototipos de pagina (9 tipos) | `drafts/prototipos-paginas/base-*.html` | HTML alta fidelidade (casca `shell.css/js` + `a11y.*`) | ✅ 9/9 (2026-06-07) |

**Tokens** espelham `drafts/kit-visual.html`. **Componentes e regras** rastreiam as Decisões 1-32 (`_config/decisoes.md`). **Interfaces de referência:** os **9 templates base** em `stages/02-design-system/drafts/prototipos-paginas/`, um por tipo de página da arquitetura de informação — itens (`base-inicio`, `base-artigo`, `base-categoria`, `base-trilha`, `base-percurso`, `base-topico`) e listagens/busca (`base-trilhas`, `base-percursos`, `base-busca`) — com `base-artigo.html` como referência principal de página de artigo (Decisão 22).

**Vínculo de percurso (Decisão 31, revisão 2026-06-08):** o pertencimento de uma trilha/artigo a um percurso aparece como entrada "Faz parte do percurso" em verde-profundo no **painel de meta do artigo** (`base-artigo.html`) e no **painel de stats da página de trilha** (`base-trilha.html`). O antigo chip dentro do acordeão de trilha foi removido — são 4 superfícies do percurso (com a página dedicada e a listagem `/percursos`).

### Estado de retomada (2026-06-08)
- ✅ As 9 páginas-tipo prototipadas; casca unificada; navegação coerente; `base-inicio-v5.html` → `base-inicio.html`.
- ✅ Decisões de layout (Step 7) validadas: categoria=hero claro+chip · trilhas=grid+filtro · busca=unificada · vínculo de percurso no meta/stats.
- ⏳ **Pendente:** validar a navegação no navegador (claro/escuro/contraste/dislexia) e **commitar** a leva — `git push`/PR são exclusivos de @devops.

### Lacunas em aberto no design.md (travam a Fase 3)
1. Referendar nomes da escala de espacamento (`--space-xs` a `--space-3xl`).
2. Validar formalmente os 6 tipos de callout (Decisao 5 ainda aberta).
3. Definir a 6a categoria do Eixo 2.
4. Definir a stack WP (tema de blocos / `theme.json` vs tema classico / `style.css`) antes de gerar `tokens.css` / `theme.json`.

### Antes desmembrado (agora consolidado em design.md)
~~`design-tokens.md`~~ · ~~`sistema-leitura.md`~~ · ~~`componentes.md`~~ · ~~`acessibilidade.md`~~ · ~~`layouts.md`~~ — todos absorvidos pelas secoes do `design.md`. Prototipos de alta fidelidade seguem em `drafts/` / futuro `output/prototipos/`.
