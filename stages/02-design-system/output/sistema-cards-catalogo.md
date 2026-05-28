# Sistema de Cards do Catálogo — Decisões de Conteúdo

> **Versão:** 1.0
> **Data:** 2026-05-28
> **Status:** Aprovado por Elton + Juliana
> **Fase:** 2 — Design System
> **Protótipo de referência:** [`drafts/prototipos-paginas/home-proposta-v4.html`](../drafts/prototipos-paginas/home-proposta-v4.html)

---

## Contexto

O [`design.md`](design.md) define **tokens** (paleta, tipografia, raios, sombras) mas deliberadamente **não atribui** cor da família dos artigos (`--art-*`) a categorias específicas — essa é decisão de conteúdo. Este documento formaliza a atribuição feita para a listagem do catálogo (home + página "Todos os artigos").

Decisão estrutural: **Opção B-lite** (de 3 alternativas analisadas):
- **Cor do card** = Categoria do artigo (1 das 6)
- **Ícone do card** = Grupo de tópico do artigo (1 dos 8)
- **Tipo do artigo** = badge neutro no body (`badge-tipo`)

Motivo da escolha: distribui melhor a variedade visual no catálogo (~63% dos artigos são Tutorial — concentrar cor por tipo cria monotonia goiaba; concentrar cor por categoria e ícone por grupo equilibra).

---

## Mapeamento Categoria → Cor

Atribuição da família `--art-*` às 6 categorias canônicas da [taxonomia.md §4](../../01-fundacoes/output/taxonomia.md).

| Categoria | Slug | Token | Hex |
|---|---|---|---|
| Ferramentas e Recursos | `ferramentas` | `--art-azul` | `#5d9bd8` |
| Gestão e Operação do Moodle | `gestao-moodle` | `--art-teal` | `#5ea9b2` |
| Pedagogia e Planejamento | `pedagogia` | `--art-coral` | `#ed8366` |
| Acessibilidade | `acessibilidade` | `--art-roxo` | `#9c6dcb` |
| Conduta e Conformidade | `conduta` | `--art-ambar` | `#e8b53a` |
| Identidade | `identidade` | `--art-magenta` | `#c46aac` |

**Reservas disponíveis** para crescimento futuro: `--art-rosa` (`#ed7b8a`), `--art-laranja` (`#e88f3c`), `--art-anil` (`#7b81d7`).

---

## Mapeamento Grupo de tópico → Ícone

Os 25 tópicos da [taxonomia.md §5](../../01-fundacoes/output/taxonomia.md) estão organizados em 8 grupos. Cada grupo tem um ícone geométrico próprio, todos no estilo "blueprint nested" (outline preto puro, sem fill, com repetição da forma primária em camadas).

| Grupo | Tópicos | Forma | Asset (branco) |
|---|---|---|---|
| Atividades e avaliação Moodle | Questionário · Banco de Questões · Tarefa · Fórum · Livro de Notas | Círculo | [`icone_circulo_branco.png`](../assets/icone_circulo_branco.png) |
| Recursos Moodle | H5P · Rótulo · Webconferência · Vídeo · Áudio e Podcast · Livro Digital | Hexágono | [`icone_hexagono_branco.png`](../assets/icone_hexagono_branco.png) |
| Gestão do AVA | Configuração de Curso · Matrícula e Inscrição · Backup e Restauração · Moodle Codes · Sala Virtual | Quadrado | [`icone_quadrado_branco.png`](../assets/icone_quadrado_branco.png) |
| Inteligência Artificial | IA Generativa · GPT Customizado | Losango | [`icone_losango_branco.png`](../assets/icone_losango_branco.png) |
| Acessibilidade | Libras · Audiodescrição · Inclusão e Desenho Universal | Triângulo | [`icone_triangulo_branco.png`](../assets/icone_triangulo_branco.png) |
| Pedagogia | Planejamento e Design Educacional | Trapézio | [`icone_trapezio_branco.png`](../assets/icone_trapezio_branco.png) |
| Identidade institucional | Padrão Visual · MOOC | Triângulo retângulo | [`icone_triangulo_retangulo_branco.png`](../assets/icone_triangulo_retangulo_branco.png) |
| Conduta | Direitos Autorais e Segurança | Pentágono | [`icone_pentagono_branco.png`](../assets/icone_pentagono_branco.png) |

**Regra de seleção do grupo num artigo com múltiplos tópicos** (2–4 tópicos por artigo, conforme regra da taxonomia §5): usar o grupo do **tópico primário** (primeiro listado).

---

## Inventário de assets

Todos os ícones em duas variantes (branco / preto), 16 arquivos no total em [`stages/02-design-system/assets/`](../assets/):

```
icone_circulo_branco.png        icone_circulo_preto.png
icone_hexagono_branco.png       icone_hexagono_preto.png
icone_losango_branco.png        icone_losango_preto.png
icone_pentagono_branco.png      icone_pentagono_preto.png
icone_quadrado_branco.png       icone_quadrado_preto.png
icone_trapezio_branco.png       icone_trapezio_preto.png
icone_triangulo_branco.png      icone_triangulo_preto.png
icone_triangulo_retangulo_branco.png  icone_triangulo_retangulo_preto.png
```

**Convenção de uso:**
- **Branco** sobre fundo colorido (cards do catálogo no light mode)
- **Preto** sobre fundo claro neutro (ícones em listagens monocromáticas, sidebar, breadcrumbs)

---

## Estrutura do card no catálogo

```
┌──────────────────────────────────┐
│                                  │
│         [ícone do GRUPO]          │ ← fundo na cor da CATEGORIA, altura 16:7
│                                  │
├──────────────────────────────────┤
│ CATEGORIA (kicker)               │
│ Título do artigo                 │
│ Descrição em 3 linhas máx        │
│ [badge tipo]  10 min             │
└──────────────────────────────────┘
```

- **Topo colorido** (`.card-illust`): fundo na cor da categoria, ícone do grupo branco centralizado (28% / max 90px).
- **Body**: kicker da categoria em maiúsculas + título + descrição + meta (badge de tipo neutro + tempo de leitura).
- **Hover**: borda `verde-claro`, `translateY(-2px)`, `shadow-md`.

---

## Componentes técnicos relacionados

| Componente | Onde vive |
|---|---|
| `card` + `card-illust` + `card-body` | CSS do protótipo, futuro Gutenberg block |
| `badge-tipo` (neutro) | Definido em `design.md` §components/badge-tipo |
| `kicker` (categoria) | Tipografia kicker do design.md, cor `ink-3` |
| Tokens `--cat-*` (cor por categoria) | Variáveis derivadas mapeando `--cat-<slug>` → `--art-*` |

---

## Histórico de versões

| Versão | Data | Mudança | Por |
|---|---|---|---|
| 1.0 | 2026-05-28 | Mapeamento inicial categoria→cor e grupo→ícone, com 8 ícones aprovados pela Juliana | Elton + Juliana |

---

## Próximos passos

1. Validar mapeamento com Marcos antes de propagar para Fase 3 (WordPress)
2. Considerar registrar como **Decisão 33 — Sistema visual do catálogo** em `_config/decisoes.md` se for considerada decisão constitucional
3. Em Fase 3: implementar como propriedades do CPT `categoria` (campo `cor`) e do tópico/grupo (campo `icone`) no Gutenberg
