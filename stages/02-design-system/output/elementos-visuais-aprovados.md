# Elementos visuais para artigos — decisão de escopo

> **Versão:** 1.0 — primeira aprovação formal do conjunto de componentes editoriais
> **Data:** 2026-05-26
> **Aprovação:** Elton
> **Fase:** 2 — Design System
> **Fonte:** revisão do catálogo [`drafts/catalogo-elementos-visuais.html`](../drafts/catalogo-elementos-visuais.html) (24 candidatos: 10 originais + 14 candidatos da pesquisa de 2026-05-26)
> **Próximo passo:** formalizar cada item aprovado no `design.md` (Fase 2) e no `contentsystem.md` §B.5.2 (blocos Gutenberg)

---

## Contexto

O catálogo de 24 elementos foi montado a partir de pesquisa em fontes editoriais e técnicas premium (Stripe Docs, Linear, Vercel, MDN, GitHub Primer, Tufte CSS, Stripe Press, NYT, The Pudding, react.dev, Anthropic Docs, Bun, Astro). Apesar de os 10 primeiros já terem sido prototipados, **nenhum elemento estava formalmente aprovado** até esta data. Este documento formaliza a aprovação seletiva.

**Critério aplicado pelo Elton:** o que enriquece a leitura de artigos técnico-educacionais sobre Moodle/EaD no IFES sem inflar a complexidade editorial e operacional.

---

## Resumo

| Status | Quantidade | Itens |
|---|---|---|
| ✅ **Aprovado** | 14 | 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 20, 23, 24 |
| ❌ **Não usar** | 10 | 4, 12, 14, 15, 16, 17, 18, 19, 21, 22 |

---

## Aprovados (14)

### ✅ 1. Bloco de Prompt / Código

**Aprovado com ajustes.**

- **Remover o título/label do cabeçalho** ("PROMPT ESTRUTURADO DE IA"). O bloco entra sem cabeçalho — o código fala por si.
- **Botão "Copiar"** vira **apenas ícone**, **sutil**. Sem texto "Copiar". Cor neutra (`var(--ink-3)`) em estado de repouso; verde IFES em hover/focus; checkmark verde sólido após cópia (mantém o microfeedback). Posicionamento: canto superior direito do bloco, sem header dedicado — flutuante sobre o conteúdo.
- Mantém: highlight de variáveis com `--sun-soft`, fonte `JetBrains Mono`, scroll horizontal em código longo.

**Quando usar:** trechos de código Moodle (Moodle Codes), prompts de IA, snippets HTML/CSS/SQL, comandos de terminal.

---

### ✅ 2. Abas de Alternância Contextual (Tabs)

**Aprovado como está.**

**Quando usar:** apresentar a mesma instrução em múltiplas plataformas (Windows/Mac/Linux), múltiplas versões do Moodle, múltiplos perfis (Professor/Mediador/Aluno). Máximo 4 abas por grupo.

---

### ✅ 3. Cartões "Certo vs Errado"

**Aprovado como está.**

**Quando usar:** demonstrar contraste pedagógico — boa prática vs antipadrão. Cartão verde (`--accent`) vs vermelho-tijolo (`--rose`). Sempre em par, nunca isolado.

---

### ❌ 4. Lista de Verificação Interativa

**Não usar.**

> Não entra no DS. Checklist interativa com checkbox e persistência cria expectativa de "estado pessoal" que conflita com a Decisão 29 (V1 sem rastreamento de progresso pessoal, sem `localStorage`).

---

### ✅ 5. Glossário / Tooltip Inline

**Aprovado como está.**

**Quando usar:** primeira menção de termo técnico que tem definição curta. Não substitui artigo conceitual — é definição-relâmpago. Borda inferior pontilhada em verde IFES; popover sobe ao hover/focus com definição + opcional "Ver artigo completo →".

---

### ✅ 6. Atalhos de Teclado (Kbd)

**Aprovado como está.**

**Quando usar:** instruções com atalhos do navegador, do Moodle ou de ferramentas externas. Combinar com `+` entre teclas (ex.: `Ctrl` + `K`). Sempre em `<kbd>` semântico.

---

### ✅ 7. Citação Editorial / Blockquote Premium

**Aprovado como está.**

**Quando usar:** citação de terceiros (Ruti, professores entrevistados, documentos oficiais). Distinto do **Pull quote (#13)** — este cita o autor; o 13 destaca trecho do próprio artigo.

---

### ✅ 8. Cartão de Recurso / Download

**Aprovado com ajustes.**

- **Deve contemplar múltiplos arquivos.** Variantes a implementar:
  - **Variante A — arquivo único:** layout atual.
  - **Variante B — lista de arquivos:** múltiplos cards empilhados (vertical), agrupados por título de "kit/pacote", cada arquivo com seu próprio nome, tamanho e botão de download.
  - **Variante C — kit baixar tudo:** botão primário "Baixar tudo (.zip — X MB)" + lista expandível dos arquivos individuais abaixo.
- Mantém: ícone por tipo de arquivo (PDF, DOCX, XLSX, PPTX, ZIP, vídeo), nome + tamanho + formato no meta, botão de download em verde IFES.

**Quando usar:** templates institucionais, planilhas, modelos de planejamento, kits visuais — qualquer recurso baixável.

---

### ✅ 9. Acordeão de FAQ

**Aprovado como está.**

**Quando usar:** seção final do artigo com perguntas frequentes específicas daquele conteúdo. Usa `<details>` nativo. Máximo ~6 itens por bloco; acima disso, considerar artigo de Referência separado.

---

### ✅ 10. Linha do Tempo / Etapas de Fluxo

**Aprovado como está.**

**Quando usar:** fluxos longos com responsáveis distintos por etapa (ex.: pipeline de revisão pedagógica, fluxo de credenciamento de tutor, etapas de aprovação de MOOC). Cada etapa tem badge de papel responsável. Diferente de **Mini-stepper (#16, rejeitado)** — este é grande, com descrição + papel; o 16 era enxuto e foi descartado.

---

### ✅ 11. Highlight Marca-texto Editorial

**Aprovado como está.**

**Quando usar:** três variantes semânticas:
- `mk-tmp` (dourado, gradiente) — destaque temporário, "leia isto agora"
- `mk-perm` (verde IFES translúcido) — definição canônica permanente
- `mk-note` (linha pontilhada inferior) — nota editorial discreta

Disciplina: máximo 1–2 highlights por seção. Borda assimétrica simulando traço manuscrito.

---

### ❌ 12. Aside Numerado à Margem (Tufte sidenote)

**Não usar.**

> Padrão muito literário/acadêmico para uma base operacional. Adiciona complexidade de layout (coluna lateral em desktop, inline em mobile) sem ganho proporcional para o público (professores procurando instrução prática).

---

### ✅ 13. Pull Quote Editorial

**Aprovado como está.**

**Quando usar:** trecho do **próprio artigo** que merece pausa visual — princípios, frases-chave, definições densas. Fraunces itálico, filetes dourados horizontais. Diferente do **Blockquote (#7)** que cita terceiros. Disciplina: 1 pull quote por artigo, no máximo.

---

### ❌ 14. TL;DR / "Em uma frase"

**Não usar.**

> Fora do escopo V1. Cruza com a **Decisão 3** registrada em `_config/decisoes.md` (TL;DR obrigatório foi **rejeitado** — não entra na V1; reavaliar na Fase 5 com dados de uso).

---

### ❌ 15. Resumo Expansível ("Leitura em N min")

**Não usar.**

> Tempo de leitura já vive no cabeçalho do artigo (Decisão 4 — Tempo de leitura + Índice). Bloco de resumo expansível adicional duplica função e polui a abertura do artigo.

---

### ❌ 16. Mini-stepper Textual Inline

**Não usar.**

> O componente **Linha do Tempo (#10)** já cobre passo a passo. Adicionar um stepper "enxuto" alternativo gera dúvida editorial sobre quando usar qual — risco maior do que ganho.

---

### ❌ 17. Painel de Pré-requisitos

**Não usar.**

> Pré-requisitos serão tratados dentro da estrutura editorial padrão (parágrafo de abertura ou lista no início do tutorial), não como componente visual dedicado. Para tutoriais que exigem pré-requisitos, **os campos do CPT `trilha` já incluem `prerequisitos`** (`contentsystem.md` §B.4) — o lugar editorial é na trilha, não em cada artigo.

---

### ❌ 18. Painel de Pós-condições

**Não usar.**

> Mesma razão do #17. Estado esperado entra como parágrafo final do tutorial ou via Linha do Tempo (#10).

---

### ❌ 19. Próximos Passos Plurais

**Não usar.**

> Coberto pelo **Box de trilha multi-trilha** (Decisão 30) na sidebar + seção obrigatória de **Artigos Relacionados** no rodapé (Decisão 9, Decisão 24). Adicionar "próximos passos plurais" no rodapé do artigo recria a complexidade rejeitada na Decisão 32 (remoção do prev/next no rodapé).

---

### ✅ 20. Matriz "Quando usar X vs Y"

**Aprovado como está.**

**Quando usar:** apoio à decisão entre opções equivalentes do Moodle (Questionário × Tarefa, Fórum × Chat, H5P × Vídeo). Duas colunas simétricas (verde × dourado) sem ganhador. Cada coluna apresenta o cenário em que aquela opção brilha. Não é tabela comparativa.

---

### ❌ 21. Pílula de Versão Inline

**Não usar.**

> A política V1 (Decisão 14) decidiu **não exibir versão do Moodle na interface pública** ("não precisa", Elton). Pílulas de versão inline contradizem essa decisão. Quando uma instrução depende de versão específica, tratar editorialmente no texto.

---

### ❌ 22. Metadata Editorial (Tempo · Dificuldade · Custo)

**Não usar.**

> Tempo de leitura já existe no cabeçalho (Decisão 4). Dificuldade e custo são metadados que não foram aprovados na Decisão 14 (Metadados obrigatórios) e adicionariam ruído de "selo" que não cabe na estética editorial sóbria.

---

### ✅ 23. Callout "Erro Comum" (Pitfall)

**Aprovado como está.**

**Quando usar:** alertar para armadilha frequente observada em sala (override que não aparece, configuração que parece salvar mas não salva, comportamento contraintuitivo do Moodle). Vermelho-tijolo dessaturado (paleta editorial), label "Erro comum" em Fraunces itálico. Disciplina: máximo 2 por artigo.

> Será um dos **tipos de callout** a entrar na lista canônica de callouts (Decisão 5 — ainda pendente de fechamento da lista completa de tipos).

---

### ✅ 24. Big Number / Estatística Destacada

**Aprovado como está.**

**Quando usar:** quando 1 número sintetiza o ponto-chave do artigo. Fraunces 4–5rem em verde IFES, fonte sempre citada inline (não em rodapé) — disciplina jornalística. Máximo 1 por artigo. Quando NÃO usar: número trivial, número sem fonte confiável, número que iludiria fora de contexto.

---

## Impactos a propagar

| Documento | Mudança |
|---|---|
| `stages/02-design-system/output/design.md` | Adicionar os 14 componentes aprovados à seção de Componentes. Remover/ignorar os 10 rejeitados. |
| `stages/01-fundacoes/output/contentsystem.md` §B.5.2 | Atualizar tabela de blocos Gutenberg customizados com a lista final. |
| `stages/02-design-system/drafts/catalogo-elementos-visuais.html` | Atualizar para refletir: ajustes do #1 (sem título, ícone sutil) e #8 (múltiplos arquivos). Marcar visualmente o status (✅ / ❌) de cada item. |
| `_config/decisoes.md` | Considerar registrar como **Decisão 33 — Escopo dos elementos visuais editoriais (Fase 2)** se Elton + Marcos quiserem essa formalização constitucional. |

---

## Decisões pendentes que decorrem deste documento

| Pendência | Bloqueia |
|---|---|
| Implementar ajustes do #1 (sem título, ícone sutil de copiar) no protótipo | Antes de levar para o `design.md` |
| Definir as 3 variantes do #8 (arquivo único, lista, kit zip) no protótipo | Antes de levar para o `design.md` |
| Fechar lista canônica de **tipos de callout** (Decisão 5 — ainda em aberto), incluindo o "Erro comum" (#23) como um dos tipos | Implementação do bloco `Callout` em Gutenberg |
| Validação com Marcos (e Juliana/Ruti, se relevante) | Antes de virar Decisão 33 formal |

---

## Histórico

| Versão | Data | Mudança | Por |
|---|---|---|---|
| 1.0 | 2026-05-26 | Aprovação inicial de 14 dos 24 candidatos. Ajustes definidos para #1 e #8. | Elton |
