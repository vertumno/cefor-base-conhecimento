# Decisões de Consolidação — Fase 0 → Fase 1

> **Versão:** 1.0
> **Data:** 2026-05-07
> **Para validação de:** Elton + Marcos (+ Juliana e Rute quando aplicável)
> **Fontes cruzadas:**
> - 🟢 Reunião de brainstorm (01/04/2026) — Elton, Marquito, Rute, Juliana
> - 🔵 Pesquisa de benchmarking — Juliana (7 sites analisados com 5 óculos)
> - 🟠 Relatório comparativo — Claude (análise consolidada de 7 sites)

---

## Como usar este documento

Cada decisão abaixo tem:
1. **O que decidir** — a pergunta
2. **O que a reunião disse** — posição da equipe no brainstorm
3. **O que a pesquisa mostrou** — evidências do benchmarking e relatório
4. **Recomendação** — proposta baseada nas evidências
5. **Campo de decisão** — para a equipe marcar `[ ] Aprovado` / `[ ] Ajustado: ...`

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

**Decisão:** `[ ] Aprovado` / `[ ] Ajustado: _______________`

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

**Decisão:** `[ ] Aprovado` / `[ ] Ajustado: _______________`

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

**Decisão:** `[ ] Aprovado` / `[ ] Ajustado: _______________`

---

## Decisão 4 — Tempo de leitura e índice de seções

**O que decidir:** Exibir tempo estimado de leitura e índice "Neste artigo" nos artigos?

🟠 **Relatório:** 43% dos sites mostram tempo de leitura (Medium, Coursera, Claude Blog). 71% oferecem índice de seções. Combinado com o TL;DR, esse trio é a **Prioridade 1** do relatório.

**Recomendação:**

- **Tempo de leitura:** Sim, abaixo do título. Cálculo: 200 palavras/minuto em português.
- **Índice "Neste artigo":** Sim, para artigos com 4+ seções. Bloco visível abaixo do H1, com links âncora. Modelo Canva.
- **Barra de progresso de leitura:** Sim, barra fina (2-3px) no topo, cor institucional.

Custo de implementação mínimo, impacto alto.

**Decisão:** `[ ] Aprovado` / `[ ] Ajustado: _______________`

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

**Decisão:** `[ ] Aprovado` / `[ ] Ajustado: _______________`

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

**Decisão:** `[ ] Aprovado` / `[ ] Ajustado: _______________`

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

**Decisão:** `[ ] Aprovado` / `[ ] Ajustado: _______________`

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

**Decisão:** `[ ] Aprovado` / `[ ] Ajustado: _______________`

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

**Decisão:** `[ ] Aprovado` / `[ ] Ajustado: _______________`

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

**Decisão:** `[ ] Aprovado` / `[ ] Ajustado: _______________`

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

**Decisão:** `[ ] Aprovado` / `[ ] Ajustado: _______________`

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

**Decisão:** `[ ] Aprovado` / `[ ] Ajustado: _______________`

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

**Decisão:** `[ ] Aprovado` / `[ ] Ajustado: _______________`

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

**Decisão:** `[ ] Aprovado` / `[ ] Ajustado: _______________`

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

**Decisão:** `[ ] Aprovado` / `[ ] Ajustado: _______________`

---

## Resumo para ação rápida

Abaixo, todas as decisões num formato para marcar rapidamente:

```
DECISÕES DE CONSOLIDAÇÃO — FASE 0 → FASE 1
Data: ___/___/2026
Presentes: _______________________________

[ ] 1.  Propósito-farol (autonomia + formação)
[ ] 2.  Segmentação por perfil (3-4 perfis na home)
[ ] 3.  TL;DR obrigatório (>3 min de leitura)
[ ] 4.  Tempo de leitura + índice + barra de progresso
[ ] 5.  4 tipos de callout (Info, Dica, Atenção, Importante)
[ ] 6.  Tipografia editorial (serifada + sans-serif)
[ ] 7.  Fundo neutro (#f7f7f5) + cards brancos
[ ] 8.  Modo escuro (CSS variables desde o dia 1)
[ ] 9.  Trilhas simplificadas (curadoria, sem tracking)
[ ] 10. Pacote acessibilidade completo (VLibras, A-/A+, contraste, dislexia)
[ ] 11. Busca textual com modal (Ctrl+K), IA na V2
[ ] 12. Feedback emoji + copiar link/seção/ABNT + reportar erro
[ ] 13. Multimodal: texto + abas desktop/mobile, TTS se viável
[ ] 14. Metadados obrigatórios (autor, revisor, data, tipo, IA)
[ ] 15. Escopo negativo V1 confirmado (chatbot, gamificação, wiki = V2+)

Aprovado por: _________________ Data: ___/___/2026
```

---

## Próximo passo após aprovação

Com as 15 decisões tomadas, a **Fase 0 está oficialmente concluída** e a equipe entra na **Fase 1 — Fundações**:

1. **Sprint 1:** Camadas 1-3 do Content System (Princípios, Voz/Tom, Vocabulário Controlado)
2. **Sprint 2:** Camadas 4-7 (Padrões, Rubrica, Legibilidade, Modelos Mentais)
3. **Sprint 3:** Taxonomia + Descoberta
4. **Em paralelo:** Juliana inicia inventário/triagem dos ~60 artigos existentes

---

*Documento criado em: 2026-05-07*
*Projeto: Base de Conhecimento CEFOR/IFes — Reformulação*
*Fontes: Ata da reunião 1 (01/04/2026), Pesquisa de benchmarking (Juliana), Relatório comparativo (Claude)*
