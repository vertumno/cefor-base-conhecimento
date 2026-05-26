# Design System — Escopo e Estrutura

> **Documento de referência**
> Define o que compõe o Design System da Base de Conhecimento CEFOR/Ifes, suas camadas, e como ele se relaciona com os 11 pilares do projeto.

---

## O que é o Design System

O Design System não é um kit de componentes visuais. É um **sistema vivo** que garante que tudo que é construído — por qualquer pessoa, em qualquer momento — siga as mesmas regras e se comporte da mesma forma.

Ele é composto por **6 camadas**, da mais abstrata à mais concreta.

---

## As 6 Camadas do Design System

---

### Camada 1 — Princípios de Design

As decisões filosóficas que guiam todas as outras. Toda decisão técnica que vem depois deve ser rastreável a um princípio.

**Exemplos de princípios (a definir na especificação):**
- "Priorizamos clareza sobre estética"
- "Acessibilidade não é feature, é requisito"
- "Conforto de leitura vem antes de densidade de informação"
- "Menos variações, mais consistência"

---

### Camada 2 — Design Tokens

A **fonte única de verdade** para todos os valores visuais do sistema. Nenhum valor aparece direto no código — tudo passa por um token.

| Categoria | Exemplos |
|---|---|
| Cor | `color.text.primary: #1a1a1a`, `color.bg.surface: #ffffff` |
| Tipografia | `font.family.body: "Inter"`, `font.size.body: 18px` |
| Espaçamento | `space.sm: 8px`, `space.md: 16px`, `space.lg: 32px` |
| Sombra | `shadow.card: 0 2px 8px rgba(0,0,0,0.08)` |
| Borda | `border.radius.md: 8px`, `border.width.default: 1px` |
| Movimento | `motion.duration.fast: 150ms`, `motion.easing.default: ease-out` |
| Breakpoints | `breakpoint.sm: 640px`, `breakpoint.md: 768px` |
| Leitura | `reading.line-height: 1.7`, `reading.column-width: 720px` |

Tokens são gerados em formatos consumíveis: CSS custom properties, JSON, Tailwind config, etc.

**O que precisa ser definido:**
- Nomenclatura dos tokens (semântica vs primitiva)
- Formato de exportação (W3C DTCG, CSS variables, Tailwind)
- Tokens de modo claro e modo escuro
- Tokens específicos de leitura (largura de coluna, altura de linha, espaço entre parágrafos)

---

### Camada 3 — Componentes (Atomic Design)

Os blocos de construção, organizados em 5 níveis:

```
ÁTOMOS (indivisíveis)
├── Heading (H1, H2, H3)
├── Paragraph
├── Button (curtir, compartilhar, copiar)
├── Tag / Badge (categoria, status, tipo de artigo)
├── Icon
├── CodeBlock
├── Quote / Destaque
├── AlertBox (dica, aviso, atenção, erro)
├── Tooltip
└── Link

MOLÉCULAS (átomos combinados com função específica)
├── AuthorCard (avatar + nome + titulação + data)
├── ArticleMeta (categoria + tags + tempo de leitura + status)
├── ActionBar (curtir + compartilhar + copiar ABNT + salvar)
├── TLDRBox (resumo rápido do artigo)
├── SectionAnchor (índice de seções com navegação âncora)
├── SearchBar (campo de busca + filtros)
├── ReadingProgress (indicador de progresso de leitura)
├── TrailNav (navegação anterior/próximo em trilhas)
├── FAQItem (pergunta + resposta colapsável)
└── ArticleCard (preview de artigo para listagens e relacionados)

ORGANISMOS (moléculas combinadas em blocos funcionais)
├── ArticleHeader (título + meta + autor + TL;DR)
├── ArticleBody (seções + destaques + code blocks + alertas)
├── ArticleFooter (referência ABNT + ações + artigos relacionados)
├── ArticleSidebar (índice de seções + progresso + ações)
├── TrailOverview (visão geral da trilha com artigos e progresso)
└── SearchResults (resultados + filtros + paginação)

TEMPLATES (layout completo sem conteúdo real)
├── ArticlePage (layout do artigo completo)
├── TrailPage (layout de trilha/percurso)
├── SearchResultsPage (layout de resultados de busca)
├── CategoryPage (layout de listagem por categoria)
└── HomePage (layout da página inicial)

PÁGINAS (templates com conteúdo real)
├── /artigo/{slug}
├── /trilha/{id}
├── /busca
├── /categoria/{slug}
└── /
```

**O que cada componente precisa ter definido:**
- Variantes (tipos, tamanhos)
- Props / API (o que é configurável)
- Comportamento responsivo (como muda por breakpoint)
- Estados (default, hover, focus, active, disabled, loading, error, success)
- Acessibilidade (semântica HTML, ARIA, teclado, contraste)
- Tokens utilizados (quais tokens alimentam o componente)

---

### Camada 4 — Padrões de Uso

Regras de **como** e **quando** usar cada componente. Sem essas regras, o sistema vira uma caixa de ferramentas sem manual.

**Exemplos de padrões (a definir na especificação):**
- "Use TLDRBox no topo de artigos com mais de 5 minutos de leitura"
- "ActionBar aparece fixo no rodapé em mobile, inline no desktop"
- "Nunca use mais de 3 níveis de heading dentro de um artigo"
- "AlertBox do tipo 'atenção' só para ações que podem causar perda de dados"
- "ArticleCard sempre mostra: título, categoria, tempo de leitura e status"
- "Badge de 'desatualizado' aparece antes do título quando artigo tem mais de 12 meses sem revisão"

---

### Camada 5 — Documentação

Cada componente documentado com:
- Quando usar / quando NÃO usar
- Exemplos visuais de cada variante e estado
- Código de implementação
- Regras de acessibilidade do componente
- Comportamento responsivo detalhado
- Tokens utilizados

**Formato de documentação (a definir):**
- Storybook, documentação em markdown, ou ambos
- Acessível para desenvolvedores e para a equipe de conteúdo

---

### Camada 6 — Ferramentas e Processos

Como o Design System é mantido vivo ao longo do tempo:
- Versionamento de tokens e componentes
- Processo para propor novos componentes
- Processo para depreciar componentes
- Testes visuais automatizados (visual regression)
- Checklist de qualidade por componente
- Responsável pela governança do DS

---

## Relação com os 11 Pilares do Projeto

### Pilares que fazem parte direta do Design System

| # | Pilar | O que alimenta no DS |
|---|---|---|
| 1 | **Sistema Visual** (Visual System) | Tokens de cor, tipografia, espaçamento, sombra, ícones. É o **núcleo** do DS. |
| 2 | **Sistema de Interação** (Interaction System) | Comportamento dos componentes, microinterações, feedback visual das ações. |
| 5 | **Sistema de Acessibilidade** (Accessibility System) | Embutido em cada token e cada componente. Não é uma camada separada — está **dentro de tudo**. Contraste, semântica HTML, ARIA, teclado, Libras. |
| 6 | **Sistema de Leitura** (Reading Experience System) | Tokens de leitura (line-height, column-width, paragraph-spacing) e componentes de leitura (ReadingProgress, SectionAnchor, TLDRBox). |
| 8 | **Sistema de Estados** (State System) | Estados de componentes (hover, focus, loading, error) e estados do usuário que viram variantes visuais (lido, salvo, em progresso). |
| 9 | **Sistema Responsivo** (Responsive Behavior System) | Breakpoints como tokens. Comportamento por dispositivo embutido em cada componente. |

### Pilar que alimenta parcialmente o Design System

| # | Pilar | Relação com o DS |
|---|---|---|
| 3 | **Modelo de Conteúdo** (Content Model) | Informa **quais componentes precisam existir**. Se o modelo de conteúdo define que artigos têm TL;DR, o DS precisa de um componente TLDRBox. Se define que existem alertas, o DS precisa de AlertBox. Mas a estrutura editorial em si (tom, linguagem, regras de escrita) não é DS. |

### Pilares que ficam fora do Design System

| # | Pilar | Por que fica fora |
|---|---|---|
| 4 | Sistema de Taxonomia | Arquitetura de informação — categorias, tags, trilhas. Afeta os dados dos componentes, mas não o DS em si. |
| 7 | Ciclo de Vida do Conteúdo | Processo editorial — estados de publicação, revisão, depreciação. O DS consome esses estados (ex: badge de "desatualizado"), mas não define o processo. |
| 10 | Sistema de Autoria | Tooling e workflow de criação de conteúdo. Pode usar componentes do DS no editor, mas é um sistema separado. |
| 11 | Sistema de Descoberta | SEO/GEO — schema.org, meta tags, busca semântica. Não é responsabilidade do DS. |

---

## Mapa Visual

```
┌────────────────────────────────────────────────────────┐
│                    DESIGN SYSTEM                        │
│                                                         │
│  ┌──────────────┐  ┌───────────────┐                   │
│  │   VISUAL     │  │    LEITURA    │   ← Tokens        │
│  │   (pilar 1)  │  │   (pilar 6)  │                   │
│  └──────────────┘  └───────────────┘                   │
│                                                         │
│  ┌──────────────┐  ┌───────────────┐                   │
│  │  INTERAÇÃO   │  │   ESTADOS    │   ← Comportamento  │
│  │   (pilar 2)  │  │   (pilar 8)  │                   │
│  └──────────────┘  └───────────────┘                   │
│                                                         │
│  ┌──────────────┐  ┌───────────────┐                   │
│  │  RESPONSIVO  │  │ACESSIBILIDADE│   ← Embutido       │
│  │   (pilar 9)  │  │   (pilar 5)  │     em tudo       │
│  └──────────────┘  └───────────────┘                   │
│                                                         │
│  ┌──────────────────────────────────────┐              │
│  │       MODELO DE CONTEÚDO             │  ← Informa   │
│  │       (pilar 3 — parcialmente)       │    quais      │
│  └──────────────────────────────────────┘    componentes│
│                                              existem    │
└────────────────────────────────────────────────────────┘

FORA DO DS (mas conectados):
  • Taxonomia (pilar 4)      → Arquitetura de informação
  • Ciclo de Vida (pilar 7)  → Processo editorial
  • Autoria (pilar 10)       → Tooling e workflow
  • Descoberta (pilar 11)    → SEO / GEO
```

---

## Interdependências dentro do Design System

Os 6 pilares do DS não podem ser especificados isoladamente — são interdependentes:

| Decisão em... | Afeta... |
|---|---|
| Uma cor do **Visual** | O **contraste de Acessibilidade** e a **legibilidade de Leitura** |
| Um **breakpoint Responsivo** | A **largura de coluna de Leitura** e a **posição da ActionBar de Interação** |
| Um **estado** de componente | A **cor do Visual**, o **comportamento de Interação** e o **contraste de Acessibilidade** |
| O **modo escuro do Visual** | Todos os tokens de **Leitura**, **Acessibilidade** e **Estados** |
| Um **componente de Leitura** | O **comportamento Responsivo** e a **Acessibilidade** |

**Consequência prática:** esses 6 pilares precisam ser especificados em conjunto, por uma mesma equipe, num mesmo ciclo. Especificar Visual isolado e depois "encaixar" Acessibilidade é a receita para retrabalho.

---

*Documento criado em: 2026-04-07*
*Versão: 0.1 — Escopo inicial, pré-benchmarking*
*Projeto: Base de Conhecimento CEFOR/Ifes — Reformulação*
