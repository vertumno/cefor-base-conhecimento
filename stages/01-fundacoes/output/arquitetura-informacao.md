# Arquitetura da Informação — Base de Conhecimento CEFOR/Ifes

> **Versão:** 1.1 — fechamento formal da IA de navegação
> **Data:** 2026-06-02
> **Status:** ✅ Aprovado (Decisões 33, 34) · ⏳ URLs semânticas — co-aprovação de Marcos pendente (Sprint 3) · ⏳ validação pedagógica conjunta com Decisões 25-32
> **Documento canônico** da arquitetura de navegação, das URLs e do breadcrumb.
> **Referência cruzada:** `taxonomia.md` (4 eixos + §8 URLs) · `_config/decisoes.md` (Decisões 17, 18, 26, 28, 29, 33, 34) · `_config/pilares.md` (Pilar 4 Taxonomia, Pilar 11 Descoberta).

---

## 1. Objetivo

Tornar explícito **como o site se organiza para navegação**, **como são as URLs** e **como o breadcrumb exibe a posição do usuário**. Resolve a ambiguidade que existia no protótipo do artigo, onde o breadcrumb misturava classificação e jornada editorial.

Este documento não redefine a taxonomia (isso é o `taxonomia.md`). Ele define a **camada de navegação e wayfinding** que se apoia nela.

---

## 2. Princípio central — as duas camadas

O sistema tem **duas estruturas distintas**. Não competem; são complementares. Confundi-las é a origem de qualquer falta de clareza na navegação.

| Camada | O que faz | Pergunta | É árvore? | Cardinalidade do "pai" |
|---|---|---|---|---|
| **Classificação** (Eixo 2 — Categoria) | *Classifica* — onde o conteúdo mora | "Onde está?" | ✅ Sim | **1 pai** (estável) |
| **Jornada editorial** (Trilha / Percurso) | *Narra* — que caminho de aprendizagem faz sentido | "Como percorrer?" | ❌ Não | **0..n** (sobreposição many-to-many) |

> Esta distinção já é lei do projeto: `taxonomia.md` §6.3 e Decisão 27 — *"Categoria classifica; percurso narra."*

**Consequência de design:**
- A **espinha de classificação** do site é `Início → Categoria → Artigo`. É a única hierarquia com pai único e estável — e é a que organiza o **breadcrumb**.
- **Trilha e Percurso são uma camada sobreposta**, não a espinha. Um artigo pertence a 0, 1 ou várias trilhas — por isso a jornada vive em um **acordeão** (Decisão 30), não no breadcrumb.
- **A URL do artigo é plana** (Decisão 34) — não reflete a categoria. Ou seja: a árvore de classificação organiza o *breadcrumb*, não o *permalink*. São coisas separadas (ver §5).

---

## 3. Sitemap

```
Início  /
│
├── [Categoria]        /{categoria}/            ← índice do domínio (6 categorias, Eixo 2)
│                                                  pai de classificação do artigo (breadcrumb)
│
├── Artigo             /{artigo-slug}           ← unidade atômica · URL PLANA na raiz (Decisão 34)
│                                                  a categoria é metadado, NÃO entra na URL
│
├── Trilhas            /trilhas                  ← listagem de trilhas
│      └── Trilha       /trilhas/{slug}          ← jornada (≥3 artigos ordenados)
│
├── Percursos          /percursos                ← listagem de percursos
│      └── Percurso     /percursos/{slug}        ← formação (trilhas + artigos avulsos)
│
├── Tópicos            /topicos/{slug}           ← descoberta lateral (Eixo 3)
│
└── Buscar             /buscar?q=…&tipo=…&categoria=…
```

> **Note bem:** o artigo **não** mora "dentro" da categoria na URL. A categoria é o pai *conceitual* (breadcrumb + página-índice), não um segmento de path. Artigo e página-índice de categoria **convivem na raiz** — daí a necessidade de slugs reservados (§4).

---

## 4. Tipos de página e URLs

| Tipo de página | URL | Origem |
|---|---|---|
| Início | `/` | — |
| Índice de categoria | `/{categoria}/` | taxonomia §8 |
| **Artigo** | `/{artigo-slug}` (plana, raiz) | taxonomia §8 · **Decisão 34** |
| Listagem de trilhas | `/trilhas` | proposto (par da listagem de percursos) |
| Trilha | `/trilhas/{slug}` | taxonomia §8 |
| Listagem de percursos | `/percursos` | taxonomia §8 |
| Percurso | `/percursos/{slug}` | taxonomia §8 |
| Tópico (descoberta) | `/topicos/{slug}` | taxonomia §8 |
| Busca | `/buscar?q=…` | taxonomia §8 · Decisão 11 |

**Slugs reservados (Decisão 34):** como artigo e página-índice de categoria convivem na raiz, os **6 slugs de categoria** (`ferramentas`, `gestao-moodle`, `pedagogia`, `acessibilidade`, `conduta`, `identidade`) + `trilhas`, `percursos`, `topicos`, `buscar` (e demais seções de topo) são **reservados**. Nenhum artigo pode usá-los como slug — validação no save.

> Slugs em minúsculas + hífen, sem acento (taxonomia §8). URLs semânticas ainda pendentes de co-aprovação de Marcos (Sprint 3); a direção (URL plana) é a Decisão 34.

---

## 5. Breadcrumb — a regra

**Regra única, ensinável e sem exceção (Decisão 33):**

> **O breadcrumb reflete a árvore de classificação — `Início → Categoria → Artigo` — onde cada ancestral é uma página real. Nunca a jornada editorial.**

Um breadcrumb é um caminho de *containment* — pai único e estável. A única camada que satisfaz isso é a **Categoria** (Eixo 2). Trilha e Percurso, por serem many-to-many, **não entram no breadcrumb** — vivem na casca (ver §7).

> **Atenção (Decisão 34):** o breadcrumb reflete a **árvore de classificação**, *não* a string da URL. Como a categoria saiu da URL do artigo (URL plana), o breadcrumb **continua mostrando a Categoria** — porque ela segue sendo o pai conceitual e tem página própria `/{categoria}/`. Breadcrumb e permalink são camadas separadas.

### 5.1 Breadcrumb por tipo de página

| Página | Breadcrumb | URL da página |
|---|---|---|
| Índice de categoria | `Início › {Categoria}` | `/{categoria}/` |
| **Artigo** | `Início › {Categoria} › {Título do artigo}` | `/{artigo-slug}` |
| Listagem de trilhas | `Início › Trilhas` | `/trilhas` |
| Trilha | `Início › Trilhas › {Nome da trilha}` | `/trilhas/{slug}` |
| Listagem de percursos | `Início › Percursos` | `/percursos` |
| Percurso | `Início › Percursos › {Nome do percurso}` | `/percursos/{slug}` |
| Tópico | `Início › Tópicos › {Nome do tópico}` | `/topicos/{slug}` |
| Busca | *(sem breadcrumb — usa título "Resultados para …")* | `/buscar` |

> No artigo, o segmento `{Categoria}` **não** corresponde a um pedaço da URL do próprio artigo — ele linka para a página-índice `/{categoria}/`. Esse é o único ponto em que breadcrumb e URL divergem, e é intencional (Decisão 34).

### 5.2 Exemplos concretos

```
Artigo:    Início › Gestão e Operação do Moodle › Configurando o livro de notas
           URL do artigo:  /configurar-livro-de-notas          (plana — sem categoria)
           Link do segmento "Gestão…":  /gestao-moodle/        (página-índice da categoria)

Trilha:    Início › Trilhas › Avaliação online de ponta a ponta
           URL:  /trilhas/avaliacao-online-de-ponta-a-ponta

Percurso:  Início › Percursos › Dominando o Moodle
           URL:  /percursos/dominando-o-moodle

Tópico:    Início › Tópicos › Questionário
           URL:  /topicos/questionario
```

### 5.3 Rótulos vs slugs

- O **rótulo** exibido é o nome humano completo da categoria (`Gestão e Operação do Moodle`), não o slug (`gestao-moodle`).
- O **último item** é a página atual: não é link, recebe `aria-current="page"` e peso visual (`.current`, já no `shell.css`).

### 5.4 Acessibilidade e SEO

- `<nav aria-label="Você está aqui">` (rever o rótulo atual "Trilha de navegação" — a palavra "trilha" colide com o conceito de Trilha do produto e pode confundir leitor de tela).
- Marcar a página atual com `aria-current="page"`.
- Emitir `Schema.org/BreadcrumbList` (JSON-LD) com o caminho `Início › Categoria › Artigo` — **importante**: é por aqui que o sinal de categoria chega ao buscador, já que a URL plana não o carrega (Decisão 34 · Pilar 11 SEO/GEO).
- Truncamento responsivo em mobile: colapsar segmentos intermediários (`Início › … › {atual}`) preservando primeiro e último; nunca quebrar o título atual no meio de palavra.

---

## 6. Por que a jornada (Trilha/Percurso) **não** entra no breadcrumb do artigo

Quatro razões, todas ancoradas em decisões já tomadas:

1. **É many-to-many.** Um artigo pode estar em várias trilhas (Decisões 18, 30 — é a razão de existir o acordeão). Um breadcrumb só comporta um caminho — escolher uma trilha seria arbitrário.
2. **Quebra a neutralidade editorial.** O artigo é editorialmente neutro quanto à trilha; a voz da sequência vive na casca (Decisão 26). Cravar um percurso no breadcrumb faz o artigo tomar partido de uma jornada.
3. **Inventa um histórico inexistente.** O vínculo de trilha é **estrutural, não comportamental** — sem referrer (Decisões 28, 29). O sistema não sabe se o leitor veio por aquela jornada; mostrá-la como caminho percorrido é ficção.
4. **Não é o pai de classificação.** O breadcrumb expressa "onde isto está classificado". Quem responde isso é a Categoria (pai único), não a trilha.

---

## 7. Onde a jornada editorial aparece, então

A camada de jornada tem suas próprias superfícies — fortes e corretas para o caso many-to-many — **separadas** do breadcrumb:

| Superfície | Onde | Decisão |
|---|---|---|
| **Acordeão "Trilhas deste artigo"** | Sidebar do artigo, sempre visível quando aplicável; posição `X/Y` mesmo colapsado; múltiplas trilhas listadas | 28, 29, 30 |
| **Página de Trilha** | `/trilhas/{slug}` — lista ordenada dos artigos | 18 |
| **Página de Percurso** | `/percursos/{slug}` — verde escuro, hero + "como percorrer" + 3 rotas de entrada por perfil | 27, 31 |
| **Chip de percurso (verde escuro)** | No topo do acordeão de trilha, quando a trilha integra um percurso | 31 |

Breadcrumb e acordeão são **complementares**: o breadcrumb responde "onde estou na classificação"; o acordeão responde "de que jornadas isto faz parte". Cada um na sua camada.

---

## 8. Estado dos protótipos

| Arquivo | Item | Estado |
|---|---|---|
| `base-artigo.html` (breadcrumb) | Mostrava `Início › Percursos › Trilha › Artigo` (jornada) | ✅ **Corrigido 2026-06-02** → `Início › {Categoria} › {Título}`, com `aria-current="page"` |
| `base-artigo.html` (masthead-meta) | Categoria duplicada no painel de meta | ✅ **Corrigido 2026-06-02** → removida do meta (vive no breadcrumb); emblema de categoria mantido |
| `base-artigo.html` (a11y) | `aria-label="Trilha de navegação"` | ✅ **Corrigido 2026-06-02** → `aria-label="Você está aqui"` |
| `base-trilha.html:398-405` | `Início › Trilhas › {Nome}` | ✅ já correto (mas `aria-label` ainda "Trilha de navegação" — ⏳ rever) |
| `base-percurso.html:310-317` | `Início › Percursos › {Nome}` | ✅ já correto (mas `aria-label` ainda "Trilha de navegação" — ⏳ rever) |
| Página-índice de categoria `/{categoria}/` | Destino do segmento de categoria no breadcrumb (hoje link placeholder `#categoria-…`) | ⏳ a construir (Fase 2) |

---

## 9. Pendências

| Pendência | Bloqueia | Responsável |
|---|---|---|
| **Co-aprovação das URLs** (URL plana — Decisão 34) | URLs em produção, implementação WP | Marcos (Sprint 3) |
| **Página-índice de categoria** `/{categoria}/` — definir layout | Destino do segmento de categoria no breadcrumb | Fase 2 (Design System) |
| **Listagem de trilhas** `/trilhas` — confirmar como página | Breadcrumb da trilha ter pai navegável | Elton (Sprint 3) |
| **Guarda de slugs reservados** — implementar validação no editor | Evitar colisão artigo × categoria/seções na raiz | Fase 3 (WP) |
| **Correção dos protótipos** (§8) | Coerência visual antes da Fase 3 | Fase 2 |
| **Validação pedagógica** das Decisões 25-34 | IA virar fonte canônica definitiva | Rute + Marquito |

---

## 10. Decisões consolidadas neste documento

| Decisão | Tema | Onde aparece |
|---|---|---|
| 17 | Taxonomia em 4 eixos | §2, §3 |
| 18 | Artigo / Trilha / Percurso | §2, §7 |
| 26 | Neutralidade editorial do artigo | §6 |
| 27 | Percurso é agregação (narra, não classifica) | §2, §7 |
| 28, 29 | Vínculo estrutural sem referrer; V1 sem progresso pessoal | §6, §7 |
| 30 | Acordeão multi-trilha | §2, §7 |
| 31 | Superfícies do percurso (verde escuro — dourado abandonado 2026-06-02) | §7 |
| **33** | **Breadcrumb reflete a árvore de classificação** | §5, §6 |
| **34** | **URL plana do artigo (categoria fora da URL)** | §2, §3, §4, §5 |

---

## Histórico de versões

| Versão | Data | Mudança | Por |
|---|---|---|---|
| 1.0 | 2026-06-02 | Documento canônico criado. Formaliza as 2 camadas (classificação vs jornada), o sitemap, os tipos de página e a regra de breadcrumb taxonômico (Decisão 33). | Elton + Claude |
| 1.1 | 2026-06-02 | **URL plana do artigo** (Decisão 34): categoria sai da URL. Sitemap, tabela de URLs e exemplos atualizados; slugs reservados; regra de breadcrumb reconciliada (reflete a árvore de classificação, não a string da URL); §5.4 reforça `BreadcrumbList` como portador do sinal de categoria. | Elton + Claude |
