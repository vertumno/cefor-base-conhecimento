# Decisões de Consolidação — Fase 0 → Fase 1

> **Versão:** 3.3 — FASE 1 EM ANDAMENTO
> **Última atualização:** 2026-05-19 (refinamento da arquitetura Trilha/Percurso — decisões 25-32)
> **Decididas por:** Elton + Juliana (sessões 2026-05-08 e 2026-05-13) + Elton + Marquito + Juliana + Rute (2026-05-14) + Elton (sessão de refinamento 2026-05-19)
> **Fonte canônica das resoluções Fase 0:** `_config/decisoes-cefor-2026-05-13.json`
> **Fonte canônica das resoluções Fase 1:** `stages/01-fundacoes/reunioes/revisao-taxonomia-2026-05-14.json`
> **Fontes cruzadas:**
> - 🟢 Reunião de brainstorm (01/04/2026) — Elton, Marquito, Rute, Juliana
> - 🔵 Pesquisa de benchmarking — Juliana (7 sites analisados com 5 óculos)
> - 🟠 Relatório comparativo — Claude (análise consolidada de 7 sites)
> - 🟣 Reunião de validação (14/05/2026) — Elton, Marquito, Juliana, Rute

---

## Status geral

| Status | Quantidade | IDs |
|---|---|---|
| ✅ Aprovado | 20 | 4, 8, 10, 11, 15, 16, **17, 19, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32** |
| 🔧 Ajustado | 10 | 1, 2, 5, 6, 9, 12, 13, 14, **18, 21** |
| ❌ Rejeitado | 2 | 3, 7 |
| ⏳ Pendente | 0 | — |

**Total: 32 decisões resolvidas.** A Fase 0 está formalmente concluída. A Fase 1 está em andamento — a reunião de 14/05/2026 validou a taxonomia em 4 eixos e a interface do artigo (8 decisões 17-24), e a sessão de refinamento de 2026-05-19 fechou questões abertas sobre a arquitetura Trilha/Percurso (8 decisões 25-32).

---

## Como usar este documento

Cada decisão abaixo tem:
1. **O que decidir** — a pergunta
2. **O que a reunião disse** — posição da equipe no brainstorm
3. **O que a pesquisa mostrou** — evidências do benchmarking e relatório
4. **Recomendação** — proposta baseada nas evidências (preservada como histórico)
5. **Resolução da equipe** — decisão final tomada com status, comentário e data

Ao final, um resumo das decisões tomadas que será o ponto de partida da Fase 1.

---

## Decisão 1 — Propósito-farol da Base

**O que decidir:** Qual é a declaração de propósito que guia todas as outras decisões?

🟢 **Reunião:** Marcos resgatou a motivação original: *"O local no qual eu posso enviar para alguém e aquela pessoa vai conseguir fazer e resolver o problema dela sem que eu tenha que resgatar todas as coisas para poder resolver."* A equipe ratificou: a base é um **instrumento de formação em serviço** — não repositório, mas espaço de autonomia.

🟠 **Relatório:** A análise dos 7 sites confirma que as melhores bases combinam **consulta pontual** (resolver problema agora) com **formação estruturada** (trilhas, séries, percursos). Nenhum dos 7 combina as duas coisas com excelência.

**Recomendação:**

> **"A Base de Conhecimento do CEFOR é o lugar onde qualquer profissional de EaD do IFES resolve problemas com autonomia e se forma continuamente."**

Duas funções em uma só base:
- **Consulta:** "Estou com um problema agora, preciso da resposta"
- **Formação:** "Quero aprender, quero evoluir"

**Resolução da equipe (2026-05-08):** 🔧 **AJUSTADO**

> "Não será uma formação estruturada, mas seria um espaço de aprendizagem e atualização contínua."

A função de formação **estruturada** (trilhas longas com início/meio/fim obrigatórios) sai do escopo do propósito-farol. A base é espaço de **consulta + aprendizagem e atualização contínua** — o leitor entra para resolver ou para aprender algo pontual, não para "fazer um curso". Trilhas existem (ver Decisão 9), mas são curadoria editorial opcional, não a coluna vertebral da experiência.

---

## Decisão 2 — Público-alvo e segmentação por perfil

**O que decidir:** Para quem é a base e como segmentar a experiência?

🟢 **Reunião:** Público definido como profissionais de EaD/tecnologias educacionais do IFES. Rute propôs **percursos por perfil** ("Sou mediadora", "Sou professor") como prioridade de experiência. Consenso unânime.

🟠 **Relatório:** A lacuna mais clara é que os 7 sites analisados são **monoaudiência**. O CEFOR atende servidores, professores, técnicos, estudantes e público externo de MOOCs simultaneamente. *"Categorização clara por perfil na entrada já diferencia."*

**Recomendação:**

Adotar segmentação por perfil na V1, com 3-4 perfis iniciais:

| Perfil | Público | Exemplo de entrada |
|---|---|---|
| **Professor / Mediador** | Quem dá aula no EaD | "Sou professor e quero..." |
| **Coordenador** | Quem gerencia cursos | "Coordeno um curso e preciso..." |
| **Estudante de MOOC** | Aluno do Vitrine | "Sou aluno e quero..." |
| **Técnico / TI** | Suporte técnico | "Preciso configurar / resolver..." |

> **Não precisa de login nem perfil de usuário na V1.** Basta categorização de conteúdo por público + navegação por perfil na home.

**Resolução da equipe (2026-05-08):** 🔧 **AJUSTADO**

> "Sim, vamos fazer segmentação por perfil mas **sem navegação por perfil na home**. Usaremos apenas a categorização de conteúdo para fazer a segmentação do perfil."

Perfis existem como filtro/categorização interna do conteúdo (e ajudam a busca e a curadoria), mas **não viram uma porta de entrada visual** no topo da home. A home não terá "Sou professor / Sou mediador / Sou coordenador" como mosaico de entrada. Isso evita travar o leitor numa identidade antes mesmo de ele descobrir o que precisa.

---

## Decisão 3 — TL;DR obrigatório

**O que decidir:** Artigos devem ter um bloco "Em resumo" no topo?

🟢 **Reunião:** Não discutido diretamente, mas o propósito-farol ("resolver rápido") implica necessidade de escaneabilidade máxima.

🔵 **Pesquisa:** Juliana observou que os melhores sites permitem ao leitor decidir rapidamente se o artigo vai ajudar, mas nenhum faz isso de forma explícita.

🟠 **Relatório:** *"Nenhum dos 7 sites entrega TL;DR de forma rotulada e explícita."* O relatório classifica como **Prioridade 1** junto com tempo de leitura e índice. *"Custo baixíssimo, ganho enorme em escaneabilidade."*

**Recomendação:**

**Sim, obrigatório para artigos com mais de 3 minutos de leitura.** Formato:

```
📌 Em resumo
• [Ponto 1 — conclusão, não promessa]
• [Ponto 2]
• [Ponto 3]
```

O TL;DR deve conter a **conclusão**, não a introdução. O leitor que lê só o resumo já sai sabendo o essencial.

**Resolução da equipe (2026-05-08):** ❌ **REJEITADO**

> "Avaliar se é um recurso utilizado atualmente."

TL;DR rotulado e obrigatório **não entra na V1**. A equipe sinalizou ceticismo quanto ao uso real do recurso e preferiu não impor um padrão antes de ver evidência de demanda. A escaneabilidade será resolvida por outros mecanismos já aprovados (índice de seções com scroll-tracking — Decisão 4, padrões de legibilidade — Camada 6 do Content System, e callouts editoriais — Decisão 5).

> **Reavaliar na Fase 5** com dados de uso reais (analytics, feedback do leitor). Não fechar a porta para o futuro.

---

## Decisão 4 — Tempo de leitura e índice de seções

**O que decidir:** Exibir tempo estimado de leitura e índice "Neste artigo" nos artigos?

🟠 **Relatório:** 43% dos sites mostram tempo de leitura (Medium, Coursera, Claude Blog). 71% oferecem índice de seções. Combinado com o TL;DR, esse trio é a **Prioridade 1** do relatório.

**Recomendação:**

- **Tempo de leitura:** Sim, abaixo do título. Cálculo: 200 palavras/minuto em português.
- **Índice "Neste artigo":** Sim, para artigos com 4+ seções. Bloco visível abaixo do H1, com links âncora. Modelo Canva.
- **Barra de progresso de leitura:** Sim, barra fina (2-3px) no topo, cor institucional.

Custo de implementação mínimo, impacto alto.

**Resolução da equipe (2026-05-08):** ✅ **APROVADO** (com complemento)

> "Índice deve acompanhar a rolagem da tela pelo usuário, estando sempre visível e localizando a posição da leitura."

Confirma os três elementos (tempo de leitura, índice, barra de progresso) e fixa um requisito adicional: o **índice é sticky com scroll-tracking** — sempre visível na sidebar enquanto o usuário rola, com a seção atual destacada. Esse comportamento entra como requisito obrigatório do Design System (Fase 2) e da implementação WordPress (Fase 3).

---

## Decisão 5 — Tipos de callout/alerta

**O que decidir:** Quantos tipos de caixa de destaque padronizar?

🟢 **Reunião:** Não discutido diretamente.

🟠 **Relatório:** 71% dos sites usam callouts. Recomendação: *"Sistema visual de callouts com 4 tipos fixos: Informação, Dica, Atenção, Exemplo."*

**Recomendação:**

4 tipos fixos, com cores e ícones consistentes:

| Tipo | Cor | Ícone | Quando usar |
|---|---|---|---|
| **ℹ️ Informação** | Azul | Info | Contexto adicional, nota explicativa |
| **💡 Dica** | Verde | Lâmpada | Atalho, boa prática, melhoria |
| **⚠️ Atenção** | Amarelo | Alerta | Cuidado, pode dar errado, reversível |
| **🔴 Importante** | Vermelho | Exclamação | Ação irreversível, perda de dados, impacto alto |

Documentar no Style Guide e exigir uso correto na produção de conteúdo.

**Resolução da equipe (2026-05-08):** 🔧 **AJUSTADO**

> "Gostamos da possibilidade de ter textos destacados, porém os tipos de informações devem ser definidas pelo content design (pois pode ter destaques do tipo: frases de efeito, citações, entre outras que vão ser definidas ainda) e as cores devem acompanhar o design system."

A ideia de **callouts/destaques editoriais é mantida**, mas:
- O **conjunto de tipos** não é fechado nesta decisão — será definido na **Biblioteca de Padrões de Conteúdo** (Camada 4 do Content System, Fase 1) e pode incluir tipos não-utilitários como **frase de efeito**, **citação**, **resumo de seção** etc., além dos tipos clássicos (informação, dica, atenção, importante).
- As **cores e estilos visuais** não são definidos aqui — saem dos tokens do **Design System** (Fase 2), garantindo consistência com a identidade.
- A lista dos 4 tipos com cores fixas proposta acima fica como **referência preliminar**, não como decisão final.

---

## Decisão 6 — Tipografia editorial

**O que decidir:** Usar serifada nos títulos ou só sans-serif?

🟠 **Relatório:** 29% dos sites combinam serifada nos títulos com sans-serif no corpo (Medium, Zendesk, Claude Blog) — *"padrão editorial premium"* que *"comunica que o conteúdo é tratado como publicação séria"*. Sugestão: Source Serif ou similar nos H1/H2, Inter ou Source Sans no corpo a 16-17px.

**Recomendação:**

**Sim, combinar serifada nos títulos com sans-serif no corpo.** Opções (Google Fonts, gratuitas):

| Elemento | Fonte sugerida | Fallback |
|---|---|---|
| H1, H2 | **Source Serif 4** ou **Lora** | Georgia, serif |
| Corpo, H3+ | **Inter** ou **Source Sans 3** | system-ui, sans-serif |
| Código | **JetBrains Mono** ou **Fira Code** | monospace |

Corpo a 17-18px, line-height 1.65-1.7. Coluna de leitura entre 680-720px.

> A decisão final de fontes pode ser tomada na Fase 2 (Design System), mas a **direção** (serifada + sans-serif) deve ser definida agora.

**Resolução da equipe (2026-05-13):** 🔧 **AJUSTADO**

> "Tudo sem serifa."

A direção mista (serifada nos títulos + sans no corpo) **foi rejeitada**. A V1 será **100% sans-serif**, em todos os níveis hierárquicos. A escolha exata da família tipográfica (Inter, Source Sans, Open Sans, Lexend etc.) e dos tamanhos/pesos fica para a **Fase 2 — Design System**. A diferenciação hierárquica virá por **peso, tamanho e espaçamento**, não por contraste serifada/sans.

---

## Decisão 7 — Fundo e identidade visual

**O que decidir:** Usar branco puro ou fundo neutro?

🟠 **Relatório:** *"Abandonar o branco padrão eleva a percepção de qualidade editorial."* Zendesk usa bege (#f3ede3), Claude Blog usa fundo escuro. Sugestão: cinza leve (#fafafa) ou bege institucional alinhado à paleta verde do IFES, com branco puro só nos cards de conteúdo.

**Recomendação:**

**Fundo cinza muito leve (#f7f7f5 ou #fafaf8) com cards brancos (#ffffff).** Reduz fadiga visual e dá identidade. Alinhar com a paleta verde institucional do IFES como cor de acento.

| Elemento | Cor sugerida |
|---|---|
| Fundo geral | #f7f7f5 (cinza-bege leve) |
| Cards / superfícies | #ffffff |
| Texto principal | #1a1a1a (quase preto) |
| Texto secundário | #5c5a50 |
| Cor de acento | Verde IFES (a extrair do manual de marca) |

> Decisão detalhada dos tokens na Fase 2. Aqui é a direção.

**Resolução da equipe (2026-05-08):** ❌ **REJEITADO** (com contraproposta)

> "Fundo deve ser **branco**. Podemos usar a cor verde, mas ela não precisa ser a destaque. Podemos explorar outras cores como a cor principal principal. Os cards não devem ser tão delimitados mas devem estar mais integrados com o layout da página."

A direção bege/cinza-leve com cards brancos delimitados **foi rejeitada**. Direção aprovada para a Fase 2:
- **Fundo:** branco (não bege, não cinza)
- **Verde IFES:** mantido como uma das cores da paleta, mas **não obrigatoriamente como cor principal** — outras cores podem ser exploradas para esse papel
- **Cards:** **menos delimitados**, mais integrados ao layout — evitar contorno forte, sombra pronunciada e contraste alto de fundo. Preferir separação por respiro/espaçamento e tipografia.

---

## Decisão 8 — Modo escuro

**O que decidir:** Implementar modo escuro desde o início?

🟠 **Relatório:** 43% dos sites oferecem (Algolia, Medium, Claude Blog). *"Usar variáveis CSS desde o início torna a implementação simples."*

🟢 **Reunião:** Não discutido, mas acessibilidade é prioridade implícita (instituição pública).

**Recomendação:**

**Sim, mas implementar com variáveis CSS desde o dia 1.** Isso significa:
- Todos os valores de cor são CSS custom properties (`--color-text-primary`, etc.)
- O tema escuro é uma troca de variáveis, não reescrita de CSS
- Toggle visível na navbar
- Respeitar `prefers-color-scheme` do sistema como padrão

Custo: praticamente zero se planejado desde o início. Custo alto se adicionado depois.

**Resolução da equipe (2026-05-08):** ✅ **APROVADO**

Modo escuro entra na V1 conforme recomendado: implementação via CSS custom properties desde o início, toggle visível, respeito a `prefers-color-scheme`. O tema escuro também é o **caminho de leitura confortável em ambientes pouco iluminados** e complementa o pacote de acessibilidade (Decisão 10).

---

## Decisão 9 — Trilhas pedagógicas na V1

**O que decidir:** Implementar trilhas/percursos com navegação previous/next e progresso na V1?

🟢 **Reunião:** Percursos por perfil são **consenso e prioridade**. Rute propôs trilhas menores + certificação (declarado como "sonho"). Marcos conectou com formação em serviço. A base atual já tem 12 percursos temáticos.

🟠 **Relatório:** Classificado como **Prioridade 4**. *"Transforma artigos isolados em jornadas estruturadas."* Trilhas sugeridas: "Comece a ensinar a distância no IFES", "Domine o Moodle", "Crie seu primeiro MOOC".

**Recomendação:**

**Sim na V1, mas em versão simplificada:**

| Funcionalidade | V1 | V2 |
|---|---|---|
| Percursos temáticos organizados | ✅ | ✅ |
| Navegação previous/next entre artigos | ✅ | ✅ |
| Sidebar de série (artigos da trilha listados) | ✅ | ✅ |
| Indicador de progresso visual | ❌ (exige estado de usuário) | ✅ |
| Marcar como "concluído" | ❌ (exige login) | ✅ |
| Quiz/certificação ao final | ❌ | V3 |

> Na V1, trilhas são **curadoria editorial** (organização de conteúdo), não funcionalidade técnica de tracking.

**Resolução da equipe (2026-05-13):** 🔧 **AJUSTADO**

> "Queremos que tenha as trilhas de aprendizagem, mas ainda não temos definido o local — se ficará na sidebar, no início do artigo ou em outro lugar melhor. **Lembrança:** importante que em todos os artigos tenha ao final da página indicação de **artigos relacionados**."

Confirmado:
- **Trilhas existem na V1** como curadoria editorial (sem tracking de progresso, sem login, sem certificação).
- **Local de exibição da trilha dentro do artigo:** **decisão deferida** para a Fase 2 (Design System) — pode ser sidebar, cabeçalho do artigo, bloco fixo no topo do conteúdo ou rodapé. Será testado no protótipo.
- **Artigos relacionados ao final do artigo:** **requisito obrigatório** em todos os artigos (independente de pertencerem ou não a uma trilha). Vira critério de aceitação do template de artigo na Fase 3.

---

## Decisão 10 — Pacote de acessibilidade

**O que decidir:** Qual nível de acessibilidade implementar na V1?

🟢 **Reunião:** Acessibilidade é premissa implícita (instituição pública federal).

🔵 **Pesquisa:** Juliana observou que nenhum dos sites pesquisados oferece widget de acessibilidade.

🟠 **Relatório:** Classificado como **Prioridade 2**. *"Nenhum dos 7 sites oferece widget de acessibilidade. Não é diferencial opcional para o CEFOR, é cumprimento de eMAG e LGPD. Implementar com qualidade coloca a Base à frente de todos os 7 sites."*

**Recomendação:**

**Implementar pacote completo na V1:**

| Recurso | Prioridade V1 | Como |
|---|---|---|
| VLibras | ✅ Obrigatório | Widget governamental gratuito |
| A-/A+ (tamanho de fonte) | ✅ Obrigatório | CSS variables + botões |
| Alto contraste (WCAG AAA) | ✅ Obrigatório | Tema preto/amarelo alternativo |
| Fonte para dislexia (OpenDyslexic/Lexend) | ✅ Obrigatório | Toggle + Google Fonts |
| Atalhos de teclado documentados | ✅ Obrigatório | Página dedicada + dica na interface |
| Text-to-speech nativo | 🟡 Desejável | Web Speech API (gratuita, sem servidor) |
| Semântica HTML rigorosa (H1 único, landmarks, ARIA) | ✅ Obrigatório | Na implementação de todos os componentes |
| "Pular para o conteúdo principal" | ✅ Obrigatório | Link no topo, padrão eMAG |

> Widget flutuante na lateral direita com ícone de acessibilidade, acessível por teclado.

**Resolução da equipe (2026-05-08):** ✅ **APROVADO**

O pacote completo de acessibilidade entra na V1 conforme recomendado. Acessibilidade não é diferencial: é cumprimento de eMAG, WCAG 2.2 AA e LGPD para uma instituição pública federal. Os requisitos virarão **checklist obrigatório por componente** no Design System (Fase 2) e critério de aceitação técnica na implementação (Fase 3).

> Esta decisão se cruza diretamente com a Decisão 13 (multimodal): vídeo em Libras dentro do artigo e audiodescrição visível para todos passam a ser **funcionalidades editoriais**, não apenas técnicas.

---

## Decisão 11 — Busca

**O que decidir:** Que tipo de busca implementar na V1?

🟢 **Reunião:** Base atual já tem busca funcional na home. Não houve discussão aprofundada sobre busca com IA.

🟠 **Relatório:** Busca é **Prioridade 3**. Modelo Algolia (Ctrl+K, modal central, atalhos). Resposta sintetizada por IA (modelo Canva/Coursera) como evolução. *"Custo médio-alto se incluir IA, baixo se for só busca textual indexada."*

**Recomendação:**

**V1: busca textual robusta com modal. V2: resposta com IA.**

| Funcionalidade | V1 | V2 |
|---|---|---|
| Modal de busca (Ctrl+K) | ✅ | ✅ |
| Busca full-text indexada | ✅ | ✅ |
| Filtros por categoria/tipo/perfil | ✅ | ✅ |
| Atalhos visíveis (ESC, setas, Enter) | ✅ | ✅ |
| Resultados agrupados por categoria | ✅ | ✅ |
| Resposta sintetizada por IA | ❌ | ✅ (evolução Sofia) |

**Resolução da equipe (2026-05-08):** ✅ **APROVADO**

Busca textual robusta com modal (Ctrl+K), filtros e atalhos visíveis entra na V1. Resposta sintetizada por IA fica para a V2. A tecnologia exata (Algolia hospedada, ElasticPress, WP-CLI search index, FlexSearch local, etc.) será escolhida na Fase 3 — Implementação WordPress.

---

## Decisão 12 — Feedback e interação do leitor

**O que decidir:** Quais interações o leitor terá com o artigo?

🟢 **Reunião:** Marcos propôs sistema de destaques/estrelas, comentários em trechos, co-criação wiki. Consenso: contribuições externas ficam para V2 (segundo semestre 2026). Citação ABNT automática foi mencionada como quick win.

🟠 **Relatório:** Feedback com emoji (modelo Canva: 😊/😟) é mais convidativo que polegar. *"Quando o usuário clica 'Não muito', abrir campo opcional 'O que faltou?'."* Copiar link da seção (modelo Algolia) permite compartilhar passagem exata.

**Recomendação:**

| Interação | V1 | V2 |
|---|---|---|
| "Esse artigo foi útil?" (😊/😟 + campo "O que faltou?") | ✅ | ✅ |
| Copiar link do artigo | ✅ | ✅ |
| Copiar link da seção (âncora) | ✅ | ✅ |
| Copiar citação ABNT formatada | ✅ | ✅ |
| Compartilhar (WhatsApp, e-mail, copiar link) | ✅ | ✅ |
| "Reportar erro" / "Sugerir atualização" | ✅ (formulário simples) | ✅ (rastreável) |
| Comentários em trechos | ❌ | V2 |
| Destaques/estrelas | ❌ | V2 |
| Salvar para ler depois | ❌ | V2 (exige login) |

**Resolução da equipe (2026-05-08):** 🔧 **AJUSTADO**

> "Não vamos usar emojis. Use **'Foi útil'** ou **'Não foi útil'**."

Feedback do leitor entra na V1 conforme proposto, **com um ajuste de forma**:
- O par 😊/😟 **sai**. No lugar, dois botões com texto literal: **"Foi útil"** e **"Não foi útil"**.
- Tom institucional, sem carga emocional/lúdica que emojis embutem.
- Resto da recomendação (campo opcional "O que faltou?", copiar link, copiar âncora de seção, copiar ABNT, compartilhar, reportar erro) **mantida**.

> Implicação para o Design System (Fase 2): o componente de feedback é tipográfico/icônico, não emoji. Mesma regra vale para qualquer outro componente — emojis ficam fora da UI institucional.

---

## Decisão 13 — Conteúdo multimodal

**O que decidir:** Artigos devem estar disponíveis em múltiplos formatos?

🟢 **Reunião:** Consenso. Juliana propôs artigos em texto, áudio, vídeo, passo-a-passo. Marcos mencionou flashcards com áudio para estudo mobile. *"Não posso ver vídeo agora, quero só o passo-a-passo em texto."*

🟠 **Relatório:** Text-to-speech como diferencial (apenas Medium oferece entre os 7 sites). Web Speech API é gratuita.

**Recomendação:**

| Formato | V1 | V2 |
|---|---|---|
| Texto (formato principal) | ✅ | ✅ |
| Áudio TTS (Web Speech API) | 🟡 Se viável | ✅ |
| Abas desktop/mobile (modelo Canva) | ✅ (quando aplicável) | ✅ |
| Vídeo embutido | ✅ (onde existir) | ✅ |
| Flashcards | ❌ | V2 |

> Abas "Computador / Dispositivo móvel" (modelo Canva) resolvem o problema real de Moodle desktop vs Moodle Mobile sem duplicar artigos.

**Resolução da equipe (2026-05-13):** 🔧 **AJUSTADO** (escopo ampliado significativamente)

> "Não precisa de aba para mobile, retire essa opção. O site sempre deve ser responsivo.
>
> Precisa ter a opção de incluir **vídeo em Libras** que será a tradução em Libras do texto do artigo. A solução pode ser um **accordion**.
>
> As imagens podem ou não ter uma legenda. E além disso, quero que tenha a opção de ter um campo de **audiodescrição que descreva a imagem para cegos e fica visível para todos**.
>
> Queremos que o artigo tenha a opção de ser **escutado em áudio**.
>
> Queremos que o artigo tenha opção de **Podcast**.
>
> Pretendemos que alguns artigos tenham a possibilidade de ter **infográficos/imagens que sintetizem, resumam, reforcem os principais conceitos** abordados no artigo."

**Reestruturação do modelo multimodal V1:**

| Formato | Status V1 | Detalhes |
|---|---|---|
| Texto | ✅ Obrigatório | Formato principal |
| **Aba "Computador / Mobile"** | ❌ **REMOVIDO** | O site é responsivo. Quando o procedimento difere por dispositivo, usar variação editorial dentro do mesmo texto (subseções, callouts), não tabs |
| **Vídeo em Libras (tradução do artigo)** | ✅ **NOVO — Obrigatório quando disponível** | Em accordion (recolhível). Tradução em Libras do texto completo do artigo, não apenas widget VLibras genérico |
| **Audiodescrição de imagens visível** | ✅ **NOVO — Padrão para imagens** | Campo de texto descritivo da imagem **visível para todos**, não apenas em `alt`. Imagens podem ter legenda opcional adicional |
| **Áudio do artigo (narração)** | ✅ Obrigatório quando viável | "Ouvir o artigo" — narração do texto. Pode usar TTS (Web Speech API) ou áudio gravado |
| **Podcast** | ✅ Quando aplicável | Formato podcast com produção dedicada (não é o mesmo que narração TTS) |
| **Infográficos/imagens-resumo** | ✅ Opcional por artigo | Componente editorial dedicado para resumir/reforçar conceitos visualmente. Não obrigatório, mas previsto no template |
| Vídeo embutido (passo-a-passo) | ✅ Onde existir | — |
| Flashcards | ❌ V2 | — |

> **Implicações pesadas para Fase 1, 2 e 3:**
> - **Camada 4 do Content System** (Biblioteca de Padrões) precisa prever os componentes: bloco Libras, bloco audiodescrição, bloco infográfico-resumo, bloco áudio/podcast.
> - **Camada 9 do Content System** (ContentOps) precisa absorver o custo de produção: gravar Libras, escrever audiodescrição, gravar narração, eventualmente produzir podcast. Isso afeta o ritmo realista de ~4-6 artigos/mês — **possivelmente reduzindo** para alguns formatos.
> - **Design System (Fase 2)** ganha 4 novos componentes obrigatórios e precisa definir o accordion de Libras, o tratamento visual de audiodescrição, o player de áudio.
> - **Implementação WordPress (Fase 3)** precisa de Custom Fields para `video_libras_url`, `audio_url`, `podcast_url`, `infografico_url`, `audiodescricao` por imagem.

---

## Decisão 14 — Metadados e autoria

**O que decidir:** Quais metadados são obrigatórios em cada artigo?

🟢 **Reunião:** Consenso forte. Autoria obrigatória (compliance com legislação de IA). Indicação "Produzido com IA" quando aplicável. Múltiplos autores, citação ABNT automática.

🟠 **Relatório:** *"Mostrar autor, revisor pedagógico, data de criação, data da última revisão e próxima revisão prevista."* Versionamento para Moodle X.Y.

**Recomendação:**

**Metadados obrigatórios por artigo:**

| Metadado | Exemplo |
|---|---|
| Autor(es) | Juliana Cassaro |
| Revisor pedagógico | Rutinelli Fávero |
| Data de publicação | 2026-05-07 |
| Data da última revisão | 2026-05-07 |
| Tempo estimado de leitura | 5 min |
| Tipo de artigo | Tutorial |
| Categoria | Moodle > Avaliação |
| Tags | questionário, avaliação, nota |
| Versão do Moodle (quando aplicável) | Moodle 4.5+ |
| Marcação IA | "Produzido com assistência de IA" |
| Licença | CC BY-SA 4.0 (ou definir) |

**Resolução da equipe (2026-05-08, complementada em 2026-05-13):** 🔧 **AJUSTADO**

> "Não precisa da versão do Moodle. Pensar se vamos mostrar tipo, categoria, tags."
>
> **Complemento 2026-05-13:** "Os artigos vão obrigatoriamente sempre ter um Autor e o nome deve ser exibido."

Confirmado:
- **Autor(es):** **OBRIGATÓRIO** em todos os artigos. **O nome do autor é exibido na interface do artigo.** Cada artigo precisa ter ao menos um autor declarado nos metadados (pode ter múltiplos). Isso atende ao consenso da reunião (autoria obrigatória, compliance com legislação de IA) e fixa a exibição como requisito de interface.
- **Revisor pedagógico:** **REMOVIDO** do modelo. A tabela legada acima sugeria exibir um "revisor pedagógico" separado do autor — esse papel não existe na operação real e foi descartado. A autoria responde tanto pela produção quanto pela qualidade do conteúdo.
- **Última revisão (data + responsável):** **REMOVIDO da interface do artigo.** A data de última revisão continua existindo como metadado interno (controle de ciclo de vida via Política de Depreciação — Camada 8), mas não é exibida no cabeçalho do artigo.
- **Versão do Moodle:** **NÃO** será exibida como metadado fixo no artigo. (A versão pode aparecer no texto quando relevante para o conteúdo, mas não como metadado de cabeçalho — evita poluir e marcar artigos como datados rapidamente.)
- **Tipo / Categoria / Tags:** **decisão deferida** para o trabalho de **Taxonomia da Fase 1**, junto com o desenho do template de artigo. A exibição (mostrar/não, onde, como) será resolvida no draft de proposta de taxonomia + interface do artigo.

> Esta decisão será reaberta no fechamento da Fase 1 — Taxonomia, quando a proposta de arquitetura taxonômica e o layout do artigo estiverem maduros. O draft `stages/02-design-system/drafts/prototipos-paginas/proposta-taxonomia-e-interface-artigo.md` traz a análise técnica e a proposta inicial.

---

## Decisão 16 — Subtítulo obrigatório (adendo de 2026-05-13)

**O que decidir:** Todo artigo precisa ter um subtítulo abaixo do título principal?

**Origem:** Decisão acrescentada durante a revisão da proposta de taxonomia + interface do artigo (Fase 1), não estava na lista original de 15.

🟢 **Contexto:** Durante o trabalho do protótipo da página de artigo, ficou claro que o subtítulo cumpre função editorial importante — orienta o leitor sobre o ângulo/escopo específico do artigo antes que ele decida investir tempo na leitura. Vários dos sites de benchmarking usam subtítulo como padrão (Medium, Zendesk, Notion).

**Resolução da equipe (2026-05-13):** ✅ **APROVADO**

> "Todo artigo deve ter um subtítulo."

**Regras:**
- **Obrigatório em todos os artigos** — sem exceção. Vira critério de aceitação do template no WordPress (Fase 3) e da rubrica de qualidade (Camada 5 do Content System).
- **Função:** delimitar o escopo do artigo, dizer "para quem" ou "para qual situação" o conteúdo serve, em uma frase única.
- **Posicionamento:** logo abaixo do H1, antes da linha de meta (autor, tempo de leitura).
- **Comprimento sugerido:** uma única frase, entre 10 e 25 palavras (a especificar na Camada 6 — Padrões de Legibilidade).
- **Tipografia:** mesma família do corpo (sans-serif, Decisão 6), peso regular, tamanho intermediário entre H1 e corpo.

**Exemplo (artigo "Configurando o livro de notas do Moodle"):**

> Como montar o gradebook do seu curso passo a passo: criar categorias, definir pesos por agrupamento, aplicar fórmulas e revisar antes de publicar para os estudantes.

> Esta decisão impacta o template de artigo (Fase 2 — Design System) e o Custom Post Type do WordPress (Fase 3), que precisará de um campo dedicado `subtitulo` obrigatório.

---

## Decisão 15 — O que fica FORA da V1

**O que decidir:** Confirmar o que não entra agora para proteger o escopo.

🟢 **Reunião:** A análise estratégica (Atlas) alertou: *"A equipe sonha com uma plataforma de aprendizagem social gamificada mas precisa entregar uma migração funcional. O risco é paralisia por ambição."*

**Recomendação:** Confirmar explicitamente o escopo negativo da V1:

| Funcionalidade | Horizonte | Origem |
|---|---|---|
| Chatbot/Tutor IA (evolução Sofia) | V2 | Rute + Marcos |
| Gamificação (badges, ranking, prêmio anual) | V3 | Marcos + Juliana + Rute |
| Contribuição wiki de professores | V2 (S2 2026) | Marcos |
| Flashcards + áudio para estudo mobile | V2 | Marcos |
| Ferramentas interativas embutidas | V2 | Marcos |
| Trilhas com certificação | V2/V3 | Rute |
| Integração profunda com Moodle (LTI/embed) | V2 | Juliana + Marcos |
| Login de usuário com perfil | V2 | — |
| Tracking de progresso em trilhas | V2 | — |
| Experiências exitosas / Vitrine | V2 | Marcos + Elton |
| Integração com Instagram | V3 | Juliana + Marcos |

**Resolução da equipe (2026-05-08):** ✅ **APROVADO**

> "Tudo fica fora do V1."

Toda a lista acima é escopo negativo confirmado. Qualquer pedido de inclusão de funcionalidade dessa lista durante as Fases 1-5 dispara uma reavaliação formal de escopo (não basta "encaixar"). Esse é o anteparo contra o risco de paralisia por ambição apontado pela análise estratégica.

### Anexo 2026-05-26 — Componentes editoriais do artigo deferidos para V3

Adendo formal após revisão da masthead do `prototipo-artigo.html`. Componentes prototipados a partir do Padrão 4.1 (Artigo encadeável, `padroes-composicao.md`) que **não entrarão em nenhum artigo da V1**:

| Componente | Onde estava | Por que sai da V1 | Quando reavaliar |
|---|---|---|---|
| **Entry-block** (pré-requisitos linkados + objetivo, no topo do artigo) | Antes do `<h2 id="contexto">` no `prototipo-artigo.html` | Pré-requisitos serão tratados editorialmente no parágrafo de abertura quando relevantes; objetivo já vive implicitamente no subtítulo. Adicionar bloco visual duplica informação. | **V3** — só voltar se métricas de Fase 5 mostrarem alto bounce em tutoriais por falta de contexto de pré-requisitos. |
| **Outcome-block** (o que você sabe fazer agora + próximos caminhos, no fim do artigo) | Após a última `<h2>` antes do `article-foot` | Coberto pelo **box de trilha multi-trilha** (Decisão 30) na sidebar + **artigos relacionados** obrigatórios no rodapé (Decisão 9 + 24). Adicionar outcome-block sobrepõe função. | **V3** — só voltar se "artigos relacionados" não funcionarem como ponte para o próximo artigo da trilha, medido via clickthrough na V1. |

**Origem:** Elton, 2026-05-26, durante refinamento da masthead. Snapshot pré-remoção: `stages/02-design-system/drafts/prototipos-paginas/historico/prototipo-artigo-2026-05-26.html`.

**Como aplicar:** Pedidos para recriar pré-requisitos no topo ou "o que você sabe fazer" no rodapé disparam reavaliação formal — não basta reativar o componente. Memória interna do projeto: `memory/backlog_v3.md`.

---

## Decisões da Fase 1 — Reunião de validação (2026-05-14)

> Participantes: Elton Vinicius, Marquito (Marcos Vinícius Forecchi Accioly), Juliana Cristina da Silva Cassaro, Rute (Rutinelli Fávero)
> Artefatos validados: `stages/02-design-system/drafts/prototipos-paginas/proposta-revisao-interativa.html` e `stages/02-design-system/drafts/prototipos-paginas/prototipo-artigo.html`
> Fonte canônica: `stages/01-fundacoes/reunioes/revisao-taxonomia-2026-05-14.json`

---

## Decisão 17 — Taxonomia em 4 eixos (aprovação formal)

**O que decidir:** A arquitetura de 4 eixos (Tipo, Categoria, Tópico, Trilha) que substitui o modelo atual (categorias + fototipos + tags livres + percursos) deve ser adotada?

🟣 **Reunião:** A equipe revisou os 4 eixos interativamente via artefato de revisão. Eixos 1, 2 e 3 aprovados sem ressalvas. Eixo 4 aprovado com ajuste (ver Decisão 18). A regra-mãe — *"cada eixo responde a uma única pergunta; se dois eixos respondem à mesma, um sai"* — foi validada.

**Resolução da equipe (2026-05-14):** ✅ **APROVADO**

**Arquitetura aprovada:**

| Eixo | Pergunta que responde | Cardinalidade | Valores |
|---|---|---|---|
| **Tipo** | Como se lê/usa este artigo? | 1 por artigo | Tutorial, Referência, Conceitual, Solução de Problema, Recurso |
| **Categoria** | Qual domínio de conhecimento? | 1 por artigo | Ferramentas e Recursos, Pedagogia e Planejamento, Acessibilidade, Conduta e Conformidade, Identidade, *(6ª a definir)* |
| **Tópico** | Qual assunto específico? | 2 a 4 por artigo | Vocabulário controlado — 25 tópicos fixos (substitui 82 tags livres) |
| **Trilha** | Faz parte de uma jornada curada? | 0 ou mais por artigo | Ver Decisão 18 |

**Impactos:**
- Tags livres **abolidas**. A pessoa escolhe entre os tópicos da lista fechada.
- 20 categorias antigas → 6 categorias. Resolve duplicidade: artigos que antes estavam em 3 categorias agora têm apenas 1.
- 12 percursos antigos → estrutura Trilha/Percurso (ver Decisão 18).

---

## Decisão 18 — Nova arquitetura Trilha/Percurso (semântica redefinida)

**O que decidir:** O modelo atual de percursos (que virou categoria de organização, perdendo o sentido de jornada) precisa ser reestruturado. Como?

🟣 **Reunião:** Marquito identificou o problema central: percursos deixaram de ser jornadas e viraram categorias de agrupamento. Rute propôs a hierarquia Percurso > Trilha. A equipe construiu juntos a nova semântica:
- **Trilha** = caminho atômico de conhecimento com começo, meio e fim reais. É composto por artigos. É pequena, focada num objetivo ferramental específico.
- **Percurso** = conjunto de trilhas (e/ou artigos soltos) que forma um caminho formativo maior, com objetivo pedagógico. É o equivalente a um "curso" dentro da base.

Analogia validada por Marquito: *"É como um parque nacional — o percurso é o parque, as trilhas são as trilhas menores que o compõem. Andar todas é completar o percurso."*

**Resolução da equipe (2026-05-14):** 🔧 **AJUSTADO** (redefine Eixo 4 e expande o modelo)

**Nova arquitetura:**

| Nível | O que é | Composto por | Objetivo |
|---|---|---|---|
| **Artigo** | Unidade atômica | — | Resolver um problema ou explicar um conceito |
| **Trilha** | Micro-jornada de conhecimento | Artigos (com começo, meio e fim) | Ensinar como fazer algo específico |
| **Percurso** | Caminho formativo maior | Trilhas e/ou artigos soltos | Profissionalizar em uma área ou tema |

**Regras:**

- Um artigo **pode estar em mais de uma trilha** (reverte a regra anterior de máximo 1 trilha por artigo).
- Um artigo **funciona dentro e fora da trilha** — deve ser útil sozinho, não apenas como parte de uma sequência.
- Uma trilha tem **começo, meio e fim reais** e pelo menos 3 artigos.
- Um percurso **não tem ordem linear obrigatória** — o leitor pode escolher por qual trilha começar.
- Um percurso pode ter **artigos soltos** além de trilhas (quando o artigo complementa mas não pertence a nenhuma trilha específica do percurso).
- Na terminologia da interface: itens de uma **trilha** são chamados de "artigos" (ex: "Artigo 3 de 7"); itens de um **percurso** são chamados de "passos" (que podem ser trilhas ou artigos).

**Exemplo concreto:**
- *Percurso:* "Dominando o Moodle" → contém as trilhas "Configurando questionários", "Gerenciando notas", "Comunicando com estudantes"
- *Trilha:* "Configurando questionários" → artigos: Criar questionário / Definir feedback por questão / Configurar tentativas e prazos
- *Artigo:* "Como fazer um bom prompt" → pode estar na trilha "IA para professores" E na trilha "IA para mediadores"

**Impactos:**
- Eixo 4 do modelo de taxonomia passa de "Trilha (máx 1)" para "Trilha (0 ou mais)".
- Percurso retorna ao escopo como nível acima das trilhas — não é mais apenas uma categoria de agrupamento.
- A interface precisará representar os três níveis: artigo, trilha, percurso.

> **O que NÃO entra na V1 (referência cruzada com Decisão 15):**
> A arquitetura Trilha/Percurso aqui aprovada é puramente **editorial/curatorial** — sem login, sem tracking de progresso por usuário, sem quiz/avaliação ao final, sem certificado/badge de conclusão. Esses itens foram propostos no brainstorm (Rute, Juliana, Marcos, Elton — ver `shared/reuniao-brainstorm.md` §4.7 e §4.8) e estão **explicitamente diferidos** na Decisão 15: tracking de progresso e mini-certificado para V2, gamificação (badges, ranking, prêmio anual) para V3. Reabrir esses temas exige reavaliação formal de escopo.

---

## Decisão 19 — Ordem dos blocos multimodais

**O que decidir:** Qual a ordem de exibição dos blocos de formato alternativo no topo do artigo?

🟣 **Reunião:** Rute pediu explicitamente que **Libras apareça sempre em primeiro lugar**, antes do áudio. Justificativa: é uma bandeira de acessibilidade importante para o setor, vale a pena deixar em destaque mesmo que tecnicamente o áudio seja mais "primário". O texto completo em Libras e o áudio são os formatos de conteúdo completo; os demais (podcast, infográfico) são sínteses.

**Resolução da equipe (2026-05-14):** ✅ **APROVADO**

**Ordem obrigatória dos blocos multimodais:**

1. **Libras** — tradução em Libras do texto completo (accordion)
2. **Ouvir** — narração em áudio do artigo (TTS ou gravado)
3. **Outros formatos** — podcast, infográfico, variações (quando existirem)

> Esta ordem vira regra editorial no Content System (Camada 4 — Biblioteca de Padrões) e requisito de interface no Design System (Fase 2).

---

## Decisão 20 — Formato da citação ABNT no rodapé

**O que decidir:** Qual o formato exato da citação ABNT a ser gerada automaticamente no rodapé de cada artigo?

🟣 **Reunião:** O exemplo concreto foi validado por Juliana durante a reunião.

**Resolução da equipe (2026-05-14):** ✅ **APROVADO**

**Formato:**

```
CASSARO, Juliana. Configurando o livro de notas do Moodle.
Base de Conhecimento CEFOR/Ifes, 2026. Revisado em 12 mai. 2026.
```

**Estrutura:**
`SOBRENOME, Nome. Título do artigo. Base de Conhecimento CEFOR/Ifes, [ano de publicação]. Revisado em [data da última revisão].`

**Regras:**
- O campo `Revisado em` usa a data de última revisão do metadado interno (não exibida no cabeçalho, mas presente no banco de dados — ver Decisão 14).
- Se o artigo tiver múltiplos autores, seguir norma ABNT para múltiplos autores.
- Gerada automaticamente pelo WordPress a partir dos campos Custom Post Type.

---

## Decisão 21 — Política de depreciação: prazo e visibilidade

**O que decidir:** O prazo de depreciação (originalmente proposto em 6 meses) e a visibilidade do badge de depreciação devem ser revistos?

🟣 **Reunião:** Rute sugeriu 12 meses (mais adequado ao ritmo real de atualização de conteúdo educacional). Elton havia removido o badge público no protótipo por achar que geraria ruído; Rute concordou que não deve ser público, mas o controle interno é valioso.

**Resolução da equipe (2026-05-14):** 🔧 **AJUSTADO**

- **Prazo de depreciação:** **12 meses** (não 6 meses como proposto originalmente).
- **Badge de revisão pendente:** exibido **apenas para administradores** — não aparece na interface pública.
- O leitor comum nunca vê conteúdo marcado como "desatualizado" — a equipe interna usa o badge para priorizar revisões.

**Impacto na Camada 8 — Política de Depreciação:** Atualizar prazo de 6 para 12 meses e especificar que o status é metadado administrativo, não público.

---

## Decisão 22 — prototipo-artigo.html como referência canônica da interface

**O que decidir:** Qual arquivo é a referência principal e mais avançada do design da página de artigo?

🟣 **Reunião:** Apresentados dois protótipos: `proposta-revisao-interativa.html` (taxonomia/validação) e `prototipo-artigo.html` (interface completa do artigo). A equipe validou o prototipo-artigo como o mais avançado e completo.

**Resolução da equipe (2026-05-14):** ✅ **APROVADO**

- **`stages/02-design-system/drafts/prototipos-paginas/prototipo-artigo.html`** é a referência canônica da interface do artigo.
- Quaisquer refinamentos de interface partem dele — não da proposta de revisão interativa.
- Próximos refinamentos identificados na reunião:
  - Box de trilha: fechar automaticamente ao rolar (com cuidado para não travar se o usuário rola dentro do box)
  - Navegação prev/next dentro da trilha: deixar mais clara a identidade da trilha (nome visível, contexto de "onde estou")
  - Botão de compartilhar: explorar menu com opção de share formatado para WhatsApp (com mensagem já redigida + link)
  - Compartilhar também acessível no topo do artigo (não só no final)

---

## Decisão 23 — Interface do artigo — cabeçalho e metadados (aprovação formal)

**O que decidir:** O cabeçalho do artigo (categoria + tipo no topo, título, subtítulo, autor, tempo de leitura) está correto?

🟣 **Reunião:** Revisado no prototipo-artigo.html. Sem ressalvas da equipe.

**Resolução da equipe (2026-05-14):** ✅ **APROVADO**

Estrutura confirmada do cabeçalho:
1. Categoria + Tipo (ex: "Pedagogia e Planejamento · Tutorial")
2. Título (H1)
3. Subtítulo (obrigatório — ver Decisão 16)
4. Autor + Tempo de leitura
5. Blocos multimodais (ver Decisão 19)
6. Índice com scroll-tracking (ver Decisão 4)

---

## Decisão 24 — Rodapé do artigo (aprovação formal)

**O que decidir:** O rodapé do artigo (citação ABNT, artigos relacionados, feedback) está correto?

🟣 **Reunião:** Revisado no prototipo-artigo.html. Aprovado sem ressalvas.

**Resolução da equipe (2026-05-14):** ✅ **APROVADO**

Estrutura confirmada do rodapé:
1. Seção de artigos relacionados (obrigatória em todos os artigos — Decisão 9)
2. Caixa "Foi útil / Não foi útil" (Decisão 12)
3. Citação ABNT automática (Decisão 20)

> **Atualização 2026-05-19:** O item original "Box de trilha com prev/next" foi **removido pela Decisão 32** — a navegação entre artigos da trilha passa a ser exclusiva do acordeão multi-trilha na sidebar (Decisão 30). O rodapé fica apenas com os 3 itens acima.

---

## Decisões da Fase 1 — Refinamento da arquitetura Trilha/Percurso (2026-05-19)

> Sessão de refinamento entre Elton e Claude para fechar questões abertas pela Decisão 18.
> Contexto: antes de iniciar o trabalho na Camada 4.5 (Padrões de Composição) do Content System, era necessário responder perguntas estruturais sobre tamanho de trilha, artigos-âncora compartilhados, semântica de percurso e regras de exibição.

---

## Decisão 25 — Tamanho da trilha

**O que decidir:** Existe um número máximo de artigos numa trilha? E qual o mínimo?

🔵 **Contexto:** A Decisão 18 fixou o mínimo de 3 artigos por trilha mas deixou o máximo em aberto. Trilhas muito longas podem virar "mini-percursos disfarçados", confundindo o leitor sobre quando uma sequência é uma trilha e quando é um percurso.

**Resolução (2026-05-19):** ✅ **APROVADO**

- **Mínimo:** 3 artigos (não muda).
- **Máximo:** **não definido** — uma trilha pode ter quantos artigos forem necessários para esgotar a micro-jornada.
- **Métrica de saúde (não bloqueante):** trilhas com mais de **~10 artigos** entram em revisão pedagógica para avaliar se não deveriam ter virado um percurso de trilhas menores. Não é regra editorial dura; é sinal de alerta para curadoria.

**Impacto:** A Camada 4.5 (Padrões de Composição) precisa lidar com trilhas de tamanho variável. A Camada 10 (Métricas) registra "tamanho médio de trilha" como métrica de saúde.

---

## Decisão 26 — Artigo-âncora pode servir múltiplas trilhas

**O que decidir:** Um mesmo artigo (especialmente conceitual, tipo "O que é Moodle") pode ser artigo-âncora — o primeiro de uma trilha — em mais de uma trilha?

🔵 **Contexto:** Decorre da regra (Decisão 18) de que um artigo pode estar em mais de uma trilha. Mas estar no meio de uma trilha é diferente de **abrir** uma trilha. Se um artigo conceitual abre várias trilhas, ele não pode dizer "esta trilha vai te ensinar X" — porque ele é âncora de várias.

**Resolução (2026-05-19):** ✅ **APROVADO**

- **Sim**, um artigo pode ser artigo-âncora (primeiro da sequência) em quantas trilhas fizer sentido editorialmente.
- **Consequência editorial dura:** o artigo-âncora é **editorialmente neutro** quanto à trilha. Ele não pode anunciar a sequência ("nesta trilha você aprenderá a configurar questionários") nem fechar com chamada específica ("no próximo passo da trilha"). Isso é trabalho do **box de trilha** e da **página da trilha**.
- **Não existe padrão específico de "artigo-âncora" no Content System.** O que faz um artigo ser âncora é a posição estrutural na trilha, não algo no conteúdo. Logo, na Camada 4 (Padrões), não se cria um padrão "Abertura de trilha" embutido no artigo — só na página da trilha.

**Impacto:** Reforça a regra-mãe que emerge da Decisão 18 — *o artigo é a unidade soberana; trilha e percurso são camadas de curadoria que envelopam, nunca alteram, o artigo*.

---

## Decisão 27 — Percurso é apenas agregação (sem progresso/certificado)

**O que decidir:** Um percurso tem mecanismo de conclusão (badge, certificado, marca de "completou")? Ou é só uma curadoria visual de trilhas?

🔵 **Contexto:** A Decisão 18 definiu percurso como conjunto de trilhas e artigos soltos, mas não fechou se haveria sistema de progresso/conclusão. Como a V1 não terá login, qualquer rastreamento de conclusão pessoal exigiria infraestrutura adicional.

**Resolução (2026-05-19):** ✅ **APROVADO**

- Percurso é **apenas agregação curada**.
- **Sem certificado.** Sem badge de conclusão. Sem rastreamento de "completou X de Y trilhas".
- **Página de percurso** = curadoria + narrativa pedagógica ("este conjunto de trilhas faz sentido junto porque…"). Lista as trilhas que o compõem e os artigos soltos, com texto explicativo.
- **Diferença formal entre percurso e categoria:** *categoria classifica* (onde o artigo encaixa no domínio de conhecimento), *percurso narra* (que jornada de aprendizagem faz sentido). Ambos são agregações tecnicamente; semanticamente são diferentes.

**Impacto:** Simplifica drasticamente Fase 3 (Implementação) e Camada 9 (ContentOps) — não precisa de sistema de progresso, sessões, identificação de leitor. A Camada 4.5 ganha padrão "Página de percurso" como artefato editorial.

---

## Decisão 28 — Box de trilha sempre visível (vínculo estrutural, não comportamental)

**O que decidir:** Quando um leitor chega a um artigo via busca ou link externo (não veio pela trilha), o box de trilha aparece mesmo assim?

🔵 **Contexto:** Discutiu-se inicialmente um modelo *contextual* (box só aparece se o leitor veio de uma página de trilha, via referrer). A equipe rejeitou: a trilha é informação útil mesmo para quem chegou "solto".

**Resolução (2026-05-19):** ✅ **APROVADO**

- O box de trilha aparece **sempre** que o artigo pertence a uma ou mais trilhas, independente da origem do leitor.
- O vínculo é **estrutural** (relação artigo–trilha registrada no CMS), não **comportamental** (referrer, cookies, sessão).
- Implementação técnica: ao renderizar o artigo, o sistema consulta em quais trilhas ele está e exibe o box correspondente. Sem dependência de estado do navegador.

**Impacto:** Resolve a Decisão 9 (local exato da trilha no artigo) — fica no sidebar do protótipo, sempre presente quando aplicável. Simplifica a implementação na Fase 3. Confirma a importância da Decisão 26 (artigo neutro): se o artigo aparece sempre com box de trilha, ele precisa funcionar dentro e fora dela sem reescrita.

---

## Decisão 29 — V1 sem rastreamento de progresso pessoal

**O que decidir:** Sem login na V1, como mostrar "progresso" na trilha? Posição estrutural, progresso pessoal via localStorage, ou nada?

🔵 **Contexto:** O protótipo atual mostra "Passo 7 de 15" com barra de progresso, sugerindo progresso pessoal. Mas sem login, não há como saber o que o leitor já leu. localStorage seria frágil (perde ao limpar cache, não sincroniza entre dispositivos).

**Resolução (2026-05-19):** ✅ **APROVADO**

- **V1 mostra apenas posição estrutural do artigo na trilha** ("Artigo 5 de 12") — metadado da trilha, independente do leitor.
- A barra de progresso visual continua existindo, **mas representa a posição estrutural** (o artigo está em 41,6% da trilha = 5/12), não o progresso do leitor.
- **Não usar localStorage** para "artigos visitados" na V1. Simplicidade > funcionalidade frágil.
- **Terminologia:** evitar "Passo X de Y" (sugere progresso). Usar **"Artigo X de Y"** dentro da trilha. ("Passo" fica reservado para itens de percurso, conforme convenção do prototipo-artigo.html.)
- **Rastreamento pessoal real fica para V2**, condicionado à existência de login institucional.

**Impacto:** Atualizar `prototipo-artigo.html` para trocar "Passo X de Y" por "Artigo X de Y" no box de trilha. Atualizar texto da Camada 9 (ContentOps) — sem fluxo de identificação de leitor na V1.

---

## Decisão 30 — Apresentação visual de múltiplas trilhas no artigo: acordeão

**O que decidir:** Quando um artigo está em N trilhas, como apresentar isso no sidebar do artigo? Três sub-opções foram exploradas em `stages/02-design-system/drafts/prototipos-paginas/exploracao-multiplas-trilhas.html`: abas (A.1), acordeão (A.2) e cards com prev/next compactos (A.3).

🔵 **Contexto:** Decorrência direta da Decisão 28 (box sempre visível). Com vínculo estrutural e múltiplas trilhas possíveis, o componente precisa lidar com 1 a N trilhas de forma elegante e escalável.

**Resolução (2026-05-19):** ✅ **APROVADO — Sub-opção A.2 (acordeão)**

**Especificação do componente:**

- **Cabeçalho do box:** rótulo "Trilhas deste artigo" + contador (`3`) à direita.
- **Cada trilha vira um item do acordeão**, com cabeçalho clicável contendo:
  - Nome da trilha (texto principal)
  - Posição compacta sempre visível (`5/12`), mesmo colapsado
  - Chevron de expansão
- **Estado inicial:** primeira trilha expandida; demais colapsadas.
- **Comportamento:** permite múltiplas trilhas abertas simultaneamente (não é acordeão exclusivo).
- **Conteúdo expandido de cada trilha:**
  - Barra de progresso estrutural (posição relativa do artigo na trilha)
  - Texto "Artigo X de Y" (não "Passo" — ver Decisão 29)
  - Lista numerada de artigos da trilha, com o artigo atual destacado (`aria-current="page"`)

**Justificativa da escolha:**

- Escala bem (3 ou 10 trilhas, sem rebentar o layout).
- Posição (`5/12`) sempre visível, mesmo para trilhas colapsadas — ajuda o leitor a decidir qual seguir sem expandir.
- Padrão estético idêntico ao box de trilha do `prototipo-artigo.html`, mantendo coerência visual.
- Rejeitadas:
  - **A.1 (Abas):** só mostra uma trilha por vez "por inteiro"; com 5+ trilhas as abas quebram em scroll horizontal.
  - **A.3 (Cards):** prev/next visíveis são uma vantagem, mas a perda da lista completa de artigos da trilha foi considerada cara — o leitor frequentemente quer ver "para onde a trilha leva", e isso é trabalho do índice da trilha.

**Impacto:**
- Substitui o componente `.side-trilha` atual do `prototipo-artigo.html` (que assume uma única trilha) por uma versão multi-trilha com acordeão.
- A Camada 4.5 (Padrões de Composição) documenta este padrão como **"Box de trilha multi-trilha"**.
- Atualizar `prototipo-artigo.html` com o componente novo (junto com a troca de "Passo" por "Artigo" — Decisão 29).

---

## Decisão 31 — Apresentação visual do percurso (página dedicada + integração no artigo)

**O que decidir:** Como o percurso aparece como entidade própria (página dedicada) e como ele se manifesta dentro de artigos e trilhas que pertencem a ele?

🔵 **Contexto:** A Decisão 27 estabeleceu que percurso é apenas agregação (sem certificado/progresso). Faltava definir a expressão visual: hierarquia visual entre percurso, trilha e artigo; cor/identidade própria; estrutura da página de percurso; presença do percurso dentro de artigos.

**Resolução (2026-05-19):** ✅ **APROVADO — Modelo de superfícies** (3 originais → **4** após a revisão de 2026-06-08)

**Referência canônica:** `stages/02-design-system/drafts/prototipos-paginas/base-percurso.html`

> **⚠️ Revisão 2026-06-02 — Dourado abandonado.** A cor reservada do percurso deixa de ser o dourado e passa a ser o **verde escuro** (`--verde-profundo`), mantendo o percurso dentro da própria família verde da marca. A diferenciação de nível agora é **claro → escuro**: trilha em verde claro (`--accent` / `--verde-claro`), percurso em verde escuro (`--verde-profundo` / `--verde-marca`). Categoria/Tópico seguem neutros. Motivo: o dourado destoava da identidade cromática e, na versão "sutil" do chip, acabou virando verde igual ao da trilha — gerando confusão de níveis. O verde escuro resolve a hierarquia sem introduzir uma cor estranha à marca. Os tokens `--gold*` permanecem **apenas** para usos decorativos pontuais (gradiente da barra de progresso, filetes de pullquote), nunca como identidade do percurso. As menções a "dourado" abaixo devem ser lidas como **verde escuro**.

> **⚠️ Revisão 2026-06-08 — Vínculo de percurso sai do acordeão, vai para o painel de meta/stats.** A **Superfície 2 original** (chip de percurso *dentro* do box de trilha, no acordeão do artigo) foi **removida** (HTML + CSS). O vínculo "Faz parte do percurso" passa a viver no **painel de informações** de cada superfície: no **meta do artigo** (`base-artigo.html`, junto de Tipo/Tempo/Compartilhar) e no **painel de stats do hero da página de trilha** (`base-trilha.html`, junto de Artigos/Tempo). Mantém a cor reservada (verde-profundo) e o link para a página do percurso. Motivo (Elton, 2026-06-08): o acordeão deve focar só na sequência de artigos da trilha; o pertencimento ao percurso é metadado e fica mais legível e consistente no painel de meta/stats, sem duplicar a informação. O modelo passa de **3 para 4 superfícies** — ver Superfícies 2–4 reescritas abaixo.

### Hierarquia de cores

| Camada | Cor reservada | Aplicação |
|---|---|---|
| **Percurso** | **Verde escuro** (`--verde-profundo` / `--verde-marca`) | Kicker/chip em pílula sólida, hero da página, borda lateral de cards |
| **Trilha** | **Verde claro** (`--accent` / `--verde-claro` / `--accent-soft`) | Border/hover do box de trilha, links em hover, barra de progresso |
| **Categoria / Tópico** | Neutro (`--ink-2` / `--ink-3`) | Sem cor própria — são classificação, não curadoria |

### Superfície 1 — Página dedicada do percurso

Estrutura obrigatória:
1. **Hero narrativo:** kicker "Percurso" (pílula em verde escuro com ícone) → H1 → subtítulo (1 linha) → 2-3 parágrafos de descrição pedagógica
2. **Stats card lateral:** N trilhas · M artigos · K complementares · ~Xh leitura. **Sem progresso pessoal.** Texto de rodapé explicita "Sem ordem obrigatória, sem certificado, sem rastreamento"
3. **"Para quem é este percurso"** + **"O que você vai dominar"** (duas colunas pedagógicas)
4. **"Como percorrer este conjunto"** — bloco em verde claro com **3 sugestões de ponto de partida por perfil** (resolve a ausência de ordem fixa sem forçá-la)
5. **Cards das trilhas** — 2 colunas, cada card com nome, descrição, **primeiros 5 artigos visíveis** + "+N artigos" quando trilha tiver mais de 5, tempo estimado e CTA "Começar pela primeira"
6. **Artigos complementares** — grid de 3 colunas com cards mais compactos para artigos soltos do percurso
7. **Sobre este percurso** — curadoria, data, outros percursos relacionados

Decisões propositais:
- **Não há botão "Começar percurso"** — não há ordem fixa, em vez disso há sugestões de ponto de partida
- **Não há barra de progresso da página de percurso** — só composição estática
- **Cards de trilha mostram 5 artigos.** Se a trilha tem ≤ 5 artigos, mostra todos sem indicador "+N". Se tem mais, mostra 5 + "+N artigos"

### Superfície 2 — Vínculo de percurso no painel de meta do artigo *(revisada 2026-06-08)*

Quando o artigo integra trilha(s) de um percurso, o painel de meta (`.masthead-meta` de `base-artigo.html`) ganha uma entrada, ao lado de Tipo/Tempo/Compartilhar:

> **FAZ PARTE DO PERCURSO**
> 📖 Dominando o Moodle ›

- Posição: `.meta-block.meta-percurso`, entre "Tempo de leitura" e "Compartilhar"
- Cor: rótulo e link em `--verde-profundo` (cor reservada), com ícone de percurso + chevron; hover em `--verde-marca`; modo escuro em `--verde-claro`
- Comportamento: clicável, leva à página dedicada do percurso
- Condicional: só renderiza quando há vínculo. Artigos sem percurso não exibem a entrada
- **Substitui** o antigo chip dentro do acordeão (removido em 2026-06-08) — o acordeão volta a focar só na sequência de artigos da trilha (cabeçalho → barra de progresso estrutural → lista numerada)

### Superfície 3 — Vínculo de percurso no painel de stats da página de trilha *(novo 2026-06-08)*

A página da trilha (`base-trilha.html`) recebe a mesma entrada no painel de stats do hero, ao lado de Artigos/Tempo de leitura:

> **FAZ PARTE DO PERCURSO**
> 📖 Dominando o Moodle ›

- Posição: `.hero-stat.hero-stat--percurso`, entre "Tempo de leitura" e "Compartilhar"
- Cor: idêntica à do artigo — `--verde-profundo`, com ícone + chevron; modo escuro em `--verde-claro`
- Condicional: só aparece quando a trilha integra ≥1 percurso. Trilhas autônomas (T4–T9) não exibem

### Superfície 4 — Página de listagem `/percursos`

- Grid de 3 colunas (responsivo)
- Cada card: borda lateral verde escura de 4px, kicker mini em verde escuro ("Percurso"), H4 do nome, descrição curta (1-2 linhas), footer com `N trilhas · M artigos · ~Xh`. Candidatos da V2 ("Em breve") usam estilo neutro/inativo, sem o verde reservado
- Diferenciação visual clara entre percursos e listagens de artigos/categorias (que ficam sóbrias)

**Impacto:**
- Documentar as **4 superfícies** na Camada 4.5 (Padrões de Composição)
- Implementar o **verde escuro** (`--verde-profundo`) como cor reservada do percurso no design tokens da Fase 2 (o dourado foi descartado para essa função — ver revisão 2026-06-02 acima)
- Vínculo de percurso implementado no meta do artigo (`base-artigo.html`) e no stats da trilha (`base-trilha.html`); listagem `/percursos` em `base-percursos.html` — todos 2026-06-08

---

## Decisão 32 — Remoção dos botões prev/next no rodapé do artigo

**O que decidir:** O `prototipo-artigo.html` tinha cards prev/next de navegação na trilha no rodapé do artigo (componente `.trilha-nav` com `.trilha-nav-card.prev` e `.trilha-nav-card.next`). Esses cards permanecem na nova arquitetura multi-trilha?

🔵 **Contexto:** O componente prev/next assumia uma única trilha por artigo. Com a Decisão 18 (artigo em múltiplas trilhas) e a Decisão 30 (acordeão multi-trilha na sidebar), prev/next no rodapé fica ambíguo — *próximo de qual trilha?* — e redundante com a lista numerada do acordeão expandido.

**Resolução (2026-05-19):** ✅ **APROVADO**

- **Remover** o componente `.trilha-nav` e seus cards `.trilha-nav-card.prev` / `.trilha-nav-card.next` do rodapé do artigo.
- Remover também os estilos CSS associados.
- A navegação entre artigos da trilha passa a ser feita **exclusivamente pelo acordeão multi-trilha na sidebar** (Decisão 30) — onde o leitor vê a lista numerada completa de cada trilha e pode pular para qualquer artigo, não apenas o adjacente.

**Razões:**
- **Sem ambiguidade:** com múltiplas trilhas possíveis, prev/next forçaria escolher uma — provavelmente a "principal", o que reintroduziria a complexidade rejeitada na Decisão 30 (opção B descartada).
- **Sem redundância:** o acordeão já mostra a lista numerada com o artigo atual destacado. Próximo/anterior estão visualmente acessíveis ali.
- **Rodapé mais limpo:** o rodapé fica só com artigos relacionados, feedback, ABNT — alinhando à Decisão 24, agora simplificada.

**Impacto:**
- Atualizar Decisão 24 (rodapé): remover linha sobre box de trilha com prev/next. Rodapé fica: Artigos relacionados → Feedback → ABNT.
- Atualizar o `prototipo-artigo.html` removendo HTML e CSS do componente.
- Documentar na Camada 4.5: "Navegação entre artigos da trilha é responsabilidade exclusiva do acordeão multi-trilha na sidebar."

---

## Decisão 33 — Breadcrumb taxonômico (espelha a URL, não a jornada)

**O que decidir:** O breadcrumb do artigo deve mostrar o caminho de **classificação** (Categoria) ou o caminho de **jornada editorial** (Percurso › Trilha)?

🔵 **Contexto:** O protótipo `base-artigo.html` exibia `Início › Percursos › Dominando o Moodle › Do Livro de Notas… › Configurando o livro de notas` — o caminho de *uma* jornada. Isso conflita com (a) a natureza many-to-many da trilha (Decisões 18, 30 — artigo pode estar em várias trilhas, por isso existe o acordeão); (b) a neutralidade editorial do artigo (Decisão 26); (c) o vínculo **estrutural, não comportamental** — sem referrer (Decisões 28, 29), ou seja, o sistema não sabe por qual jornada o leitor chegou; e (d) não bate com a URL `/{categoria}/{slug}` (taxonomia §8).

**Resolução (2026-06-02):** ✅ **APROVADO** (sessão Elton + Claude) — ⏳ mesma validação pedagógica pendente das Decisões 25-32 (Rute + Marquito)

> **Reconciliação 2026-06-02 com a Decisão 34:** como a categoria saiu da URL do artigo (URL plana), o breadcrumb deixa de "espelhar a string da URL" e passa a **refletir a árvore de classificação** (`Início → Categoria → Artigo`), onde cada ancestral é uma **página real**. A categoria continua no breadcrumb mesmo não estando na URL.

- O breadcrumb **reflete a árvore de classificação** — `Início › {Categoria} › {Título}` — nunca a jornada editorial.
- Cada ancestral do breadcrumb é uma página navegável: `{Categoria}` linka para a página-índice `/{categoria}/`.
- Trilha e Percurso continuam comunicados **apenas na casca** (acordeão de trilha na sidebar + páginas dedicadas), nunca no breadcrumb.
- Regra única e ensinável: *um breadcrumb = um caminho de containment estável e de pai único*. A única camada que satisfaz isso é a **Categoria** (Eixo 2, "onde está?").

**Razões:**
- **Estabilidade:** pai único e fixo, ao contrário da trilha (0..n pais).
- **SEO/GEO:** `Schema.org/BreadcrumbList` (Pilar 11) entrega a hierarquia `Início › Categoria › Artigo` ao buscador — compensando a categoria ausente da URL plana (Decisão 34).
- **Não-fabricação:** não inventa um histórico de navegação que a V1 não rastreia (Decisões 28, 29).

**Impacto:**
- Corrigir o breadcrumb do `base-artigo.html` (**deferido** — apenas documentado nesta sessão; correção dos protótipos não foi executada).
- **Restaurar a Categoria visível** no cabeçalho/breadcrumb: o comentário em `base-artigo.html:1315` a removeu do painel de meta supondo que ela vivia no breadcrumb — mas não vivia (o breadcrumb mostrava a trilha). A Categoria ficou ausente das duas pontas.
- Implica a existência de uma **página-índice de categoria** `/{categoria}/` como destino do segmento intermediário.
- Fonte canônica da IA: novo documento `stages/01-fundacoes/output/arquitetura-informacao.md`.

---

## Decisão 34 — URL plana do artigo (categoria fora da URL)

**O que decidir:** A URL do artigo inclui a categoria (`/{categoria}/{slug}`, como propunha a taxonomia §8) ou é plana?

🔵 **Contexto:** A `taxonomia.md` §8 propunha `/{categoria}/{slug}` com o princípio "categoria sustenta a URL", e havia rejeitado a variante sem categoria. Elton decidiu (2026-06-02) tirar a categoria da URL. A §8 deixava em aberto justamente o "versionamento de URL ao mudar artigo de categoria" — que a URL plana resolve.

**Resolução (2026-06-02):** ✅ **APROVADO** (direção de Elton) — ✅ **co-aprovado por Marcos em 2026-06-10**, condicionado ao plano de redirects abaixo

- URL do artigo é **plana, na raiz:** `/{artigo-slug}` (ex.: `/configurar-livro-de-notas`). **Sem categoria, sem prefixo `/artigos/`.**
- A **categoria continua existindo** como classificação e navegação — página-índice `/{categoria}/` e breadcrumb (Decisão 33) —, mas **não compõe o permalink**.
- **Slugs reservados:** como artigo e página-índice de categoria convivem na raiz, os 6 slugs de categoria + `trilhas`, `percursos`, `topicos`, `buscar` (e demais seções de topo) são reservados — nenhum artigo pode usá-los. Validação no save.

**Razões:**
- **Recategorizar nunca quebra o link** — a categoria não está no permalink. Resolve a pergunta aberta da taxonomia §8.
- **URL curta.**

**Trade-off assumido:** perde-se o sinal de categoria na URL para SEO/GEO — recuperado em parte pelo `Schema.org/BreadcrumbList` (Decisão 33).

> **⚠️ Adendo 2026-06-10 — Co-aprovação de Marcos condicionada ao plano de redirects das URLs legadas.** As URLs antigas dos 139 artigos seguem o padrão `conhecimento.cefor.ifes.edu.br/base/{slug}/` (inventário em `data/base-antiga/`) — nenhum esquema novo (plano ou com categoria) as preserva, então a mitigação é por redirect 301, já prevista na taxonomia §8 para a Fase 5. A URL plana até **simplifica** o redirect: vira uma regra genérica única, sem tabela artigo-a-artigo de categorias. Plano acordado:
> 1. **Fase E (carga):** gravar o slug legado de cada artigo como post meta (ex.: `_cgte_slug_legado`) — o WXR traz `<link>` e `<wp:post_name>`.
> 2. **Regra genérica 301:** `^/base/(.+)$` → `/$1` (`.htaccess` ou hook `template_redirect`) — cobre todo artigo que preservar o slug.
> 3. **Fallback por meta:** artigos renomeados (Fase 4; ex.: o slug numérico legado `/base/2141/`) são resolvidos por busca no meta `_cgte_slug_legado` + 301 — renomear nunca quebra o link antigo.
> 4. **Colisão de namespace:** as URLs legadas `/percursos/{slug}/` usam "percurso" no conceito antigo (agrupamento de navegação) e colidem com o namespace novo `/percursos/` — exigem **mapa manual** (poucos casos) apontando para a categoria/tópico novo equivalente.
> 5. **QA de lançamento (Fase 5):** script percorre o inventário completo de URLs antigas e confere `301 → 200`.
>
> Premissa: a nova base assume o mesmo domínio no lançamento; se o domínio mudar, os redirects vivem no host antigo.

**Impacto:**
- Atualizar `taxonomia.md` §8 (padrão de URL, princípios, exemplos, pergunta aberta resolvida) e §2/§4 (categoria não "sustenta URL").
- Atualizar `arquitetura-informacao.md` (sitemap, tabela de URLs, regra de breadcrumb).
- Implementação WP: post type de artigo com permalink na raiz + guarda de slugs reservados.
- **Plano de redirects** (adendo 2026-06-10): meta de slug legado na Fase E · regra `/base/*` + fallback por meta na Fase 3/5 · mapa manual dos `/percursos/*` legados · QA de 301 na Fase 5.

---

## Decisão 35 — Faixa de leitura centralizada (layout do artigo)

**O que decidir:** O layout do artigo usa uma coluna de texto **elástica** (`1fr`, que estica além da medida de leitura) ou uma **faixa de largura fixa centralizada**?

🔵 **Contexto:** O `base-artigo.html` usava `grid-template-columns: minmax(0,1fr) 300px`, dando à coluna do texto ~852px enquanto o texto era travado em `max-width: 700px` e alinhado à esquerda. Sobravam ~152px de vazio morto *dentro* da coluna, somados ao gap de 64px → um "buraco" de ~216px entre o fim do texto e a sidebar. O cabeçalho usava grade diferente (`1fr / 220px / gap 56`), deixando a régua do meta ~80px fora do eixo do índice abaixo. Resultado: desalinhamento entre título e corpo + vão visual desconfortável.

**Resolução (2026-06-02):** ✅ **APROVADO** (direção de Elton) — refinamento de implementação do DS (Fase 2).

- O artigo passa a usar uma **faixa de leitura centralizada**: texto + sidebar formam um bloco único de largura fixa, centralizado via `justify-content: center`. A sobra de largura vira **margem simétrica** nas bordas — não um vão entre as colunas.
- Medidas em tokens CSS de eixo único (mude `--measure` e tudo acompanha):

  | Token | Valor | Papel |
  |---|---|---|
  | `--measure` | `660px` | coluna de texto (~70–75 caracteres) |
  | `--rail` | `300px` | sidebar / índice |
  | `--band-gap` | `72px` | gutter entre texto e sidebar |

- Cabeçalho (`.masthead-inner`), corpo (`.shell`), barra de ações (`.article-actions`) e painel de Libras (`.libras-accordion`) compartilham **o mesmo eixo** — alinhados à esquerda na borda do texto/título e à direita na borda da sidebar.
- A medida de leitura caiu de **700px → 660px** (mais perto da faixa ideal de 65–75 caracteres).

**Razões:**
- **Elimina o vão** entre texto e sidebar sem precisar engordar nem "puxar" a sidebar (o que desequilibraria a direita).
- **Alinha** cabeçalho e corpo no mesmo eixo vertical (régua do meta sobre o card do índice).
- **Leiturabilidade preservada:** a coluna nunca estica além da medida confortável.

**Impacto:**
- `base-artigo.html` atualizado (tokens `--measure`/`--rail`/`--band-gap`/`--reading-band`; `.shell`, `.masthead-inner`, `.prose`, `.article-actions`, `.libras-accordion`).
- `output/design.md` §Layout atualizado com as medidas e o padrão.
- **Não será propagado** aos demais protótipos de página (`base-trilha`, `base-percurso`, `base-inicio-v5`) — decisão de Elton (2026-06-02). A faixa de leitura aplica-se especificamente ao layout do artigo; o tema WordPress (Fase 3) é o ponto de consolidação dos tokens.
- Fase 3 (WordPress): replicar os tokens da faixa no tema.

---

## Decisão 36 — Ampliação do Eixo 3: 25 → 31 tópicos (cobertura do acervo real)

**O que decidir:** O vocabulário fechado de 25 tópicos cobre o acervo real? O mapeamento artigo-a-artigo da Fase G (2026-06-10) deixou **70 dos 129 artigos classificados abaixo da cardinalidade mínima de 2 tópicos** — não por preguiça de curadoria, mas porque assuntos reais do acervo não tinham termo: guias de atividades sem tópico próprio (Wiki, Glossário, Escolha, Página, Pasta…), ferramentas externas (Canva, Padlet, PowToon…), gamificação (emblemas, Level Up, barra de progresso), comunicação (mensagens, webconferência como interação, netiqueta), produção de material didático e procedimentos institucionais (diploma digital, contas, processos MOOC).

**Resolução (2026-06-10):** ✅ **APLICADO como proposta** (direção de Marcos; validação pedagógica formal Elton + Rute pendente, mesma régua das Decisões 25–32) — **+6 tópicos**, total **31**:

| Tópico novo | Grupo | Artigos reais cobertos |
|---|---|---|
| `Atividades e Recursos` | Recursos Moodle | ~24 (guias de referência das atividades/recursos e operações do dia a dia) |
| `Produção de Conteúdo` | Pedagogia | ~23 (mídias, objetos educacionais, gravação de tela, H5P, templates) |
| `Comunicação e Interação` | Gestão do AVA | ~10 (mensagens, fóruns, webconferências, netiqueta) |
| `Ferramentas Externas` | Ferramentas externas *(grupo novo)* | ~10 (Canva, Padlet, PowToon, Medium, Captura…) |
| `Procedimentos Institucionais` | Conduta | ~8 (diploma digital, contas, sistema acadêmico, processos MOOC) |
| `Gamificação e Engajamento` | Gestão do AVA | ~7 (emblemas, Level Up, barra de progresso, conclusão) |

**Critérios aplicados (anti-cauda-longa):**
- Cada tópico novo cobre **≥7 artigos reais** do acervo carregado (a regra antiga eliminou tags de uso ≤2 — nenhum tópico novo recai nisso).
- Ortogonais aos 25 existentes: complementam, não duplicam (ex.: `Atividades e Recursos` convive com `Tarefa`/`Fórum` — o específico quando existe, o geral para o guia).
- Assuntos de **apenas 2 artigos** (ex.: aplicativo Moodle Mobile) **não** ganharam tópico — receberam a melhor combinação dos existentes.

**Impacto (sincronização obrigatória — regra do §5 da taxonomia):**
- `taxonomia.md` §5 (v1.5) · `contentsystem.md` §B.3 (v1.2) · `vocabulario-controlado.json` → `topicos_controlados` (v1.2, com definições e sinônimos).
- Plugin `cgte-estrutura`: `data/topicos.php` 25→31 + semeadura re-executada.
- Fase G reaplicada: déficit de cardinalidade zerado nos 129 artigos classificados.

---

## Decisões ainda em aberto — Refinamento 2026-05-19

| Tema | Pergunta em aberto | Onde será fechado |
|---|---|---|
| **Limite editorial de trilhas por artigo** | A partir de quantas trilhas um artigo vira "ruído"? | Camada 5 (Rubrica) ou Camada 10 (Métricas) — proposta inicial: 1-3 ideal, 4-5 amarelo, 6+ vermelho |
| **Validação com Rute e Marquito** | As Decisões 25-32 foram tomadas em sessão entre Elton e Claude. Precisam de validação formal da equipe pedagógica antes de virar fonte canônica definitiva. | Reunião de validação a marcar |

---

## Resumo final — todas as decisões

| # | Decisão | Status | Resumo da resolução |
|---|---|---|---|
| 1 | Propósito-farol | 🔧 Ajustado | Consulta + aprendizagem e atualização contínua (não formação estruturada) |
| 2 | Segmentação por perfil | 🔧 Ajustado | Existe na categorização interna; **sem navegação por perfil na home** |
| 3 | TL;DR obrigatório | ❌ Rejeitado | Não entra na V1; reavaliar na Fase 5 com dados |
| 4 | Tempo de leitura + índice + progresso | ✅ Aprovado | Índice sticky com scroll-tracking sempre visível |
| 5 | Tipos de callout | 🔧 Ajustado | Mantidos como conceito; tipos definidos pelo Content Design (Fase 1), cores pelo DS (Fase 2) |
| 6 | Tipografia editorial | 🔧 Ajustado | **100% sans-serif** (rejeita direção serifada nos títulos) |
| 7 | Fundo e identidade visual | ❌ Rejeitado | Fundo **branco**; verde IFES não obrigatoriamente principal; cards menos delimitados |
| 8 | Modo escuro | ✅ Aprovado | Implementado via CSS custom properties desde o dia 1 |
| 9 | Trilhas pedagógicas | 🔧 Ajustado | Trilhas existem na V1; local no artigo deferido para Fase 2; **artigos relacionados obrigatórios ao final** |
| 10 | Pacote de acessibilidade | ✅ Aprovado | Pacote completo conforme proposto (VLibras, A-/A+, contraste, dislexia, atalhos) |
| 11 | Busca | ✅ Aprovado | Modal Ctrl+K, full-text, filtros e atalhos visíveis; IA fica para V2 |
| 12 | Feedback do leitor | 🔧 Ajustado | **"Foi útil" / "Não foi útil"** em texto (sem emojis); resto da recomendação mantido |
| 13 | Conteúdo multimodal | 🔧 Ajustado (ampliado) | **Sem abas desktop/mobile.** Adicionados: Libras em accordion, audiodescrição visível, áudio do artigo, podcast, infográficos-resumo |
| 14 | Metadados obrigatórios | 🔧 Ajustado | **Autor obrigatório e exibido**. Sem versão do Moodle, sem revisor pedagógico, sem última revisão na interface |
| 15 | Escopo negativo V1 | ✅ Aprovado | Tudo confirmado fora da V1 |
| 16 | Subtítulo obrigatório *(adendo Fase 1)* | ✅ Aprovado | **Todo artigo tem um subtítulo abaixo do H1** |
| **17** | **Taxonomia em 4 eixos** *(Fase 1 — 2026-05-14)* | ✅ **Aprovado** | Tipo (1) + Categoria (1) + Tópico (2-4) + Trilha (0+). Tags livres abolidas. 20 categorias → 6. |
| **18** | **Nova arquitetura Trilha/Percurso** *(Fase 1 — 2026-05-14)* | 🔧 **Ajustado** | Trilha = jornada atômica de artigos. Percurso = conjunto de trilhas. Um artigo pode estar em múltiplas trilhas. |
| **19** | **Ordem dos blocos multimodais** *(Fase 1 — 2026-05-14)* | ✅ **Aprovado** | **1. Libras · 2. Ouvir · 3. Outros formatos** |
| **20** | **Formato da citação ABNT** *(Fase 1 — 2026-05-14)* | ✅ **Aprovado** | `SOBRENOME, Nome. Título. Base de Conhecimento CEFOR/Ifes, [ano]. Revisado em [data].` |
| **21** | **Política de depreciação** *(Fase 1 — 2026-05-14)* | 🔧 **Ajustado** | **12 meses** (não 6); badge visível **apenas para admins**, não público |
| **22** | **prototipo-artigo.html como referência** *(Fase 1 — 2026-05-14)* | ✅ **Aprovado** | `stages/02-design-system/drafts/prototipos-paginas/prototipo-artigo.html` é a referência canônica da interface |
| **23** | **Cabeçalho do artigo** *(Fase 1 — 2026-05-14)* | ✅ **Aprovado** | Categoria · Tipo → H1 → Subtítulo → Autor + Tempo → Multimodal → Índice |
| **24** | **Rodapé do artigo** *(Fase 1 — 2026-05-14)* | ✅ **Aprovado** | Artigos relacionados → Feedback → ABNT → Box de trilha (se aplicável) |
| **25** | **Tamanho da trilha** *(Fase 1 — 2026-05-19)* | ✅ **Aprovado** | Mínimo 3 artigos. **Sem máximo.** Alerta de saúde acima de ~10 (revisão pedagógica) |
| **26** | **Artigo-âncora em múltiplas trilhas** *(Fase 1 — 2026-05-19)* | ✅ **Aprovado** | Permitido. Artigo é **editorialmente neutro** quanto à trilha — não anuncia a sequência. Voz da sequência vive na casca (box + página de trilha) |
| **27** | **Percurso é apenas agregação** *(Fase 1 — 2026-05-19)* | ✅ **Aprovado** | **Sem certificado, sem badge, sem rastreamento.** Categoria classifica; percurso narra |
| **28** | **Box de trilha sempre visível** *(Fase 1 — 2026-05-19)* | ✅ **Aprovado** | Vínculo **estrutural** (CMS), não comportamental (referrer). Aparece sempre que o artigo pertence a uma trilha |
| **29** | **V1 sem rastreamento de progresso pessoal** *(Fase 1 — 2026-05-19)* | ✅ **Aprovado** | Mostrar apenas **posição estrutural** ("Artigo X de Y"). Sem localStorage. Progresso pessoal fica para V2 com login |
| **30** | **Apresentação de múltiplas trilhas: acordeão** *(Fase 1 — 2026-05-19)* | ✅ **Aprovado** | Box "Trilhas deste artigo" usa **acordeão (A.2)**. Posição "X/Y" visível mesmo colapsado. Primeira expandida por padrão. Múltiplas abertas simultaneamente permitidas |
| **31** | **Apresentação visual do percurso** *(Fase 1 — 2026-05-19; cor revisada 2026-06-02; superfícies revisadas 2026-06-08)* | ✅ **Aprovado** | **Verde escuro (`--verde-profundo`) é a cor reservada do percurso** — dourado abandonado em 2026-06-02. **4 superfícies:** página dedicada (hero + stats + "como percorrer" + cards de trilhas) · vínculo "Faz parte do percurso" no **meta do artigo** · idem no **stats da página de trilha** · listagem `/percursos` (grid com borda verde escura). O chip dentro do acordeão de trilha foi **removido em 2026-06-08** — o vínculo migrou para meta/stats. Referências: `base-percurso.html`, `base-percursos.html`, `base-artigo.html`, `base-trilha.html` |
| **32** | **Remoção do prev/next do rodapé do artigo** *(Fase 1 — 2026-05-19)* | ✅ **Aprovado** | Cards `.trilha-nav-card.prev/next` **removidos.** Navegação entre artigos da trilha passa a ser exclusiva do acordeão multi-trilha na sidebar |
| **33** | **Breadcrumb taxonômico** *(Fase 1 — 2026-06-02)* | ✅ **Aprovado** | Breadcrumb reflete a **árvore de classificação** (`Início › Categoria › Artigo`), cada ancestral é página real; nunca a jornada. Trilha/percurso só na casca. Fonte: `arquitetura-informacao.md` |
| **34** | **URL plana do artigo** *(Fase 1 — 2026-06-02; co-aprovada por Marcos em 2026-06-10)* | ✅ **Aprovado** | Categoria **sai da URL**. Artigo = `/{slug}` na raiz (sem categoria, sem `/artigos/`), com slugs reservados. Categoria fica só em breadcrumb + página-índice. Recategorizar não quebra o link. Co-aprovação condicionada ao **plano de redirects 301** das URLs legadas `/base/{slug}` (adendo 2026-06-10) |
| **35** | **Faixa de leitura centralizada** *(Fase 2 — 2026-06-02)* | ✅ **Aprovado** | Texto + sidebar = bloco fixo centralizado; sobra vira margem simétrica (sem vão). Tokens `--measure: 660px` / `--rail: 300px` / `--band-gap: 72px`, eixo único para cabeçalho, corpo, ações e Libras. Medida 700 → 660px |

---

## Próximos passos — estado atual da Fase 1

A **Fase 0 está oficialmente concluída**. A **Fase 1 — Fundações** está em andamento.

### O que já foi validado (2026-05-14)

- ✅ Taxonomia em 4 eixos (Decisão 17)
- ✅ Arquitetura Trilha/Percurso (Decisão 18)
- ✅ Interface do artigo — cabeçalho, blocos multimodais, rodapé (Decisões 19-24)
- ✅ Protótipo `prototipo-artigo.html` referendado como referência canônica

### Refinamentos da arquitetura Trilha/Percurso (2026-05-19)

- ✅ Tamanho da trilha definido — mín 3, sem máx (Decisão 25)
- ✅ Artigo-âncora pode servir múltiplas trilhas, mantendo neutralidade editorial (Decisão 26)
- ✅ Percurso é apenas agregação curada, sem progresso/certificado (Decisão 27)
- ✅ Box de trilha sempre visível por vínculo estrutural (Decisão 28)
- ✅ V1 sem rastreamento pessoal — apenas posição estrutural (Decisão 29)
- ✅ Apresentação de múltiplas trilhas: **acordeão** escolhido (Decisão 30 — referência `drafts/exploracao-multiplas-trilhas.html`)
- ✅ Apresentação visual do percurso: verde escuro (`--verde-profundo`) como cor reservada — dourado abandonado em 2026-06-02 —, **4 superfícies** após revisão de 2026-06-08 (página dedicada · meta do artigo · stats da trilha · listagem `/percursos`); chip do acordeão removido (Decisão 31 — referências `base-percurso.html`, `base-percursos.html`, `base-artigo.html`, `base-trilha.html`)
- ✅ Prev/next no rodapé do artigo: **removido** (Decisão 32 — navegação fica exclusivamente no acordeão)
- ⏳ Validação das Decisões 25-32 com Rute e Marquito (foram tomadas em sessão Elton + Claude)

### O que falta na Fase 1 (sprints pendentes)

| Sprint | Entregas | Com quem |
|---|---|---|
| Sprint 1 | Camadas 1-3 do Content System (Princípios, Voz/Tom, Vocabulário Controlado) | Elton + Rute + Juliana |
| Sprint 2 | Camadas 4-7 (Padrões, Rubrica de Qualidade, Legibilidade, Modelos Mentais) | Elton + Rute + Juliana |
| Sprint 3 | Taxonomia formal + URLs semânticas + Estratégia de busca | Elton + Marquito |
| Sprint 4 | Camadas 8-10 (Depreciação, ContentOps, Métricas) + Revisão final | Elton + Marquito |

> **Nota:** Rute quer participar ativamente das Camadas 1-7 (especialmente Rubrica de Qualidade e Modelos Mentais). Ela está pesquisando qualidade de conteúdo educacional e vê sinergia direta com o que foi mostrado.

### Refinamentos pendentes no protótipo (prioridade antes da Fase 2)

| Item | O que fazer |
|---|---|
| Box de trilha | Fechar ao rolar (com cuidado para não travar se usuário rola dentro do box). Nome da trilha em destaque. |
| Navegação prev/next | Contexto claro de "estou na trilha X, artigo Y de Z" — não apenas dois botões soltos |
| Botão compartilhar | Explorar menu com opção de share formatado (WhatsApp com mensagem + link). Manter no topo também. |
| Terminologia | Na trilha: "artigos". No percurso: "passos". Não usar "passo" para itens de trilha. |

### Decisões deferidas ainda abertas

| Origem | O que falta decidir | Onde será fechado |
|---|---|---|
| Decisão 5 | Tipos exatos de callout/destaque | Camada 4 — Biblioteca de Padrões |
| Decisão 17 | Nome e definição da 6ª categoria (se necessária) | Sprint 3 — Taxonomia formal |

> Decisão 9 (local exato de exibição da trilha no artigo) — **fechada pela Decisão 28**: sidebar do artigo, sempre presente quando aplicável.
> Decisão 28 *(apresentação multi-trilha)* — **fechada pela Decisão 30**: acordeão (sub-opção A.2).
> Decisão 31 *(apresentação do percurso)* — **fechada na sessão 2026-05-19**: ver descrição completa acima.

---

*Documento criado em: 2026-05-07*
*Sessões de decisão: 2026-05-08 · 2026-05-13 · 2026-05-14 · 2026-05-19*
*Participantes: Elton Vinicius, Juliana Cassaro, Marcos Vinícius Forecchi Accioly (Marquito), Rutinelli Fávero (Rute)*
*Projeto: Base de Conhecimento CEFOR/Ifes — Reformulação*
