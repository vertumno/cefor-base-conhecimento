# Camada 1 — Princípios Editoriais

> **Versão:** 1.0 — DRAFT
> **Status:** Carece de validação formal com Ruti Fávero (orientação pedagógica)
> **Última atualização:** 2026-05-19
> **Decisões consolidadas:** 1, 14, 15, 17, 18, 21, 22, 25, 26, 27, 29, 30
> **Camada-irmã:** Camada 4.5 (Padrões de Composição), Camada 3 (Vocabulário Controlado)

---

## 1. O que esta camada faz

Esta camada estabelece os **princípios inegociáveis** que orientam toda decisão editorial da Base de Conhecimento CEFOR/Ifes. Em conflito entre duas opções, é o conjunto de princípios aqui que arbitra.

Não são valores genéricos. Cada princípio tem **implicação prática verificável** — gera regras de produção, define o que cabe e o que não cabe na Base, e dá ao linter e à IA critérios objetivos de aceitação.

> **Hierarquia de autoridade dentro do Content System:**
> Princípios (Camada 1) → Decisões formais (`_config/decisoes.md`) → Padrões de Composição (Camada 4.5) → demais camadas.
> Em conflito, princípio prevalece.

---

## 2. Escopo da Base

### 2.1 — O que a Base É

| Característica | Decorrência prática |
|---|---|
| **Fonte oficial do CEFOR/Ifes** sobre uso pedagógico e técnico do Moodle institucional | Tom institucional, mesmo em artigos assinados |
| **Espaço de consulta + aprendizagem + atualização contínua** | Suporta tanto quem chega com pressa quanto quem quer aprofundar |
| **Editorialmente curada** | Toda publicação passa por revisão humana — não há contribuição aberta na V1 |
| **Acessível por padrão** | Multimodalidade (Libras, áudio), tipografia legível, contraste WCAG AA mínimo |
| **Atualizada** | Política de depreciação ativa (Decisão 21 — 12 meses) |

### 2.2 — O que a Base NÃO É

| A Base NÃO é… | Por quê |
|---|---|
| Um repositório de PDFs | PDFs viram conteúdo no Moodle, não na Base |
| Um blog de notícias | Não publicamos conteúdo datado sem valor permanente |
| Um manual técnico do Moodle | Documentação oficial do Moodle não precisa ser replicada — focamos no contexto Ifes |
| Um espaço de opinião pessoal | Tom institucional, mesmo quando assinado |
| Uma enciclopédia completa | Cobrimos o que o público precisa, não tudo que existe |
| Uma plataforma de cursos formais | Não há matrícula, certificado, frequência — isso é responsabilidade do AVA (Moodle) |
| Um sistema de gamificação | Sem badges, sem ranking, sem progresso pessoal rastreado (Decisão 27, 29) |

**Decisão de origem do escopo negativo:** Decisão 15 (escopo negativo V1), 27 (sem certificado), 29 (sem rastreamento).

---

## 3. Os 9 Princípios

### Família A — Arquitetura editorial

#### Princípio 1 — O artigo é a unidade soberana

**Enunciado:** Todo conteúdo da Base é, em última instância, um artigo. Trilhas e percursos são camadas de curadoria que envelopam, nunca alteram, o artigo.

**O que significa:**
- A "voz da sequência" ("este é o próximo passo", "você está na metade") vive na casca (box de trilha, página de trilha, página de percurso), **nunca no conteúdo do artigo**.
- Trilhas e percursos podem ser reorganizadas, criadas, depreciadas — e os artigos permanecem.
- Excluir uma trilha não exclui os artigos. Excluir um artigo, sim, afeta as trilhas que o contêm.

**Implicação prática:** Quando estiver escrevendo, esqueça onde o artigo será colocado. Escreva como se fosse a única coisa que o leitor vai ler.

**Decisão de origem:** Decisões 18, 22, 26.

---

#### Princípio 2 — Autossuficiente E encadeável

**Enunciado:** Todo artigo precisa resolver o problema dele sozinho (autossuficiente) E poder ser colocado em qualquer trilha sem reescrita (encadeável).

**O que significa:**
- Pré-requisitos são declarados explicitamente no topo (com link), nunca pressupostos.
- "Próximos passos" são lista plural, nunca item único.
- O artigo não referencia "o artigo anterior" — porque o anterior muda de trilha para trilha.
- A conclusão é fechada no próprio artigo; a continuação é responsabilidade da casca.

**Implicação prática:** Verificável pelo Checklist de Encadeabilidade (10 critérios objetivos da Camada 4.5). 5 dos critérios são automatizáveis via linter.

**Decisão de origem:** Decisões 18, 26.

---

### Família B — Qualidade do conteúdo

#### Princípio 3 — Se o leitor precisa perguntar para alguém depois de ler, o artigo falhou

**Enunciado:** Autonomia do leitor é critério de qualidade, não cortesia opcional.

**O que significa:**
- O artigo precisa cobrir o caminho feliz E os erros mais comuns.
- Termos técnicos são explicados na primeira ocorrência, mesmo que estejam no Vocabulário Controlado.
- Quando há decisão a tomar (Workshop vs Tarefa, rubrica vs nota direta), o artigo orienta a decisão — não só descreve as opções.

**Implicação prática:** Dimensão "Acionabilidade" da Rubrica de Qualidade (Camada 5, peso 20%). Score 5 = leitor sai sabendo fazer, verificar e corrigir se algo der errado.

**Decisão de origem:** Decisões 1 (propósito-farol — autonomia), 15 (escopo negativo).

---

#### Princípio 4 — Ensinamos fazendo, não explicando

**Enunciado:** Todo artigo conceitual inclui aplicação prática. Todo artigo prático contextualiza a decisão.

**O que significa:**
- Conceito sem aplicação vira filosofia abstrata.
- Aplicação sem contexto vira receita cega — leitor faz mas não sabe quando aplicar.
- Os 5 tipos de artigo (Tutorial, Referência, Conceitual, Solução, Recurso) variam na proporção contexto/aplicação, mas nenhum tipo é só uma das duas coisas.

**Implicação prática:** Mesmo artigo "Referência" (90% instrução) tem um parágrafo de contexto no topo. Mesmo artigo "Conceitual" (60% contexto) termina com aplicação prática.

**Decisão de origem:** Decisão 17 (tipos de artigo).

---

#### Princípio 5 — Acessível não é simples — é claro

**Enunciado:** Não simplificar a ponto de perder precisão técnica ou nuance pedagógica.

**O que significa:**
- O público da Base é profissional (professores, mediadores, coordenadores) — respeitar a inteligência do leitor.
- Linguagem simples é diferente de linguagem rasa. O artigo pode ser denso e claro ao mesmo tempo.
- Termos técnicos podem (e devem) aparecer — explicados na primeira ocorrência, mas não evitados.
- Padrões de Legibilidade (Camada 6) definem limites mensuráveis (Flesch ≥ 50 para tutorial), não regras de empobrecimento.

**Implicação prática:** Antes de simplificar um termo, perguntar: estou tornando mais claro, ou estou tornando menos preciso? Se for o segundo, manter o termo e explicar.

**Decisão de origem:** Decisões 5 (callouts/destaques), 10 (acessibilidade), 13 (multimodalidade).

---

#### Princípio 6 — Honestidade técnica antes de afeto

**Enunciado:** Não prometer ao leitor o que não há mecanismo real para entregar.

**O que significa:**
- Sem rastreamento de progresso pessoal porque não há login na V1 (Decisão 29).
- Sem certificado de conclusão de percurso porque não há infraestrutura para isso (Decisão 27).
- Sem badges, ranking ou gamificação fake — a Base não é Duolingo.
- O que aparece como "Artigo 5 de 12" é posição estrutural, não progresso. E o nome diz isso.

**Implicação prática:** Linguagem honesta na interface. "Artigo 5 de 12" em vez de "Você completou 5 de 12". "Sem ordem obrigatória" em vez de "comece aqui".

**Decisão de origem:** Decisões 27, 29.

---

### Família C — Operação editorial

#### Princípio 7 — Conteúdo tem prazo de validade

**Enunciado:** Todo artigo nasce com data de revisão programada. Nenhum artigo é "para sempre".

**O que significa:**
- O Moodle atualiza. Práticas pedagógicas evoluem. A regulamentação muda.
- Política formal de depreciação (Camada 8): 12 meses sem revisão = badge "revisão pendente" (visível só para admins).
- A data da última revisão é metadado interno; aparece na citação ABNT do rodapé, mas não no cabeçalho do artigo.

**Implicação prática:** Quem cria um artigo cria também a tarefa de revisão programada. Sem isso, o artigo nasce dívida.

**Decisão de origem:** Decisões 14 (metadados), 21 (12 meses).

---

#### Princípio 8 — IA acelera, humano valida

**Enunciado:** Nenhum conteúdo gerado por IA é publicado sem revisão pedagógica humana.

**O que significa:**
- IA gera rascunho. Sempre.
- Juliana revisa estrutura, precisão técnica, tom.
- Ruti revisa adequação pedagógica.
- Elton revisa conformidade técnica.
- Só então publica.
- Artigos produzidos com assistência de IA são marcados como tal (compliance legal).

**Implicação prática:** O gargalo real da operação não é geração de conteúdo (IA é rápida). É revisão humana. A Camada 9 (ContentOps) define capacidade real considerando esse gargalo: ~4-6 artigos publicados por mês.

**Decisão de origem:** Camada 9 do escopo original; sem decisão formal específica ainda — a validar com Ruti.

---

#### Princípio 9 — Menos artigos excelentes > muitos artigos medianos

**Enunciado:** Qualidade sobre volume. Sempre.

**O que significa:**
- A Base não precisa cobrir todos os tópicos possíveis na V1.
- Um artigo excelente sobre questionários é mais valioso que cinco artigos medianos sobre cinco temas.
- Critério de excelência: score ≥ 4 na Rubrica de Qualidade (Camada 5).
- Artigos com score 2.5-3.4 entram com badge "em melhoria" e prazo de revisão de 30 dias. Score < 2.5 não publica.

**Implicação prática:** Cobertura por categoria não é meta numérica fixa. Categoria pode ter 3 artigos excelentes e nada mais. Crescemos quando há excelência para crescer.

**Decisão de origem:** Decisão 1 (propósito-farol — não é formação estruturada).

---

## 4. Hierarquia dos princípios em conflito

Princípios podem aparentemente entrar em choque. A ordem abaixo resolve isso na decisão editorial:

```
1. O artigo é a unidade soberana
   ↓
2. Autossuficiente E encadeável
   ↓
6. Honestidade técnica antes de afeto
   ↓
3. Autonomia do leitor (não precisa perguntar)
   ↓
5. Acessível não é simples — é claro
   ↓
4. Ensinamos fazendo, não explicando
   ↓
9. Menos artigos excelentes > muitos medianos
   ↓
7. Conteúdo tem prazo de validade
   ↓
8. IA acelera, humano valida
```

**Por que essa ordem:**
- Princípios 1 e 2 são arquiteturais — quebrá-los quebra a integridade da Base.
- Princípio 6 protege a credibilidade — quebrar honestidade técnica corrói a confiança do leitor.
- Princípios 3, 4, 5 cuidam da qualidade do artigo em si.
- Princípio 9 orienta priorização — vem depois dos princípios de qualidade individual.
- Princípios 7 e 8 são operacionais — importantes, mas não fundadores.

---

## 5. Casos concretos de aplicação

### Caso A — Artigo prevê um exemplo do "artigo anterior"

> "Conforme vimos no artigo anterior, ao configurar o feedback..."

**Princípio violado:** 2 (Encadeabilidade).
**Por quê:** "Anterior" muda dependendo da trilha em que o artigo está sendo lido.
**Correção:** Substituir por "Ao configurar feedback (ver [artigo X](#))..." — link explícito, não posição relativa.

---

### Caso B — Página de percurso tem botão "Receber certificado"

**Princípio violado:** 6 (Honestidade técnica).
**Por quê:** Não há infraestrutura para certificação na V1 (Decisão 27).
**Correção:** Remover. Reavaliar em V2 se houver login e processo formal.

---

### Caso C — Artigo evita explicar "questionário" porque "todo mundo sabe"

**Princípio violado:** 3 (Autonomia do leitor).
**Por quê:** "Todo mundo sabe" assume um leitor padrão que não existe. Quem caiu pelo Google pode não saber.
**Correção:** Explicar na primeira ocorrência, mesmo brevemente — Vocabulário Controlado (Camada 3) tem a definição.

---

### Caso D — Equipe quer publicar 20 artigos rasos para "ter conteúdo no lançamento"

**Princípio violado:** 9 (Qualidade sobre volume).
**Por quê:** 20 artigos com score < 3 prejudicam a credibilidade da Base mais do que ajudam.
**Correção:** Publicar os ~6-8 artigos que passam na Rubrica. O lançamento é da Base, não de um número de artigos.

---

## 6. Relação com outras camadas

| Esta camada alimenta… | Como |
|---|---|
| **Camada 2 — Voz e Tom** | Princípios 4, 5 definem registros válidos de voz; Princípio 3 define proximidade adequada com o leitor |
| **Camada 3 — Vocabulário Controlado** | Princípio 5 (claro, não simples) define quando manter termo técnico vs adaptar |
| **Camada 4 — Padrões de Conteúdo** | Princípios 2, 3, 4 definem estrutura mínima de cada padrão narrativo |
| **Camada 4.5 — Padrões de Composição** | Princípios 1, 2, 6 são a base arquitetural |
| **Camada 5 — Rubrica de Qualidade** | Princípios 3, 4, 5, 9 viram dimensões de qualidade |
| **Camada 8 — Depreciação** | Princípio 7 é a justificativa direta |
| **Camada 9 — ContentOps** | Princípios 8, 9 definem capacidade e gargalo |

---

## 7. O que ainda falta nesta camada

- [ ] **Validação formal com Ruti Fávero** — os princípios derivam de decisões registradas, mas a Ruti ainda não os reviu como conjunto fechado
- [ ] **Princípio sobre acessibilidade?** — pode ser um décimo princípio explícito ("acessibilidade é design, não correção") ou ficar absorvido pelo Princípio 5. Avaliar com Ruti.
- [ ] **Casos de uso aplicados** — esta versão tem 4 casos. Conforme a operação rodar, novos casos vão alimentar a seção 5.

---

## 8. Histórico de versões

| Versão | Data | Mudança | Por |
|---|---|---|---|
| 1.0 | 2026-05-19 | Versão inicial — 9 princípios em 3 famílias, 4 casos aplicados | Elton + Claude |

---

*Camada 1 do Content System · Base de Conhecimento CEFOR/Ifes · Fase 1 — Fundações*
