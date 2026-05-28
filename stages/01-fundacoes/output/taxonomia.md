# Taxonomia — Base de Conhecimento CEFOR/Ifes

> **Versão:** 1.0 — fechamento formal da arquitetura taxonômica
> **Data:** 2026-05-26
> **Status:** ✅ Aprovado (Decisões 17, 18, 25–32) · ⏳ URLs semânticas pendentes (Sprint 3)
> **Documento canônico** do Bloco 2 da Fase 1.
> **Referência cruzada:** `_config/decisoes.md` (Decisões 17–32) · `output/contentsystem.md` §B.3–B.4 · `output/vocabulario-controlado.json` (Eixo 3 — definições)

---

## 1. Objetivo

Definir a arquitetura taxonômica única da nova Base de Conhecimento — substitui o modelo antigo (20 categorias + 10 tipos + 82 tags livres + 12 percursos) por **quatro eixos ortogonais** + camada de curadoria **Trilha/Percurso**.

**Regra-mãe** (Decisão 17): *cada eixo responde a uma única pergunta; se dois eixos respondem à mesma, um sai.*

---

## 2. Os 4 eixos

| Eixo | Pergunta | Cardinalidade | Define |
|---|---|---|---|
| **1. Tipo** | Como se lê/usa este artigo? | 1 por artigo | Expectativa de leitura, badge no cabeçalho |
| **2. Categoria** | Em que domínio de conhecimento mora? | 1 por artigo | Agrupamento principal, URL semântica |
| **3. Tópico** | Que assuntos específicos aborda? | 2 a 4 por artigo | Descoberta lateral, relacionados, filtros de busca |
| **4. Trilha** | Faz parte de uma jornada curada? | 0 ou mais por artigo | Curadoria editorial (sequência didática) |

> **Decisão 17** — `_config/decisoes.md:560`.

---

## 3. Eixo 1 — Tipo (5 valores fechados)

| Tipo | Quando usar |
|---|---|
| **Tutorial** | Passo a passo de execução. "Como fazer X." |
| **Referência** | Material consultável, não-linear. Tabelas, parâmetros, códigos. |
| **Conceitual** | Explicação de conceito ou fundamento. "O que é / por que." |
| **Solução de Problema** | Diagnóstico + correção. "Erro X aparece quando…" |
| **Recurso** | Apresentação de ferramenta, GPT, template, livro digital. |

**Regras:**
- Cardinalidade fixa: **1 e somente 1** por artigo.
- Sem digitação livre. Select único.
- Casing fixo (`Tutorial`, não `tutorial` nem `Tutoriais`).

---

## 4. Eixo 2 — Categoria (6 valores fechados — 2026-05-21)

| Categoria | Slug | Domínio | Consolida (antigas) |
|---|---|---|---|
| **Ferramentas e Recursos** | `ferramentas` | Atividades e recursos Moodle (Questionário, Tarefa, Fórum, H5P, Rótulo, Webconferência), ferramentas externas, GPTs | Recurso Educacional · Ferramentas de autoria · Ferramentas de comunicação |
| **Gestão e Operação do Moodle** | `gestao-moodle` | Operação do AVA: configuração de curso, matrícula, livro de notas, backup, navegação, Moodle Codes | AVA · Ambiente virtual · Moodle · Gestão e Config |
| **Pedagogia e Planejamento** | `pedagogia` | Planejamento, design educacional, fundamentos pedagógicos | Aspectos Pedagógicos · Conhecimentos Pedagógicos · Tecnologias Educacionais (conceitual) |
| **Acessibilidade** | `acessibilidade` | Libras, audiodescrição, inclusão, desenho universal | (transversal antes — virou categoria por peso estratégico, Decisão 10) |
| **Conduta e Conformidade** | `conduta` | Direitos autorais, segurança digital, netiqueta, procedimentos | Direitos Autorais · Netiqueta · Segurança · Procedimento Administrativo |
| **Identidade** | `identidade` | Padrão visual CEFOR, MOOC, ReLiCefor, templates institucionais | Padrão Visual · MOOC · Livros Digitais |

**Por que "Moodle" não vira uma categoria única:** ~60% do acervo antigo era Moodle. Uma categoria que abriga 60% não navega — apenas reproduz o problema das tags. O operacional vai para *Gestão e Operação do Moodle*; as atividades, para *Ferramentas e Recursos*; "avaliação" atravessa as duas e é unificada pelo Eixo 3 (Tópicos).

**Regras:**
- Cardinalidade fixa: **1 e somente 1** por artigo.
- Slug estável (sustenta URL semântica — ver §8).
- Lista fechada. Nova categoria exige decisão formal (Elton + Marcos).

---

## 5. Eixo 3 — Tópico (25 valores fechados — 2026-05-21)

Substitui as 82 tags livres da base antiga. **Sem auto-criação, sem digitação livre, casing fixo.**

| Grupo | Tópicos |
|---|---|
| **Atividades e avaliação Moodle** | `Questionário` · `Banco de Questões` · `Tarefa` · `Fórum` · `Livro de Notas` |
| **Recursos Moodle** | `H5P` · `Rótulo` · `Webconferência` · `Vídeo` · `Áudio e Podcast` · `Livro Digital` |
| **Gestão do AVA** | `Configuração de Curso` · `Matrícula e Inscrição` · `Backup e Restauração` · `Moodle Codes` · `Sala Virtual` |
| **Inteligência Artificial** | `IA Generativa` · `GPT Customizado` |
| **Acessibilidade** | `Libras` · `Audiodescrição` · `Inclusão e Desenho Universal` |
| **Pedagogia** | `Planejamento e Design Educacional` |
| **Identidade institucional** | `Padrão Visual` · `MOOC` |
| **Conduta** | `Direitos Autorais e Segurança` |

**Total: 25 tópicos.**

**Regras de governança** (operacionalizadas na Camada 9 — ContentOps):
- Cardinalidade: **mínimo 2, máximo 4** por artigo.
- Validação no save (não publica fora desse intervalo).
- Casing fixo. `Questionário` (não `questionário`, `Questionários`, `Quiz`, `Prova`).
- Sinônimos rejeitados explicitamente em `vocabulario-controlado.json` → `topicos_controlados`. Ex.: "Prova" é sinônimo popular de *Questionário*, não é tópico.
- Adição/remoção de tópico exige decisão formal (Elton + Rute) + atualização sincronizada deste documento, do `contentsystem.md` §B.3 e do `vocabulario-controlado.json`.
- Tópicos órfãos (sem nenhum artigo) entram em revisão no ciclo mensal de ContentOps.
- Os Grupos da tabela serão utilizados para identificação da iconografia a ser utilizada para o artigo ("o artigo x faz parte do grupo y"). 

> Definições, sinônimos aceitos e rejeitados, e termo popular: ver `output/vocabulario-controlado.json` (campo `topicos_controlados`). Refinamento pedagógico fino pendente com Rute (status `a_validar` — não bloqueia operação).

---

## 6. Eixo 4 — Trilha + Percurso (camada de curadoria)

A semântica dos três níveis (Decisão 18):

| Nível | O que é | Composto por | Objetivo |
|---|---|---|---|
| **Artigo** | Unidade atômica | — | Resolver um problema ou explicar um conceito |
| **Trilha** | Micro-jornada de conhecimento (começo, meio, fim reais) | Artigos (ordenados) | Ensinar como fazer algo específico |
| **Percurso** | Caminho formativo maior | Trilhas + artigos complementares soltos | Profissionalizar em uma área ou tema |

**Analogia validada (Marquito):** *"É como um parque nacional — o percurso é o parque, as trilhas são as trilhas menores que o compõem."*

### 6.1 Regras de Trilha

| Regra | Decisão |
|---|---|
| Mínimo **3 artigos** | 18, 25 |
| **Sem máximo**. Alerta editorial (não bloqueante) acima de ~10 artigos: revisar se não deveria virar percurso de trilhas menores | 25 |
| Um artigo **pode estar em múltiplas trilhas** | 18 |
| Um artigo **funciona dentro e fora da trilha** — deve ser útil sozinho | 18 |
| Artigo-âncora (primeiro da sequência) pode servir múltiplas trilhas. **Conteúdo do artigo é editorialmente neutro quanto à trilha** — não anuncia a sequência, não fecha com "próximo passo da trilha". A voz da sequência vive na **casca** (box de trilha + página da trilha) | 26 |
| Box de trilha aparece **sempre** que o artigo pertence a ≥1 trilha — vínculo **estrutural** (CMS), não comportamental (referrer) | 28 |
| V1 mostra **apenas posição estrutural** ("Artigo X de Y"). Sem rastreamento de progresso pessoal, sem localStorage | 29 |
| Apresentação multi-trilha no artigo: **acordeão** (`BoxTrilhaAcordeao`). Posição compacta `X/Y` sempre visível mesmo colapsado. Primeira expandida por padrão. Múltiplas abertas simultaneamente permitidas | 30 |
| Terminologia: itens de uma **trilha** chamam-se *artigos* ("Artigo 3 de 7") | 18, 29 |

### 6.2 Regras de Percurso

| Regra | Decisão |
|---|---|
| Percurso é **apenas agregação curada**. Sem certificado, badge, rastreamento ou marca de "completou" | 27 |
| Percurso **não tem ordem linear obrigatória** — o leitor escolhe por qual trilha começar. A página dedicada sugere **3 rotas de entrada por perfil** | 18, 27, 31 |
| Pode conter **trilhas + artigos soltos complementares** | 18, 27 |
| **Cor reservada: dourado** (`--gold` / `--gold-soft` / `--gold-deep`). Verde IFES fica reservado para trilha. Categoria/Tópico são neutros | 31 |
| Três superfícies de apresentação: (a) página dedicada `/percursos/{slug}` · (b) chip dourado no topo do acordeão de trilha · (c) listagem `/percursos` (grid com borda dourada de 4px) | 31 |
| Terminologia: itens de um **percurso** chamam-se *passos* (podem ser trilhas ou artigos) | 18 |

### 6.3 Diferença formal entre Categoria e Percurso

| Camada | Função | Como ler |
|---|---|---|
| **Categoria** (Eixo 2) | *Classifica* — onde o artigo encaixa no domínio | Resposta a "onde está?" |
| **Percurso** | *Narra* — que jornada de aprendizagem faz sentido junto | Resposta a "como percorrer?" |

Ambos são agregações tecnicamente; semanticamente são diferentes (Decisão 27).

### 6.4 Trilhas-piloto V1 (5 trilhas)

| Trilha | Consolida da base antiga | Artigos estimados |
|---|---|---|
| **Iniciando no Moodle** | Iniciando no Moodle + parte de Professor Moodle | ~12 |
| **Avaliação no Moodle** | Tudo sobre prova online + Livro de Notas | ~15 |
| **Acessibilidade no AVA** | Acessibilidade no AVA | ~7 |
| **IA para Professores** | Inteligência Artificial | ~8 |
| **Padrão Visual Cefor** | (novo, a partir de Identidade Cefor) | ~5 |

> Lista de partida do Sprint 3 — validação pedagógica das sequências (ordem + começo/meio/fim) é responsabilidade de Rute + Juliana, antes da Fase 4 (Produção de Conteúdo).

> Percursos V1: a definir conforme as trilhas amadureçam. Candidato natural: **"Dominando o Moodle"** (Iniciando no Moodle + Avaliação no Moodle + complementares).

---

## 7. Mapeamento da base antiga → nova arquitetura

### 7.1 Categorias (20 → 6)

```
AVA / Ambiente virtual / Moodle              → Gestão e Operação do Moodle
Gestão e Config do Moodle                    → Gestão e Operação do Moodle
Recurso Educacional                          \
Ferramentas de autoria                        ├→ Ferramentas e Recursos
Ferramentas de comunicação                   /
IA aplicada (parte ferramental)               ↗
Aspectos Pedagógicos                         \
Conhecimentos Pedagógicos                     ├→ Pedagogia e Planejamento
Tecnologias Educacionais (conceitual)        /
IA (parte conceitual)                         ↗
(transversal)                                → Acessibilidade
Direitos Autorais · Netiqueta · Segurança    ├→ Conduta e Conformidade
Procedimento Administrativo                  /
Padrão Visual · MOOC · Templates             → Identidade
"Outros" (30 artigos) + (vazia, 5 artigos)   → Redistribuir conforme conteúdo real
```

### 7.2 Tipos (10 → 5)

```
Tutorial / Tutorial-Avaliação                → Tutorial
Referência Moodle / Template-Code            ├→ Referência
Institucional-Padrão Visual                  /
Conceitual                                   → Conceitual
(novo)                                       → Solução de Problema
Ferramenta Externa / Ferramenta-GPT          → Recurso
Evento-Divulgação                            → REMOVIDO (não pertence à base)
"Outros"                                     → Reclassificar
```

### 7.3 Tags → Tópicos (82 → 25)

Eliminada a cauda longa (62% das tags antigas eram cauda longa de uso ≤2). Casing único. Veja `vocabulario-controlado.json` para mapeamento sinônimo→preferido completo.

### 7.4 Percursos (12 → 5 trilhas + estrutura Percurso)

```
Iniciando no Moodle + Professor Moodle       → trilha "Iniciando no Moodle"
Tudo sobre prova online + Livro de Notas     → trilha "Avaliação no Moodle"
Acessibilidade no AVA                        → trilha "Acessibilidade no AVA"
Inteligência Artificial                      → trilha "IA para Professores"
(novo de Identidade)                         → trilha "Padrão Visual Cefor"

Direitos Autorais e Segurança (5)            → REMOVIDO (vira categoria Conduta)
Ferramentas educacionais (9)                 → REMOVIDO (sobrepõe categoria)
Moodle Codes (8)                             → REMOVIDO (vira tópico transversal)
Gamificação (5)                              → REMOVIDO (volume insuficiente)
Gestão e Config do Moodle (10)               → REMOVIDO (vira categoria)
Planejamento e Design Educacional            → REMOVIDO (já 404)
Professor Moodle                             → REMOVIDO (escopo amplo demais)
```

> Mapeamento artigo-a-artigo dos 131 artigos antigos é entregável de Fase 4.1 (Triagem por Rubrica) — Juliana + Elton.

---

## 8. URLs semânticas — proposta (⏳ pendente de aprovação Elton + Marcos)

Padrão proposto:

```
/{categoria-slug}/{artigo-slug}        Artigo (categoria sustenta URL — estável)
/trilhas/{trilha-slug}                 Página de trilha
/percursos/{percurso-slug}             Página de percurso
/percursos                             Listagem de percursos
/topicos/{topico-slug}                 Página de descoberta por tópico
/buscar?q=...&tipo=...&categoria=...   Busca com filtros (Decisão 11)
```

**Princípios:**
- **Categoria sustenta URL** (eixo mais estável). Tipo e tópico são metadados, não compõem URL.
- **Slugs em minúsculas + hífen.** Sem acento, sem caractere especial.
- **Sem prefixo `/artigos/`** — a categoria já posiciona o conteúdo. Reduz profundidade da URL.
- **Slug do artigo é livre** (gerado a partir do H1, editável). Não inclui tipo, autor ou data.
- **URLs antigas** redirecionam via 301 para o novo endereço (responsabilidade da Fase 5 — Lançamento).

**Exemplos:**
```
/gestao-moodle/configurar-livro-de-notas
/ferramentas/h5p-conteudo-interativo
/acessibilidade/tempo-ampliado-no-questionario
/trilhas/avaliacao-no-moodle
/percursos/dominando-o-moodle
/topicos/questionario
```

> Variante considerada e rejeitada: `/artigos/{slug}` (sem categoria na URL). Perde sinal semântico para SEO/GEO e desacopla a URL do agrupamento principal.

**Pergunta aberta:** versionamento de URL ao mudar artigo de categoria. Proposta: redirect 301 + alias permanente. **Decidir junto com a Estratégia de Descoberta** (`output/descoberta-seo-geo.md`, ainda não produzido).

---

## 9. Implementação em WordPress (resumo)

Detalhamento em `contentsystem.md` §B.3 e §B.4. Mapeamento:

| Eixo | Implementação WP |
|---|---|
| Tipo | Taxonomia custom `tipo` (não hierárquica) |
| Categoria | Taxonomia custom `categoria` (não hierárquica) |
| Tópico | Taxonomia custom `topico` (não hierárquica, validação 2–4) |
| Trilha | **CPT `trilha`** (com campo `artigos` relationship ordenado) — não é taxonomia, é entidade |
| Percurso | **CPT `percurso`** (com campos `trilhas` + `artigos_complementares` + `como_percorrer`) |

> Trilha/Percurso são CPTs (não taxonomias) porque têm metadados ricos (descrição pedagógica, "para quem é", "como percorrer", ordenação) que taxonomias do WordPress não suportam bem.

---

## 10. Regras de validação no editor

| Campo | Regra | Bloqueante? |
|---|---|---|
| `tipo` | Exatamente 1 (select único, lista fechada) | ✅ |
| `categoria` | Exatamente 1 (select único, lista fechada) | ✅ |
| `topico` | Mínimo 2, máximo 4 (multi-select, lista fechada — sem digitação livre) | ✅ |
| `trilha` | 0 ou mais (relationship) | — |
| Trilha → `artigos` | Mínimo 3 (Decisão 25) | ✅ |
| Trilha → `artigos` | Alerta acima de 10 (revisão pedagógica) | ⚠️ não bloqueante |

---

## 11. Pendências (Sprint 3 e adiante)

| Pendência | Bloqueia | Responsável |
|---|---|---|
| **URLs semânticas** — aprovação formal do padrão proposto em §8 | Implementação WP (Fase 3) · Estratégia SEO/GEO | Elton + Marcos |
| **Estratégia de Descoberta** (SEO estrutural + GEO + busca interna) — `output/descoberta-seo-geo.md` | Implementação SEO/busca (Fase 3) | Elton + Marcos (Sprint 3) |
| **Validação pedagógica das Decisões 25–32** (Trilha/Percurso) | Arquitetura Trilha/Percurso vira fonte canônica definitiva | Reunião com Rute + Marquito a marcar |
| **Validação das 5 trilhas-piloto** (ordem, começo/meio/fim) | Fase 4 (Produção de Conteúdo) | Rute + Juliana |
| **Refino pedagógico fino dos 25 tópicos** (status `a_validar` no vocabulário) | Linter e busca completos (não bloqueia operação) | Rute |
| **Mapeamento dos 131 artigos antigos** nos novos eixos | Triagem (Fase 4.1) | Elton + Juliana |
| **Definição dos percursos V1** a partir das trilhas-piloto | Componente "página de percurso" carregar conteúdo real | Elton + Rute (após validação das trilhas) |

---

## 12. Decisões consolidadas neste documento

| Decisão | Tema | Onde aparece |
|---|---|---|
| 17 | Taxonomia em 4 eixos | §2 |
| 18 | Arquitetura Artigo / Trilha / Percurso | §6 |
| 25 | Tamanho da trilha (mín 3, sem máx) | §6.1 |
| 26 | Artigo-âncora em múltiplas trilhas + neutralidade editorial | §6.1 |
| 27 | Percurso é apenas agregação (sem progresso/certificado) | §6.2, §6.3 |
| 28 | Box de trilha sempre visível (vínculo estrutural) | §6.1 |
| 29 | V1 sem rastreamento de progresso pessoal | §6.1 |
| 30 | Apresentação multi-trilha por acordeão | §6.1 |
| 31 | Apresentação visual do percurso (3 superfícies, cor dourada) | §6.2 |
| 32 | Remoção do prev/next no rodapé do artigo | §6.1 (consequência: navegação exclusiva pelo acordeão) |
| Fechamento 2026-05-21 | 6ª categoria (Gestão e Operação do Moodle) + 25 tópicos | §4, §5 |

---

## Histórico de versões

| Versão | Data | Mudança | Por |
|---|---|---|---|
| 1.0 | 2026-05-26 | Documento canônico criado. Consolida Decisões 17, 18, 25–32 + fechamento da 6ª categoria e 25 tópicos (2026-05-21). URLs semânticas em §8 como proposta pendente. | Elton + Claude |
