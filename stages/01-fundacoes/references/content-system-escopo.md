# Content System — Escopo e Estrutura

> **Documento de referência**
> Define o que compõe o Content System da Base de Conhecimento CEFOR/Ifes, suas camadas, e como ele se relaciona com os 11 pilares e o Design System do projeto.

---

## O que é o Content System

O Content System não é um guia de estilo editorial. É um **sistema de decisões, padrões e instrumentos** que garante que todo conteúdo produzido — por qualquer pessoa, com ou sem IA, em qualquer momento — tenha a mesma qualidade, a mesma voz e a mesma utilidade.

Se o Design System responde **"como as coisas se parecem e se comportam"**, o Content System responde **"como as coisas são escritas, organizadas, avaliadas e mantidas"**.

Ele é composto por **10 camadas**, da mais filosófica à mais operacional.

---

## Relação com o Design System

O Content System e o Design System são **sistemas irmãos, não hierárquicos**. Nenhum existe bem sem o outro.

```
┌──────────────────────────────────────────────────────────────┐
│                     BASE DE CONHECIMENTO                      │
│                                                               │
│   ┌─────────────────┐           ┌─────────────────┐          │
│   │ SISTEMA DE       │◄────────►│  DESIGN SYSTEM   │          │
│   │ CONTEÚDO         │  informa  │                  │          │
│   │  Como se escreve │  ◄────►  │  Como se vê      │          │
│   │  Como se organiza│  ◄────►  │  Como se comporta│          │
│   │  Como se avalia  │          │  Como se navega   │          │
│   │  Como se mantém  │          │  Como se acessa   │          │
│   └─────────────────┘           └─────────────────┘          │
│                                                               │
│   ┌──────────────────────────────────────────────────┐       │
│   │              TAXONOMIA + DESCOBERTA               │       │
│   │        (Arquitetura de informação + SEO/GEO)      │       │
│   └──────────────────────────────────────────────────┘       │
└──────────────────────────────────────────────────────────────┘
```

### Pontos de contato direto

| Decisão no Content System | Consequência no Design System |
|---|---|
| "Artigos têm TL;DR obrigatório" | DS precisa do componente `TLDRBox` |
| "Existem 4 tipos de alerta" | DS precisa de 4 variantes de `AlertBox` |
| "Tutoriais têm checkpoints" | DS precisa de componente `Checkpoint` |
| "Tom muda conforme contexto do leitor" | DS pode usar variantes visuais para sinalizar tom |
| "Artigos mostram nível de dificuldade" | DS precisa de badge de `DifficultyLevel` |
| "Vocabulário controlado exige tooltip" | DS precisa de `Tooltip` com definição inline |

---

## As 10 Camadas do Content System

---

### Camada 1 — Guia Editorial Estratégico (Content Playbook)

Assim como o Design System começa com princípios de design, o Content System começa com **princípios editoriais** — as decisões filosóficas que orientam toda escrita.

**O que define:**
- A identidade editorial da base — quem ela é como "voz"
- Os valores inegociáveis da produção de conteúdo
- O que a base **é** e o que ela **não é** (escopo negativo)

**Princípios candidatos (a validar com a equipe):**

| Princípio | Implicação prática |
|---|---|
| "Ensinamos fazendo, não explicando" | Todo artigo conceitual inclui aplicação prática |
| "Se o leitor precisa perguntar para alguém depois de ler, o artigo falhou" | Autonomia como critério de qualidade |
| "Acessível não é simples — é claro" | Não simplificar a ponto de perder precisão |
| "Conteúdo tem prazo de validade" | Todo artigo nasce com data de revisão programada |
| "IA acelera, humano valida" | Nenhum conteúdo gerado por IA é publicado sem revisão humana |
| "Menos artigos excelentes > muitos artigos medianos" | Qualidade sobre volume |

**Escopo negativo — o que a base NÃO é:**

| A base NÃO é... | Consequência |
|---|---|
| Um repositório de PDFs | Não hospedar documentos que deveriam estar no Moodle |
| Um blog de notícias | Não publicar conteúdo datado sem valor permanente |
| Um manual técnico do Moodle | Focar no "como fazer no contexto do Ifes", não replicar a documentação oficial |
| Um espaço de opinião pessoal | Tom institucional, mesmo quando assinado por autor |
| Uma enciclopédia completa | Cobrir o que o público precisa, não tudo que existe |

**Quem define:** Elton + Ruti (validação pedagógica)

**Relação com pilares:** Transversal — alimenta todos os pilares de conteúdo.

---

### Camada 2 — Matriz de Voz e Tom (Voice & Tone Matrix)

A voz da base é **uma só** (identidade constante). O tom **varia** conforme o contexto do leitor e o tipo de conteúdo.

**O que define:**
- A voz institucional da base (personalidade consistente)
- As variações de tom por situação do leitor
- As variações de tom por tipo de artigo

#### 2.1 Voz (constante)

**A voz da base é:** (a definir com a equipe — candidatos abaixo)

| Atributo | É | Não é |
|---|---|---|
| Tom geral | Colega experiente que explica com paciência | Professor na frente da sala |
| Registro | Semiformal — profissional mas acessível | Informal (gírias) nem burocrático (juridiquês) |
| Postura | Orientadora — conduz, não impõe | Impositiva ("você deve") nem passiva ("talvez considere") |
| Relação com o leitor | Respeita a inteligência, não assume ignorância | Condescendente ("é muito fácil, basta...") |

#### 2.2 Tom por contexto do leitor

| O leitor está... | Tom adequado | Exemplo de abertura |
|---|---|---|
| Perdido, não sabe por onde começar | Acolhedor, orientador | "Vamos por partes. Primeiro, entenda o que é [conceito]..." |
| Com pressa, precisa da resposta rápida | Direto, sem rodeios | "Para [ação]: Acesse [caminho] > Clique em [botão]." |
| Enfrentando um erro ou problema | Empático, sem julgamento | "Esse erro acontece quando [causa]. Para resolver..." |
| Explorando possibilidades | Inspirador, mostra caminhos | "O Moodle permite [possibilidade]. Veja como..." |
| Estudando para aprender o conceito | Didático, com analogias | "Pense em [analogia]. Na prática do Moodle, isso funciona assim..." |
| Voltando para consultar algo que já fez | Objetivo, formato de referência | Tabela ou lista numerada, sem introdução longa |

#### 2.3 Tom por tipo de artigo

| Tipo de artigo | Tom predominante | Proporção instrução/contexto |
|---|---|---|
| Tutorial passo a passo | Guia prático — "faça isso" | 70% instrução, 30% contexto |
| Guia conceitual | Professor — "entenda por quê" | 40% instrução, 60% contexto |
| Referência rápida | Consulta — "aqui está" | 90% instrução, 10% contexto |
| Troubleshooting | Técnico empático — "resolva isso" | 80% instrução, 20% contexto |
| Template/modelo | Facilitador — "use isso como base" | 50% template, 30% instrução, 20% contexto |
| Boas práticas | Mentor — "aprenda com quem fez" | 30% instrução, 50% exemplo, 20% contexto |

**Quem define:** Ruti (orientação pedagógica) + Juliana (execução)

**Relação com pilares:** Pilar 3 (Modelo de Conteúdo) e Pilar 10 (Sistema de Autoria).

---

### Camada 3 — Vocabulário Controlado (Controlled Vocabulary)

Vai além de um glossário. É o **padrão terminológico autoritativo** da base — define como chamar cada coisa, resolve ambiguidades e mapeia o vocabulário do público com o vocabulário do sistema.

**O que define:**
- Termo preferido vs termos rejeitados (sinônimos que NÃO usamos)
- Mapeamento: termo CEFOR → termo Moodle → termo MEC → termo popular
- Relações hierárquicas entre termos
- Regras de uso em contexto

#### 3.1 Por que isso é crítico para o CEFOR

O público da base opera em pelo menos 4 registros terminológicos simultâneos:

| Registro | Exemplo para o mesmo conceito |
|---|---|
| Popular | "Prova online" |
| Moodle técnico | "Questionário" (Quiz) |
| Pedagógico/MEC | "Avaliação somativa" |
| CEFOR interno | "Atividade avaliativa" |

Sem vocabulário controlado, um artigo chama de "prova", outro de "questionário", outro de "avaliação" — e o leitor não sabe se é a mesma coisa.

#### 3.2 Estrutura do vocabulário controlado

Para cada entrada:

```
TERMO PREFERIDO: Questionário
  SINÔNIMOS ACEITOS: quiz (em contexto técnico Moodle)
  SINÔNIMOS REJEITADOS: prova, teste, avaliação (genéricos demais)
  TERMO MOODLE: Quiz / Questionário
  TERMO MEC: Avaliação (quando aplicável)
  DEFINIÇÃO: Atividade do Moodle que apresenta perguntas ao aluno 
             com correção automática.
  CONTEXTO DE USO: Usar "Questionário" sempre que se referir à 
                   atividade específica do Moodle. Usar "avaliação" 
                   apenas quando se referir ao conceito pedagógico 
                   mais amplo.
  VER TAMBÉM: Tarefa, Fórum de discussão avaliativo
```

#### 3.3 Categorias do vocabulário

| Categoria | Exemplos de termos a padronizar |
|---|---|
| **Atividades Moodle** | Questionário, Tarefa, Fórum, Wiki, Glossário, H5P |
| **Recursos Moodle** | Arquivo, Página, URL, Livro, Rótulo |
| **Papéis** | Mediador, Professor, Tutor, Coordenador, Estudante |
| **Conceitos pedagógicos** | Sala virtual, Ambiente virtual, AVA, Percurso formativo |
| **Conceitos técnicos** | Backup, Restauração, Inscrição, Matrícula, Bloco |
| **Conceitos CEFOR** | Base de Conhecimento, Percurso, Trilha, Artigo |

#### 3.4 Regra de ouro

> Quando o vocabulário do Moodle e o vocabulário pedagógico divergem, **usar o termo do Moodle na primeira menção** (é o que aparece na interface) **seguido do termo pedagógico entre parênteses**: "Configure o Questionário (a ferramenta de avaliação com correção automática do Moodle)".

**Quem define:** Ruti (termos pedagógicos) + Elton (termos técnicos) + Juliana (termos do dia a dia)

**Relação com pilares:** Pilar 3 (Modelo de Conteúdo) e Pilar 4 (Taxonomia).

**Formato de entrega:** Planilha ou JSON estruturado — deve ser consultável por humanos e por IA durante a produção de conteúdo.

---

### Camada 4 — Biblioteca de Padrões de Conteúdo (Content Patterns Library)

Equivalente à pattern library do Design System, mas para **estruturas narrativas**. São blocos reutilizáveis de organização textual que os autores (humanos e IA) aplicam conforme o tipo de informação.

**O que define:**
- Padrões recorrentes de estrutura textual
- Quando usar cada padrão
- Estrutura e exemplo de cada um
- Armadilhas comuns

#### 4.1 Catálogo de padrões

---

**Padrão: Passo a Passo com Checkpoint**

| Atributo | Valor |
|---|---|
| **Quando usar** | Tutoriais com mais de 5 passos |
| **Estrutura** | Passos numerados. A cada 3-4 passos, um bloco de checkpoint: "Neste ponto, você deve ver [X] na tela." |
| **Por que funciona** | O leitor valida que está no caminho certo antes de continuar. Reduz frustração de "fiz tudo e não deu certo no final". |
| **Armadilha** | Checkpoint vago ("deve estar funcionando"). O checkpoint precisa ser **verificável visualmente**. |

---

**Padrão: Problema → Diagnóstico → Solução**

| Atributo | Valor |
|---|---|
| **Quando usar** | Artigos de troubleshooting |
| **Estrutura** | 1. Sintoma (o que o leitor vê/sente) → 2. Causa provável (por que isso acontece) → 3. Solução (passos para resolver) → 4. Prevenção (como evitar no futuro) |
| **Por que funciona** | O leitor chega com um sintoma, não com um diagnóstico. Começar pelo sintoma gera identificação imediata. |
| **Armadilha** | Pular o diagnóstico e ir direto à solução. Sem entender a causa, o leitor não sabe se a solução aplica ao seu caso. |

---

**Padrão: Quando Usar / Quando NÃO Usar**

| Atributo | Valor |
|---|---|
| **Quando usar** | Artigos sobre ferramentas ou recursos que têm alternativas (ex: "Fórum vs Fórum de perguntas e respostas") |
| **Estrutura** | Tabela comparativa: cenário → ferramenta recomendada → por quê. Seguida de "Use X quando..." e "NÃO use X quando...". |
| **Por que funciona** | O professor não quer saber tudo sobre a ferramenta — quer saber se é a certa para o que precisa. |
| **Armadilha** | Listar apenas vantagens. O "quando NÃO usar" é o que diferencia o artigo de um manual e o torna um conselheiro. |

---

**Padrão: Analogia do Mundo Real**

| Atributo | Valor |
|---|---|
| **Quando usar** | Conceitos abstratos ou técnicos que o público não domina |
| **Estrutura** | 1. Analogia com algo familiar → 2. Mapeamento explícito (o X da analogia = o Y do sistema) → 3. Onde a analogia **para de funcionar** (limites) |
| **Por que funciona** | Reduz carga cognitiva. Professores de EaD são pedagogos — entendem via exemplos concretos, não abstrações. |
| **Armadilha** | Analogia imprecisa que cria concepção errada. Sempre declarar os limites. |

---

**Padrão: Antes/Depois**

| Atributo | Valor |
|---|---|
| **Quando usar** | Configurações que mudam o visual ou comportamento de algo |
| **Estrutura** | Screenshot ou descrição do "antes" → o que mudar → screenshot ou descrição do "depois" |
| **Por que funciona** | O leitor vê o impacto antes de fazer. Gera confiança e motivação. |
| **Armadilha** | Screenshots sem contexto. Sempre indicar onde na tela olhar (seta, destaque, legenda). |

---

**Padrão: FAQ Invertido**

| Atributo | Valor |
|---|---|
| **Quando usar** | Seções de perguntas frequentes dentro de artigos |
| **Estrutura** | Ordenar pela pergunta mais **comum**, não pela mais básica. A primeira pergunta deve ser a que 60% dos leitores têm. |
| **Por que funciona** | FAQ ordenada do básico ao avançado força o leitor a passar por respostas que ele já sabe. Invertida, ele encontra a resposta rápido. |
| **Armadilha** | Ordenar por lógica do autor ("primeiro o conceito, depois a prática"). A lógica do leitor é a urgência, não a didática. |

---

**Padrão: Resumo Executivo + Profundidade Progressiva**

| Atributo | Valor |
|---|---|
| **Quando usar** | Artigos conceituais ou guias longos (>5 min de leitura) |
| **Estrutura** | TL;DR no topo (3-4 linhas) → Visão geral (1 parágrafo) → Detalhamento por seção → Referências |
| **Por que funciona** | Atende dois públicos no mesmo artigo: quem quer a resposta rápida e quem quer entender a fundo. |
| **Armadilha** | TL;DR que é uma introdução, não um resumo. O TL;DR deve conter a **conclusão**, não a promessa do artigo. |

---

#### 4.2 Como usar os padrões

1. **Identifique o tipo de artigo** (Camada 6 — Modelo de Conteúdo no roadmap)
2. **Consulte os padrões recomendados** para aquele tipo
3. **Combine padrões** quando necessário — um tutorial pode usar "Passo a Passo com Checkpoint" + "Antes/Depois" + "FAQ Invertido" no final
4. **Documente os padrões usados** nos metadados do artigo (facilita auditoria e IA)

**Quem mantém:** Elton (estrutura) + Ruti (validação pedagógica)

**Formato de entrega:** Documento vivo. Novos padrões são adicionados conforme a produção identifica necessidades recorrentes.

---

### Camada 5 — Rubrica de Qualidade (Content Quality Scorecard)

O instrumento que transforma "esse artigo é bom" em **avaliação objetiva e mensurável**. Usado na revisão de artigos novos, na triagem da base antiga e como meta de qualidade para produção com IA.

**O que define:**
- Dimensões de qualidade e seus pesos
- Escala de avaliação por dimensão
- Score mínimo para publicação
- Processo de avaliação

#### 5.1 As 7 dimensões de qualidade

| # | Dimensão | Peso | O que avalia |
|---|---|---|---|
| 1 | **Acionabilidade** | 20% | O leitor consegue fazer o que o artigo propõe? |
| 2 | **Escaneabilidade** | 15% | Dá para achar a informação sem ler tudo? |
| 3 | **Precisão técnica** | 20% | A informação está correta e verificável? |
| 4 | **Completude** | 15% | Cobre o caminho feliz E os erros comuns? |
| 5 | **Clareza textual** | 15% | A linguagem é acessível ao público? |
| 6 | **Conformidade estrutural** | 10% | Segue o modelo de conteúdo do tipo de artigo? |
| 7 | **Frescor** | 5% | Está atualizado com a versão atual do sistema? |

#### 5.2 Escala de avaliação

| Score | Significado | Critério |
|---|---|---|
| 1 | Inadequado | Não atende o mínimo. Precisa reescrita completa. |
| 2 | Insuficiente | Tem problemas sérios. Precisa revisão substancial. |
| 3 | Aceitável | Funcional, mas com lacunas. Revisão pontual necessária. |
| 4 | Bom | Atende bem. Melhorias são de polimento, não de substância. |
| 5 | Excelente | Referência de qualidade. Pode ser usado como modelo. |

#### 5.3 Detalhamento por dimensão

**1. Acionabilidade** (peso 20%)

| Score | Descrição |
|---|---|
| 1 | Só teoria, sem aplicação prática |
| 2 | Tem passos, mas vagos ou incompletos ("configure conforme necessário") |
| 3 | Passos claros para o caminho feliz, mas sem tratar erros |
| 4 | Passos claros + tratamento dos erros mais comuns |
| 5 | Leitor sai sabendo fazer, verificar e corrigir se algo der errado |

**2. Escaneabilidade** (peso 15%)

| Score | Descrição |
|---|---|
| 1 | Parede de texto, sem headings nem destaques |
| 2 | Tem headings, mas genéricos ("Introdução", "Desenvolvimento") |
| 3 | Headings descritivos + algum destaque visual |
| 4 | Headings descritivos + TL;DR + destaques + índice de seções |
| 5 | Qualquer informação encontrável em <10 segundos via escaneamento |

**3. Precisão técnica** (peso 20%)

| Score | Descrição |
|---|---|
| 1 | Informação incorreta ou não verificável |
| 2 | Genericamente correto, mas com imprecisões ("clique no botão" — qual botão?) |
| 3 | Correto e específico para o caminho principal |
| 4 | Correto, específico e com caminhos alternativos quando existem |
| 5 | Correto, específico, verificável e com versionamento (funciona no Moodle X.Y) |

**4. Completude** (peso 15%)

| Score | Descrição |
|---|---|
| 1 | Faltam passos críticos — leitor não consegue completar a tarefa |
| 2 | Cobre o básico, mas omite pré-requisitos ou consequências |
| 3 | Cobre o caminho feliz completo |
| 4 | Caminho feliz + 2-3 cenários de erro mais comuns |
| 5 | Caminho feliz + erros + edge cases + "e se eu quiser fazer diferente?" |

**5. Clareza textual** (peso 15%)

| Score | Descrição |
|---|---|
| 1 | Jargão excessivo sem explicação, frases longas e confusas |
| 2 | Linguagem técnica sem contextualizar para o público |
| 3 | Linguagem acessível no geral, com termos técnicos explicados no glossário |
| 4 | Linguagem clara, termos explicados inline, frases curtas e diretas |
| 5 | Qualquer profissional de EaD entende na primeira leitura, independente de background técnico |

**6. Conformidade estrutural** (peso 10%)

| Score | Descrição |
|---|---|
| 1 | Não segue o modelo de conteúdo do tipo de artigo |
| 2 | Segue parcialmente — tem os blocos obrigatórios, mas fora de ordem ou incompletos |
| 3 | Segue o modelo, mas sem os blocos opcionais que agregariam valor |
| 4 | Segue o modelo completo (obrigatórios + opcionais relevantes) |
| 5 | Modelo perfeito + usa os padrões de conteúdo adequados (Camada 4) |

**7. Frescor** (peso 5%)

| Score | Descrição |
|---|---|
| 1 | Desatualizado — refere-se a versão descontinuada ou interface que mudou |
| 2 | Funcional, mas com screenshots ou caminhos de versão anterior |
| 3 | Atualizado para a versão corrente, sem indicação de versão |
| 4 | Atualizado + indica versão ("Moodle 4.x") |
| 5 | Atualizado + versionado + data de última revisão visível |

#### 5.4 Regras de publicação

| Score médio ponderado | Decisão |
|---|---|
| **< 2.5** | Não publica. Reescrita necessária. |
| **2.5 – 3.4** | Publica com ressalvas: marcado como "em melhoria" + prazo de revisão de 30 dias. |
| **3.5 – 4.4** | Publica normalmente. |
| **≥ 4.5** | Publica como artigo de referência (pode ser usado como modelo para IA e novos autores). |

#### 5.5 Uso na triagem da base antiga

Para os ~60 artigos existentes, o scorecard define a decisão:

| Score | Ação |
|---|---|
| < 2.0 | Descartar ou reescrever do zero |
| 2.0 – 3.0 | Reescrever substancialmente |
| 3.0 – 3.5 | Atualizar e reformatar |
| > 3.5 | Migrar com ajustes menores |

**Quem avalia:** Ruti (dimensões 1, 4, 5) + Juliana (dimensões 2, 3, 6) + Elton (dimensão 7 + score final)

**Relação com pilares:** Pilar 7 (Ciclo de Vida) e Pilar 10 (Sistema de Autoria).

---

### Camada 6 — Padrões de Legibilidade (Readability Standards)

Métricas objetivas e testáveis para o texto — o equivalente ao contraste WCAG para o conteúdo.

**O que define:**
- Limites mensuráveis para legibilidade do texto
- Critérios por tipo de artigo
- Ferramentas de verificação

#### 6.1 Métricas e limites

| Métrica | Limite Tutorial | Limite Conceitual | Limite Referência | Como medir |
|---|---|---|---|---|
| **Palavras por frase** (média) | ≤ 20 | ≤ 25 | ≤ 15 | Contador automático |
| **Frases por parágrafo** (máx) | 4 | 5 | 3 | Visual / linter |
| **Índice Flesch adaptado PT-BR** | ≥ 50 (fácil) | ≥ 40 (padrão) | ≥ 60 (muito fácil) | Ferramenta Flesch |
| **Jargão não explicado por seção** (máx) | 2 termos | 3 termos | 1 termo | Cruzamento com Vocabulário Controlado |
| **Voz passiva** (máx por artigo) | 15% das frases | 20% das frases | 10% das frases | Linter de texto |
| **Parágrafos sem heading** (máx consecutivos) | 3 | 4 | 2 | Estrutural |

#### 6.2 Regras de ouro de legibilidade

1. **Uma ideia por parágrafo.** Se o parágrafo trata de dois assuntos, quebrar em dois.
2. **Primeira frase carrega o peso.** O leitor que só lê a primeira frase de cada parágrafo deve entender o fluxo do artigo.
3. **Instruções em voz ativa e imperativa.** "Clique em Salvar" — não "O botão Salvar deve ser clicado".
4. **Números concretos, não adjetivos vagos.** "Leva cerca de 3 minutos" — não "é bem rápido".
5. **Termos técnicos na primeira ocorrência.** Sempre explicar na primeira vez que aparecer no artigo, mesmo que esteja no glossário.

#### 6.3 Verificação

| Tipo | Ferramenta | Quando |
|---|---|---|
| Automática | Linter de texto (a configurar) | Pré-publicação |
| Automática | Checklist nos prompts de IA | Durante geração |
| Manual | Teste de leitura em voz alta | Revisão final |

**Teste de leitura em voz alta:** Se o revisor tropeça ao ler em voz alta, a frase está longa ou confusa demais. É o teste mais simples e mais eficaz.

**Quem define:** Ruti (padrões pedagógicos) + Elton (automação)

**Relação com pilares:** Pilar 3 (Modelo de Conteúdo) e Pilar 6 (Sistema de Leitura).

---

### Camada 7 — Mapa de Modelos Mentais do Público (Audience Mental Model Map)

Não é persona. É um mapa de **como o público pensa, o que acredita saber, e onde tropeça** — insumo direto para decisões de tom, estrutura e vocabulário.

**O que define:**
- Modelos mentais corretos e incorretos do público
- Vocabulário natural (como eles falam, não como o sistema fala)
- Momentos de busca (quando procuram a base e por quê)
- Atalhos mentais (comparações que fazem espontaneamente)

#### 7.1 Perfis mentais do público CEFOR

| Perfil | O que acredita | Realidade | Consequência para o conteúdo |
|---|---|---|---|
| **Professor que migrou do presencial** | "O Moodle é tipo um Google Classroom mais complicado" | Moodle é mais poderoso, mas com paradigma diferente | Usar analogias com ferramentas que já conhece. Nunca dizer "é simples". |
| **Mediador experiente** | "Eu já sei mexer no Moodle" | Sabe o básico bem, mas não explora recursos avançados | Artigos devem ter camadas — o básico para validar e o avançado para expandir. |
| **Coordenador de curso** | "Eu não preciso saber técnico" | Precisa entender para tomar decisões pedagógicas informadas | Artigos de decisão (Quando Usar / Quando NÃO Usar) são mais úteis que tutoriais. |
| **Professor novo no EaD** | "Isso é muito difícil para mim" | A barreira é medo, não capacidade | Tom acolhedor é obrigatório. Checkpoints frequentes. Celebrar pequenas vitórias. |
| **Técnico de TI do campus** | "Eu sei mais que a documentação" | Pode saber o sistema, mas não o contexto pedagógico | Artigos devem separar claramente o técnico do pedagógico. |

#### 7.2 Momentos de busca

| Momento | O que sente | O que busca | Formato ideal |
|---|---|---|---|
| **"Tenho que fazer isso agora"** | Urgência, pressão | Passo a passo direto | Tutorial com TL;DR no topo |
| **"Deu erro e não sei por quê"** | Frustração, ansiedade | Diagnóstico + solução | Troubleshooting (Problema → Solução) |
| **"Meu chefe mandou usar isso"** | Obrigação, resistência | Justificativa + mínimo viável | "Por que isso importa" + quickstart |
| **"Quero melhorar meu curso"** | Motivação, curiosidade | Inspiração + exemplos | Boas práticas + Antes/Depois |
| **"Preciso ensinar isso para minha equipe"** | Responsabilidade | Material compartilhável | Artigo autocontido + citação ABNT |
| **"Já fiz isso antes, esqueci como"** | Impaciência | Referência rápida | Formato consulta, sem introdução |

#### 7.3 Vocabulário natural do público

| O professor diz... | O sistema chama... | O artigo deve usar... |
|---|---|---|
| "Minha sala" | Curso / Ambiente virtual | "Sua sala virtual (o curso no Moodle)" |
| "Postar atividade" | Adicionar atividade ao curso | "Adicionar uma atividade" |
| "Nota" | Avaliação / Item de nota | "Nota" (e contextualizar quando necessário) |
| "Abrir o Moodle" | Acessar o AVA | "Acessar o Moodle" |
| "Aquele chat" | Mensagens / Chat | "Chat do Moodle (Mensagens)" |

**Quem define:** Ruti + Juliana (convivem com o público diariamente)

**Relação com pilares:** Pilar 3 (Modelo de Conteúdo) e Pilar 10 (Sistema de Autoria).

**Como manter atualizado:** Registrar termos novos do público sempre que surgirem em atendimentos, e-mails, reuniões. Juliana e Ruti são as "antenas" do vocabulário real.

---

### Camada 8 — Política de Depreciação e Desativação (Content Deprecation & Sunset Policy)

Define regras **objetivas e formais** para quando e como conteúdo envelhece, é marcado como desatualizado e eventualmente removido.

**O que define:**
- Critérios objetivos de obsolescência
- Fluxo de depreciação
- Responsabilidades
- Tratamento de conteúdo removido

#### 8.1 Gatilhos de obsolescência

| Gatilho | Tipo | Ação automática |
|---|---|---|
| Artigo completou 6 meses sem revisão | Temporal | Marcar como "Revisão pendente" |
| Artigo completou 12 meses sem revisão | Temporal | Marcar como "Possivelmente desatualizado" |
| Nova versão do Moodle foi lançada | Evento | Marcar artigos de tutorial como "Verificar compatibilidade" |
| Artigo teve 0 acessos nos últimos 90 dias | Uso | Avaliar relevância (pode ser nicho legítimo ou conteúdo morto) |
| Leitor reportou erro ou desatualização | Feedback | Priorizar na fila de revisão |

#### 8.2 Fluxo de depreciação

```
Publicado
    │
    ├── [gatilho temporal] ──→ "Revisão pendente" (badge discreto, visível só para editores)
    │                              │
    │                              ├── Revisado → volta para "Publicado" (reset do timer)
    │                              │
    │                              └── Não revisado em 30 dias → "Possivelmente desatualizado"
    │
    ├── "Possivelmente desatualizado" (badge visível para o leitor)
    │       │
    │       ├── Revisado e atualizado → volta para "Publicado"
    │       ├── Revisado e ainda relevante → volta para "Publicado" (sem alteração)
    │       └── Declarado obsoleto → "Depreciado"
    │
    └── "Depreciado"
            │
            ├── Tem artigo substituto → Redirect 301 + banner: "Este artigo foi substituído por [link]"
            ├── Não tem substituto → Banner: "Este conteúdo está desatualizado e será removido em [data]"
            └── Após 90 dias depreciado → "Arquivado" (removido da navegação, acessível por URL direta)
```

#### 8.3 O que NUNCA fazer

| Ação proibida | Por quê |
|---|---|
| Deletar artigo sem redirect | Quebra links externos, prejudica SEO, frustra leitores |
| Remover conteúdo silenciosamente | Em instituição pública, transparência é obrigação |
| Marcar como desatualizado sem propor ação | "Desatualizado" sem prazo de atualização é abandono, não gestão |
| Depender de "alguém perceber" que está velho | O sistema de gatilhos temporais existe para isso |

**Quem executa:** Juliana (triagem) + Ruti (decisão pedagógica de relevância)

**Relação com pilares:** Pilar 7 (Ciclo de Vida) e Pilar 8 (Sistema de Estados).

---

### Camada 9 — Operação de Conteúdo (ContentOps Charter)

Define a **capacidade operacional real** da equipe e os processos que sustentam a produção contínua de conteúdo — não apenas o lançamento, mas o funcionamento permanente.

**O que define:**
- Capacidade de produção sustentável
- Cadência de revisão
- Métricas de saúde da base
- Processo de solicitação de conteúdo novo
- SLAs

#### 9.1 Capacidade de produção

| Recurso | Capacidade estimada (a validar) | Premissas |
|---|---|---|
| Juliana (produção + IA) | 4-6 artigos/mês (novos ou reescritos) | Considerando outras responsabilidades no CEFOR |
| Ruti (revisão pedagógica) | 6-8 revisões/mês | Disponibilidade parcial (Portugal, outros projetos) |
| IA (geração de rascunho) | Ilimitada em volume, limitada por revisão humana | Gargalo é a revisão, não a geração |
| Elton (revisão técnica + publicação) | 8-10 publicações/mês | Considerando trabalho técnico paralelo |

**Gargalo real:** A capacidade da base é definida pelo elo mais lento da cadeia de revisão, não pela velocidade de produção. Com a equipe atual, estimar **4-6 artigos publicados por mês** como ritmo sustentável.

#### 9.2 Cadência de revisão obrigatória

| Tipo de artigo | Prazo máximo sem revisão | Justificativa |
|---|---|---|
| Tutorial passo a passo | 6 meses | Interfaces mudam com atualizações do Moodle |
| Guia conceitual | 12 meses | Conceitos pedagógicos são mais estáveis |
| Referência rápida | 6 meses | Dados técnicos precisam estar corretos |
| Troubleshooting | 3 meses | Problemas mudam conforme o sistema atualiza |
| Template/modelo | 12 meses | Estrutura muda menos que conteúdo técnico |
| Boas práticas | 12 meses | Práticas evoluem devagar |

#### 9.3 Métricas de saúde da base

| Métrica | Meta V1 | Como medir |
|---|---|---|
| % de artigos com score ≥ 3.5 | 80% | Scorecard (Camada 5) |
| % de artigos revisados no prazo | 90% | Data de última revisão vs cadência |
| Buscas internas sem resultado | < 10% | Analytics de busca |
| Tempo médio para publicar artigo novo | < 5 dias úteis (do rascunho à publicação) | Workflow de publicação |
| Artigos com "possivelmente desatualizado" | < 15% da base | Sistema de estados |
| Cobertura por categoria | Sem categoria com < 3 artigos | Contagem por taxonomia |

#### 9.4 Processo de solicitação de conteúdo novo

```
Solicitação chega (e-mail, reunião, demanda espontânea)
    │
    ├── É urgente? (mudança no Moodle, erro crítico)
    │       → SLA: 48h para publicar correção/atualização
    │
    └── É planejado?
            → Entra na fila de produção mensal
            → Priorização: impacto no público × esforço de produção
            → Responsável: Juliana (produção) + Ruti (validação)
```

#### 9.5 Fluxo de produção com IA

```
1. Juliana seleciona tema + tipo de artigo
    │
2. Gera rascunho via prompt template (Camada 4 + Vocabulário Controlado)
    │
3. Juliana revisa: estrutura, precisão, tom, completude
    │
4. Ruti revisa: adequação pedagógica, clareza, público
    │
5. Elton revisa: precisão técnica, conformidade, metadados
    │
6. Scorecard aplicado (Camada 5) — score ≥ 3.5?
    │           │
    │     Não → volta para etapa 3 com feedback
    │
7. Publicação + metadados preenchidos
    │
8. Marcação: "Produzido com assistência de IA" (compliance legal)
```

**Quem define:** Elton (processos) + Marcos (capacidade e priorização)

**Relação com pilares:** Pilar 7 (Ciclo de Vida) e Pilar 10 (Sistema de Autoria).

---

### Camada 10 — Métricas de Sucesso do Conteúdo (Content Measurement Framework)

Define como medir se o conteúdo está cumprindo o **propósito-farol da base**: o leitor consegue resolver o problema dele com autonomia.

**O que define:**
- Métricas por nível de maturidade
- Fontes de dados
- Frequência de análise
- Ações baseadas nos dados

#### 10.1 Métricas por nível

| Nível | Métrica | Pergunta que responde | Fonte | Meta V1 |
|---|---|---|---|---|
| **Utilidade** | Taxa de resolução (leitor chegou ao fim do tutorial) | O artigo resolve o problema? | Scroll depth + tempo na página | > 60% leem até o final |
| **Clareza** | Bounce rate por tipo de artigo | O artigo confunde ou responde? | Analytics | < 40% bounce em tutoriais |
| **Confiança** | Taxa de retorno à base (mesmo usuário volta) | O leitor confia na base? | Analytics (cookies/login) | > 30% retorno em 30 dias |
| **Cobertura** | Buscas sem resultado / termos mais buscados | O que falta na base? | Log de busca interna | Lista mensal de gaps |
| **Frescor** | % de artigos revisados no prazo | A base está envelhecendo? | Sistema de estados | > 90% no prazo |
| **Satisfação** | "Este artigo foi útil?" (sim/não) | Feedback direto do leitor | Widget no rodapé do artigo | > 80% "sim" |
| **Eficiência** | Horas por artigo publicado | A operação é sustentável? | Registro manual ou timer | < 8h/artigo (com IA) |

#### 10.2 Dashboard de saúde (revisão mensal)

```
SAÚDE DA BASE — Mês/Ano
├── Artigos publicados este mês: X
├── Artigos revisados este mês: Y
├── Score médio da base: Z.Z
├── Artigos "possivelmente desatualizado": N (X%)
├── Top 5 buscas sem resultado: [lista]
├── Top 10 artigos mais acessados: [lista]
├── Taxa média de "artigo útil": XX%
└── Próximas revisões obrigatórias: [lista com datas]
```

**Quem analisa:** Elton (mensal, com apoio de analytics)

**Relação com pilares:** Pilar 11 (Sistema de Descoberta) e Pilar 7 (Ciclo de Vida).

---

## Mapa de Camadas por Fase do Roadmap

| Camada | Fase 0 | Fase 1 | Fase 2 | Fase 3 | Fase 4 | Fase 5 |
|---|---|---|---|---|---|---|
| 1. Guia Editorial Estratégico | — | **Define** | — | — | **Usa** | Itera |
| 2. Matriz de Voz e Tom | — | **Define** | — | — | **Usa** | Itera |
| 3. Vocabulário Controlado | Pesquisa | **Define** | — | — | **Usa** | Itera |
| 4. Biblioteca de Padrões de Conteúdo | Pesquisa | **Define** | Informa DS | — | **Usa** | Itera |
| 5. Rubrica de Qualidade | — | **Define** | — | — | **Usa** | Itera |
| 6. Padrões de Legibilidade | — | **Define** | — | Automação | **Usa** | Itera |
| 7. Mapa de Modelos Mentais | Pesquisa | **Define** | Informa DS | — | **Usa** | Itera |
| 8. Política de Depreciação | — | **Define** | — | Implementa | — | **Opera** |
| 9. Operação de Conteúdo | — | **Define** | — | — | **Opera** | Itera |
| 10. Métricas de Sucesso | — | — | — | Implementa | — | **Opera** |

**Observação:** Todas as camadas de 1 a 9 são definidas na **Fase 1 (Fundações)** — confirmando que essa é a fase mais crítica do projeto. A Camada 10 só faz sentido quando há conteúdo publicado para medir.

---

## Relação com os 11 Pilares do Projeto

### Pilares que o Content System alimenta diretamente

| # | Pilar | Camadas do CS que alimentam |
|---|---|---|
| 3 | **Modelo de Conteúdo** | Camadas 1, 2, 3, 4, 6 |
| 7 | **Ciclo de Vida** | Camadas 5, 8, 9 |
| 10 | **Sistema de Autoria** | Camadas 1, 2, 4, 5, 6, 9 |

### Pilares que o Content System informa parcialmente

| # | Pilar | O que informa |
|---|---|---|
| 4 | **Taxonomia** | Vocabulário Controlado (Camada 3) alimenta a nomenclatura de categorias e tags |
| 6 | **Sistema de Leitura** | Padrões de Legibilidade (Camada 6) define requisitos de legibilidade que o DS implementa |
| 8 | **Sistema de Estados** | Política de Depreciação (Camada 8) define os estados de conteúdo |
| 11 | **Sistema de Descoberta** | Métricas de Sucesso (Camada 10) define métricas de busca e cobertura |

### Pilares fora do Content System

| # | Pilar | Por que fica fora |
|---|---|---|
| 1 | Sistema Visual | Responsabilidade do Design System |
| 2 | Sistema de Interação | Responsabilidade do Design System |
| 5 | Acessibilidade | Responsabilidade do Design System (com inputs de legibilidade do Content System) |
| 9 | Sistema Responsivo | Responsabilidade do Design System |

---

## Interdependências dentro do Content System

| Decisão em... | Afeta... |
|---|---|
| Um **princípio editorial** (Camada 1) | O **tom** (Camada 2), os **padrões** (Camada 4) e o **scorecard** (Camada 5) |
| O **vocabulário controlado** (Camada 3) | A **legibilidade** (Camada 6) e os **modelos mentais** (Camada 7) |
| Os **padrões de conteúdo** (Camada 4) | O **scorecard** (Camada 5) — conformidade é dimensão de qualidade |
| O **scorecard** (Camada 5) | A **política de depreciação** (Camada 8) — score < 2.0 = descartar |
| Os **modelos mentais** (Camada 7) | O **tom** (Camada 2) e os **padrões** (Camada 4) |
| A **capacidade operacional** (Camada 9) | As **métricas de sucesso** (Camada 10) — não medir o que não se pode agir |

**Consequência prática:** As Camadas 1 a 7 devem ser definidas em conjunto, por um mesmo grupo, num mesmo ciclo — assim como os 6 pilares do Design System. Definir tom sem vocabulário, ou padrões sem entender o público, gera retrabalho.

---

## Paralelo Content System ↔ Design System

| Design System | Content System |
|---|---|
| Princípios de Design | Guia Editorial Estratégico (Camada 1) |
| Design Tokens | Vocabulário Controlado (Camada 3) |
| Component Library | Biblioteca de Padrões de Conteúdo (Camada 4) |
| Padrões de Uso | Matriz de Voz e Tom (Camada 2) |
| WCAG/e-MAG Checklist | Padrões de Legibilidade (Camada 6) |
| Visual QA | Rubrica de Qualidade (Camada 5) |
| DesignOps | Operação de Conteúdo (Camada 9) |
| Analytics de uso de componentes | Métricas de Sucesso do Conteúdo (Camada 10) |

---

## Ordem sugerida de especificação

```
1. Guia Editorial Estratégico (Camada 1) ← define a direção de tudo
   +
   Mapa de Modelos Mentais do Público (Camada 7) ← define para quem
       ↓
2. Matriz de Voz e Tom (Camada 2) + Vocabulário Controlado (Camada 3)
       ↓
3. Biblioteca de Padrões de Conteúdo (Camada 4) + Padrões de Legibilidade (Camada 6)
       ↓
4. Rubrica de Qualidade (Camada 5) ← depende de padrões e legibilidade estarem definidos
       ↓
5. Política de Depreciação (Camada 8) + Operação de Conteúdo (Camada 9)
       ↓
6. Métricas de Sucesso do Conteúdo (Camada 10) ← último, quando há conteúdo para medir
```

**Dependência:** Benchmarking (Fase 0) concluído. Muitas decisões do Content System se beneficiam de ver como outros fazem — especialmente Matriz de Voz e Tom, Biblioteca de Padrões e Padrões de Legibilidade.

---

*Documento criado em: 2026-04-07*
*Versão: 0.1 — Escopo inicial, pré-benchmarking*
*Projeto: Base de Conhecimento CEFOR/Ifes — Reformulação*
