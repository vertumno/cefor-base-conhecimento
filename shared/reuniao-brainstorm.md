# Análise — Reunião 1: Brainstorm Base de Conhecimento CEFOR

> **Analista:** Atlas (Analyst Agent) | **Data da reunião:** 01/04/2026 | **Duração:** 94 min
> **Data da análise:** 03/04/2026

---

## 1. Contexto e Participantes

| Participante | Papel | Contribuição Principal |
|---|---|---|
| **Elton Vinicius** | Tech Lead / CGTE | Facilitação, visão técnica, overview da base atual |
| **Marcos Vinicius F. Accioly** ("Marquito") | Produto/Tech / CGTE | Ideação intensa, gestão de tempo, próximos passos |
| **Juliana Cristina da S. Cassaro** ("Ju") | Conteudista/Pedagógica | Inventário de artigos, visão de acessibilidade multimodal |
| **Rutinelli da Penha Fávero** ("Rute") | Gestão/Pedagógica (remota, Portugal) | Visão formativa, percursos, chatbot, certificação |

**Motivador urgente:** O servidor atual precisa ser desligado — a base WordPress está tão desatualizada que não recebe mais patches de segurança. A TI já disponibilizou servidor novo. Prazo: **abril/2026**.

---

## 2. Diagnóstico da Base Atual

### Estrutura Existente
- Home com busca funcional
- 12 percursos temáticos
- 60+ artigos (tutoriais, institucionais, ferramentas/GPTs, conceituais)
- Plataforma: WordPress (versão obsoleta, sem atualizações de segurança)

### Problemas Identificados (via análise prévia com IA)
| Problema | Impacto |
|---|---|
| Thumbnails genéricas nos percursos | Baixa atratividade visual |
| Títulos inconsistentes (mix de formatos) | Confusão na navegação |
| Datas misturadas/invisíveis | Usuário não sabe se conteúdo está atualizado |
| Artigos velhos ao lado de novos sem marcação | Perda de confiança no conteúdo |
| Lista sem filtros, paginação ou busca interna | Dificuldade de encontrar conteúdo |
| Metadados invisíveis (sem autor, tempo de leitura, nível, versão) | Falta de contexto para o leitor |
| Percursos pouco visíveis dentro do artigo | Usuário ignora a navegação temática |

### Pontos Fortes
- Conteúdo bem escrito, pedagógico e claro
- Templates de GPTs padronizados e de qualidade
- Percursos como conceito de curadoria temática — boa ideia validada
- Busca funcional na home

### Trabalho em Andamento (Juliana)
- Inventário completo dos artigos (planilha de controle)
- Classificação: deletar / atualizar por terceiros / atualizar pessoalmente
- Alguns artigos já atualizados diretamente na base
- Tutoriais de IA atualizados (mudança do Moodle)
- Bloqueada: base fora do ar desde semana anterior à reunião

---

## 3. Propósito-Farol da Base

> **"O local no qual eu posso enviar para alguém e aquela pessoa vai conseguir fazer e resolver o problema dela sem que eu tenha que resgatar todas as coisas para poder resolver."** — Marcos, resgatando a motivação original

**Propósito ratificado pela equipe:** A base é um **instrumento de formação em serviço** — não apenas repositório de consulta, mas um espaço onde o profissional **aprende fazendo**, com autonomia.

**Público-alvo:** Profissionais que atuam na educação a distância ou uso de tecnologias educacionais no IFES (mediadores, professores, coordenadores).

---

## 4. Mapa de Ideias do Brainstorm

### 4.1 Percurso Formativo por Perfil (Rute)
- **Conceito:** Ao entrar na base, o usuário se identifica ("Sou mediadora", "Sou professor") e recebe percursos personalizados
- **Mecanismo:** Perfil → percursos relacionados → artigos → links para Moodle/cursos → formação contínua
- **Valor:** A base deixa de ser consulta passiva e vira **jornada de aprendizagem**

### 4.2 Chatbot/Tutor com IA Generativa (Rute + Marcos)
- Evoluir a Sofia (chatbot existente) para tutor com IA generativa
- Funções: responder perguntas, sugerir percursos, gerar quizzes/avaliações
- **Restrição conhecida:** Custos de API de IA generativa
- Sofia já funciona e é portável (serviço externo, funciona ao importar salas)

### 4.3 Conteúdo Multimodal (Juliana)
- Artigos disponíveis em **múltiplos formatos**: texto, áudio, vídeo, passo-a-passo
- Atender diferentes estilos de aprendizagem e necessidades do momento
- Exemplo: "Não posso ver vídeo agora, quero só o passo-a-passo em texto"
- **Audioartigos**: conteúdo narrado (text-to-speech) para consumo em movimento

### 4.4 Colaboração e Co-criação Wiki (Marcos)
- Permitir contribuições de usuários (com moderação)
- Sistema de destaques/estrelas em trechos específicos (como Kindle compartilhado)
- Comentários em partes específicas do artigo
- Feed de atividade: "X pessoas destacaram este trecho"
- **Sem login:** destaques e estrelas anônimas
- **Com login:** comentários, contribuições, perfil de autor
- Inspiração: modelo Wikipedia com hierarquia de editores e gamificação

### 4.5 Experiências Exitosas / Vitrine de Boas Práticas (Marcos + Elton)
- Capturar inovações dos professores nas salas de aula (virtual e presencial)
- "Aprenda com Rutinelli" — seções com práticas reais de professores
- Selo/chancela do CEFOR para práticas destacadas
- Conexão com eventos (ex.: Concefor) para premiar e coletar práticas
- Histórias emocionantes da sala de aula → narrativas, podcasts, áudios

### 4.6 Ferramentas Interativas na Base (Marcos)
- Não ser só artigos — ter **mini-ferramentas** embutidas
- Exemplo: correlacionar Taxonomia de Bloom com recursos educacionais
- Planejador de sala virtual ("quero uma sala mais interativa" → sugestões)
- Flashcards gerados a partir dos artigos (estilo Duolingo/Anki)
- Flashcards com áudio para estudo em movimento
- "Construir coisas" na base, não só ler

### 4.7 Trilhas Menores + Certificação (Rute)
- Trilhas = micro-percursos dentro de um percurso maior
- Ex.: "Quero aprender só a aplicar padrão visual no meu curso" → trilhazinha
- Ao completar trilha → quiz/avaliação gerada por IA → mini-certificado
- **Sonho declarado**, mas alinhado com a visão de formação em serviço

### 4.8 Gamificação e Premiação (Marcos + Juliana + Rute)
- Prêmio anual "Destaque Conhecimento" para maiores contribuidores
- Plaquinhas/badges (estilo influenciadores)
- Wallpapers com selo de contribuidor
- Ranking de leitores, marcadores, contribuidores
- Incentivo para participação ativa na base

### 4.9 Integração com Ecossistema CEFOR (Juliana + Marcos)
- Links para cursos Moodle dentro dos percursos (não só artigos)
- Possibilidade de hospedar conteúdo didático dos professores (livros interativos)
- Embedar conteúdo da base dentro do Moodle (como H5P)
- Integração com Instagram do CEFOR (gerar conteúdo para redes sociais a partir da base)

### 4.10 Metadados e Autoria (todos)
- **Obrigatório:** autor, data de última atualização, versão, licença
- Indicação "Produzido com IA" quando aplicável
- Múltiplos autores por artigo
- Autores cadastrados na base (com perfil)
- Citação ABNT automática (copiar referência formatada)
- **Legislação de IA (PL aprovado):** responsabilização exige autoria clara

### 4.11 Facilitação da Produção de Conteúdo (Marcos)
- Facilitar criação para a equipe CGTE, não só para o usuário final
- Fluxo: e-mail com resposta útil → transformar em artigo na base
- IA acelera produção, mas olhar humano valida
- Linha editorial e critérios de publicação necessários

---

## 5. Decisões e Consensos

| # | Decisão | Status |
|---|---|---|
| 1 | Migração é urgente — não continuar atualizando artigos na base velha | **Consenso** |
| 2 | Propósito-farol: resolver problemas com autonomia + formação em serviço | **Consenso** |
| 3 | Público: profissionais de EaD/tecnologias educacionais no IFES | **Consenso** |
| 4 | Percursos por perfil são prioridade de experiência | **Consenso** |
| 5 | Conteúdo multimodal (texto + áudio + vídeo + passo-a-passo) | **Consenso** |
| 6 | Autoria obrigatória (compliance com legislação de IA) | **Consenso** |
| 7 | Sempre puxar para aplicabilidade prática (quando possível, não como regra absoluta) | **Consenso com ressalva** (Marcos: "sempre é palavra forte") |
| 8 | Contribuições externas de professores = passo 2, segundo semestre 2026 | **Consenso** |
| 9 | Plataforma: WordPress (nova instalação) | **Implícito** (ref. linha 418) |

---

## 6. Próximos Passos Declarados na Reunião

| # | Ação | Responsável | Prazo |
|---|---|---|---|
| 1 | Organizar transcrição e ideias do brainstorm | Elton | ~1 semana |
| 2 | Criar plano + proposta de estrutura da nova base | Elton + Marcos | ~1 semana |
| 3 | Desenhar interface/layouts com IA (home, artigo, percurso) | Elton + Juliana | Após plano |
| 4 | Validar layouts com a equipe | Todos | Após design |
| 5 | Implementar no WordPress novo e experimentar | Elton + Marcos | Abril/2026 |
| 6 | Importar conteúdo existente para nova base | Elton + Marcos | Abril/2026 |
| 7 | Organizar tarefas no board CGTE (projeto "Base de Conhecimento 2026") | Marcos | Imediato |
| 8 | Resgatar documento "Modelo de orientações para produção de artigos" | Rute + Juliana | Imediato |

**Referências externas mencionadas:**
- Planilha de inventário de artigos (Juliana)
- Documento Google Docs: orientações para artigos (`11_Ef5s6fbAKmXWggRUAaq-SmHWzauqtjysgVObDSjZo`)
- Texto de padrão de artigos enviado por Rute aos professores
- Board CGTE: tarefas #7685 (atualização artigos), #7804 (interface), #7809 (projeto)

---

## 7. Análise Estratégica — Atlas

### Tensão Central
A equipe sonha com uma **plataforma de aprendizagem social gamificada** mas precisa entregar uma **migração funcional em abril**. O risco é paralisia por ambição.

### Camadas de Implementação Sugeridas

| Camada | Escopo | Horizonte |
|---|---|---|
| **V1 — Migração** | WordPress novo, artigos migrados, metadados visíveis (autor, data, versão), percursos reorganizados, busca com filtros, layout moderno, responsivo | Abril 2026 |
| **V1.5 — Quick Wins** | Áudio TTS nos artigos, citação ABNT automática, compartilhar link fácil, indicação "produzido com IA", percursos por perfil (mediador/professor) | Maio 2026 |
| **V2 — Interatividade** | Chatbot com IA (evolução Sofia), flashcards, ferramentas interativas embutidas, login de usuário, trilhas com progresso | S2 2026 |
| **V3 — Comunidade** | Contribuições de professores, gamificação, destaques/estrelas, experiências exitosas, prêmio anual, integração Instagram/Moodle | 2027 |

### Riscos Identificados

| Risco | Probabilidade | Mitigação |
|---|---|---|
| Escopo da V1 crescer além da migração | Alta | Definir MVP rígido com critérios de "done" |
| Custo de IA generativa para chatbot | Média | Avaliar modelos open-source (Llama, Mistral) ou limitar uso |
| Baixa adoção da colaboração wiki | Média | Gamificação + eventos (Concefor) como motor de engajamento |
| Juliana bloqueada sem base para editar | Alta (já ocorrendo) | Priorizar ambiente de staging na nova base |
| Falta de linha editorial formal | Média | Formalizar antes de abrir contribuições externas |

### Insights Não-Óbvios

1. **"Cérebro do CEFOR"** (expressão da Rute) — a base não é um site, é a **memória institucional viva**. Essa metáfora pode guiar toda a arquitetura de informação e até o branding.

2. **O maior ativo não são os artigos — são as práticas dos 80+ profissionais** do grupo MTE. A base hoje captura ~0% dessa inteligência tácita. O ROI maior está em criar um fluxo de captura leve (entrevista → texto → áudio → base).

3. **A Sofia funciona onde importa** — já é portável entre salas Moodle. Isso é uma vantagem técnica subestimada para escalar o chatbot.

4. **A legislação de IA brasileira (PL aprovado)** cria uma obrigação legal de autoria que pode ser transformada em feature: "Todo conteúdo tem um humano responsável" como diferencial de confiança.

5. **Flashcards + áudio = formação assíncrona mobile** — isso resolve um problema real de professores que não têm tempo de sentar para ler, mas poderiam estudar no carro/transporte.

---

## 8. Perguntas Abertas (para próxima reunião)

1. **WordPress ou plataforma diferente?** A ambição (gamificação, perfis, flashcards, ferramentas) pode ultrapassar o que WordPress oferece nativamente. Avaliar: Docusaurus, GitBook, plataforma custom, ou WordPress + plugins específicos?
2. **Autenticação:** SSO com sistema IFES existente? Cadastro próprio? Ambos?
3. **Orçamento para IA generativa:** Existe verba? Quanto? Isso define se chatbot é V1.5 ou V3.
4. **Governança de conteúdo:** Quem aprova artigos de terceiros? Qual o fluxo editorial?
5. **Métricas de sucesso:** Como medir se a nova base está cumprindo o propósito-farol?
6. **Integração Moodle:** Qual nível de integração técnica é viável (embed, LTI, API)?

---

*— Atlas, investigando a verdade 🔎*
