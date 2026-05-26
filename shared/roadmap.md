# Roadmap — Base de Conhecimento CEFOR/Ifes

> **Versão:** 0.3 — Taxonomia e interface do artigo validadas
> **Data:** 2026-05-14 (criado 2026-04-07)
> **Aprovação:** Elton + Marcos
> **Plataforma:** WordPress (servidor novo, já instalado)

---

## Visão do Projeto

Criar uma nova Base de Conhecimento **muito bem estruturada, bonita, com experiência de leitura excelente, extremamente útil e funcional** para profissionais de EaD do Ifes. Ambições maiores (gamificação, chatbot, contribuição wiki, certificação) ficam para fases futuras.

---

## Equipe

| Pessoa | Papéis | Responsabilidades no projeto |
|---|---|---|
| **Elton** | Tech Lead, Dev, Designer | Responsável pelo projeto, decisões técnicas, design, implementação |
| **Marcos** | Dev, Chefe do Elton | Desenvolvimento, aprovação final junto com Elton |
| **Juliana** | Designer, Conteudista | Design visual, pesquisa, produção e reescrita de conteúdo |
| **Rute** | Consultora pedagógica | Orientação editorial, padrões pedagógicos, revisão de qualidade |

---

## Premissas

- WordPress é a plataforma. Não haverá avaliação de alternativas nesta versão.
- O servidor novo já está pronto com WordPress atualizado e instalado.
- O conteúdo será migrado no final, após as definições estarem prontas.
- Os ~60 artigos atuais provavelmente serão **reescritos** seguindo o novo padrão editorial, textual e estrutural — não apenas copiados.
- O foco é qualidade e estrutura, não velocidade de entrega.

---

## Arquitetura do Projeto: 3 Sistemas

O projeto é sustentado por **3 sistemas interdependentes**. Nenhum funciona bem sem os outros dois.

```
┌──────────────────────────────────────────────────────────────┐
│                     BASE DE CONHECIMENTO                      │
│                                                               │
│   ┌─────────────────┐           ┌─────────────────┐          │
│   │ CONTENT SYSTEM   │◄────────►│  DESIGN SYSTEM   │          │
│   │  10 camadas      │  informa  │  6 camadas       │          │
│   │                  │  ◄────►  │                  │          │
│   │  Como se escreve │          │  Como se vê      │          │
│   │  Como se organiza│          │  Como se comporta│          │
│   │  Como se avalia  │          │  Como se navega   │          │
│   │  Como se mantém  │          │  Como se acessa   │          │
│   └─────────────────┘           └─────────────────┘          │
│                                                               │
│   ┌──────────────────────────────────────────────────┐       │
│   │         TAXONOMIA + DESCOBERTA                    │       │
│   │    Arquitetura de informação + SEO/GEO            │       │
│   └──────────────────────────────────────────────────┘       │
└──────────────────────────────────────────────────────────────┘
```

| Sistema | Documento de referência | Pilares que cobre |
|---|---|---|
| Content System | `docs/content-system-escopo.md` | 3 (Modelo de Conteúdo), 7 (Ciclo de Vida), 10 (Autoria) + inputs para 4, 6, 8, 11 |
| Design System | `docs/design-system-escopo.md` | 1 (Visual), 2 (Interação), 5 (Acessibilidade), 6 (Leitura), 8 (Estados), 9 (Responsivo) |
| Taxonomia + Descoberta | A definir na Fase 1 | 4 (Taxonomia), 11 (Descoberta) |

---

## As 6 Fases

```
Fase 0 ─ Pesquisa e Benchmarking
    ↓
Fase 1 ─ Fundações (Content System + Taxonomia + Descoberta)
    ↓
Fase 2 ─ Design System (Visual + Leitura + Acessibilidade + Interação)
    ↓
Fase 3 ─ Implementação WordPress (Tema + Componentes + Templates)
    ↓
Fase 4 ─ Produção de Conteúdo (Triagem por rubrica + reescrita + novos)
    ↓
Fase 5 ─ Lançamento e Operação Contínua
```

---

## Fase 0 — Pesquisa e Benchmarking ✅ CONCLUÍDA

**Objetivo:** Colecionar referências e ideias que alimentem as decisões de todas as fases seguintes.

**Status:** ✅ CONCLUÍDA — 16 decisões registradas em `_config/decisoes.md`

| Entrega | Responsável | Descrição |
|---|---|---|
| Fichas de benchmarking (mín. 6 sites) | Juliana | Pesquisa com os 5 óculos: Visual, Leitura, Interação, Estrutura do Texto, Acessibilidade |
| Análise consolidada do benchmarking | Elton + Juliana | Revisão conjunta, identificação de padrões recorrentes e decisões |
| Análise da base atual | Juliana | Inventário finalizado: o que deletar, atualizar ou reescrever |

**Pilares alimentados:** Todos os 11. O benchmarking é insumo transversal.

**Critério de conclusão:** Fichas entregues, padrões identificados, equipe alinhada sobre referências.

---

## Fase 1 — Fundações 🔄 EM ANDAMENTO

**Objetivo:** Definir as regras do jogo antes de tocar em visual ou código. Sem essa fase, o design fica bonito mas sem alma, e a produção de conteúdo fica inconsistente.

**Esta é a fase mais crítica do projeto. É aqui que se define o que torna a base excelente — não no visual.**

**Status parcial (2026-05-14):**
- ✅ Taxonomia em 4 eixos validada (Tipo, Categoria, Tópico, Trilha) — Decisão 17
- ✅ Arquitetura Trilha/Percurso definida — Decisão 18
- ✅ Interface do artigo validada (cabeçalho, multimodal, rodapé) — Decisões 19-24
- ✅ Protótipo `prototipo-artigo.html` referendado como referência canônica
- ⏳ Content System (camadas 1-10) — pendente
- ⏳ URLs semânticas + Estratégia de descoberta — pendente

A Fase 1 é composta por 3 blocos: o **Content System** (10 camadas), a **Taxonomia** e a **Estratégia de Descoberta**.

---

### Bloco 1 — Content System — 10 camadas

Referência completa: `docs/content-system-escopo.md`

As camadas 1 a 7 são interdependentes e devem ser definidas em conjunto.

| # | Camada | Pilar | Responsável | O que entrega |
|---|---|---|---|---|
| 1 | **Princípios Editoriais** (Content Playbook) | Transversal | Elton + Rute | Princípios editoriais inegociáveis. Escopo positivo e negativo da base ("o que somos / o que não somos"). |
| 2 | **Matriz de Voz e Tom** (Voice & Tone Matrix) | Pilares 3, 10 | Rute + Juliana | Voz constante da base + variações de tom por contexto do leitor e tipo de artigo. |
| 3 | **Vocabulário Controlado** (Controlled Vocabulary) | Pilares 3, 4 | Rute + Elton + Juliana | Vocabulário padronizado: termos preferidos, sinônimos rejeitados, mapeamento CEFOR ↔ Moodle ↔ MEC ↔ popular. |
| 4 | **Biblioteca de Padrões de Conteúdo** (Content Patterns Library) | Pilares 3, 10 | Elton + Rute | Padrões reutilizáveis de estrutura textual: passo a passo com checkpoint, problema→solução, quando usar/não usar, analogia, antes/depois, FAQ invertido, resumo progressivo. |
| 5 | **Rubrica de Qualidade** (Quality Scorecard) | Pilares 7, 10 | Rute + Juliana + Elton | Rubrica com 7 dimensões ponderadas (acionabilidade, escaneabilidade, precisão, completude, clareza, conformidade, frescor). Score mínimo para publicação. Também usado na triagem dos ~60 artigos existentes. |
| 6 | **Padrões de Legibilidade** (Readability Standards) | Pilares 3, 6 | Rute + Elton | Métricas objetivas de legibilidade: palavras por frase, frases por parágrafo, índice Flesch PT-BR, voz passiva, jargão. Limites por tipo de artigo. |
| 7 | **Mapa de Modelos Mentais do Público** (Audience Mental Model Map) | Pilares 3, 10 | Rute + Juliana | Perfis mentais do público (professor migrante, mediador experiente, coordenador, novato, técnico TI). Momentos de busca. Vocabulário natural. |
| 8 | **Política de Depreciação** (Deprecation & Sunset Policy) | Pilares 7, 8 | Elton + Juliana | Gatilhos de obsolescência (temporal, evento, uso, feedback). Fluxo: publicado → revisão pendente → desatualizado → depreciado → arquivado. Regras de redirect e transparência. |
| 9 | **Operação de Conteúdo** (ContentOps Charter) | Pilares 7, 10 | Elton + Marcos | Capacidade operacional real: ~4-6 artigos/mês. Cadência de revisão por tipo. Fluxo de produção com IA (prompt → geração → revisão Juliana → revisão Rute → revisão Elton → scorecard → publicação). SLAs. |
| 10 | **Métricas de Sucesso** (Measurement Framework) | Pilares 7, 11 | Elton | Métricas de sucesso: taxa de resolução, bounce rate, retorno, buscas sem resultado, "artigo útil?", horas/artigo. Dashboard mensal de saúde. *Definido na Fase 1, operacionalizado na Fase 5.* |

---

### Bloco 2 — Taxonomia

> ✅ Arquitetura de 4 eixos aprovada em 2026-05-14. Falta formalizar o documento de output em `stages/01-fundacoes/output/taxonomia.md`.

| Entrega | Pilar | Status | Responsável | Descrição |
|---|---|---|---|---|
| **Arquitetura em 4 eixos** | Pilar 4 | ✅ Validado | Elton + Marquito | Tipo (1) + Categoria (1) + Tópico (2-4) + Trilha (0+). Tags livres abolidas. 25 tópicos controlados. |
| **Arquitetura Trilha/Percurso** | Pilar 4 | ✅ Validado | Elton + Marquito + Rute | Trilha = jornada atômica de artigos (começo, meio, fim). Percurso = conjunto de trilhas + possíveis artigos soltos. Um artigo pode estar em múltiplas trilhas. |
| **Documento formal de taxonomia** | Pilar 4 | ⏳ Pendente | Elton | Formalizar em `stages/01-fundacoes/output/taxonomia.md` com todos os valores, regras e exemplos. |
| **URLs Semânticas** | Pilar 4 | ⏳ Pendente | Elton + Marcos | Estrutura de URLs para artigos, trilhas, percursos, categorias e busca. |

---

### Bloco 3 — Estratégia de Descoberta

| Entrega | Pilar | Responsável | Descrição |
|---|---|---|---|
| **SEO Estrutural** | Pilar 11 | Elton + Marcos | Schema.org (`EducationalArticle`), meta tags, Open Graph, sitemap, canonical tags. |
| **GEO (Generative Engine Optimization)** | Pilar 11 | Elton + Marcos | Estrutura citável por IAs: definições explícitas, formato Q&A, FAQ por artigo, sinais de autoria. |
| **Busca Interna** | Pilar 11 | Elton + Marcos | Estratégia de busca (full-text vs semântica), filtros, ranking de relevância. |

---

### Sistema de Estados (transversal)

| Entrega | Pilar | Responsável | Descrição |
|---|---|---|---|
| **Mapa de Estados** | Pilar 8 | Elton | Estados do conteúdo (alinhados com a Deprecation Policy) + estados do usuário (lido, salvo, em progresso — o que for viável no WordPress V1) + estados de componentes de interface. |

---

**Dependência:** Fase 0 concluída (benchmarking entregue e analisado).

**Critério de conclusão:** Cada entrega documentada e aprovada por Elton + Marcos. Rute valida as camadas 1-7 do Content System. Todos os documentos de referência atualizados.

---

## Fase 2 — Design System

**Objetivo:** Definir a linguagem visual completa da base — tokens, componentes, comportamento responsivo, acessibilidade, experiência de leitura.

**Os 6 pilares do Design System são interdependentes e devem ser trabalhados juntos nesta fase.**

| Entrega | Pilar | Responsável | Descrição |
|---|---|---|---|
| **Design Tokens** | Pilar 1 | Elton + Juliana | Paleta de cores (claro + escuro), escala tipográfica, espaçamento, sombras, bordas, breakpoints. Fonte única de verdade para todos os valores visuais |
| **Sistema de Leitura** | Pilar 6 | Elton + Juliana | Largura de coluna, altura de linha, espaçamento entre parágrafos, indicador de progresso, tempo de leitura, índice de seções. Foco em conforto para leitura longa |
| **Componentes (Atomic Design)** | Pilares 1, 2, 8 | Elton + Juliana | Átomos, moléculas e organismos definidos no documento de escopo do DS. Cada componente com variantes, estados, comportamento responsivo e acessibilidade |
| **Acessibilidade** | Pilar 5 | Elton + Juliana | Conformidade e-MAG + WCAG 2.2 AA. Contraste, navegação por teclado, semântica HTML, ARIA, Libras (widget). Embutido em cada componente, não como camada separada |
| **Comportamento Responsivo** | Pilar 9 | Elton + Juliana | Breakpoints, comportamento de cada componente por dispositivo. Atenção especial: índice de seções, action bar, blocos de código, tabelas em mobile |
| **Interações** | Pilar 2 | Elton + Marcos | Curtir, compartilhar, copiar ABNT, salvar, comentar (se viável em V1). Feedback visual, estados, microinterações |
| **Layouts de Página** | — | Elton + Juliana | Templates: Home, Artigo, Percurso/Trilha, Busca, Categoria. Protótipos de alta fidelidade antes de codificar |

**Dependência:** Fase 1 concluída. O Modelo de Conteúdo define quais componentes existem (se tem TL;DR, precisa de TLDRBox; se tem alertas, precisa de AlertBox).

**Critério de conclusão:** Protótipos de alta fidelidade aprovados por Elton + Marcos. Tokens documentados. Checklist de acessibilidade validado.

---

## Fase 3 — Implementação WordPress

**Objetivo:** Transformar o Design System e as definições editoriais em um tema WordPress funcional.

| Entrega | Responsável | Descrição |
|---|---|---|
| **Tema WordPress** | Elton + Marcos | Tema customizado implementando os tokens, componentes e templates do DS. Responsivo, acessível, performático |
| **Custom Post Types e Campos** | Elton + Marcos | Tipos de artigo, campos de metadados (autor, data de revisão, tempo de leitura, tipo, status), taxonomias (categorias, tags, percursos) |
| **Blocos Gutenberg Customizados** | Elton + Marcos | Blocos para os componentes editoriais: AlertBox, TLDRBox, CodeBlock, Quote, FAQItem. Para que quem escreve consiga montar artigos no padrão sem saber código |
| **Workflow de Publicação** | Elton + Marcos | Implementação do fluxo definido na Fase 1: estados, transições, permissões, revisão periódica |
| **SEO/GEO Técnico** | Elton + Marcos | Schema.org, meta tags automáticas, sitemap, Open Graph, canonical tags |
| **Busca Interna** | Elton + Marcos | Busca com filtros (categoria, tipo, percurso), relevância, resultados bem apresentados |
| **Widget de Acessibilidade** | Elton + Marcos | Alto contraste, ajuste de fonte, Libras (se viável via plugin/widget), atalhos de teclado |
| **Testes** | Todos | Testes de responsividade, acessibilidade (e-MAG), performance (Core Web Vitals), funcionalidade do workflow |

**Dependência:** Fase 2 concluída (protótipos aprovados, tokens definidos, componentes especificados). Content System (Fase 1) como referência para implementação dos blocos editoriais e workflow.

**Critério de conclusão:** Base funcional no servidor novo com todas as entregas acima. Testes passando. Aprovação de Elton + Marcos.

---

## Fase 4 — Produção de Conteúdo

**Objetivo:** Reescrever os artigos existentes e produzir novos seguindo o Content System completo (10 camadas) definido na Fase 1.

### Etapa 4.1 — Triagem por Rubrica de Qualidade (pode iniciar em paralelo à Fase 3)

Usa a Rubrica de Qualidade (Camada 5 do Content System) para decidir o destino de cada artigo existente.

| Score | Ação | Volume estimado |
|---|---|---|
| < 2.0 | Descartar ou reescrever do zero | A medir |
| 2.0 – 3.0 | Reescrever substancialmente | A medir |
| 3.0 – 3.5 | Atualizar e reformatar | A medir |
| > 3.5 | Migrar com ajustes menores | A medir |

**Responsável:** Juliana (avaliação) + Rute (validação pedagógica) + Elton (score final)

### Etapa 4.2 — Produção e Reescrita

| Entrega | Responsável | Descrição |
|---|---|---|
| **Reescrita dos artigos** | Juliana + Rute + IA | Seguindo o fluxo da Operação de Conteúdo (Camada 9): prompt template → geração IA → revisão Juliana → revisão Rute → revisão Elton → rubrica ≥ 3.5 → publicação |
| **Padrões de conteúdo aplicados** | Juliana | Cada artigo usa os padrões da Biblioteca de Padrões de Conteúdo (Camada 4): passo a passo com checkpoint, problema→solução, FAQ invertido, etc. |
| **Vocabulário Controlado aplicado** | Juliana + Rute | Termos padronizados conforme Vocabulário Controlado (Camada 3). Termos Moodle na primeira menção + termo pedagógico entre parênteses. |
| **Padrões de Legibilidade validados** | Juliana | Cada artigo passa nas métricas de legibilidade (Camada 6): palavras por frase, índice Flesch, voz passiva. |
| **Organização em percursos** | Juliana + Rute | Artigos organizados nas trilhas/percursos definidos na taxonomia |
| **Metadados completos** | Juliana | Autor, data, tipo, categoria, tags, tempo de leitura, versão, licença, marcação "produzido com assistência de IA" quando aplicável |
| **Artigos-piloto** | Juliana + Elton | 3-5 artigos completos publicados como teste real antes de migrar tudo |

**Dependência:** Etapa 4.1 depende do Content System (Fase 1). Etapa 4.2 depende da base funcional (Fase 3) para publicação, mas a reescrita em documentos pode iniciar antes.

**Capacidade estimada:** ~4-6 artigos publicados por mês (conforme Operação de Conteúdo, Camada 9).

**Critério de conclusão:** Artigos prioritários reescritos com score ≥ 3.5, revisados e publicados. Percursos organizados. Artigos-piloto validados pela equipe.

---

## Fase 5 — Lançamento e Operação Contínua

**Objetivo:** Colocar a base no ar, ativar a operação contínua de conteúdo (ContentOps) e o monitoramento de saúde da base.

### Etapa 5.1 — Lançamento

| Entrega | Responsável | Descrição |
|---|---|---|
| **Lançamento interno (beta)** | Elton | Base disponível para equipe CGTE e grupo seleto de usuários. Coleta de feedback estruturado |
| **Ajustes pós-feedback** | Elton + Marcos | Correções e melhorias baseadas no feedback real |
| **Redirecionamento da base antiga** | Elton + Marcos | URLs antigas redirecionadas para os novos artigos (301 redirects). Evita links quebrados |
| **Lançamento público** | Elton + Marcos | Base disponível para todos os profissionais de EaD do Ifes |

### Etapa 5.2 — Operação Contínua (ContentOps)

Ativação da Operação de Conteúdo (Camada 9) e das Métricas de Sucesso (Camada 10) do Content System.

| Atividade | Frequência | Responsável | Descrição |
|---|---|---|---|
| **Produção de artigos novos** | Contínua (~4-6/mês) | Juliana + Rute + IA | Conforme fluxo da Operação de Conteúdo (Camada 9) |
| **Revisão periódica obrigatória** | Conforme cadência por tipo | Juliana + Rute | Tutoriais: 6 meses. Troubleshooting: 3 meses. Conceituais: 12 meses. |
| **Deprecation Policy ativa** | Automática + mensal | Elton + Juliana | Gatilhos temporais ativam badges. Revisão mensal dos artigos sinalizados. |
| **Dashboard de saúde da base** | Mensal | Elton | Score médio, artigos desatualizados, buscas sem resultado, taxa de "artigo útil", top acessos. |
| **Análise de gaps de conteúdo** | Mensal | Elton + Juliana | Termos mais buscados sem resultado → priorização de novos artigos. |
| **Atualização do Vocabulário Controlado** | Contínua | Rute + Juliana | Novos termos do público registrados conforme surgem em atendimentos e e-mails. |

### Etapa 5.3 — Evolução

| Entrega | Responsável | Descrição |
|---|---|---|
| **Plano de evolução V2** | Elton + Marcos | Definição do que entra na próxima versão: chatbot IA, gamificação, contribuição wiki, certificação, multimodal |

**Dependência:** Fase 4 com volume mínimo de artigos publicados.

**Critério de conclusão:** Base pública, redirecionamentos funcionando, ContentOps operando, dashboard de saúde configurado.

---

## Mapa de Pilares por Fase

| Pilar | Fase 0 | Fase 1 | Fase 2 | Fase 3 | Fase 4 | Fase 5 |
|---|---|---|---|---|---|---|
| 1. Sistema Visual | Pesquisa | — | **Define** | Implementa | — | Itera |
| 2. Sistema de Interação | Pesquisa | — | **Define** | Implementa | — | Itera |
| 3. Modelo de Conteúdo | Pesquisa | **Define (CS 1-7)** | Informa DS | Implementa | **Usa** | Itera |
| 4. Sistema de Taxonomia | Pesquisa | **Define** | — | Implementa | **Usa** | Itera |
| 5. Acessibilidade | Pesquisa | — | **Define** | Implementa | — | Audita |
| 6. Sistema de Leitura | Pesquisa | Inputs (CS 6) | **Define** | Implementa | — | Itera |
| 7. Ciclo de Vida | — | **Define (CS 5,8,9)** | — | Implementa | **Usa** | **Opera** |
| 8. Sistema de Estados | — | **Define (CS 8)** | Detalha DS | Implementa | — | Itera |
| 9. Sistema Responsivo | Pesquisa | — | **Define** | Implementa | — | Itera |
| 10. Sistema de Autoria | — | **Define (CS 1-9)** | — | Implementa | **Usa** | **Opera** |
| 11. Sistema de Descoberta | — | **Define** | — | Implementa | Inputs (CS 10) | **Opera** |

*CS = Camada do Content System*

---

## Mapa de Camadas do Content System por Fase

| Camada | Fase 0 | Fase 1 | Fase 2 | Fase 3 | Fase 4 | Fase 5 |
|---|---|---|---|---|---|---|
| 1. Princípios Editoriais (Content Playbook) | — | **Define** | — | — | **Usa** | Itera |
| 2. Matriz de Voz e Tom (Voice & Tone) | — | **Define** | — | — | **Usa** | Itera |
| 3. Vocabulário Controlado (Controlled Vocabulary) | Pesquisa | **Define** | — | — | **Usa** | Itera |
| 4. Biblioteca de Padrões (Content Patterns) | Pesquisa | **Define** | Informa DS | — | **Usa** | Itera |
| 5. Rubrica de Qualidade (Quality Scorecard) | — | **Define** | — | — | **Usa (triagem)** | Itera |
| 6. Padrões de Legibilidade (Readability Standards) | — | **Define** | — | Automação | **Usa** | Itera |
| 7. Modelos Mentais do Público (Mental Model Map) | Pesquisa | **Define** | Informa DS | — | **Usa** | Itera |
| 8. Política de Depreciação (Deprecation Policy) | — | **Define** | — | Implementa | — | **Opera** |
| 9. Operação de Conteúdo (ContentOps Charter) | — | **Define** | — | — | **Opera** | **Opera** |
| 10. Métricas de Sucesso (Measurement Framework) | — | Define | — | Implementa | — | **Opera** |

---

## Dependências Críticas

```
Fase 0 (Benchmarking)
    │
    └──→ Fase 1 (Content System + Taxonomia + Descoberta)
              │
              ├──→ Fase 2 (Design System) ── Biblioteca de Padrões e Modelos Mentais informam quais componentes criar
              │         │
              │         └──→ Fase 3 (WordPress) ── implementa Design System + Content System + Taxonomia
              │                    │
              │                    └──→ Fase 4.2 (Publicação) ── publica artigos na base funcional
              │                              │
              │                              └──→ Fase 5 (Lançamento + Operação)
              │
              ├──→ Fase 4.1 (Triagem por Rubrica) ── pode iniciar em paralelo à Fase 2
              │         │
              │         └──→ Fase 4.2 (Reescrita em documentos) ── em paralelo à Fase 3
              │
              └──→ Content System camadas 1-7 devem ser definidas JUNTAS
                   (mesma lógica dos 6 pilares do DS — são interdependentes)
```

**Oportunidades de paralelismo:**

| O que pode rodar em paralelo | Quando pode começar | Quem executa |
|---|---|---|
| Triagem dos artigos por rubrica (4.1) | Assim que Fase 1 fechar | Juliana + Rute |
| Reescrita de artigos em documentos (4.2) | Assim que Fase 1 fechar | Juliana + Rute + IA |
| Publicação no WordPress (4.2) | Quando Fase 3 estiver funcional | Juliana + Elton |

Isso significa que **Juliana e Rute não ficam paradas** esperando o WordPress. A triagem e a reescrita em documentos podem acontecer ao longo de toda a Fase 2 e 3.

---

## O que fica para o futuro (pós V1)

Ideias do brainstorm que **não** entram neste roadmap, mas ficam registradas:

| Ideia | Origem | Quando considerar |
|---|---|---|
| Chatbot/Tutor IA (evolução Sofia) | Rute + Marcos | V2 — após base estabilizada |
| Gamificação (badges, ranking, prêmio anual) | Marcos + Juliana + Rute | V3 — após comunidade ativa |
| Contribuição wiki de professores | Marcos | V2 — segundo semestre 2026 |
| Flashcards + áudio para estudo mobile | Marcos | V2 |
| Ferramentas interativas embutidas | Marcos | V2 |
| Trilhas com certificação | Rute | V2/V3 |
| Integração profunda com Moodle (LTI/embed) | Juliana + Marcos | V2 |
| Percurso por perfil (mediador, professor) | Rute | V1.5 — quick win pós-lançamento |

---

*Documento criado em: 2026-04-07*
*Atualizado em: 2026-05-14*
*Versão: 0.3 — Taxonomia e interface do artigo validadas*
*Projeto: Base de Conhecimento CEFOR/Ifes — Reformulação*
