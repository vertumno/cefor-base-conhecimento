---
name: Base de Conhecimento CEFOR/Ifes
version: beta
description: >
  Design System da Base de Conhecimento do CEFOR/Ifes — plataforma pública de
  formação em serviço para profissionais de EaD. Estética "papel editorial":
  fundo branco quente, tinta quase-preta, verde institucional refinado em
  quatro tons como marca, e uma família calibrada de cores para os artigos.
  100% sans-serif, acessível por padrão (WCAG 2.2 AA + e-MAG), com modo
  escuro e alto contraste desde o dia 1. Tokens são a fonte única de verdade
  para a implementação WordPress (Fase 3).

# ============================================================
# COLORS — modo claro (default). Todas as cores também
# expressas em OKLCH para garantir consistência perceptual.
# Hex é o fallback de implementação. Decisões 7, 8, 10.
# ============================================================
colors:
  # --------------------------------------------------------
  # Superfícies — três camadas de papel
  # --------------------------------------------------------
  bg:           "#ffffff"   # fundo geral da página
  bg-2:         "#f7f5f1"   # blocos sutis, hover, sidebar
  bg-3:         "#efeae0"   # blocos de destaque neutro
  paper:        "#ffffff"   # superfície de cards
  # --------------------------------------------------------
  # Tinta — texto em três pesos perceptuais
  # --------------------------------------------------------
  ink:          "#14110d"   # títulos, texto principal
  ink-2:        "#4a4439"   # corpo de texto, parágrafos
  ink-3:        "#8a8273"   # metadados, legendas, placeholders
  # --------------------------------------------------------
  # Linhas e divisores
  # --------------------------------------------------------
  line:         "#e7e3d8"   # bordas padrão, divisores
  line-2:       "#d4cdba"   # bordas de ênfase
  # --------------------------------------------------------
  # Marca — Verde institucional, refinado em quatro tons.
  # Mesma família de matiz (~158°), variando apenas em
  # luminosidade e chroma para cobrir todos os papéis de UI.
  # --------------------------------------------------------
  verde-profundo: "#1c4a36"   # oklch(0.34 0.054 158) — header, footer
  verde-marca:    "#2e7355"   # oklch(0.52 0.080 158) — CTAs, links, ênfase
  verde-claro:    "#6ea892"   # oklch(0.72 0.060 158) — hover, badges sutis
  verde-palido:   "#e6efe9"   # oklch(0.94 0.014 158) — fundos de seção
  # --------------------------------------------------------
  # Acento dourado suave — único remanescente da família
  # dourada. Aplicação livre (highlights, destaques quentes).
  # --------------------------------------------------------
  gold-soft:    "#f3e7d0"
  # --------------------------------------------------------
  # Família dos artigos — paleta principal.
  # Mesma calibração perceptual: L 0.64–0.82, C 0.10–0.18.
  # Nenhuma cor pré-atribuída a categoria, trilha ou seção
  # — atribuição é decisão de conteúdo, não do DS.
  # --------------------------------------------------------
  art-roxo:     "#9c6dcb"   # oklch(0.64 0.17 305)
  art-azul:     "#5d9bd8"   # oklch(0.72 0.13 235)
  art-ambar:    "#e8b53a"   # oklch(0.82 0.15 75)
  art-magenta:  "#c46aac"   # oklch(0.68 0.18 340)
  art-coral:    "#ed8366"   # oklch(0.74 0.16 35)
  art-teal:     "#5ea9b2"   # oklch(0.74 0.10 195)
  # --------------------------------------------------------
  # Família dos artigos — reservas.
  # Disponíveis para uso futuro caso a taxonomia expanda.
  # Mesma família perceptual da paleta principal.
  # --------------------------------------------------------
  art-rosa:     "#ed7b8a"   # oklch(0.74 0.17 12)
  art-laranja:  "#e88f3c"   # oklch(0.76 0.16 55)
  art-anil:     "#7b81d7"   # oklch(0.66 0.15 270)
  # --------------------------------------------------------
  # Semânticas — callouts (Decisão 5). Função fixa.
  # Independentes da família dos artigos.
  # --------------------------------------------------------
  sky:          "#2c5e8f"   # Informação / Nota
  sky-soft:     "#d9e7f3"
  sun:          "#c98a1e"   # Atenção
  sun-soft:     "#f7e6c4"
  rose:         "#b3433a"   # Cuidado / risco
  rose-soft:    "#f4dcd7"
  violet:       "#7a5a9b"   # Acessibilidade
  violet-soft:  "#ece3f2"
  violet-deep:  "#553d70"
  # --------------------------------------------------------
  # Papéis convencionais (mapeamento para o schema)
  # --------------------------------------------------------
  primary:      "#2e7355"   # = verde-marca
  secondary:    "#1c4a36"   # = verde-profundo
  surface:      "#ffffff"   # = bg
  text:         "#14110d"   # = ink
  text-muted:   "#8a8273"   # = ink-3
  border:       "#e7e3d8"   # = line
  error:        "#b3433a"   # = rose
  warning:      "#c98a1e"   # = sun
  info:         "#2c5e8f"   # = sky
  success:      "#2e7355"   # afirmativo reusa verde-marca

# ============================================================
# TYPOGRAPHY — 100% sans-serif (Decisão 6). Inter no texto,
# JetBrains Mono em código, Lexend para dislexia.
# Base 16px, escala em rem com multiplicador --font-scale.
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
    fontSize: 0.9rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0em
  mono:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: 0.82rem
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0em
  dyslexic:                 # alternativa via toggle (Decisão 10)
    fontFamily: "Lexend, Inter, sans-serif"

# ============================================================
# ROUNDED — raio cresce com o tamanho do elemento.
# ============================================================
rounded:
  sm:   6px       # chips, code inline, botões pequenos
  md:   10px      # botões, callouts, inputs, code block
  lg:   16px      # cards
  xl:   24px      # superfícies grandes, modais
  full: 99px      # pílulas (kicker, badge, chip, toggle)

# ============================================================
# SPACING — escala base 4px.
# ============================================================
spacing:
  xs:  4px
  sm:  8px
  md:  16px
  lg:  24px
  xl:  32px
  2xl: 48px
  3xl: 64px

# ============================================================
# COMPONENTS — props normativas. Cor de artigo (--art-*)
# NÃO está pré-atribuída a nenhum componente: a aplicação
# é definida na camada de conteúdo/taxonomia.
# ============================================================
components:
  button-primary:
    background: verde-marca
    color: "#ffffff"
    hoverBackground: verde-profundo
    padding: 10px 20px
    rounded: md
    fontWeight: 600
  button-secondary:
    background: paper
    color: verde-marca
    border: 1px solid line-2
    hoverBorder: verde-marca
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
    hoverBorder: verde-claro
    hoverTransform: translateY(-2px)
    hoverShadow: shadow-md
  card-com-cor:                # variante com barra lateral colorida
    accentBar: "var(--art-*)"  # 4px à esquerda; cor atribuída pelo conteúdo
    hoverBorder: "var(--art-*)"
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
  kicker-marca:
    background: verde-palido
    color: verde-profundo
    rounded: full
  kicker-warm:
    background: gold-soft
    color: ink
    rounded: full

# ============================================================
# ELEVATION — papel não flutua muito.
# ============================================================
elevation:
  shadow-sm: "0 1px 2px rgba(20,17,13,.04)"
  shadow-md: "0 4px 12px rgba(20,17,13,.06), 0 2px 4px rgba(20,17,13,.04)"
  shadow-lg: "0 24px 48px -12px rgba(20,17,13,.12)"

# ============================================================
# BREAKPOINTS — site sempre responsivo (Pilar 9, Decisão 13).
# ============================================================
breakpoints:
  mobile:  600px
  tablet:  860px
  desktop: 1024px
---

## Overview

A Base de Conhecimento do CEFOR/Ifes é um **instrumento de formação em serviço** para profissionais de EaD do IFES — não um repositório, mas um espaço onde qualquer profissional resolve problemas com autonomia e se mantém atualizado (Decisão 1). O design serve duas funções na mesma superfície: **consulta** ("preciso da resposta agora") e **aprendizagem contínua** ("quero evoluir").

A linguagem visual é deliberadamente **editorial e sóbria** — "papel de qualidade". A regra-mãe da identidade cromática é resumida em uma frase:

> **Verde institucional. Variedade nas bordas.**

Isso significa: a moldura institucional (header, tipografia, botões, ações) vive em **verde refinado em quatro tons** — uma família de matiz único (~158° em OKLCH) que varia só em luminosidade e chroma, cobrindo todo o trabalho de UI institucional sem precisar de outras cores. Verde profundo no header, verde marca nos CTAs e links, verde claro nos hovers, verde pálido nos fundos de seção. A variedade visual fica reservada aos **artigos**: cada card pode portar uma cor da família tonal calibrada — seis matizes principais (mais três reservas para crescimento futuro), todos na mesma faixa de luminosidade e saturação para que leiam como uma família, não como uma feira de cores.

Três compromissos atravessam todos os tokens:

1. **100% sans-serif** (Decisão 6) — hierarquia por peso, tamanho e espaçamento. Nunca por contraste serifada/sans.
2. **Acessibilidade por padrão** (Decisão 10) — WCAG 2.2 AA + e-MAG. Modo escuro, alto contraste e fonte para dislexia são tokens, não retoques. Cumprimento legal de instituição pública federal, não diferencial.
3. **Tokens como fonte única de verdade** — todo valor visual vive como CSS custom property. Trocar de tema é trocar variáveis, nunca reescrever CSS. É o que torna a Fase 3 (WordPress) barata.

> **Fonte canônica dos tokens:** `stages/02-design-system/drafts/kit-visual.html` (style guide vivo, com modos claro/escuro/contraste demonstráveis). A interface de referência do artigo é `stages/02-design-system/drafts/prototipos-paginas/prototipo-artigo.html` (Decisão 22). Este `design.md` é a destilação normativa dos dois para a implementação.

## Colors

A paleta tem **quatro camadas**, e a separação entre elas é o que sustenta a leitura:

1. **Papel** — três superfícies neutras (`bg`, `bg-2`, `bg-3`, `paper`), tinta em três pesos (`ink`, `ink-2`, `ink-3`) e duas linhas (`line`, `line-2`). É onde 90% da página vive.
2. **Marca — verde em quatro tons** — `verde-profundo`, `verde-marca`, `verde-claro`, `verde-palido`. Todos no mesmo matiz (~158°), variando apenas em luminosidade (0.34 → 0.94) e chroma (0.014 → 0.080). Header e footer no profundo, CTAs/links/ênfase no marca, hovers e badges sutis no claro, fundos de seção no pálido. Família autossuficiente para toda a moldura institucional.
3. **Família dos artigos** — seis cores principais (`roxo`, `azul`, `ambar`, `magenta`, `coral`, `teal`) mais três reservas (`rosa`, `laranja`, `anil`) para crescimento. Todas calibradas no mesmo espaço perceptual (L 0.64–0.82, C 0.10–0.18). Carregam **variedade decorativa** — nunca **significado funcional**. Como têm chroma controlada, convivem com o verde institucional sem competir.
4. **Acento quente** — `gold-soft`. Único token quente do sistema, reservado para destaques sutis (highlight, chip de novidade, fundo de bloco "em destaque"). Não compete com o verde nem com a família dos artigos.
5. **Semânticas** — `sky`, `sun`, `rose`, `violet`. Existem para os callouts (Decisão 5) e têm função fixa de **significar** (informação, atenção, cuidado, acessibilidade). Não se confundem com a família dos artigos mesmo quando matizes coincidem.

### Sobre a família dos artigos

As nove cores existem como **vocabulário cromático aberto**. **O DS não atribui qual cor pertence a qual categoria, trilha, percurso ou seção** — essa atribuição é decisão da camada de conteúdo (CMS, editor, mantenedor). O DS garante apenas que, *quando* duas ou mais cores aparecem juntas, elas se comportam como uma família e não competem com a marca.

Regras de uso da família:
- **Mesma família**, sempre. Não introduzir cores fora da faixa L 0.64–0.82 / C 0.10–0.18 — quebra a harmonia.
- **Aplicação típica**: barra lateral de card (`4px`), fundo de chip/pílula, ícone categórico, fundo de hero de listagem. Sempre como assinatura visual de classificação, nunca como cor de UI funcional (botão, link, foco).
- **Contraste de texto sobre cor**: branco para todos os matizes principais (verificado AA com texto >= 18px ou peso 600). Para texto pequeno preto, usar a cor da família apenas como contorno/barra, não como fundo.

### Modos

Os três modos são trocas de tokens, ativados por atributos no `<html>`. Convivem: alto contraste e fonte-dislexia são toggles independentes do par claro/escuro.

**Modo escuro** (`[data-theme="dark"]`) — Decisão 8. Inverte superfícies e tinta. O verde clareia para preservar contraste sobre fundo escuro: `verde-marca` sobe para um tom mais luminoso, `verde-claro` ganha mais saturação. A família dos artigos sobrevive intacta — foi calibrada para luminosidade média e funciona em qualquer fundo.

| Token            | Claro       | Escuro      |
|---               |---          |---          |
| `bg`             | `#ffffff`   | `#0e0c0a`   |
| `paper`          | `#ffffff`   | `#1a1612`   |
| `ink`            | `#14110d`   | `#f4f1ea`   |
| `ink-2`          | `#4a4439`   | `#c9c2b3`   |
| `line`           | `#e7e3d8`   | `#2a251e`   |
| `verde-profundo` | `#1c4a36`   | `#2e7355`   |
| `verde-marca`    | `#2e7355`   | `#6cb89a`   |
| `verde-claro`    | `#6ea892`   | `#9ed1bd`   |
| `verde-palido`   | `#e6efe9`   | `#1f3329`   |
| `gold-soft`      | `#f3e7d0`   | `#3d3424`   |
| `art-*`          | inalterado  | inalterado  |

**Alto contraste** (`[data-contrast="high"]`) — Decisão 10, alvo WCAG AAA. Esquema preto/amarelo: fundo `#000000`, texto `#ffff00`, linhas `#ffff00`/`#ffffff`, verde vira `#00ff88`. As semânticas ganham versões saturadas; as cores de artigo, no modo alto contraste, **desligam-se** (todas reduzidas a borda branca + texto amarelo) — a variedade decorativa cede à legibilidade.

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

O **subtítulo** é tipograficamente distinto de propósito: mesma família, peso regular, tamanho intermediário entre H1 e corpo, em `ink-2`. Delimita o escopo do artigo numa frase (Decisão 16). O **kicker** é o rótulo curto em caixa alta que identifica tipo de página/conteúdo; sua cor segue o contexto (`verde-profundo` sobre `verde-palido` no padrão, ou cor da família dos artigos quando o conteúdo pede assinatura cromática).

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

Páginas-chave a desenhar (Fase 2, Step 7): Home, Artigo (referência canônica pronta), Trilha, Percurso, Listagem `/percursos`, Busca (modal Ctrl+K), Categoria.

## Elevation & Depth

Elevação é discreta — papel editorial não flutua. Três níveis apenas:

- **`shadow-sm`** — `0 1px 2px rgba(20,17,13,.04)`. Separação mínima, quase imperceptível.
- **`shadow-md`** — `0 4px 12px ...`. Estado *hover* de cards.
- **`shadow-lg`** — `0 24px 48px -12px ...`. Modais (busca Ctrl+K), drawers, popovers.

Cards em repouso usam **borda + respiro**, não sombra (Decisão 7). A sombra entra só na interação: hover de card sobe `translateY(-2px)` + `shadow-md`.

## Shapes

Quatro raios, escalando com o tamanho do elemento, mais a pílula:

- `sm 6px` — chips, code inline, botões pequenos
- `md 10px` — botões, callouts, inputs, blocos de código
- `lg 16px` — cards
- `xl 24px` — superfícies grandes, modais
- `full 99px` — pílulas: kicker, badge, chip, toggles, botões de ação circulares

Ícones são lineares (stroke), `stroke-width` ~2–2.4, `stroke-linecap/linejoin: round`, herdando `currentColor`. **Sem emoji na UI institucional** (Decisão 12) — feedback e ações usam ícone + texto, nunca carinhas.

## Components

Componentes derivados dos protótipos canônicos e da análise dos 131 artigos da base antiga. Cada um rastreia a decisão que o originou.

### Botões — 3 níveis de ênfase
- **Primário** (`button-primary`): fundo `verde-marca`, texto branco, hover `verde-profundo`. Ação principal ("Começar pela primeira trilha"). `padding 10px 20px`, `rounded md`.
- **Secundário** (`button-secondary`): fundo `paper`, texto `verde-marca`, borda `line-2`, hover borda `verde-marca`. Ação alternativa.
- **Fantasma** (`button-ghost`): transparente, texto `ink-2`, hover fundo `bg-2`. Ações terciárias (compartilhar, copiar).

### Kickers e pílulas
Rótulo curto em caixa alta identificando tipo de página. Padrão institucional usa `verde-palido`/`verde-profundo`. Quando o conteúdo carrega cor de família (categoria, trilha, percurso), o kicker pode adotar a cor `--art-*` correspondente — sempre como pílula `rounded full`, com texto branco sobre o matiz.

### Badges (metadados de taxonomia — Eixos 1 e 2, Decisão 17)
- **Tipo de artigo** (`badge-tipo`, fundo cheio neutro): Tutorial · Referência · Conceitual · Solução de Problema · Recurso.
- **Categoria** (`badge-categoria`, contorno): Ferramentas e Recursos · Pedagogia e Planejamento · Acessibilidade · Conduta e Conformidade · Identidade · *(6ª a definir)*.

> A atribuição de **cor da família dos artigos** a categorias/trilhas/percursos é decisão de conteúdo, não do DS. As 6 cores principais cobrem o conjunto atual; as 3 reservas existem para expansão.

### Callouts — 6 tipos (Decisão 5)
Bloco de destaque com `border-left 4px` + fundo soft. Quatro de severidade + dois contextuais do CEFOR:

| Tipo | Cor | Quando usar |
|---|---|---|
| **Dica** | `verde-marca` | Atalho, boa prática |
| **Nota** | `sky` | Contexto, nota explicativa |
| **Atenção** | `sun` | Cuidado reversível, "confira antes" |
| **Cuidado** | `rose` | Ação de alto impacto, risco real |
| **Pré-requisito** | `ink-3` | O que o leitor precisa ter antes |
| **Acessibilidade** | `violet` | Lembrete de inclusão (audiodescrição, Libras) |

> Os tipos são *conceito* fixado aqui; a lista exata e regras de uso editorial pertencem à Camada 4 do Content System (Fase 1). As cores são fixadas pelo DS.

### Cards (previews de listagem)
`card` base: `paper`, borda `line`, `rounded lg`, hover sobe e ganha borda `verde-claro` + `shadow-md`.

Variante `card-com-cor` recebe uma barra lateral de `4px` em uma cor da família dos artigos (`var(--art-*)`), atribuída pela camada de conteúdo conforme o eixo classificatório usado naquela listagem (categoria, trilha, percurso, etc.). Hover acompanha: a borda também adota a cor.

### Box de trilha multi-trilha (acordeão) — Decisões 28, 29, 30, 32
Componente da sidebar. Cabeçalho "Trilhas deste artigo" + contador. Cada trilha é um item de acordeão com nome + posição compacta (`5/12`) sempre visível mesmo colapsado + chevron. Primeira trilha expandida por padrão; múltiplas podem abrir juntas. Expandido mostra: chip do percurso (se aplicável) → barra de progresso **estrutural** → "Artigo X de Y" (**nunca "Passo"** — Decisão 29) → lista numerada de artigos com o atual em `aria-current="page"`.

> A navegação entre artigos da trilha é **exclusiva deste acordeão** — não há prev/next no rodapé (Decisão 32). A barra representa posição estrutural do artigo na trilha, **não** progresso pessoal do leitor (V1 sem login, Decisão 29).

### Chip de percurso — Decisão 31
Pílula com ícone de livro: "Faz parte do percurso **X**". A cor da pílula vem da família dos artigos (`var(--art-*)`) atribuída ao percurso, com fundo soft + texto da cor cheia, ou fundo cheio + texto branco. Aparece no topo do conteúdo expandido do item de trilha no acordeão. Clicável → página dedicada do percurso.

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
Ordem: **Artigos relacionados** (obrigatório em todo artigo, Decisão 9) → **Feedback** ("Foi útil/Não foi útil") → **Citação ABNT** automática no formato `SOBRENOME, Nome. Título. Base de Conhecimento CEFOR/Ifes, [ano]. Revisado em [data].`

### Busca (Decisão 11)
Modal central acionado por **Ctrl+K**, full-text, filtros por eixo de taxonomia, atalhos visíveis (ESC, setas, Enter), resultados agrupados por categoria. Resposta sintetizada por IA fica para a V2.

### Breadcrumb, progresso estrutural, índice sticky
Navegação de contexto refletindo a hierarquia de informação. Barra de progresso fina (`verde-marca`) representa posição estrutural. Índice "Neste artigo" sticky com scroll-tracking (Decisão 4).

### Widget de acessibilidade (Decisão 10)
Flutuante na lateral, acessível por teclado: A-/A+ (escala de fonte via `--font-scale`), alto contraste, fonte para dislexia, VLibras, "Pular para o conteúdo". Toda a UI navegável por teclado com foco visível em `verde-marca`.

## Do's and Don'ts

**Faça**
- Use o **verde institucional** para tudo que é institucional/funcional (header, CTAs, links, foco) e as **cores da família dos artigos** apenas como assinatura decorativa de classificação.
- Trate todo valor visual como token CSS — é o que mantém os 3 modos baratos e a Fase 3 viável.
- Separe cards por **respiro e tipografia**; reserve sombra para o hover.
- Diga "**Artigo** X de Y" dentro de trilha; "passo" só para itens de percurso.
- Garanta foco de teclado visível, contraste AA e audiodescrição visível em imagens informativas.
- Mantenha a coluna de leitura em ~65–72ch e o corpo a 16px / line-height 1.65.
- Para texto sobre cor de artigo, use branco a partir de peso 600 ou tamanho ≥18px. Para texto preto sobre cor, prefira o matiz só como contorno/barra.

**Não faça**
- Não use **cor da família dos artigos para UI funcional** (botão, link, foco, ícone de sistema) — isso é território exclusivo do verde institucional. Cor de artigo é decorativa, não acionável.
- Não use verde como cor de artigo/categoria — verde pertence exclusivamente à marca. Misturar quebra a leitura de hierarquia.
- Não introduza cores fora da família calibrada (L 0.64–0.82 / C 0.10–0.18) — quebra a harmonia da paleta.
- Não use **emoji** na UI institucional (feedback, ações) — ícone + texto (Decisão 12).
- Não introduza **fontes serifadas** para criar hierarquia (Decisão 6).
- Não exiba badge de "desatualizado" para o público — é metadado administrativo (Decisão 21).
- Não use prev/next de trilha no rodapé — a navegação vive no acordeão da sidebar (Decisão 32).
- Não mostre progresso *pessoal* nem use localStorage na V1 — só posição estrutural (Decisão 29).
- Não delimite cards com contorno forte ou sombra pesada (Decisão 7).
- Não use bege/cinza no fundo geral — o fundo é branco quente (Decisão 7).

---

> **Procedência:** Tokens espelham `stages/02-design-system/drafts/kit-visual.html`. Componentes e regras rastreiam as Decisões 1–32 de `_config/decisoes.md` e os Pilares 1, 2, 5, 6, 8, 9 de `_config/pilares.md`. Interface de referência: `stages/02-design-system/drafts/prototipos-paginas/prototipo-artigo.html` (Decisão 22). Versão **beta** — substitui o par verde-IFES/dourado da versão alpha por verde refinado em quatro tons + família calibrada de cores para artigos + `gold-soft` como único acento quente.
