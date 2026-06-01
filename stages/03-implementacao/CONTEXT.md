# Fase 3 -- Implementacao WordPress

Transformar o Design System e as definicoes editoriais em um tema WordPress funcional.

## Inputs

| Source | File/Location | Section/Scope | Why |
|---|---|---|---|
| Design System | `../02-design-system/output/design.md` | Full file | Tokens visuais, componentes, layouts e regras de acessibilidade |
| Taxonomia | `../01-fundacoes/output/taxonomia.md` | Full file | Categorias, tópicos, trilhas e percursos aprovados |
| Content System (Consolidado) | `../01-fundacoes/output/contentsystem.md` | Full file (Partes A e B) | Políticas editoriais, fluxo de publicação (ContentOps), estados de depreciação e especificações acionáveis para WordPress |

## Process

1. Criar tema WordPress customizado com tokens do DS
2. Implementar Custom Post Types e campos de metadados
3. Criar blocos Gutenberg para componentes editoriais (AlertBox, TLDRBox, etc.)
4. Implementar workflow de publicacao (estados, transicoes, permissoes)
5. Implementar SEO/GEO tecnico (Schema.org, meta tags, sitemap, Open Graph)
6. Implementar busca interna com filtros e modal (Ctrl+K)
7. Implementar widget de acessibilidade (VLibras, A-/A+, contraste, dislexia)
8. Testar responsividade, acessibilidade (eMAG), performance (Core Web Vitals)

## Outputs

| Artifact | Location | Format |
|---|---|---|
| Tema WordPress | `output/theme/` | PHP/CSS/JS |
| Documentacao tecnica | `output/docs-tecnica.md` | Markdown |
| Resultado dos testes | `output/testes.md` | Markdown |
