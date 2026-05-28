# Fase 1 -- Fundacoes (Content System + Taxonomia + Descoberta)

Definir as regras do jogo antes de tocar em visual ou codigo. Esta e a fase mais critica do projeto.

## Inputs

| Source | File/Location | Section/Scope | Why |
|---|---|---|---|
| Decisoes Fase 0 | `../../_config/decisoes.md` | Full file | 15 decisoes aprovadas que orientam todas as definicoes |
| Relatorio comparativo | `../00-benchmarking/output/relatorio-comparativo.md` | Secoes 3-5 (Lacunas, Recomendacoes, Prioridades) | Insumos do benchmarking |
| Pilares do sistema | `../../_config/pilares.md` | Pilares 3, 4, 7, 8, 10, 11 | Escopo dos pilares que esta fase define |
| Content System escopo | `references/content-system-escopo.md` | Full file | Rascunhos das 10 camadas (ponto de partida) |
| Design System escopo | `references/design-system-escopo.md` | Secao "Relacao com os 11 Pilares" | Pontos de contato CS ↔ DS |
| Ata da reuniao | `../../shared/reuniao-brainstorm.md` | Secoes 3-5 (Proposito, Ideias, Decisoes) | Consensos da equipe |

## Process

### Sprint 1: Camadas 1-3 do Content System (Elton + Ruti + Juliana)

1. **Principios Editoriais** (Camada 1) -- Validar os principios candidatos do escopo. Definir escopo positivo e negativo da base.
2. **Matriz de Voz e Tom** (Camada 2) -- Validar tabelas de voz/tom do escopo com Ruti. Coletar exemplos concretos de cada tom.
3. **Vocabulario Controlado** (Camada 3) -- Construir planilha/JSON com termos preferidos, sinonimos, mapeamento CEFOR-Moodle-MEC.

### Sprint 2: Camadas 4-7 (Elton + Ruti + Juliana)

4. **Biblioteca de Padroes** (Camada 4) -- Validar os 7 padroes do escopo. Adicionar novos se necessario.
5. **Rubrica de Qualidade** (Camada 5) -- Validar as 7 dimensoes e pesos. Testar com 2-3 artigos existentes.
6. **Padroes de Legibilidade** (Camada 6) -- Validar limites de Flesch, palavras/frase. Testar com artigos.
7. **Modelos Mentais** (Camada 7) -- Validar perfis mentais com Ruti e Juliana. Atualizar vocabulario natural.

### Sprint 3: Taxonomia + Descoberta (Elton + Marcos)

8. Definir estrutura de categorias e tags (alinhada com Vocabulario Controlado)
9. Definir modelo de percursos/trilhas (simplificado para V1)
10. Definir URLs semanticas
11. Definir estrategia SEO/GEO estrutural
12. Definir estrategia de busca interna

### Sprint 4: Camadas 8-10 + Consolidacao

13. **Politica de Depreciacao** (Camada 8) -- Validar fluxo do escopo.
14. **ContentOps** (Camada 9) -- Validar capacidade operacional com a equipe real.
15. **Metricas de Sucesso** (Camada 10) -- Definir metricas V1, operacionalizar na Fase 5.
16. Revisao final da Fase 1 com Elton + Marcos.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|---|---|---|
| Sprint 1 (step 3) | Principios + Voz/Tom + Vocabulario Controlado draft | Ruti valida adequacao pedagogica |
| Sprint 2 (step 7) | Rubrica testada em artigos reais + Modelos Mentais | Equipe valida antes de seguir para Taxonomia |
| Sprint 3 (step 12) | Estrutura de categorias + URLs + estrategia SEO | Elton + Marcos aprovam arquitetura tecnica |

## Audit

| Check | Pass Condition |
|---|---|
| Camadas 1-7 definidas em conjunto | Todas as 7 interdependentes validadas no mesmo ciclo |
| Vocabulario Controlado consultavel | Formato planilha ou JSON, nao texto corrido |
| Rubrica testada em artigos reais | Pelo menos 3 artigos existentes avaliados |
| Categorias alinhadas com Vocabulario | Termos de categoria existem no Vocabulario Controlado |
| URLs semanticas definidas | Padrao documentado com exemplos |
| Ruti validou camadas 1-7 | Aprovacao explicita registrada |

## Outputs

| Artifact | Location | Format |
|---|---|---|
| Principios Editoriais | `output/principios-editoriais.md` | Markdown |
| Matriz de Voz e Tom | `output/voz-e-tom.md` | Markdown com tabelas |
| Vocabulario Controlado | `output/vocabulario-controlado.json` | JSON estruturado |
| Biblioteca de Padroes | `output/biblioteca-padroes.md` | Markdown com catalogo |
| Rubrica de Qualidade | `output/rubrica-qualidade.md` | Markdown com tabelas de score |
| Padroes de Legibilidade | `output/padroes-legibilidade.md` | Markdown com limites |
| Modelos Mentais | `output/modelos-mentais.md` | Markdown com perfis |
| Taxonomia | `output/taxonomia.md` | Markdown com arvore + regras |
| Estrategia de Descoberta | `output/descoberta-seo-geo.md` | Markdown |
| Politica de Depreciacao | `output/politica-depreciacao.md` | Markdown com fluxo |
| ContentOps Charter | `output/contentops.md` | Markdown |
| Metricas de Sucesso | `output/metricas-sucesso.md` | Markdown com dashboard |
