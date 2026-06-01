# Fase 4 -- Producao de Conteudo

Reescrever os artigos existentes e produzir novos seguindo o Content System completo.

## Inputs

| Source | File/Location | Section/Scope | Why |
|---|---|---|---|
| Content System (Consolidado) | `../01-fundacoes/output/contentsystem.md` | Seções A.2 (Voz e Tom), A.4 (Padrões), A.5 (Rubrica) e A.6 (Legibilidade) | Diretrizes e regras para produção e avaliação de conteúdo |
| Vocabulário Controlado | `../01-fundacoes/output/vocabulario-controlado.json` | Full file | Dicionário de termos preferidos, sinônimos aceitos e proibidos |
| Inventario base antiga | `../../data/base-antiga/` | Full folder | Artigos existentes |

## Process

### Etapa 4.1 -- Triagem (pode iniciar em paralelo a Fase 3)
1. Avaliar cada artigo existente com a Rubrica de Qualidade (Camada 5)
2. Classificar: descartar (<2.0), reescrever (2.0-3.0), atualizar (3.0-3.5), migrar (>3.5)

### Etapa 4.2 -- Producao e Reescrita
3. Para cada artigo: gerar rascunho via prompt template + Vocabulario Controlado
4. Juliana revisa: estrutura, precisao, tom, completude
5. Rute revisa: adequacao pedagogica, clareza, publico
6. Elton revisa: precisao tecnica, conformidade, metadados
7. Aplicar Rubrica -- score >= 3.5? Se nao, volta ao passo 4
8. Publicar com metadados completos + marcacao IA quando aplicavel

### Artigos-Piloto
9. Publicar 3-5 artigos completos como teste real antes de migrar tudo

## Outputs

| Artifact | Location | Format |
|---|---|---|
| Triagem dos artigos | `output/triagem-artigos.md` | Markdown com tabela |
| Artigos reescritos | `output/artigos/` | Markdown por artigo |
| Artigos-piloto | `output/pilotos/` | Publicados no WordPress |
