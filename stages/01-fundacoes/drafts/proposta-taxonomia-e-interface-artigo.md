# Proposta — Taxonomia + Interface do Artigo

> **Versão:** 0.1 (DRAFT — proposta inicial, ainda não validada pela equipe)
> **Data:** 2026-05-13
> **Autor:** Claude (a partir de análise do inventário da base antiga e das 15 decisões consolidadas)
> **Objetivo:** Propor uma arquitetura de organização/categorização/rotulagem de artigos para a Fase 1 e definir o que deve ser exibido na interface do artigo
> **Insumos:**
> - `data/base-antiga/base-conhecimento-cefor-inventario.json` (inventário completo de 131 artigos da base atual)
> - `data/base-antiga/relatorio-base-conhecimento-cefor.md` (contexto institucional)
> - `_config/decisoes.md` v2.0 (15 decisões consolidadas Fase 0 → Fase 1)
> - `_config/pilares.md` (pilares 3, 4, 11)
> - `shared/roadmap.md` (Content System — Camadas 3, 4 e Taxonomia/Descoberta)
> **Resolve total ou parcialmente:** Decisão 9 (local de trilhas — só parcial), Decisão 14 (metadados — proposta de fechamento)

---

## 1. Diagnóstico da base antiga

131 artigos organizados em 4 eixos sobrepostos: **categoria** (1 fixa), **tipo** (1 fixo), **temas/tags** (N livres), **percursos** (N opcionais). Cada eixo tem problemas estruturais.

### 1.1 Categorias — 20 itens com duplicação e cauda longa

| Categoria | Artigos | Problema |
|---|---|---|
| Ambiente Virtual de Aprendizagem | 59 | — |
| Ambiente virtual | 12 | **Duplicata da #1** (casing diferente) |
| Recurso Educacional | 10 | OK |
| Moodle | 7 | **Sobrepõe AVA** |
| Inteligência Artificial | 7 | OK |
| Tutoriais | 5 | Confunde com o eixo "Tipo=Tutorial" |
| *(vazia)* | 5 | Sem categoria |
| Tecnologias Educacionais | 4 | Vago |
| Ferramentas de comunicação | 4 | OK |
| Ferramentas de autoria | 3 | OK |
| +10 categorias | 1-2 cada | **Cauda longa inútil** (Aspectos Pedagógicos, Processos, Procedimento Administrativo, Moodle x Sistema Acadêmico, MOOC, Livros Digitais etc.) |

### 1.2 Tipos — 10 itens misturando formato, finalidade e meta

| Tipo | Artigos | Análise |
|---|---|---|
| Tutorial | 41 | Formato |
| **Outros** | 30 | **23% do acervo sem classificação útil** |
| Referência Moodle | 15 | Mistura formato (referência) + plataforma (Moodle) |
| Tutorial/Avaliação | 10 | Sub-tipo de Tutorial |
| Ferramenta Externa | 8 | Não é tipo, é tópico |
| Conceitual | 8 | Formato |
| Template/Code | 6 | Formato |
| Institucional/Padrão Visual | 5 | Mistura formato + tópico |
| Ferramenta/GPT | 4 | Não é tipo, é tópico |
| Evento/Divulgação | 4 | Não pertence a base de conhecimento |

### 1.3 Temas (tags) — 82 únicos, 62% usados 1 vez

- Top 5: Moodle (70), Ferramenta (29), Atividade (15), Questionário (11), Configuração (11)
- 51 dos 82 temas aparecem em **um único artigo** — não servem para descoberta
- Casing e plural inconsistentes: `Ferramenta` vs `Ferramentas`, `mooc` vs `MOOC`, `código` vs `Moodle Codes`
- Média 2,21 temas/artigo; **14 artigos sem nenhum tema**

### 1.4 Percursos — 12, com problemas operacionais

| Percurso | Declarado | Encontrado | Status |
|---|---|---|---|
| Professor Moodle | 44 | 11 | **Inflado/quebrado** |
| Planejamento e Design Educacional | 21 | — | **404 (página inacessível)** |
| Tudo sobre prova online | 18 | 11 | Parcial |
| Iniciando no Moodle | 15 | 11 | Parcial |
| Gestão e Configuração do Moodle | 9 | 10 | OK |
| Ferramentas educacionais | 8 | 9 | Sobrepõe categoria |
| Moodle Codes | 7 | 8 | É um tópico transversal, não trilha |
| Inteligência Artificial | 7 | 8 | Sobrepõe categoria |
| Livro de Notas | 6 | 7 | Sub-trilha de Avaliação |
| Acessibilidade no AVA | 6 | 7 | Sobrepõe categoria |
| Gamificação | 4 | 5 | Pequeno demais para trilha |
| Direitos Autorais e Segurança | 4 | 5 | Sobrepõe categoria |

### 1.5 Achados críticos

- **55 artigos (42%) não estão em nenhum percurso** — o modelo de percurso não cobre o acervo, é decorativo
- O artigo "Dúvidas & Sugestões" está em **todos os 11 percursos visíveis** — meta-conteúdo poluindo trilhas
- **6 dos 12 percursos têm o mesmo nome de uma categoria** — duplicação conceitual flagrante
- Apenas 7 artigos estão em mais de um percurso — modelo está sendo usado como "categoria alternativa", não como sequência didática
- 7 artigos com alerta de obsoleto, 14 sem temas, 5 sem categoria
- 62% dos temas são cauda longa de 1 uso — não suportam descoberta

---

## 2. Princípios da nova arquitetura

A regra-mãe: **cada eixo responde a uma única pergunta**. Se dois eixos respondem a mesma, um deles sai.

| Princípio | Por que |
|---|---|
| **Eixos com papéis distintos e não-sobrepostos** | A base antiga sofre porque categoria, tipo e percurso disputam o mesmo papel. Cada eixo aqui responde a uma pergunta clara e diferente |
| **Vocabulários controlados, casing único** | 62% de cauda longa nos temas atuais mostra que tags livres não funcionam para descoberta |
| **Critérios rígidos de adesão** | Hoje 42% dos artigos estão fora de trilha. Trilha que não cobre o acervo é decoração — melhor poucas trilhas verdadeiras |
| **Hierarquia rasa** | Categoria de 1 nível. Profundidade vira problema de manutenção e prejudica busca |
| **Categoria define URL, não o tipo nem a trilha** | URL semântica precisa ser estável. Tipo e trilha mudam mais facilmente |
| **Ancorado nas decisões já tomadas** | Não inventa para resolver problemas que a equipe já endereçou (perfis sem navegação na home, sem aba mobile, sem TL;DR obrigatório etc.) |

---

## 3. Proposta — 4 eixos taxonômicos

### Eixo 1 — TIPO (formato editorial)

> **Pergunta:** *"Que tipo de leitura esperar deste artigo?"*
> **Cardinalidade:** 1 por artigo (fixo)
> **Valores:** 5 (fechado, sem auto-criação)
> **Define:** template visual, esqueleto editorial, expectativa de leitura

| Tipo | O que é | Substitui hoje | Esqueleto editorial mínimo |
|---|---|---|---|
| **Tutorial** | Passo-a-passo executável | Tutorial, Tutorial/Avaliação | Pré-requisitos → Passos numerados → Verificação → Próximos passos |
| **Referência** | Consulta rápida, listas, dicionários, modelos | Referência Moodle, Template/Code, Institucional/Padrão Visual | Resumo → Lista/tabela → Detalhes por item |
| **Conceitual** | Entender o "porquê", fundamentos pedagógicos | Conceitual | Problema → Conceitos → Aplicação prática |
| **Solução de Problema** | Troubleshooting, FAQ invertido | *(novo — antes vinha como "Outros")* | Sintoma → Causa provável → Solução → Como evitar |
| **Recurso** | Apresenta uma ferramenta, link, GPT, plugin | Ferramenta Externa, Ferramenta/GPT | O que é → Quando usar → Como acessar → Exemplo |

> **Eliminados:**
> - **"Outros"** (30 artigos atuais) — não é tipo, é falta de classificação; cada um precisa ser reclassificado em um dos 5 acima
> - **"Evento/Divulgação"** (4 artigos) — não pertence a uma base de conhecimento; vai para um agregador de notícias ou para a home

### Eixo 2 — CATEGORIA (área de conhecimento)

> **Pergunta:** *"Em que parte da base esse artigo mora?"*
> **Cardinalidade:** 1 por artigo (fixo)
> **Valores:** 6 (fechado, hierarquia rasa)
> **Define:** URL semântica e agrupamento principal de navegação

| Categoria | Slug URL | Volume estimado | Consolida das categorias antigas |
|---|---|---|---|
| **Moodle (AVA)** | `/moodle/` | ~75 | AVA (59) + Ambiente virtual (12) + Moodle (7) |
| **Ferramentas e Recursos** | `/ferramentas/` | ~20 | Recurso Educacional (10) + Ferramentas de autoria (3) + Ferramentas de comunicação (4) + IA aplicada como ferramenta (parte de IA) |
| **Pedagogia e Planejamento** | `/pedagogia/` | ~10 | Aspectos Pedagógicos + Conhecimentos Pedagógicos + parte conceitual de IA + Tecnologias Educacionais (parte) |
| **Acessibilidade** | `/acessibilidade/` | ~8 | Transversal hoje, mas tem peso estratégico (Decisão 10) |
| **Conduta e Conformidade** | `/conduta/` | ~6 | Direitos Autorais + Netiqueta + Segurança + Procedimentos |
| **Identidade Cefor** | `/identidade/` | ~7 | Padrões Visuais + MOOC + Templates institucionais |

> **Por que não duplicar com Tipo:** Categoria é *sobre o que*, Tipo é *como se lê*. Um Tutorial pode existir em qualquer categoria.
> **Por que 6 e não 10+:** uma categoria precisa abrigar volume suficiente para ser navegável; uma categoria com 2 artigos é uma tag, não uma seção.

### Eixo 3 — TÓPICOS (tags substantivas, vocabulário controlado)

> **Pergunta:** *"Que assuntos específicos esse artigo aborda?"*
> **Cardinalidade:** 2 a 4 por artigo (multivalorado)
> **Valores:** ~25 termos (controlado, lista fechada, sem auto-criação)
> **Define:** descoberta lateral, sugestão de relacionados, filtros da busca

Substitui os 82 temas atuais (62% cauda longa) por uma lista enxuta consolidada. **Casing único definido na lista.**

**Lista candidata inicial (a refinar com a Ruti na Camada 3 do Content System):**

| Grupo | Tópicos |
|---|---|
| Operacionais Moodle | `Questionário`, `Prova`, `Banco de Questões`, `Notas`, `Livro de Notas`, `Tarefa`, `Fórum`, `Sala Virtual`, `Backup`, `Matrícula`, `Configuração de Curso` |
| Mídia e Recursos | `Vídeo`, `H5P`, `Rótulo`, `Livro Digital`, `Webconferência`, `Áudio`, `Apresentação` |
| Inteligência Artificial | `IA Generativa`, `GPT Customizado`, `IA na Aula` |
| Acessibilidade | `Libras`, `Audiodescrição`, `Contraste`, `Inclusão` |
| Identidade e Padrões | `Padrão Visual`, `MOOC`, `ReLiCefor` |
| Conduta e Conformidade | `Direitos Autorais`, `Segurança Digital`, `Netiqueta` |

> **Regras de governança** (a formalizar na Camada 9 — ContentOps):
> - Casing único e fixo (sempre `Questionário`, nunca `questionario` nem `Questionários`)
> - Sinônimos rejeitados explicitamente (ex.: `Ferramenta` e `Ferramentas` saem; viram tópicos específicos como `H5P`)
> - Adição de novo tópico exige validação (papel de curadoria do Vocabulário Controlado a ser definido na Camada 9)
> - Tópicos órfãos (sem nenhum artigo) são removidos no ciclo mensal

### Eixo 4 — TRILHA (percurso didático sequencial)

> **Pergunta:** *"Esse artigo faz parte de uma jornada de aprendizagem com ordem?"*
> **Cardinalidade:** 0 ou 1 por artigo (opcional, mutuamente exclusivo)
> **Valores:** ~5 trilhas (fechado V1)
> **Define:** sequência didática validada, navegação Anterior/Próximo, agrupamento de "Comece por aqui"

**Critério rígido de adesão** (para evitar o problema atual onde 42% não têm trilha e ela vira decoração):
- Tem sequência didática real (começo → meio → fim)
- Validada pela Ruti como percurso pedagógico
- Ao menos 5 artigos completos
- Cada artigo aparece em **no máximo 1 trilha**
- Trilha que não atinge o mínimo é dissolvida, e seus artigos voltam a viver apenas pela categoria + tópicos

**Trilhas viáveis V1** (consolidando as 12 atuais):

| Nova trilha | Consolida | Artigos estimados |
|---|---|---|
| **Iniciando no Moodle** | Iniciando no Moodle + parte de Professor Moodle | ~12 |
| **Avaliação no Moodle** | Tudo sobre prova online + Livro de Notas | ~15 |
| **Acessibilidade no AVA** | Acessibilidade no AVA | ~7 |
| **IA para Professores** | Inteligência Artificial | ~8 |
| **Padrão Visual Cefor** | *(novo, a partir de Identidade Cefor)* | ~5 |

> **Eliminados:**
> - **Direitos Autorais e Segurança** (5 artigos): vira a categoria Conduta e Conformidade
> - **Ferramentas Educacionais** (9 artigos): sobrepõe a categoria Ferramentas e Recursos
> - **Moodle Codes** (8 artigos): vira o tópico `Moodle Codes` (transversal a Tutoriais e Referências dentro de Moodle)
> - **Gamificação** (5 artigos): volume insuficiente para trilha; artigos viram parte da categoria Moodle (AVA) com tópicos próprios
> - **Professor Moodle** (declarava 44, só 11 visíveis): escopo amplo demais, vira a própria categoria Moodle (AVA)
> - **Planejamento e Design Educacional** (já 404 hoje): conteúdo vai para a categoria Pedagogia e Planejamento, sem trilha

### Como os 4 eixos respondem juntos — exemplo

> *Artigo:* "Como configurar tempo ampliado no questionário sem expor o estudante com NE"
>
> - **Tipo:** Tutorial
> - **Categoria:** Acessibilidade
> - **Tópicos:** `Questionário`, `Inclusão`, `Configuração de Curso`
> - **Trilha:** Acessibilidade no AVA (posição 4 de 7)

### Como isso atende às decisões já tomadas

| Decisão | Como esta proposta resolve |
|---|---|
| #2 (Segmentação por perfil sem navegação por perfil) | Perfis emergem da combinação `Categoria + Tópicos`, sem precisar de eixo "perfil" separado nem porta de entrada visual |
| #9 (Trilhas + artigos relacionados ao fim) | Trilhas viram opcionais e enxutas (Eixo 4); "Artigos relacionados" são gerados por interseção de Tópicos + mesma Categoria |
| #11 (Busca com filtros) | Categoria e Tipo viram filtros principais; Tópicos viram filtros secundários |
| #14 (Metadados — deferida) | Proposta concreta de quais metadados exibir e onde — ver seção 5 |
| #15 (Escopo negativo) | Sem login, sem perfil de usuário, sem tracking de progresso — trilhas são puramente editoriais |

---

## 4. Mapeamento conceitual — consolidações principais

Da base antiga (estado caótico) para a proposta (estado limpo):

```
ANTIGO (20 categorias)              →  NOVO (6 categorias)
─────────────────────────────────────────────────────────────
Ambiente Virtual de Aprendizagem    \
Ambiente virtual                     ├→ Moodle (AVA)
Moodle                              /

Recurso Educacional                  \
Ferramentas de autoria                ├→ Ferramentas e Recursos
Ferramentas de comunicação            /
(parte de) Inteligência Artificial

Aspectos Pedagógicos                  \
Conhecimentos Pedagógicos              ├→ Pedagogia e Planejamento
Tecnologias Educacionais (conceitual)  /
(parte de) Inteligência Artificial

(transversal hoje)                   →  Acessibilidade

Direitos Autorais                    \
Netiqueta                              ├→ Conduta e Conformidade
Segurança                              /
Procedimento Administrativo

Padrão Visual                        \
MOOC                                   ├→ Identidade Cefor
Templates institucionais              /

Outros (30 artigos!)                 →  Distribuídos entre os 6 conforme conteúdo real
(vazia, 5 artigos)                   →  Distribuídos entre os 6 conforme conteúdo real
```

```
ANTIGO (10 tipos)                    →  NOVO (5 tipos)
─────────────────────────────────────────────────────────────
Tutorial                              \
Tutorial/Avaliação                     ├→ Tutorial

Referência Moodle                     \
Template/Code                          ├→ Referência
Institucional/Padrão Visual           /

Conceitual                            →  Conceitual

(novo — virá de "Outros")             →  Solução de Problema

Ferramenta Externa                    \
Ferramenta/GPT                         ├→ Recurso

Outros                                →  Reclassificar em um dos 5
Evento/Divulgação                     →  REMOVIDO (não pertence à base)
```

```
ANTIGO (12 percursos)                →  NOVO (5 trilhas)
─────────────────────────────────────────────────────────────
Iniciando no Moodle (11)              \
(parte de) Professor Moodle (11)       ├→ Iniciando no Moodle

Tudo sobre prova online (11)          \
Livro de Notas (7)                     ├→ Avaliação no Moodle

Acessibilidade no AVA (7)             →  Acessibilidade no AVA

Inteligência Artificial (8)           →  IA para Professores

(novo, vindo de Identidade Cefor)     →  Padrão Visual Cefor

Direitos Autorais e Segurança (5)     →  REMOVIDO (vira categoria Conduta)
Ferramentas educacionais (9)          →  REMOVIDO (sobrepõe categoria)
Moodle Codes (8)                      →  REMOVIDO (vira tópico transversal)
Gamificação (5)                       →  REMOVIDO (volume insuficiente)
Gestão e Config do Moodle (10)        →  REMOVIDO (vira parte da categoria Moodle/AVA)
Planejamento e Design Educacional     →  REMOVIDO (já 404)
Professor Moodle (44 → 11)            →  REMOVIDO (escopo amplo demais)
```

---

## 5. Interface do artigo — o que exibir e onde

Refina a Decisão 14 (deferida) e incorpora as ampliações da Decisão 13 (multimodal), da Decisão 4 (índice + tempo de leitura + progresso) e da Decisão 12 (feedback "Foi útil"/"Não foi útil" sem emoji).

### 5.1 Topo do artigo (cabeçalho)

| Elemento | Mostrar? | Onde | Origem da decisão |
|---|---|---|---|
| Breadcrumb (Home › Categoria › Título) | ✅ Sim | Acima do título | Proposta — Categoria sustenta URL |
| Selo do Tipo (Tutorial / Conceitual / Solução de Problema / Referência / Recurso) | ✅ Sim | Junto ao breadcrumb, com cor por tipo | Proposta — orienta expectativa de leitura |
| Título (H1) | ✅ Sim | — | — |
| **Subtítulo** | ✅ **Sim — obrigatório em todos os artigos** | Logo abaixo do H1, antes da linha de meta | **Decisão 16 (2026-05-13)** |
| **Autor(es) — nome exibido** | ✅ **Sim — obrigatório em todos os artigos** | Linha de meta abaixo do subtítulo (formato "Por Fulano de Tal" ou "Por Fulano e Beltrano") | Decisão 14 (complemento 2026-05-13) |
| Tempo de leitura | ✅ Sim | Linha de meta abaixo do subtítulo | Decisão 4 |
| Trilha + posição na trilha (ex.: "Acessibilidade no AVA · 4 de 7") | ✅ Sim, **se pertencer a uma trilha** | **Sidebar do artigo** (proposta atual) — em destaque, acima ou junto ao índice | Decisão 9 |
| **Categoria como badge separado** | ❌ Não — já está no breadcrumb | — | Evita poluição |
| **Tags/Tópicos no topo** | ❌ Não — vão no rodapé | — | Tópicos servem descoberta lateral, não cabeçalho |
| **Revisor pedagógico** | ❌ Não — papel não existe na operação | — | Decisão 14 (ajuste 2026-05-13) |
| **Última revisão (data + responsável)** | ❌ Não exibir na interface | — | Decisão 14 (ajuste 2026-05-13) |
| **Versão do Moodle** | ❌ Não | — | Decisão 14 (Elton: "não precisa") |

> **Subtítulo — regras de produção (Decisão 16):**
> - **Obrigatório em todos os artigos.** Vira critério de aceitação na rubrica (Camada 5) e no template do WordPress (Fase 3 — Custom Field `subtitulo` obrigatório).
> - **Função:** delimitar o escopo do artigo, dizer "para quem" ou "para qual situação" o conteúdo serve, em uma frase única.
> - **Comprimento sugerido:** 10 a 25 palavras (a confirmar na Camada 6 — Padrões de Legibilidade).
> - **Tipografia:** sans-serif (Decisão 6), peso regular, tamanho intermediário entre H1 e corpo.

> **Autoria — regras de produção (consequência de tornar o autor obrigatório):**
> - Todo artigo precisa ter ao menos um autor declarado nos metadados antes de ser publicado (vira critério de aceitação na rubrica e no workflow do WordPress).
> - Autores múltiplos são suportados (ex.: "Por Fulano e Beltrano").
> - Quando há produção com IA, manter a marcação "Produzido com assistência de IA" em adição ao(s) autor(es) humano(s) responsáveis pela curadoria.
> - **Não há "revisor pedagógico" separado:** a autoria responde pela qualidade do conteúdo. Esse papel foi descartado da Decisão 14 em 2026-05-13.
> - O autor também é exibido **no rodapé do artigo** (eco), com bloco de atribuição mais completo (ver seção 5.4).
> - A página de autor (lista de artigos por autor) pode ficar para V1.5; o requisito da V1 é apenas a **exibição do nome no artigo** e o registro como metadado.

### 5.2 Lado direito (sidebar sticky)

A sidebar fica **enxuta** — apenas o que precisa estar visível durante a leitura. Feedback e compartilhar saem da sidebar (vão para o rodapé do artigo) para evitar duplicação.

| Elemento | Mostrar? | Origem |
|---|---|---|
| **Trilha + posição na trilha** (se aplicável) | ✅ Sim — em destaque no topo da sidebar | Decisão 9 (proposta atual) |
| **Índice de seções com scroll-tracking** | ✅ Sim — sempre visível, com seção atual destacada | Decisão 4 |
| ~~Botão "Foi útil / Não foi útil"~~ | ❌ Não — só no rodapé | Ajuste 2026-05-13 |
| ~~Compartilhar / Copiar link~~ | ❌ Não — só no rodapé | Ajuste 2026-05-13 |
| ~~Copiar referência ABNT~~ | ❌ Não — só no rodapé | Ajuste 2026-05-13 |

### 5.3 Multimodal — blocos opcionais dentro/junto do artigo (Decisão 13)

A Decisão 13 ampliou significativamente o que cabe dentro do artigo. **Cada item abaixo é opcional por artigo**, mas todos precisam ter um componente editorial pronto no Design System.

| Bloco | Onde aparece | Quando exibir | Componente |
|---|---|---|---|
| **Vídeo em Libras (tradução do artigo)** | Topo, em **accordion recolhível** | Quando existir gravação Libras | Accordion expansível, fechado por padrão; rótulo "Tradução em Libras" |
| **Áudio do artigo (narração)** | Topo, junto ao tempo de leitura | Quando existir | Player simples ("Ouvir o artigo · 6 min") |
| **Podcast** | Topo, separado da narração | Quando existir podcast produzido | Player de podcast com capa, episódio, duração |
| **Imagens com audiodescrição visível** | Inline, junto à imagem | Sempre que houver imagens não-decorativas | Imagem + bloco de texto "Descrição da imagem: ..." visível para todos. Legenda opcional separada |
| **Infográfico/imagem-resumo** | Final ou meio do artigo | Em artigos longos ou conceituais | Bloco dedicado com imagem + texto alternativo + audiodescrição |

> **Implicação para ContentOps (Camada 9):** cada formato adicional aumenta o custo de produção. A meta de ~4-6 artigos/mês precisa ser revista considerando quais artigos receberão quais formatos.
> **Implicação para Custom Fields no WordPress:** `video_libras_url`, `audio_url`, `podcast_url`, `audiodescricao` (por imagem), `infografico_url`.

### 5.4 Fim do artigo

| Elemento | Mostrar? | Origem |
|---|---|---|
| Tópicos como chips clicáveis | ✅ Sim — descoberta lateral por tópico | Proposta — Eixo 3 |
| **"Foi útil?" / "Não foi útil?"** (única ocorrência no artigo) | ✅ Sim — em texto, sem emoji | Decisão 12 |
| **Bloco de autoria** (autor + atribuição, eco do topo) | ✅ Sim — junto ao bloco de feedback | Decisão 14 (ajuste 2026-05-13) |
| **Botão "Compartilhar" com dropdown** (Copiar link · Copiar ABNT) | ✅ Sim — botão único que abre menu | Ajuste 2026-05-13 — consolida copiar/compartilhar |
| **Bloco "Faz parte da trilha"** com contexto da trilha completa | ✅ Sim, **se em trilha** — envolve o Anterior/Próximo deixando claro que pertencem a uma jornada | Decisão 9 (refinamento 2026-05-13) |
| Anterior / Próximo na trilha | ✅ Sim, **se está em trilha** — dentro do bloco "Faz parte da trilha" | Proposta — Eixo 4 |
| **"Artigos relacionados" (3 a 5)** | ✅ Sim — **obrigatório em todos os artigos** | Decisão 9 (lembrança explícita) |
| ~~Data de última revisão (eco)~~ | ❌ Não — removido junto da Decisão 14 | Ajuste 2026-05-13 |

### 5.5 Esquema visual de referência

```
┌──────────────────────────────────────────────────────────────┐
│  Início › Acessibilidade            [Tutorial]               │ ← breadcrumb + tipo
│                                                              │
│  Como configurar tempo ampliado no questionário              │ ← H1
│  sem expor o estudante com NE                                │
│                                                              │
│  Subtítulo: o passo a passo para configurar tempo extra      │ ← SUBTÍTULO obrigatório
│  sem que o estudante apareça como exceção para os colegas.   │   (Decisão 16)
│                                                              │
│  Por Juliana Cassaro · ⏱ 6 min                               │ ← autor + tempo
│                                                              │
│  ▾ Tradução em Libras                            [accordion] │ ← Libras (Decisão 13)
│  ▶ Ouvir o artigo (6 min)   🎙 Podcast (ep. 4)               │ ← áudio + podcast
│                                                              │
│  [conteúdo do artigo]                ┌─ Sidebar ───────────┐ │
│   ...                                │ 📚 TRILHA          │ │ ← trilha na sidebar
│   ...                                │ Acessibilidade...   │ │   (refinamento)
│   [imagem]                           │ 4 de 7              │ │
│   Descrição da imagem: tela do       │                     │ │
│   Moodle mostrando o painel...       │ ─── Neste artigo    │ │
│   ...                                │ • Pré-requisitos   │ │
│                                      │ • Passo 1          │←│ ← scroll-tracking
│   [infográfico-resumo]               │ • Passo 2          │ │   (Decisão 4)
│                                      │ • Verificação      │ │
│                                      └─────────────────────┘ │
│  ─── fim do conteúdo ───                                     │
│                                                              │
│  Tópicos: Questionário · Inclusão · Configuração de Curso    │
│                                                              │
│  [Foi útil?]  [Não foi útil]   [📤 Compartilhar ▾]           │ ← share dropdown
│                                  ├─ Copiar link              │   abre menu
│                                  └─ Copiar ABNT              │
│                                                              │
│  ┌─ Faz parte da trilha: Acessibilidade no AVA · 4 de 7 ─┐  │ ← bloco explícito
│  │  ← Anterior · 3 de 7      |     Próximo · 5 de 7 →    │  │   da trilha
│  │  "Botão de acessibilidade  |  "Audiodescrição em       │  │   (refinamento)
│  │   no AVA"                  |   imagens do Moodle"      │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  Sobre o autor                                               │ ← autor no rodapé
│  Juliana Cassaro · designer e conteudista CEFOR              │   (eco do topo)
│                                                              │
│  Artigos relacionados (3-5 cards)                            │
└──────────────────────────────────────────────────────────────┘
```

---

## 6. Pendências e próximos passos

### 6.1 Validação necessária

| Item | Quem valida | Critério |
|---|---|---|
| 6 categorias propostas (Moodle, Ferramentas, Pedagogia, Acessibilidade, Conduta, Identidade) | Elton + Marcos | Cobrem o acervo? Viram URL semântica estável? |
| 5 tipos propostos (Tutorial, Referência, Conceitual, Solução de Problema, Recurso) | Equipe | Cobrem os 131 artigos? Cada tipo tem esqueleto editorial claro? |
| Lista candidata de ~25 tópicos | Equipe (Camada 3 do Content System) | Vocabulário pedagógico correto? Faltam termos? Há sinônimos a fundir? |
| 5 trilhas propostas | Equipe | Cada uma tem sequência didática real (não é só agrupamento)? |
| Interface do artigo proposta (seção 5) | Elton + Marcos + Juliana | Fecha a Decisão 14? Os blocos multimodais (Decisão 13) cabem no layout? Subtítulo obrigatório (Decisão 16) está acomodado? |

### 6.2 Decisões ainda em aberto que esta proposta toca

| Decisão | Status nesta proposta |
|---|---|
| **#9** (local da trilha no artigo) | **Não resolvido aqui** — fica para Fase 2 conforme decidido. Esta proposta só sinaliza que o lugar precisa caber no fluxo do esquema visual |
| **#14** (mostrar Tipo/Categoria/Tags) | **Proposta fechada nesta seção 5** — Categoria sai por breadcrumb, Tipo por badge ao lado, Tópicos no rodapé. Aguarda aprovação para fechar a decisão |

### 6.3 Próximas ações sugeridas

1. **Revisão da equipe** (Elton + Marcos + Ruti + Juliana) sobre os 4 eixos e a seção da interface do artigo. Ajustar até consenso.
2. **Mapeamento dos 131 artigos** nos novos eixos (categoria + tipo + tópicos + trilha). Isso:
   - Valida a proposta na prática (se algum artigo "não couber", revisamos os eixos)
   - Vira insumo direto da **triagem da Fase 4.1** (artigos antigos passam pela Rubrica para decidir reescrita/descarte/migração)
   - Calibra o **Vocabulário Controlado** (Camada 3) com o acervo real
   - Detecta lacunas (categorias subpopuladas indicam gaps de conteúdo)
3. Após aprovação, esta proposta vira o ponto de partida dos outputs oficiais da Fase 1:
   - `stages/01-fundacoes/output/taxonomia.md` (Eixos 1-4 formalizados)
   - `stages/01-fundacoes/output/vocabulario-controlado.json` (Eixo 3 expandido)
   - Insumo do template de artigo na Fase 2 (Design System) e na Fase 3 (Implementação WordPress)

---

*Draft criado em: 2026-05-13*
*Fonte canônica: este arquivo*
*Status: aguardando revisão de Elton + Marcos + Ruti + Juliana*
