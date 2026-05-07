# Fase 0 -- Pesquisa e Benchmarking

Colecionar referencias e ideias que alimentem as decisoes de todas as fases seguintes. **STATUS: CONCLUIDA.**

## Inputs

| Source | File/Location | Section/Scope | Why |
|---|---|---|---|
| Tarefa | `references/tarefa-benchmarking.md` | Full file | Definicao da pesquisa (5 oculos, sites sugeridos) |

## Process

1. Juliana pesquisou 7 sites com ferramenta HTML estruturada (5 oculos: Visual, Leitura, Interacao, Estrutura, Acessibilidade)
2. Dados exportados e alimentados ao Claude para analise comparativa
3. Claude gerou relatorio consolidado com padroes, destaques, lacunas e prioridades
4. Elton revisou e cruzou com ata da reuniao de brainstorm
5. 15 decisoes de consolidacao documentadas em `_config/decisoes.md`

## Outputs

| Artifact | Location | Format |
|---|---|---|
| Pesquisa completa (Juliana) | `output/pesquisa-juliana.html` | HTML interativo com dados de 7 sites |
| Dados brutos (backup) | `output/pesquisa-juliana.zip` | ZIP com dados exportados |
| Analise Claude Blog | `output/analise-claude-blog.json` | JSON com analise de um site |
| Relatorio comparativo | `output/relatorio-comparativo.md` | Markdown -- padroes, prioridades, recomendacoes |

## Audit

| Check | Pass Condition |
|---|---|
| Minimo 6 sites analisados | 7 sites concluidos |
| 5 oculos por site | Todos os 5 oculos preenchidos |
| Padroes identificados com percentuais | Relatorio contem estatisticas |
| Top 5 prioridades ranqueadas | Presentes no relatorio |
| Decisoes de consolidacao documentadas | 15 decisoes em `_config/decisoes.md` |
