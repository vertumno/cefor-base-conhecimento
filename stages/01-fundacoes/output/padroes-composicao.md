# Camada 4.5 — Padrões de Composição

> **Versão:** 1.0 — DRAFT
> **Status:** Primeira camada formal do Content System
> **Última atualização:** 2026-05-19
> **Decisões consolidadas:** 17, 18, 22, 25, 26, 27, 28, 29, 30, 31, 32
> **Referências canônicas:** `stages/01-fundacoes/drafts/prototipo-artigo.html`, `drafts/exploracao-multiplas-trilhas.html`, `drafts/exploracao-pagina-percurso.html`

---

## 1. O que esta camada faz

A **Camada 4.5 — Padrões de Composição** define **como artigos, trilhas e percursos se compõem entre si**. É a camada que documenta a arquitetura estrutural do conteúdo — não o que está escrito *dentro* de um artigo (Camada 4) nem sua qualidade textual (Camada 5), mas **como as unidades se relacionam, se sinalizam e se navegam**.

### Onde ela se encaixa nas 10 camadas

Esta camada não estava no escopo original do `content-system-escopo.md`. Ela emerge das Decisões 18 e 25-32 (sessões de 14/05 e 19/05/2026), que estabeleceram a arquitetura Artigo → Trilha → Percurso. Sem uma camada dedicada a compor essas três entidades, padrões estruturais ficariam espalhados entre as Camadas 1, 4 e 9 sem coerência.

| Camada vizinha | O que faz | Diferença para a 4.5 |
|---|---|---|
| **Camada 4 — Biblioteca de Padrões de Conteúdo** | Padrões narrativos *dentro* de um artigo (passo a passo, problema-solução, analogia, etc.) | Camada 4 é sobre **escrita**; Camada 4.5 é sobre **composição entre artigos** |
| **Camada 3 — Vocabulário Controlado** | Termos padronizados (questionário vs prova, etc.) | A 4.5 *consome* a terminologia (Artigo/Trilha/Percurso/Passo) — não a define |
| **Camada 9 — ContentOps** | Fluxos operacionais de produção | A 4.5 dá ao ContentOps as *especificações* de o que precisa ser produzido para que uma trilha ou percurso exista |

### Posição no Content System

```
Camada 1 — Princípios Editoriais
Camada 2 — Voz e Tom
Camada 3 — Vocabulário Controlado
Camada 4 — Padrões de Conteúdo (dentro do artigo)
Camada 4.5 — Padrões de Composição (entre artigos)   ← aqui
Camada 5 — Rubrica de Qualidade
Camada 6 — Padrões de Legibilidade
Camada 7 — Modelos Mentais do Público
Camada 8 — Política de Depreciação
Camada 9 — ContentOps
Camada 10 — Métricas de Sucesso
```

---

## 2. A regra-mãe editorial

> **O artigo é a unidade soberana. Trilha e percurso são camadas de curadoria que envelopam, nunca alteram, o artigo.**

Esta frase é a consequência editorial direta da Decisão 18 (artigo pode estar em múltiplas trilhas) e da Decisão 26 (artigo-âncora pode servir múltiplas trilhas). Como o artigo não sabe em qual trilha está sendo lido, ele precisa funcionar **sempre** de forma autossuficiente, mas se encaixar **quando** estiver numa sequência.

### Os dois lados do contrato

| Propriedade | O que significa | Quem garante |
|---|---|---|
| **Autossuficiência** | O artigo resolve o problema dele sozinho. Quem chega por busca consegue completar a tarefa sem precisar ler outro artigo. | Conteúdo do artigo |
| **Encadeabilidade** | O artigo pode ser colocado em qualquer trilha sem reescrita, e a trilha funciona como sequência coerente. | Conteúdo do artigo + casca (box de trilha) |

A **voz da sequência** — "este é o próximo passo", "você está na metade", "ao final desta trilha" — vive na **casca** (box de trilha, página de trilha, página de percurso), nunca no conteúdo do artigo.

---

## 3. Checklist de Encadeabilidade (10 critérios objetivos)

Critérios verificáveis por inspeção, sem julgamento subjetivo. Cinco deles (1, 2, 3, 5, 6) são **automatizáveis via linter** — viram regra de publicação.

| # | Critério | Verificação | Auto? |
|---|---|---|---|
| 1 | **Título não contém número de ordem nem "Parte X"** | Regex no título: `Parte \d+`, `\d+ -`, `Passo \d+` | ✅ |
| 2 | **Não usa expressões de posição relativa no corpo** | Buscar: "como vimos antes/anteriormente", "no artigo anterior", "no próximo artigo/passo", "a seguir veremos", "como mostrado anteriormente" | ✅ |
| 3 | **Tem seção explícita de pré-requisitos no topo** (mesmo que vazia) | Presença do bloco "Antes de começar" / "Pré-requisitos" | ✅ |
| 4 | **Pré-requisitos são linkados, não pressupostos** | Cada item da lista tem `<a href>` para outro artigo (ou declara link externo) | Parcial |
| 5 | **Tem seção explícita de "o que você sabe ao fim"** | Presença do bloco de saída ("O que você sabe fazer agora" / "Resultado esperado") | ✅ |
| 6 | **Próximos passos são lista plural, não item único** | Rodapé tem N ≥ 2 caminhos sugeridos (ou nenhum). Nunca um único "próximo" | ✅ |
| 7 | **Exemplos são autocontidos** | Nenhum exemplo referencia "o exemplo do artigo X" ou "use o curso que criamos antes" | Manual |
| 8 | **Screenshots têm contexto próprio** | Cada screenshot tem legenda dizendo onde foi tirada | Manual |
| 9 | **Vocabulário é definido na primeira ocorrência local** | Termo técnico aparece pela primeira vez explicado/linkado *neste* artigo | Manual |
| 10 | **Teste do artigo solto** | Removendo o box de trilha, o artigo ainda faz sentido | Manual |

### Como esse checklist entra no fluxo

- **Camada 5 (Rubrica de Qualidade)** vai consumir esses 10 critérios como dimensão de **Atomicidade** (ou expansão de "Completude").
- **Camada 9 (ContentOps)** inclui o checklist como etapa obrigatória do fluxo de revisão pré-publicação.
- O **linter automatizado** (Fase 3) implementa os 5 critérios automatizáveis como verificação pré-publicação.

---

## 4. Catálogo de Padrões

### 4.1 — Artigo encadeável (padrão estrutural raiz)

Define a estrutura mínima de qualquer artigo da base.

| Atributo | Valor |
|---|---|
| **Quando usar** | Todos os artigos da base, sem exceção |
| **Estrutura mínima** | 1. Cabeçalho (Categoria · Tipo → H1 → Subtítulo → Autor + tempo → Multimodal → Índice) **·** 2. Bloco de entrada (pré-requisitos + objetivo) **·** 3. Miolo do artigo **·** 4. Bloco de saída (o que você sabe fazer agora + próximos passos plurais) **·** 5. Rodapé (relacionados + feedback + ABNT) |
| **Por que funciona** | Garante que o artigo funcione lido sozinho E encaixado em uma trilha. A entrada e saída explícitas permitem que o leitor saiba se está no lugar certo, independente de como chegou |
| **Armadilha** | Pré-requisitos pressupostos em vez de declarados ("agora que você já tem o questionário criado…" sem linkar como criar) |

**Decisão de origem:** Decisões 18, 23, 24, 26
**Referência:** `prototipo-artigo.html` (todo o layout)

---

### 4.2 — Box de trilha multi-trilha (sidebar)

Componente que aparece no sidebar do artigo quando ele pertence a uma ou mais trilhas.

| Atributo | Valor |
|---|---|
| **Quando aparecer** | Sempre que o artigo está vinculado a pelo menos uma trilha (Decisão 28) |
| **Quando NÃO aparecer** | Quando o artigo não pertence a nenhuma trilha |
| **Cardinalidade** | Suporta 1 a N trilhas. Sem limite técnico; alerta editorial acima de 5 trilhas |

**Estrutura visual:**

```
┌────────────────────────────────────────┐
│ TRILHAS DESTE ARTIGO              [N] │  ← cabeçalho com contador
├────────────────────────────────────────┤
│ Nome da trilha 1            5/12  ▼   │  ← item expandido
│ ┌──────────────────────────────────┐  │
│ │ 📖 Faz parte do percurso X       │  │  ← chip de percurso (se aplicável)
│ │ ▓▓▓▓▓░░░░░  Artigo 5 de 12       │  │  ← barra estrutural
│ │ 1. Artigo um                     │  │
│ │ 2. Artigo dois                   │  │
│ │ 3. ...                           │  │
│ │ 5. Artigo atual (destacado)      │  │
│ │ 6. ...                           │  │
│ └──────────────────────────────────┘  │
│ Nome da trilha 2            3/9   ▶   │  ← item colapsado
└────────────────────────────────────────┘
```

**Regras:**

- **Posição "X/Y"** visível mesmo quando o item está colapsado — ajuda o leitor a comparar trilhas sem expandir.
- **Primeira trilha expandida por padrão.**
- **Múltiplas trilhas abertas simultaneamente** são permitidas (não é acordeão exclusivo).
- **Texto da posição é "Artigo X de Y"**, nunca "Passo X de Y" — "Passo" fica reservado a itens de percurso (Decisão 29).
- **Barra de progresso é estrutural**, não pessoal — preenchimento representa a posição relativa do artigo na trilha (Decisão 29).

**Decisões de origem:** Decisões 18, 28, 29, 30
**Referência:** `prototipo-artigo.html` (componente `.side-trilha`), `drafts/exploracao-multiplas-trilhas.html` (sub-opção A.2)

---

### 4.3 — Chip de atribuição a percurso

Sinaliza, dentro do box de trilha, que aquela trilha faz parte de um percurso.

| Atributo | Valor |
|---|---|
| **Quando usar** | Toda trilha que pertence a pelo menos um percurso |
| **Posição** | Topo do conteúdo expandido do item da trilha (acima da barra de progresso) |
| **Cor** | Fundo `--gold-soft`, texto `--gold-deep`, ícone de "livro aberto" |
| **Comportamento** | Clicável; leva à página dedicada do percurso |
| **Texto-padrão** | "Faz parte do percurso **{Nome do Percurso}**" |

**Quando a trilha pertence a múltiplos percursos** (raro, mas possível): mostrar chips empilhados em ordem editorial. Mais de 3 percursos é sinal de alerta — provavelmente a trilha foi mal classificada.

**Decisão de origem:** Decisão 31
**Referência:** `drafts/exploracao-pagina-percurso.html` (Parte 2, mini-demo), `prototipo-artigo.html` (chip aplicado)

---

### 4.4 — Página de trilha

| Atributo | Valor |
|---|---|
| **Quando usar** | Toda página dedicada de uma trilha (URL `/trilhas/{slug}`) |
| **Quando NÃO usar** | Trilhas com 0 artigos publicados (a página não existe até a trilha ter conteúdo) |

**Estrutura obrigatória** (na ordem):

1. **Hero narrativo**
   - Kicker "Trilha" em pílula **verde** (`--accent-soft`) com ícone — diferencia visualmente do kicker dourado do percurso
   - H1 do nome da trilha
   - Subtítulo de uma linha
   - 2-3 parágrafos de descrição pedagógica explicando o que a trilha cobre, para quem é e por que a ordem dos artigos importa
   - **Chip dourado de percurso** (Padrão 4.3) se a trilha pertencer a um ou mais percursos
2. **Stats card** (lateral no desktop)
   - N artigos em sequência, ~Xh leitura, N pré-requisitos, N percursos vinculados
   - **CTA "Começar pelo primeiro artigo"** — único caso em todas as superfícies onde um CTA "começar" faz sentido, porque na trilha a ordem importa
3. **"Para quem é esta trilha"** + **"O que você vai dominar"** (duas colunas)
4. **Pré-requisitos da trilha** — bloco horizontal com lista de links para artigos da própria base (ou indicação clara de pré-requisitos externos)
5. **Lista ordenada dos artigos** (o coração da página)
   - Ver Padrão 4.4.1
6. **Resultado esperado ao final** — bloco destacado em verde com:
   - Label "Ao final desta trilha"
   - H3 com a conclusão do leitor (frase em voz ativa: "Você terá conduzido…")
   - 1-2 parágrafos sintetizando o que foi aprendido
   - Sugestões de próximas trilhas/artigos
7. **"Como esta trilha foi pensada"** — bloco narrativo curto explicando a lógica da ordem (3-4 frases)
8. **Trilhas relacionadas** — grid de 3 cards (mesmo percurso ou outros)
9. **Sobre esta trilha** (rodapé editorial)
   - Curadoria, datas, política de revisão
   - Box destacado dourado: "Pertence ao percurso X" com link

**Decisões propositais:**

- **CTA "Começar pelo primeiro artigo" existe** (diferente da página de percurso, que não tem). Justificativa: na trilha a ordem importa; no percurso, não.
- **Sem barra de progresso na página da trilha** — só posição estrutural de cada artigo (Decisão 29).
- **Verde IFES é a cor reservada da trilha** — kicker, stats border, CTA, hover dos cards.
- **Dourado aparece apenas no chip de percurso e no box de pertencimento** — sinaliza atribuição, não identidade da trilha.

### 4.4.1 — Item de artigo na lista da trilha

Cada artigo na lista numerada da página de trilha tem:

- **Número de ordem** em círculo destacado (1, 2, 3…) — animação de hover muda para fundo verde
- **Card clicável** com: H3 do título do artigo, badge de tipo (Tutorial / Referência / Conceitual / Solução / Recurso), tempo estimado de leitura, descrição curta (1-2 linhas)
- **Stream visual vertical** — linha conectando os números, indica continuidade
- **Checkpoints intermediários opcionais** entre artigos (a cada 3-5 artigos): bloco em verde claro com texto curto da curadoria sinalizando fim de "bloco temático" e o que vem a seguir. **Texto estático escrito pela curadoria** (não rastreamento pessoal — compatível com Decisão 29)

**Decisões de origem:** Decisões 18, 23, 25, 27, 29, 31
**Referência:** `drafts/exploracao-pagina-trilha.html`

---

### 4.5 — Página de percurso

| Atributo | Valor |
|---|---|
| **Quando usar** | Toda página dedicada de um percurso (URL `/percursos/{slug}`) |
| **Quando NÃO usar** | Não confundir com página de categoria — categoria classifica, percurso narra |

**Estrutura obrigatória** (na ordem):

1. **Hero narrativo**
   - Kicker "Percurso" em pílula dourada com ícone
   - H1 do nome do percurso
   - Subtítulo (uma linha)
   - 2-3 parágrafos de descrição pedagógica explicando por que esse conjunto faz sentido
2. **Stats card** (lateral no desktop)
   - N trilhas, M artigos em trilhas, K artigos complementares, ~Xh leitura
   - Texto-rodapé do card: "Sem ordem obrigatória, sem certificado, sem rastreamento"
3. **"Para quem é este percurso"** + **"O que você vai dominar"** (duas colunas)
4. **"Como percorrer este conjunto"** (bloco em verde claro)
   - 3 sugestões de ponto de partida por perfil
   - Resolve a ausência de ordem fixa sem forçar uma
5. **Cards das trilhas** (grid de 2 colunas)
   - Ver Padrão 4.6
6. **Artigos complementares** (grid de 3 colunas, cards compactos)
   - Apenas se houver artigos soltos no percurso
7. **Sobre este percurso** (rodapé editorial)
   - Curadoria, data de criação, última revisão
   - Lista de outros percursos relacionados

**Decisões propositais:**

- **Não há botão "Começar percurso"** — não há ordem fixa.
- **Não há barra de progresso na página de percurso** — só composição estática (Decisão 27, 29).
- **Sem certificado, sem badge, sem conclusão.**

**Decisões de origem:** Decisões 18, 27, 31
**Referência:** `drafts/exploracao-pagina-percurso.html` (Parte 1)

---

### 4.6 — Card de trilha em página de percurso

Card individual de cada trilha listada numa página de percurso.

| Atributo | Valor |
|---|---|
| **Estrutura** | Kicker "Trilha" → H3 do nome → contador de artigos → descrição (1-2 linhas) → lista dos **primeiros 5 artigos** → CTA "Começar pela primeira" + tempo estimado |
| **Acento visual** | Borda lateral verde (`--accent`) de 3px à esquerda |
| **Hover** | Border-color → verde, translate-y -2px, sombra média |

**Regra de exibição dos artigos:**

| Tamanho da trilha | O que mostrar |
|---|---|
| ≤ 5 artigos | Todos visíveis, sem indicador de "+N" |
| > 5 artigos | Primeiros 5 + linha "+ N artigos" em verde, ao final |

**Decisões de origem:** Decisões 25 (tamanho de trilha), 31 (página de percurso)
**Referência:** `drafts/exploracao-pagina-percurso.html` (seção "Trilhas deste percurso")

---

### 4.7 — Card de percurso em listagem

Card que aparece na página de listagem `/percursos`.

| Atributo | Valor |
|---|---|
| **Estrutura** | Kicker mini "Percurso" → H4 do nome → descrição (1-2 linhas) → footer com `N trilhas · M artigos · ~Xh` |
| **Acento visual** | Borda lateral **dourada** (`--gold`) de 4px à esquerda — diferencia de cards de artigo/categoria |
| **Hover** | Border-color → dourada, translate-y -2px, sombra média |

**Por que dourado:** cor reservada do percurso (Decisão 31). Sinaliza visualmente que é uma camada acima — categoria/tópico ficam neutros.

**Decisão de origem:** Decisão 31
**Referência:** `drafts/exploracao-pagina-percurso.html` (Parte 3)

---

## 5. Regras de Composição

### 5.1 Cardinalidade

| Entidade | Mínimo | Máximo | Decisão |
|---|---|---|---|
| **Artigo solto** (fora de trilhas e percursos) | — | — | Permitido, mas raro |
| **Trilha** | 3 artigos | Sem limite técnico | Decisão 25 |
| **Artigo em trilhas** | 0 | Sem limite técnico | Decisão 18 |
| **Trilha em percursos** | 0 | Sem limite técnico | Decisão 27 |
| **Percurso** | 1 trilha **ou** ≥ 1 artigo solto | Sem limite | Decisão 18 |

### 5.2 Alertas de saúde (não bloqueantes)

Sinais para revisão editorial. Não impedem publicação, mas entram em relatório mensal (Camada 10).

| Sinal | Alerta | Interpretação provável |
|---|---|---|
| Trilha com > 10 artigos | Amarelo | Pode ter virado um mini-percurso disfarçado. Avaliar quebra em trilhas menores. |
| Trilha com < 3 artigos | Bloqueante | Não atende cardinalidade mínima. Não publica. |
| Artigo em 1-3 trilhas | Verde | Ideal |
| Artigo em 4-5 trilhas | Amarelo | Verificar se o artigo não ficou genérico demais |
| Artigo em ≥ 6 trilhas | Vermelho | Provavelmente artigo "curinga" que deveria virar 2-3 artigos mais específicos, ou virar um conceitual fora de trilhas |
| Trilha sem chip de percurso | Verde | Trilha standalone — comportamento esperado |
| Trilha em ≥ 4 percursos | Amarelo | Curadoria provavelmente confusa — revisar |

### 5.3 Regras do conteúdo do artigo (consequências da encadeabilidade)

| Regra | O que NÃO fazer | O que fazer |
|---|---|---|
| **Sem expressões de posição relativa** | "Como vimos anteriormente…" | "[Conceito X], como definido [aqui]…" |
| **Sem título numerado** | "Parte 3: Configurando feedback" | "Configurando feedback por questão" |
| **Pré-requisitos explícitos no topo** | "Agora que você criou o questionário…" | "Este artigo assume que você já criou um questionário. [Veja como criar]" |
| **Saída explícita** | Texto termina abruptamente após últimos passos | "O que você sabe fazer agora" / "Resultado esperado" |
| **Próximos passos plurais** | "Próximo passo: configurar feedback" | "Próximos caminhos: [Configurar feedback] · [Exportar notas] · [Aplicar rubricas]" |

---

## 6. Mapeamento padrão → Decisão → Referência

| Padrão | Decisões de origem | Arquivo de referência canônica |
|---|---|---|
| 4.1 — Artigo encadeável | 18, 23, 24, 26 | `prototipo-artigo.html` |
| 4.2 — Box de trilha multi-trilha | 18, 28, 29, 30 | `prototipo-artigo.html` (`.side-trilha`), `drafts/exploracao-multiplas-trilhas.html` (A.2) |
| 4.3 — Chip de atribuição a percurso | 31 | `drafts/exploracao-pagina-percurso.html` (Parte 2) + `prototipo-artigo.html` |
| 4.4 — Página de trilha | 18, 23, 25, 27, 29, 31 | `drafts/exploracao-pagina-trilha.html` |
| 4.4.1 — Item de artigo na lista da trilha | 18, 23, 25 | `drafts/exploracao-pagina-trilha.html` (seção "Lista de Artigos") |
| 4.5 — Página de percurso | 18, 27, 31 | `drafts/exploracao-pagina-percurso.html` (Parte 1) |
| 4.6 — Card de trilha em página de percurso | 25, 31 | `drafts/exploracao-pagina-percurso.html` |
| 4.7 — Card de percurso em listagem | 31 | `drafts/exploracao-pagina-percurso.html` (Parte 3) |

---

## 7. O que esta camada NÃO faz

Para evitar sobreposição com outras camadas:

| Esta camada NÃO… | Quem faz |
|---|---|
| Define cores em hexa, fontes específicas, tamanhos exatos | **Design System** (Fase 2) |
| Define a voz e tom dos textos dentro do artigo | **Camada 2 — Voz e Tom** |
| Define o que é um termo "preferido" do vocabulário | **Camada 3 — Vocabulário Controlado** |
| Define como escrever um tutorial passo a passo | **Camada 4 — Padrões de Conteúdo** |
| Define se um artigo é "bom" ou "ruim" | **Camada 5 — Rubrica de Qualidade** |
| Define legibilidade (Flesch, palavras por frase) | **Camada 6 — Legibilidade** |
| Define quando depreciar conteúdo | **Camada 8 — Depreciação** |

A Camada 4.5 define **a arquitetura de composição**. Cores, voz, qualidade e legibilidade dos padrões aqui especificados são responsabilidade das outras camadas.

---

## 8. Entregáveis para a Fase 2 (Design System)

A Fase 2 precisa implementar como componentes reutilizáveis:

| Componente DS | Padrão de origem | Cor/identidade |
|---|---|---|
| `BoxTrilhaAcordeao` | 4.2 | Verde IFES (`--accent`) |
| `ChipPercurso` | 4.3 | Dourado (`--gold-soft` + `--gold-deep`) |
| `PaginaTrilhaHero` | 4.4 | Kicker em pílula verde |
| `StatsCardTrilha` | 4.4 | Border-left verde nos stats |
| `ListaArtigosTrilha` | 4.4.1 | Stream vertical com números em círculo |
| `CheckpointIntermediario` | 4.4.1 | Bloco em `--accent-soft` |
| `ResultadoEsperadoTrilha` | 4.4 | Border `--accent` 2px |
| `PaginaPercursoHero` | 4.5 | Kicker em pílula dourada |
| `StatsCardComposicao` | 4.5 | Border-left dourado nos stats |
| `BlocoComoPercorrer` | 4.5 | Fundo `--accent-soft` |
| `CardTrilhaEmPercurso` | 4.6 | Border-left verde |
| `CardPercursoListagem` | 4.7 | Border-left dourado |

Tokens de design já definidos no `prototipo-artigo.html`:
- `--gold` `#b08544` (cor principal do percurso)
- `--gold-soft` `#f3e7d0` (fundo de chips/pílulas)
- `--gold-deep` `#8c6a36` (texto em fundos suaves)
- `--accent` `#1f5142` (verde IFES — trilha)
- `--accent-soft` `#e3ecdf` (fundo verde claro)

---

## 9. O que ainda falta nesta camada

- [x] ~~Padrão "Página de trilha" (4.4)~~ — **concluído em 2026-05-19** (`drafts/exploracao-pagina-trilha.html`)
- [ ] **Padrão "Listagem de trilhas"** — página `/trilhas`, semelhante a 4.7 mas com cor verde
- [ ] **Padrão "Recomendação de próximo artigo"** — refinamento futuro: quando o leitor chega ao fim de um artigo, o que mostrar como sugestão?
- [ ] **Padrão "Artigo solto em percurso"** — artigos complementares ainda não têm padrão dedicado dentro de uma trilha (eles aparecem fora dela na página do percurso)
- [ ] **Validação com Rute e Marquito** — todos os padrões aqui foram derivados de decisões tomadas só com Elton

---

## 10. Histórico de versões

| Versão | Data | Mudança | Por |
|---|---|---|---|
| 1.0 | 2026-05-19 | Versão inicial consolidando Decisões 17, 18, 22, 25-32 | Elton + Claude |
| 1.1 | 2026-05-19 | Padrão 4.4 (Página de trilha) preenchido. Adicionado padrão 4.4.1 (Item de artigo na lista). Fecha o triângulo Artigo/Trilha/Percurso visualmente. | Elton + Claude |

---

*Camada 4.5 do Content System · Base de Conhecimento CEFOR/IFes · Fase 1 — Fundações*
