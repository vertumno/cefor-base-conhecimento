# Fase 2 -- Design System

Definir a linguagem visual completa da base: tokens, componentes, comportamento responsivo, acessibilidade, experiencia de leitura. Os 6 pilares do DS sao interdependentes e devem ser trabalhados juntos.

## Inputs

| Source | File/Location | Section/Scope | Why |
|---|---|---|---|
| Pilares do sistema | `../../_config/pilares.md` | Pilares 1, 2, 5, 6, 8, 9 | Escopo dos pilares de design |
| Design System escopo | `../01-fundacoes/references/design-system-escopo.md` | Full file | Camadas, componentes, padroes |
| Decisoes visuais | `../../_config/decisoes.md` | Decisoes 6-8 (tipografia, fundo, modo escuro) | Direcoes visuais aprovadas |
| Biblioteca de Padroes | `../01-fundacoes/output/biblioteca-padroes.md` | Full file | Quais componentes o CS exige |
| Modelos Mentais | `../01-fundacoes/output/modelos-mentais.md` | Momentos de busca | Informam UX |
| Relatorio comparativo | `../00-benchmarking/output/relatorio-comparativo.md` | Secao 4 (Recomendacoes por Oculos) | Referencias visuais |

## Process

1. Definir Design Tokens (paleta claro/escuro, tipografia, espacamento, sombras, breakpoints)
2. Definir Sistema de Leitura (coluna, line-height, progresso, tempo de leitura, indice)
3. Mapear Componentes em Atomic Design (atomos, moleculas, organismos, templates)
4. Definir comportamento de acessibilidade por componente (contraste, ARIA, teclado)
5. Definir comportamento responsivo por componente
6. Definir interacoes (feedback, curtir, compartilhar, copiar, salvar)
7. Criar layouts de pagina (Home, Artigo, Trilha, Busca, Categoria)
8. Produzir prototipos de alta fidelidade

## Checkpoints

| After Step | Agent Presents | Human Decides |
|---|---|---|
| Step 1 | Tokens visuais (cores, fontes, espacamento) | Elton + Juliana validam identidade visual |
| Step 3 | Catalogo de componentes mapeados | Elton confirma viabilidade tecnica no WP |
| Step 7 | Layouts de pagina | Equipe valida antes de prototipar |

## Outputs

| Artifact | Location | Format |
|---|---|---|
| Design Tokens | `output/design-tokens.md` | Markdown + CSS variables |
| Sistema de Leitura | `output/sistema-leitura.md` | Markdown |
| Catalogo de Componentes | `output/componentes.md` | Markdown com Atomic Design |
| Checklist de Acessibilidade | `output/acessibilidade.md` | Markdown |
| Layouts de Pagina | `output/layouts.md` | Markdown + mockups |
| Prototipos | `output/prototipos/` | HTML/imagens |
