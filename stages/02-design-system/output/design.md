---
name: Base de Conhecimento CEFOR/IFes
version: alpha
description: >
  Design System da Base de Conhecimento do CEFOR/IFes — plataforma pública de
  formação em serviço para profissionais de EaD. Estética "papel editorial":
  fundo branco quente, tinta quase-preta, verde IFES como acento institucional
  e dourado reservado à camada de percurso. 100% sans-serif, acessível por
  padrão (WCAG 2.2 AA + e-MAG), com modo escuro e alto contraste desde o dia 1.
  Tokens são a fonte única de verdade para a implementação WordPress (Fase 3).

# ============================================================
# COLORS — modo claro (default). Modos escuro e alto contraste
# em ## Colors > Modos. Token = nome da CSS custom property.
# Decisões 7 (fundo branco), 8 (dark mode), 10 (alto contraste).
# ============================================================
colors:
  # Superfícies
  bg: "#ffffff"          # fundo geral da página
  bg-2: "#f7f5f1"        # blocos sutis, hover, sidebar
  bg-3: "#efeae0"        # blocos de destaque neutro
  paper: "#ffffff"       # superfície de cards
  # Tinta (texto)
  ink: "#14110d"         # títulos e texto principal
  ink-2: "#4a4439"       # corpo de texto, parágrafos
  ink-3: "#8a8273"       # metadados, legendas, placeholders
  # Linhas e divisores
  line: "#e7e3d8"        # bordas padrão, divisores
  line-2: "#d4cdba"      # bordas de ênfase
  # Verde IFES — acento institucional + identidade da TRILHA
  accent: "#1f5142"      # links, botões, foco, identidade da trilha
  accent-2: "#2d6a4f"    # hover de verde
  accent-soft: "#e3ecdf" # fundos de pílula/callout verde
  accent-deep: "#143a30" # texto sobre fundo verde claro
  # Dourado — RESERVADO ao PERCURSO (Decisão 31)
  gold: "#b08544"        # borda/acento de percurso
  gold-soft: "#f3e7d0"   # fundo de chip de percurso
  gold-deep: "#8c6a36"   # texto sobre fundo dourado claro
  # Semânticas (callouts — Decisão 5)
  sky: "#2c5e8f"         # Informação / Nota
  sky-soft: "#d9e7f3"
  sun: "#c98a1e"         # Atenção
  sun-soft: "#f7e6c4"
  rose: "#b3433a"        # Cuidado / risco
  rose-soft: "#f4dcd7"
  violet: "#7a5a9b"      # Acessibilidade (cor reservada)
  violet-soft: "#ece3f2"
  violet-deep: "#553d70"
  # Papéis convencionais (mapeamento para o schema)
  primary: "#1f5142"     # = accent
  secondary: "#b08544"   # = gold
  surface: "#ffffff"     # = bg
  text: "#14110d"        # = ink
  text-muted: "#8a8273"  # = ink-3
  border: "#e7e3d8"      # = line
  error: "#b3433a"       # = rose
  warning: "#c98a1e"     # = sun
  info: "#2c5e8f"        # = sky
  success: "#1f5142"     # afirmativo reusa o verde institucional

# ============================================================
# TYPOGRAPHY — 100% sans-serif (Decisão 6). Inter no texto,
# JetBrains Mono em código, Lexend como alternativa dislexia.
# fontSize base = 16px; escala em rem. Diferenciação por
# peso/tamanho/espaçamento, não por contraste serifada/sans.
# ============================================================
typography:
  h1:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 3rem          # 48px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.015em
  h2:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 1.8rem        # ~29px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.01em
  h3:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 1.3rem        # ~21px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0em
  subtitle:                 # subtítulo obrigatório do artigo (Decisão 16)
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 1.18rem       # ~19px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0em
  body:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 1rem          # 16px (escala com --font-scale via A-/A+)
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0em
  meta:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 0.82rem       # ~13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0em
  kicker:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 0.72rem       # ~11.5px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.14em
    textTransform: uppercase
  label:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 0.9rem        # rótulos de botão
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0em
  mono:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: 0.82rem
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0em
  dyslexic:                 # alternativa por preferência do usuário (Decisão 10)
    fontFamily: "Lexend, Inter, sans-serif"

# ============================================================
# ROUNDED — quanto maior o elemento, maior o raio.
# ============================================================
rounded:
  sm: 6px       # --r-sm — chips, code inline, botões pequenos
  md: 10px      # --r-md — botões, callouts, inputs, code block
  lg: 16px      # --r-lg — cards
  xl: 24px      # --r-xl — superfícies grandes, modais
  full: 99px    # pílulas (kicker, badge, chip, toggle)

# ============================================================
# SPACING — escala base de múltiplos de 4px.
# ============================================================
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px
  3xl: 64px

# ============================================================
# COMPONENTS — props normativas. Detalhamento em ## Components.
# ============================================================
components:
  button-primary:
    background: accent
    color: "#ffffff"
    hoverBackground: accent-2
    padding: 10px 20px
    rounded: md
    fontWeight: 600
  button-secondary:
    background: paper
    color: accent
    border: 1px solid line-2
    hoverBorder: accent
    rounded: md
  button-ghost:
    background: transparent
    color: ink-2
    hoverBackground: bg-2
    rounded: md
  card:
    background: paper
    border: 1px solid line
    rounded: lg
    padding: 22px 24px
    hoverBorder: accent
    hoverTransform: translateY(-2px)
    hoverShadow: shadow-md
  card-trilha:
    accentBar: accent        # borda lateral verde 4px
  card-percurso:
    accentBar: gold          # borda lateral dourada 4px
    hoverBorder: gold
  callout:
    rounded: md
    borderLeft: 4px solid
    padding: 16px 18px 16px 20px
  badge-tipo:
    background: bg-2
    color: ink-2
    rounded: full
  badge-categoria:
    background: transparent
    color: ink-3
    border: 1px solid line-2
    rounded: full
  kicker-trilha:
    background: accent-soft
    color: accent-deep
    rounded: full
  kicker-percurso:
    background: gold-soft
    color: gold-deep
    rounded: full

# ============================================================
# ELEVATION — sombras discretas (papel não flutua muito).
# ============================================================
elevation:
  shadow-sm: "0 1px 2px rgba(20,17,13,.04)"
  shadow-md: "0 4px 12px rgba(20,17,13,.06), 0 2px 4px rgba(20,17,13,.04)"
  shadow-lg: "0 24px 48px -12px rgba(20,17,13,.12)"

# ============================================================
# BREAKPOINTS — comportamento responsivo (Pilar 9).
# ============================================================
breakpoints:
  mobile: 600px
  tablet: 860px
  desktop: 1024px
---

## Overview

A Base de Conhecimento do CEFOR/IFes é um **instrumento de formação em serviço** para profissionais de EaD do IFES — não um repositório, mas um espaço onde qualquer profissional resolve problemas com autonomia e se mantém atualizado (Decisão 1). O design precisa servir duas funções na mesma superfície: **consulta** ("preciso da resposta agora") e **aprendizagem contínua** ("quero evoluir").

A linguagem visual é deliberadamente **editorial e sóbria** — "papel de qualidade". Fundo branco quente, tinta quase-preta, muito respiro, e cor usada com economia. A regra-mãe da identidade cromática: **cor narra hierarquia**. O leitor sabe em que nível está só pela cor — verde é trilha e ação institucional, dourado é exclusivamente percurso, e tudo que é classificação (categoria, tópico) fica em neutro. Cards são pouco delimitados (Decisão 7): separam-se por respiro e tipografia, não por contorno forte ou sombra pesada.

Três compromissos inegociáveis atravessam todos os tokens:

1. **100% sans-serif** (Decisão 6) — hierarquia por peso, tamanho e espaçamento, nunca por contraste serifada/sans.
2. **Acessibilidade por padrão** (Decisão 10) — WCAG 2.2 AA + e-MAG. Modo escuro, alto contraste e fonte para dislexia são tokens, não retoques. Por ser instituição pública federal, isso é cumprimento legal, não diferencial.
3. **Tokens como fonte única de verdade** — todo valor visual vive como CSS custom property. Trocar de tema é trocar variáveis, nunca reescrever CSS. É o que torna a Fase 3 (WordPress) barata.

> **Fonte canônica dos tokens:** `stages/02-design-system/drafts/kit-visual.html` (style guide vivo, interativo, com os modos claro/escuro/contraste demonstráveis). A interface de referência do artigo é `stages/01-fundacoes/drafts/prototipo-artigo.html` (Decisão 22). Este `design.md` é a destilação normativa dos dois para levar à implementação.

## Colors

A paleta é construída em camadas de papel: três superfícies (branco, branco quente, bege neutro), três tons de tinta e duas linhas de divisor. Sobre essa base monocromática entram dois acentos institucionais e quatro semânticos — cada um com um trabalho exclusivo.

**Verde IFES (`accent` `#1f5142`)** é a cor de ação e de pertencimento: links, botões primários, foco de teclado, identidade da **trilha**. É a única cor "quente de marca" que aparece com frequência. **Dourado (`gold` `#b08544`)** é a assinatura visual do **percurso** — e *somente* do percurso (Decisão 31). Chip de atribuição, borda lateral de card de percurso, kicker de percurso. Usar dourado para qualquer outra coisa quebra a leitura de hierarquia.

As cores semânticas servem aos callouts (Decisão 5) e nunca competem com verde/dourado: **`sky`** (informação/nota), **`sun`** (atenção), **`rose`** (cuidado/risco) e **`violet`** (acessibilidade — cor reservada que comunica a bandeira de inclusão do CEFOR sem depender da escrita do autor).

A tinta é narrow de propósito: `ink` para títulos, `ink-2` para o corpo (o texto que o leitor habita por minutos), `ink-3` para metadados e legendas. Categoria e tópico — que classificam, não narram — vivem só em tinta neutra, sem cor própria.

### Modos

Os três modos são trocas de tokens, ativados por atributos no `<html>`. Convivem: alto contraste e fonte-dislexia são toggles independentes do par claro/escuro.

**Modo escuro** (`[data-theme="dark"]`) — Decisão 8. Inverte superfícies (fundo `#0e0c0a`, papel `#1a1612`) e tinta (`#f4f1ea`). O verde clareia para `#6cb89a` e o dourado para `#d9a955`, preservando contraste sobre fundo escuro. Respeita `prefers-color-scheme` como padrão.

| Token | Claro | Escuro |
|---|---|---|
| `bg` | `#ffffff` | `#0e0c0a` |
| `paper` | `#ffffff` | `#1a1612` |
| `ink` | `#14110d` | `#f4f1ea` |
| `ink-2` | `#4a4439` | `#c9c2b3` |
| `line` | `#e7e3d8` | `#2a251e` |
| `accent` | `#1f5142` | `#6cb89a` |
| `gold-deep` | `#8c6a36` | `#d9a955` |

**Alto contraste** (`[data-contrast="high"]`) — Decisão 10, alvo WCAG AAA. Esquema preto/amarelo: fundo `#000000`, texto `#ffff00`, linhas `#ffff00`/`#ffffff`, verde vira `#00ff88`. As semânticas ganham versões saturadas (`rose #ff6b6b`, `sun #ffaa00`, `sky #66ccff`, `violet #cc88ff`).

**Fonte para dislexia** (`[data-font="dyslexic"]`) — troca `--sans` por Lexend, sem mexer em cor ou layout.

## Typography

Uma família para tudo: **Inter** (Decisão 6). A diferenciação hierárquica vem de peso (400/500/600/700), tamanho e espaçamento de letra — nunca de troca serifada/sans. **JetBrains Mono** carrega código e valores técnicos; **Lexend** é a alternativa de leitura para dislexia, ativável pelo usuário.

A escala parte de 16px (corpo) e respira para cima. O corpo roda a `1rem / 1.65` em `ink-2` — calibrado para leitura técnica sustentada (Pilar 6). O tamanho base é multiplicado por `--font-scale`, controlado pelos botões **A- / A+** do widget de acessibilidade, então toda a escala em `rem` reescala junta.

| Papel | Tamanho | Peso | Line-height | Uso |
|---|---|---|---|---|
| H1 | 3rem (48px) | 700 | 1.05 | Título do artigo, hero |
| H2 | 1.8rem | 700 | 1.2 | Seções (alvos do índice) |
| H3 | 1.3rem | 700 | 1.3 | Subseções |
| Subtítulo | 1.18rem | 400 | 1.5 | Subtítulo obrigatório do artigo (Decisão 16) |
| Corpo | 1rem | 400 | 1.65 | Texto-base, parágrafos |
| Meta | 0.82rem | 400 | 1.4 | Autor, tempo de leitura, legendas |
| Kicker | 0.72rem | 700 | — | Rótulos em caixa alta (`letter-spacing .14em`) |
| Label | 0.9rem | 600 | — | Rótulos de botão |
| Mono | 0.82rem | 400 | 1.5 | Código inline e blocos |

O **subtítulo** é tipograficamente distinto de propósito: mesma família, peso regular, tamanho intermediário entre H1 e corpo, em `ink-2`. Delimita o escopo do artigo numa frase (Decisão 16). O **kicker** é o rótulo curto em caixa alta que identifica tipo de página/conteúdo; sua cor segue a identidade cromática (verde na trilha, dourado no percurso, neutro no resto).

## Layout

O grid central é a **coluna de leitura** flanqueada por uma sidebar de navegação contextual. A largura da coluna de texto segue a recomendação de leitura técnica (~65–72ch). Espaçamento na escala de 4px — `md (16px)` é o ritmo interno de componentes, `lg (24px)` o gutter entre blocos, `2xl (48px)`/`3xl (64px)` separam seções maiores.

**Sidebar do artigo** abriga, sempre presentes quando aplicáveis:
- **Índice "Neste artigo"** com scroll-tracking *sticky* — sempre visível, seção atual destacada (Decisão 4). Obrigatório em artigos com 4+ seções.
- **Box de trilha multi-trilha** (acordeão) — sempre exibido quando o artigo pertence a ≥1 trilha, por vínculo estrutural do CMS, não por referrer (Decisões 28, 30).

**Comportamento responsivo** (Pilar 9, Decisão 13 — site sempre responsivo, sem abas desktop/mobile):

| Breakpoint | Comportamento |
|---|---|
| `mobile` ≤ 600px | Sidebar colapsa; índice vira drawer/acordeão recolhível; barra de ações vira rodapé fixo ou menu; tabelas com scroll horizontal; código com scroll-x |
| `tablet` ≤ 860px | Sidebar pode recolher; grid de cards cai para 1–2 colunas |
| `desktop` ≥ 1024px | Layout pleno: coluna de leitura + sidebar sticky |

Páginas-chave a desenhar (Pilar — Fase 2, Step 7): Home, Artigo (referência canônica pronta), Trilha, Percurso (`drafts/exploracao-pagina-percurso.html`), Listagem `/percursos`, Busca (modal Ctrl+K), Categoria.

## Elevation & Depth

Elevação é discreta — papel editorial não flutua. Três níveis apenas:

- **`shadow-sm`** — `0 1px 2px rgba(20,17,13,.04)`. Separação mínima, quase imperceptível.
- **`shadow-md`** — `0 4px 12px ...`. Estado *hover* de cards.
- **`shadow-lg`** — `0 24px 48px -12px ...`. Modais (busca Ctrl+K), drawers, popovers.

Cards em repouso usam **borda + respiro**, não sombra (Decisão 7 — cards menos delimitados). A sombra entra só na interação (hover de card sobe `translateY(-2px)` + `shadow-md`).

## Shapes

Quatro raios, escalando com o tamanho do elemento, mais a pílula:

- `sm 6px` — chips, code inline, botões pequenos
- `md 10px` — botões, callouts, inputs, blocos de código
- `lg 16px` — cards
- `xl 24px` — superfícies grandes, modais
- `full 99px` — pílulas: kicker, badge, chip de percurso, toggles, botões de ação circulares

Ícones são lineares (stroke), `stroke-width` ~2–2.4, `stroke-linecap/linejoin: round`, herdando `currentColor`. **Sem emoji na UI institucional** (Decisão 12) — feedback e ações usam ícone + texto, nunca carinhas.

## Components

Componentes derivados dos protótipos canônicos e da análise dos 131 artigos da base antiga. Cada um rastreia a decisão que o originou.

### Botões — 3 níveis de ênfase
- **Primário** (`button-primary`): fundo `accent`, texto branco, hover `accent-2`. Ação principal ("Começar pela primeira trilha"). `padding 10px 20px`, `rounded md`.
- **Secundário** (`button-secondary`): fundo `paper`, texto `accent`, borda `line-2`, hover borda `accent`. Ação alternativa.
- **Fantasma** (`button-ghost`): transparente, texto `ink-2`, hover fundo `bg-2`. Ações terciárias (compartilhar, copiar).

### Kickers e pílulas
Rótulo curto em caixa alta identificando tipo de página. **Trilha** = `accent-soft`/`accent-deep` com ícone de nó-no-caminho; **Percurso** = `gold-soft`/`gold-deep` com ícone de livro aberto. `rounded full`.

### Badges (metadados de taxonomia — Eixos 1 e 2, Decisão 17)
- **Tipo de artigo** (`badge-tipo`, fundo cheio neutro): Tutorial · Referência · Conceitual · Solução de Problema · Recurso.
- **Categoria** (`badge-categoria`, contorno): Ferramentas e Recursos · Pedagogia e Planejamento · Acessibilidade · Conduta e Conformidade · Identidade · *(6ª a definir)*.

### Callouts — 6 tipos (Decisão 5)
Bloco de destaque com `border-left 4px` + fundo soft. Quatro de severidade + dois contextuais do CEFOR:

| Tipo | Cor | Quando usar |
|---|---|---|
| **Dica** | `accent` (verde) | Atalho, boa prática |
| **Nota** | `sky` (azul) | Contexto, nota explicativa |
| **Atenção** | `sun` (amarelo) | Cuidado reversível, "confira antes" |
| **Cuidado** | `rose` (vermelho) | Ação de alto impacto, risco real |
| **Pré-requisito** | `ink-3` (neutro) | O que o leitor precisa ter antes |
| **Acessibilidade** | `violet` (roxo) | Lembrete de inclusão (audiodescrição, Libras) |

> Os tipos são *conceito* fixado aqui; a lista exata e regras de uso editorial pertencem à Camada 4 do Content System (Fase 1). As cores são fixadas pelo DS.

### Cards (previews de listagem)
`card` base: `paper`, borda `line`, `rounded lg`, hover sobe e ganha borda `accent` + `shadow-md`. Variantes por borda lateral de 4px: **artigo** (neutro), **trilha** (`card-trilha`, barra verde), **percurso** (`card-percurso`, barra dourada, hover dourado).

### Box de trilha multi-trilha (acordeão) — Decisões 28, 29, 30, 32
Componente da sidebar. Cabeçalho "Trilhas deste artigo" + contador. Cada trilha é um item de acordeão com nome + posição compacta (`5/12`) sempre visível mesmo colapsado + chevron. Primeira trilha expandida por padrão; múltiplas podem abrir juntas. Expandido mostra: chip de percurso dourado (se aplicável) → barra de progresso **estrutural** → "Artigo X de Y" (**nunca "Passo"** — Decisão 29) → lista numerada de artigos com o atual em `aria-current="page"`.

> A navegação entre artigos da trilha é **exclusiva deste acordeão** — não há prev/next no rodapé (Decisão 32). A barra representa posição estrutural do artigo na trilha, **não** progresso pessoal do leitor (V1 sem login, Decisão 29).

### Chip de percurso — Decisão 31
Pílula dourada (`gold-soft`/`gold-deep`) com ícone de livro: "Faz parte do percurso **X**". Aparece no topo do conteúdo expandido do item de trilha no acordeão. Clicável → página dedicada do percurso.

### Blocos multimodais — ordem fixa (Decisão 19)
No cabeçalho do artigo, sempre nesta ordem: **1. Libras** (accordion com tradução em Libras do texto completo) → **2. Ouvir** (narração em áudio, TTS ou gravada) → **3. Outros formatos** (podcast, infográfico-resumo, quando existirem). A audiodescrição de imagens é **texto visível para todos** (não só `alt`) — Decisão 13.

### Passo a passo (tutoriais)
Passos numerados sobre linha contínua, com espaço para captura de tela e **checkpoints de verificação** entre blocos. O checkpoint é sempre verificável visualmente ("você deve ver X"), nunca vago. É o componente do tipo de artigo mais comum no CEFOR.

### Componentes técnicos da base
- **Selo de versão do Moodle**: badge no cabeçalho ("Validado no Moodle 4.x"); variante *outdated* (revisão pendente) visível **só para admins**, nunca pública (Decisão 21).
- **Bloco MoodleCode**: para a categoria #MoodleCodes — código pronto para colar, com botão copiar e instrução de "onde colar".

### Feedback do leitor — Decisão 12
Dois botões com **texto literal**: **"Foi útil"** / **"Não foi útil"** (sem emoji). Ao marcar "Não foi útil", abre campo opcional "O que faltou?". Tom institucional.

### Rodapé do artigo — Decisões 20, 24, 32
Ordem: **Artigos relacionados** (obrigatório em todo artigo, Decisão 9) → **Feedback** ("Foi útil/Não foi útil") → **Citação ABNT** automática no formato `SOBRENOME, Nome. Título. Base de Conhecimento CEFOR/IFes, [ano]. Revisado em [data].`

### Busca (Decisão 11)
Modal central acionado por **Ctrl+K**, full-text, filtros por eixo de taxonomia, atalhos visíveis (ESC, setas, Enter), resultados agrupados por categoria. Resposta sintetizada por IA fica para a V2.

### Breadcrumb, progresso estrutural, índice sticky
Navegação de contexto refletindo a hierarquia de informação. Barra de progresso fina (`accent`) representa posição estrutural. Índice "Neste artigo" sticky com scroll-tracking (Decisão 4).

### Widget de acessibilidade (Decisão 10)
Flutuante na lateral, acessível por teclado: A-/A+ (escala de fonte via `--font-scale`), alto contraste, fonte para dislexia, VLibras, "Pular para o conteúdo". Toda a UI navegável por teclado com foco visível em `accent`.

## Do's and Don'ts

**Faça**
- Use **dourado apenas para percurso** e **verde para trilha/ação**. A cor é a forma do leitor saber em que nível está.
- Trate todo valor visual como token CSS — é o que mantém os 3 modos baratos e a Fase 3 viável.
- Separe cards por **respiro e tipografia**; reserve sombra para o hover.
- Diga "**Artigo** X de Y" dentro de trilha; "passo" só para itens de percurso.
- Garanta foco de teclado visível, contraste AA e audiodescrição visível em imagens informativas.
- Mantenha a coluna de leitura em ~65–72ch e o corpo a 16px / line-height 1.65.

**Não faça**
- Não use **emoji** na UI institucional (feedback, ações) — ícone + texto (Decisão 12).
- Não introduza **fontes serifadas** para criar hierarquia (Decisão 6).
- Não exiba badge de "desatualizado" para o público — é metadado administrativo (Decisão 21).
- Não use prev/next de trilha no rodapé — a navegação vive no acordeão da sidebar (Decisão 32).
- Não mostre progresso *pessoal* nem use localStorage na V1 — só posição estrutural (Decisão 29).
- Não delimite cards com contorno forte ou sombra pesada (Decisão 7).
- Não use bege/cinza no fundo geral — o fundo é branco quente (Decisão 7).

---

> **Procedência:** Tokens espelham `stages/02-design-system/drafts/kit-visual.html`. Componentes e regras rastreiam as Decisões 1–32 de `_config/decisoes.md` e os Pilares 1, 2, 5, 6, 8, 9 de `_config/pilares.md`. Interface de referência: `stages/01-fundacoes/drafts/prototipo-artigo.html` (Decisão 22). Schema conforme spec `design.md` (google-labs-code), versão alpha.
