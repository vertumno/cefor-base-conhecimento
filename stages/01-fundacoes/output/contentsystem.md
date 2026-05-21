# Content System — Base de Conhecimento CEFOR/IFes

> **Documento mestre consolidado.** Reúne as 10+ camadas do Content System em um único lugar e deriva delas a especificação acionável para a implementação no WordPress (Fase 3).
>
> **Versão:** 1.0 — DRAFT consolidado
> **Última atualização:** 2026-05-21
> **Autoria:** Elton Vinicius + Claude
> **Fontes canônicas:**
> - `_config/decisoes.md` (32 decisões formais)
> - `stages/01-fundacoes/output/principios-editoriais.md` (Camada 1)
> - `stages/01-fundacoes/output/vocabulario-controlado.json` (Camada 3)
> - `stages/01-fundacoes/output/padroes-composicao.md` (Camada 4.5)
> - `stages/01-fundacoes/references/content-system-escopo.md` (escopo das 10 camadas)
> - `stages/01-fundacoes/drafts/prototipo-artigo.html` (interface canônica do artigo)

---

## Como ler este documento

Ele tem **duas partes**:

| Parte | O que é | Para quem |
|---|---|---|
| **Parte A — Governança Editorial** | As 10+ camadas do Content System: princípios, voz, vocabulário, padrões, qualidade, legibilidade, modelos mentais, depreciação, operação, métricas. Responde *"como o conteúdo é escrito, organizado, avaliado e mantido"*. | Equipe editorial (Elton, Rute, Juliana, Marquito), IA de produção |
| **Parte B — Spec WordPress** | A tradução acionável da Parte A em configuração técnica: Custom Post Types, Custom Fields, taxonomias, blocos, estados, URLs e checklist de aceitação. Responde *"o que precisa existir no WordPress"*. | Implementação (Fase 3), tema e plugins |

> A Parte B **deriva** da Parte A. Quando uma decisão editorial mudar na Parte A, a Parte B deve ser revisada.

---

## Status das camadas

| Camada | Nome | Status | Onde está a versão completa |
|---|---|---|---|
| 1 | Princípios Editoriais | ✅ Formalizada (DRAFT, pendente Rute) | `output/principios-editoriais.md` |
| 2 | Voz e Tom | 🟡 DRAFT neste doc — **pendente Rute** | aqui (§A.2) |
| 3 | Vocabulário Controlado | 🟡 Parcial (6/12 seções — Eixos 2 e 3 fechados) | `output/vocabulario-controlado.json` |
| 4 | Biblioteca de Padrões de Conteúdo | 🟡 DRAFT neste doc — **pendente Rute** (callouts) | aqui (§A.4) |
| 4.5 | Padrões de Composição | ✅ Formalizada (DRAFT, pendente Rute) | `output/padroes-composicao.md` |
| 5 | Rubrica de Qualidade | 🟡 DRAFT neste doc — **pendente Rute** | aqui (§A.5) |
| 6 | Padrões de Legibilidade | 🟡 DRAFT neste doc — **pendente Rute** | aqui (§A.6) |
| 7 | Modelos Mentais do Público | 🟡 DRAFT neste doc — **pendente Rute** | aqui (§A.7) |
| 8 | Política de Depreciação | 🟡 DRAFT neste doc | aqui (§A.8) |
| 9 | ContentOps | 🟡 DRAFT neste doc | aqui (§A.9) |
| 10 | Métricas de Sucesso | 🟡 DRAFT neste doc — opera na Fase 5 | aqui (§A.10) |

> **Legenda de pendência:** as camadas marcadas **"pendente Rute"** derivam de decisões já registradas, mas a orientação pedagógica (Rute Fávero) ainda não validou o conjunto fechado. Não são fonte canônica definitiva até essa validação.

---

## Hierarquia de autoridade

Em conflito entre dois artefatos, prevalece o de cima:

```
1. Princípios Editoriais (Camada 1)
2. Decisões formais (_config/decisoes.md)
3. Padrões de Composição (Camada 4.5)
4. Demais camadas
```

---
---

# PARTE A — GOVERNANÇA EDITORIAL

---

## A.1 — Princípios Editoriais (Camada 1)

> **Versão completa:** `output/principios-editoriais.md`. Resumo abaixo.

### O que a Base É / NÃO é

**É:** fonte oficial do CEFOR/IFes sobre uso pedagógico e técnico do Moodle institucional · espaço de consulta + aprendizagem + atualização contínua · editorialmente curada (revisão humana sempre) · acessível por padrão · atualizada (depreciação ativa).

**NÃO é:** repositório de PDFs · blog de notícias · réplica do manual do Moodle · espaço de opinião pessoal · enciclopédia completa · plataforma de cursos formais (sem matrícula/certificado/frequência) · sistema de gamificação (sem badges/ranking/progresso pessoal).

### Os 9 princípios (3 famílias)

**A — Arquitetura editorial**
1. **O artigo é a unidade soberana.** Trilha e percurso envelopam, nunca alteram, o artigo.
2. **Autossuficiente E encadeável.** Resolve sozinho E encaixa em qualquer trilha sem reescrita.

**B — Qualidade do conteúdo**
3. **Se o leitor precisa perguntar depois de ler, o artigo falhou.** Autonomia é critério de qualidade.
4. **Ensinamos fazendo, não explicando.** Conceito tem aplicação; prática tem contexto.
5. **Acessível não é simples — é claro.** Não simplificar a ponto de perder precisão.
6. **Honestidade técnica antes de afeto.** Não prometer o que não há mecanismo para entregar.

**C — Operação editorial**
7. **Conteúdo tem prazo de validade.** Todo artigo nasce com revisão programada.
8. **IA acelera, humano valida.** Nenhum conteúdo de IA publica sem revisão humana.
9. **Menos artigos excelentes > muitos medianos.** Qualidade sobre volume.

### Hierarquia em conflito

`1 → 2 → 6 → 3 → 5 → 4 → 9 → 7 → 8` (arquiteturais quebram menos; operacionais cedem primeiro).

**Consequência para o WordPress:** os princípios 1, 2 e 6 são a justificativa de toda a arquitetura Artigo/Trilha/Percurso da Parte B — a "voz da sequência" vive na casca (componentes de trilha/percurso), nunca no corpo do artigo.

---

## A.2 — Voz e Tom (Camada 2) · 🟡 DRAFT — pendente Rute

A voz é **uma só** (constante). O tom **varia** conforme o contexto do leitor e o tipo de artigo.

### A.2.1 — A voz (constante)

| Atributo | É | Não é |
|---|---|---|
| Tom geral | Colega experiente que explica com paciência | Professor na frente da sala |
| Registro | Semiformal — profissional mas acessível | Informal (gírias) nem burocrático (juridiquês) |
| Postura | Orientadora — conduz, não impõe | Impositiva ("você deve") nem passiva ("talvez considere") |
| Relação com o leitor | Respeita a inteligência, não assume ignorância | Condescendente ("é muito fácil, basta...") |
| Carga emocional | Institucional, sem emojis na UI nem no conteúdo (Decisão 12) | Lúdica/emocional |

### A.2.2 — Tom por contexto do leitor

| O leitor está... | Tom adequado | Exemplo de abertura |
|---|---|---|
| Perdido | Acolhedor, orientador | "Vamos por partes. Primeiro, entenda o que é [conceito]..." |
| Com pressa | Direto, sem rodeios | "Para [ação]: Acesse [caminho] > Clique em [botão]." |
| Diante de um erro | Empático, sem julgamento | "Esse erro acontece quando [causa]. Para resolver..." |
| Explorando | Inspirador, mostra caminhos | "O Moodle permite [possibilidade]. Veja como..." |
| Estudando o conceito | Didático, com analogias | "Pense em [analogia]. Na prática do Moodle..." |
| Reconsultando | Objetivo, formato de referência | Tabela ou lista, sem introdução longa |

### A.2.3 — Tom por tipo de artigo

Alinhado aos 5 tipos do Eixo 1 (ver §A.3 e vocabulário):

| Tipo de artigo | Tom predominante | Proporção instrução/contexto |
|---|---|---|
| Tutorial | Guia prático — "faça isso" | 70 / 30 |
| Conceitual | Professor — "entenda por quê" | 40 / 60 |
| Referência | Consulta — "aqui está" | 90 / 10 |
| Solução de Problema | Técnico empático — "resolva isso" | 80 / 20 |
| Recurso | Facilitador — "use isso como base" | 50 template / 30 instrução / 20 contexto |

> **Pendente Rute:** validar a voz e coletar 2-3 exemplos reais de cada tom em artigos do CEFOR. **Pendente decisão de origem formal** — esta camada ainda não tem decisão registrada em `decisoes.md`.

---

## A.3 — Vocabulário Controlado (Camada 3) · 🟡 Parcial (4/10 categorias)

> **Versão completa e consultável:** `output/vocabulario-controlado.json` (JSON estruturado, consumido por IA, busca e linter).

**Regra de ouro:** quando o termo do Moodle e o pedagógico divergem, usar o termo do Moodle na primeira menção (é o que aparece na interface) **seguido do pedagógico entre parênteses**. Ex.: *"Configure o Questionário (a ferramenta de avaliação com correção automática do Moodle)"*.

**Schema de cada termo:** `termo_preferido`, `sinonimos_aceitos`, `sinonimos_rejeitados`, `definicao`, `contexto_uso`, `termo_moodle`, `termo_mec`, `termo_popular`, `ver_tambem`, `decisao_origem`, `status`.

| Categoria | Status |
|---|---|
| `arquitetura_cefor` (Base, Artigo, Trilha, Percurso, Passo, Artigo-âncora, Encadeabilidade, Autossuficiência) | ✅ Completa |
| `tipos_de_artigo` (Tutorial, Referência, Conceitual, Solução de Problema, Recurso) | ✅ Completa |
| `eixos_da_taxonomia` (Tipo, Categoria, Tópico, Trilha) | ✅ Completa |
| `componentes_ui_da_base` (Box de trilha, Chip de percurso, Acordeão multi-trilha, Checkpoint, Posição estrutural) | ✅ Completa |
| `atividades_moodle` | 🟡 1 termo de exemplo (Questionário) — **pendente Juliana + Rute** |
| `recursos_moodle` | ⏳ Estrutura criada — **pendente** |
| `papeis` | ⏳ **pendente Rute + Juliana** (identidade profissional) |
| `conceitos_pedagogicos` | ⏳ **pendente Rute** |
| `conceitos_tecnicos` | ⏳ **pendente Elton** |
| `vocabulario_natural_do_publico` | ⏳ Documento vivo — **pendente Juliana + Rute** |

**Consumo no WordPress (ver Parte B):** cada termo com `sinonimos_rejeitados` não-vazio vira regra do linter; `sinonimos_aceitos` + `termo_popular` alimentam o índice de busca interna.

---

## A.4 — Biblioteca de Padrões de Conteúdo (Camada 4) · 🟡 DRAFT — pendente Rute

Padrões de **estrutura narrativa dentro do artigo** (a Camada 4.5 cuida da composição *entre* artigos). São blocos reutilizáveis que autores (humanos e IA) aplicam conforme o tipo de informação.

### A.4.1 — Catálogo de padrões narrativos

| Padrão | Quando usar | Estrutura | Armadilha |
|---|---|---|---|
| **Passo a Passo com Checkpoint** | Tutoriais com 5+ passos | Passos numerados; a cada 3-4, um checkpoint verificável ("você deve ver X na tela") | Checkpoint vago — precisa ser verificável visualmente |
| **Problema → Diagnóstico → Solução** | Solução de Problema | Sintoma → Causa provável → Solução → Prevenção | Pular o diagnóstico e ir direto à solução |
| **Quando Usar / Quando NÃO Usar** | Ferramentas com alternativas | Tabela cenário → ferramenta → porquê; "use quando..." / "NÃO use quando..." | Listar só vantagens; o "quando NÃO" é o diferencial |
| **Analogia do Mundo Real** | Conceitos abstratos/técnicos | Analogia → mapeamento explícito → onde a analogia para de funcionar | Analogia imprecisa; sempre declarar limites |
| **Antes/Depois** | Configurações que mudam visual/comportamento | "antes" → o que mudar → "depois" | Screenshots sem contexto; indicar onde olhar |
| **FAQ Invertido** | Seções de perguntas frequentes | Ordenar pela pergunta mais **comum**, não pela mais básica | Ordenar pela lógica do autor, não da urgência do leitor |
| **Resumo Executivo + Profundidade Progressiva** | Conceituais/guias longos | Visão geral → detalhamento por seção → referências | Resumo que é introdução, não conclusão |

> **Nota sobre TL;DR:** o bloco "Em resumo" rotulado e obrigatório foi **rejeitado na V1** (Decisão 3). O padrão "Resumo Executivo" acima é opcional e usa visão geral em prosa, não um TL;DR rotulado.

### A.4.2 — Tipos de callout / destaque editorial · ⏳ Decisão 5 pendente

A Decisão 5 manteve o conceito de destaques editoriais mas **não fechou os tipos**. Lista preliminar (a confirmar nesta camada, com cores vindas do Design System na Fase 2):

| Tipo candidato | Função |
|---|---|
| Informação | Contexto adicional, nota explicativa |
| Dica | Atalho, boa prática |
| Atenção | Cuidado, reversível |
| Importante | Ação irreversível, impacto alto |
| Frase de efeito / citação | Destaque editorial não-utilitário (mencionado na Decisão 5) |
| Resumo de seção | Síntese intermediária |

> **Pendente:** definir o conjunto fechado de tipos de callout (Decisão 5) e os componentes multimodais editoriais (bloco Libras, audiodescrição, infográfico-resumo, áudio/podcast) — ver §A.4.3.

### A.4.3 — Componentes multimodais (Decisão 13, 19)

Componentes editoriais previstos no template (consequência da Decisão 13). **Ordem obrigatória dos blocos de formato alternativo no topo (Decisão 19):**

1. **Libras** — tradução em Libras do texto completo do artigo, em accordion (recolhível). Não é o widget VLibras genérico.
2. **Ouvir** — narração em áudio do artigo (TTS via Web Speech API ou áudio gravado).
3. **Outros formatos** — podcast (produção dedicada), infográfico-resumo (quando existir).

Outros componentes multimodais:
- **Audiodescrição de imagem visível** — campo descritivo da imagem **visível para todos**, não só no `alt`. Legenda opcional adicional.
- **Vídeo embutido** (passo a passo) onde existir.
- **Infográfico/imagem-resumo** — opcional por artigo, para sintetizar conceitos.

> **Removido (Decisão 13):** abas "Computador / Mobile" — o site é responsivo; diferenças por dispositivo viram variação editorial no mesmo texto.

### A.4.4 — Como usar os padrões

1. Identifique o **tipo de artigo** (Eixo 1). 2. Consulte os padrões recomendados para o tipo. 3. Combine padrões quando necessário. 4. (Opcional) registre os padrões usados nos metadados para auditoria/IA.

> **Pendente Rute:** validação pedagógica dos padrões e fechamento dos tipos de callout (Decisão 5).

---

## A.4.5 — Padrões de Composição (Camada 4.5)

> **Versão completa:** `output/padroes-composicao.md`. Resumo abaixo — esta é a camada estrutural mais consequente para o WordPress.

### Regra-mãe

> **O artigo é a unidade soberana. Trilha e percurso são camadas de curadoria que envelopam, nunca alteram, o artigo.**

A voz da sequência ("próximo passo", "você está na metade") vive na casca (box de trilha, página de trilha, página de percurso), nunca no conteúdo do artigo.

### Checklist de Encadeabilidade (10 critérios; 5 automatizáveis)

| # | Critério | Auto? |
|---|---|---|
| 1 | Título sem número de ordem nem "Parte X" | ✅ |
| 2 | Sem expressões de posição relativa ("como vimos antes", "no próximo artigo") | ✅ |
| 3 | Tem seção explícita de pré-requisitos no topo | ✅ |
| 4 | Pré-requisitos linkados, não pressupostos | Parcial |
| 5 | Tem seção de "o que você sabe ao fim" | ✅ |
| 6 | Próximos passos são lista plural (≥2 ou nenhum) | ✅ |
| 7 | Exemplos autocontidos | Manual |
| 8 | Screenshots com contexto próprio (legenda) | Manual |
| 9 | Vocabulário definido na primeira ocorrência local | Manual |
| 10 | Teste do artigo solto (faz sentido sem o box de trilha) | Manual |

### Catálogo de padrões de composição

| Padrão | O que é |
|---|---|
| **4.1 Artigo encadeável** | Estrutura mínima: Cabeçalho → Entrada (pré-req + objetivo) → Miolo → Saída (o que sabe + próximos passos plurais) → Rodapé |
| **4.2 Box de trilha multi-trilha** | Acordeão na sidebar; aparece sempre que o artigo pertence a ≥1 trilha; "Artigo X de Y" estrutural |
| **4.3 Chip de atribuição a percurso** | Chip dourado no topo da trilha expandida, leva à página do percurso |
| **4.4 Página de trilha** | Hero verde + stats com CTA "Começar pelo primeiro" + lista ordenada de artigos + resultado esperado |
| **4.4.1 Item de artigo na lista da trilha** | Número em círculo, card com tipo/tempo, stream vertical, checkpoints opcionais |
| **4.5 Página de percurso** | Hero dourado + stats sem progresso + "como percorrer" (3 rotas por perfil) + cards de trilha |
| **4.6 Card de trilha em percurso** | Borda verde, mostra os 5 primeiros artigos |
| **4.7 Card de percurso em listagem** | Borda dourada de 4px em `/percursos` |

### Cardinalidade e cores reservadas

- **Trilha:** mín 3 artigos, sem máximo (alerta de saúde >10). **Verde IFES** (`--accent`).
- **Artigo em trilhas:** 0 a N (alerta amarelo em 4-5, vermelho em ≥6).
- **Percurso:** agregação de trilhas + artigos soltos; sem ordem fixa. **Dourado** (`--gold`).
- **Categoria/Tópico:** neutros — classificam, não narram.

---

## A.5 — Rubrica de Qualidade (Camada 5) · 🟡 DRAFT — pendente Rute

Transforma "esse artigo é bom" em avaliação objetiva. Usada na revisão de artigos novos, na triagem da base antiga e como meta de qualidade para produção com IA.

### A.5.1 — As 7 dimensões e pesos

| # | Dimensão | Peso | O que avalia |
|---|---|---|---|
| 1 | Acionabilidade | 20% | O leitor consegue fazer o que o artigo propõe? |
| 2 | Escaneabilidade | 15% | Dá para achar a informação sem ler tudo? |
| 3 | Precisão técnica | 20% | A informação está correta e verificável? |
| 4 | Completude | 15% | Cobre o caminho feliz E os erros comuns? |
| 5 | Clareza textual | 15% | A linguagem é acessível ao público? |
| 6 | Conformidade estrutural | 10% | Segue o modelo do tipo de artigo + Checklist de Encadeabilidade? |
| 7 | Frescor | 5% | Está atualizado com a versão atual do sistema? |

> **Integração com a Camada 4.5:** o Checklist de Encadeabilidade (10 critérios) entra como parte da dimensão **Conformidade estrutural** (ou como dimensão "Atomicidade" dedicada — a decidir com Rute).

### A.5.2 — Escala (1 a 5)

1 Inadequado · 2 Insuficiente · 3 Aceitável · 4 Bom · 5 Excelente (referência/modelo).

### A.5.3 — Regras de publicação (score médio ponderado)

| Score | Decisão |
|---|---|
| < 2.5 | Não publica — reescrita necessária |
| 2.5 – 3.4 | Publica com badge "em melhoria" + revisão em 30 dias |
| 3.5 – 4.4 | Publica normalmente |
| ≥ 4.5 | Publica como artigo de referência (modelo para IA e novos autores) |

### A.5.4 — Triagem da base antiga (~60 artigos)

| Score | Ação |
|---|---|
| < 2.0 | Descartar ou reescrever do zero |
| 2.0 – 3.0 | Reescrever substancialmente |
| 3.0 – 3.5 | Atualizar e reformatar |
| > 3.5 | Migrar com ajustes menores |

> **Pendente Rute:** validar dimensões/pesos, decidir se "Atomicidade" vira dimensão própria, e **testar a rubrica em 2-3 artigos reais** (critério de auditoria da Fase 1). Limite editorial de trilhas por artigo (1-3 ideal / 4-5 amarelo / 6+ vermelho) pode ancorar aqui ou na Camada 10.

---

## A.6 — Padrões de Legibilidade (Camada 6) · 🟡 DRAFT — pendente Rute

Métricas objetivas e testáveis — o equivalente ao contraste WCAG, mas para o texto.

### A.6.1 — Métricas e limites por tipo

| Métrica | Tutorial | Conceitual | Referência | Como medir |
|---|---|---|---|---|
| Palavras por frase (média) | ≤ 20 | ≤ 25 | ≤ 15 | Contador automático |
| Frases por parágrafo (máx) | 4 | 5 | 3 | Linter |
| Flesch adaptado PT-BR | ≥ 50 | ≥ 40 | ≥ 60 | Ferramenta Flesch |
| Jargão não explicado por seção (máx) | 2 | 3 | 1 | Cruzamento com Vocabulário Controlado |
| Voz passiva (máx por artigo) | 15% | 20% | 10% | Linter |
| Parágrafos sem heading (máx consecutivos) | 3 | 4 | 2 | Estrutural |

### A.6.2 — Regras de ouro

1. Uma ideia por parágrafo. 2. Primeira frase carrega o peso. 3. Instruções em voz ativa e imperativa ("Clique em Salvar"). 4. Números concretos, não adjetivos vagos ("cerca de 3 minutos", não "bem rápido"). 5. Termos técnicos explicados na primeira ocorrência.

### A.6.3 — Subtítulo (Decisão 16)

Todo artigo tem subtítulo obrigatório: uma frase, **10 a 25 palavras**, delimitando escopo/para quem serve. Posicionado abaixo do H1.

### A.6.4 — Verificação

Automática (linter pré-publicação + checklist nos prompts de IA) + manual (teste de leitura em voz alta — se o revisor tropeça, a frase está longa).

> **Pendente Rute:** validar os limites de Flesch e palavras/frase contra artigos reais do CEFOR (podem estar otimistas ou conservadores para o público real).

---

## A.7 — Modelos Mentais do Público (Camada 7) · 🟡 DRAFT — pendente Rute

Não é persona. É mapa de **como o público pensa, o que acredita saber e onde tropeça** — insumo direto para tom, estrutura e vocabulário.

### A.7.1 — Perfis mentais

| Perfil | O que acredita | Realidade | Consequência para o conteúdo |
|---|---|---|---|
| Professor que migrou do presencial | "Moodle é um Google Classroom complicado" | Paradigma diferente, mais poderoso | Analogias com o que já conhece; nunca dizer "é simples" |
| Mediador experiente | "Já sei mexer no Moodle" | Sabe o básico, não explora avançado | Artigos em camadas — básico valida, avançado expande |
| Coordenador de curso | "Não preciso saber técnico" | Precisa decidir com base pedagógica | "Quando Usar / Quando NÃO" > tutoriais |
| Professor novo no EaD | "Isso é difícil demais para mim" | A barreira é medo, não capacidade | Tom acolhedor obrigatório; checkpoints frequentes |
| Técnico de TI do campus | "Sei mais que a documentação" | Sabe o sistema, não o contexto pedagógico | Separar claramente o técnico do pedagógico |

### A.7.2 — Momentos de busca

| Momento | O que busca | Formato ideal |
|---|---|---|
| "Tenho que fazer isso agora" | Passo a passo direto | Tutorial |
| "Deu erro e não sei por quê" | Diagnóstico + solução | Solução de Problema |
| "Meu chefe mandou usar isso" | Justificativa + mínimo viável | "Por que importa" + quickstart |
| "Quero melhorar meu curso" | Inspiração + exemplos | Boas práticas + Antes/Depois |
| "Preciso ensinar para minha equipe" | Material compartilhável | Artigo autocontido + citação ABNT |
| "Já fiz, esqueci como" | Referência rápida | Consulta, sem introdução |

### A.7.3 — Vocabulário natural

Alimenta a categoria `vocabulario_natural_do_publico` (Camada 3) e a busca interna. Ex.: "minha sala" → curso/ambiente virtual; "postar atividade" → adicionar atividade; "abrir o Moodle" → acessar o AVA.

> **Pendente Rute + Juliana:** elas são as "antenas" do vocabulário real. Esta camada é documento vivo — termos novos entram conforme aparecem em atendimentos.

---

## A.8 — Política de Depreciação (Camada 8) · 🟡 DRAFT

Regras objetivas para quando e como o conteúdo envelhece. **Atualizada pela Decisão 21: prazo de 12 meses; badge visível apenas para administradores.**

### A.8.1 — Gatilhos de obsolescência

| Gatilho | Tipo | Ação |
|---|---|---|
| 12 meses sem revisão | Temporal | Marcar "Revisão pendente" (**badge só para admins** — Decisão 21) |
| Nova versão do Moodle lançada | Evento | Marcar tutoriais como "Verificar compatibilidade" |
| 0 acessos em 90 dias | Uso | Avaliar relevância (nicho legítimo vs. conteúdo morto) |
| Leitor reportou erro/desatualização | Feedback | Priorizar na fila de revisão |

### A.8.2 — Fluxo

```
Publicado
   ├─ [12 meses sem revisão] → "Revisão pendente" (badge interno, admin-only)
   │       ├─ Revisado → volta a "Publicado" (reset do timer)
   │       └─ Não revisado em +30 dias → avaliar depreciação
   ├─ "Depreciado"
   │       ├─ Tem substituto → Redirect 301 + banner "substituído por [link]"
   │       └─ Sem substituto → banner "será removido em [data]"
   └─ Após 90 dias depreciado → "Arquivado" (fora da navegação, acessível por URL direta)
```

> **Diferença da V0 do escopo:** o escopo original previa um badge público "possivelmente desatualizado". A Decisão 21 **removeu a visibilidade pública** — o leitor comum nunca vê conteúdo marcado como desatualizado; o badge é ferramenta interna de priorização.

### A.8.3 — O que NUNCA fazer

Deletar sem redirect · remover silenciosamente (instituição pública = transparência) · marcar desatualizado sem propor ação/prazo · depender de "alguém perceber".

> **Origem:** Decisões 14, 21. Princípio 7 (conteúdo tem prazo de validade).

---

## A.9 — ContentOps (Camada 9) · 🟡 DRAFT

Capacidade operacional real e processos que sustentam a produção contínua.

### A.9.1 — Capacidade (a validar com a equipe)

| Recurso | Capacidade estimada | Premissa |
|---|---|---|
| Juliana (produção + IA) | 4-6 artigos/mês | Outras responsabilidades no CEFOR |
| Rute (revisão pedagógica) | 6-8 revisões/mês | Disponibilidade parcial |
| IA (rascunho) | Ilimitada | Gargalo é a revisão, não a geração |
| Elton (revisão técnica + publicação) | 8-10 publicações/mês | Trabalho técnico paralelo |

**Gargalo real:** o elo mais lento é a revisão humana. Ritmo sustentável estimado: **4-6 artigos/mês**.

> **Ajuste pela Decisão 13:** os novos formatos (Libras, audiodescrição, narração, podcast, infográfico) **aumentam o custo de produção por artigo** — o ritmo pode reduzir para artigos com pacote multimodal completo.

### A.9.2 — Cadência de revisão obrigatória

| Tipo | Prazo máximo sem revisão |
|---|---|
| Tutorial | 6 meses (interfaces mudam) |
| Solução de Problema | 3 meses |
| Referência | 6 meses |
| Conceitual | 12 meses |
| Recurso / Boas práticas | 12 meses |

> A cadência por tipo é mais granular que o gatilho geral de 12 meses (§A.8). O gatilho de 12 meses é o piso; tipos voláteis têm prazo menor.

### A.9.3 — Fluxo de produção com IA

```
1. Juliana seleciona tema + tipo de artigo
2. Gera rascunho via prompt (Camada 4 + Vocabulário Controlado + Padrões de Composição)
3. Juliana revisa: estrutura, precisão, tom, completude
4. Rute revisa: adequação pedagógica, clareza, público
5. Elton revisa: precisão técnica, conformidade, metadados
6. Scorecard (Camada 5) — score ≥ 3.5? Não → volta ao passo 3
7. Checklist de Encadeabilidade (Camada 4.5) + linter (Camada 6)
8. Publicação + metadados + marcação "Produzido com assistência de IA"
```

### A.9.4 — SLA de demanda

Urgente (mudança no Moodle, erro crítico): publicar correção em 48h. Planejado: fila mensal, priorização impacto × esforço.

> **Origem:** Camada 9 do escopo + Princípios 8, 9. Sem decisão formal específica ainda — a validar.

---

## A.10 — Métricas de Sucesso (Camada 10) · 🟡 DRAFT — opera na Fase 5

Mede se o conteúdo cumpre o propósito-farol: o leitor resolve o problema dele com autonomia. **Só faz sentido quando há conteúdo publicado — implementada na Fase 3, operada na Fase 5.**

### A.10.1 — Métricas por nível

| Nível | Métrica | Fonte | Meta V1 |
|---|---|---|---|
| Utilidade | Taxa de chegada ao fim do tutorial | Scroll depth + tempo | > 60% leem até o fim |
| Clareza | Bounce rate por tipo | Analytics | < 40% em tutoriais |
| Confiança | Taxa de retorno à base | Analytics | > 30% em 30 dias |
| Cobertura | Buscas sem resultado / termos buscados | Log de busca | Lista mensal de gaps |
| Frescor | % de artigos revisados no prazo | Sistema de estados | > 90% |
| Satisfação | "Foi útil / Não foi útil" (Decisão 12) | Widget no rodapé | > 80% "Foi útil" |
| Eficiência | Horas por artigo publicado | Registro | < 8h/artigo (com IA) |
| **Saúde da composição** | Tamanho médio de trilha; nº de trilhas por artigo | Taxonomia/relações | Trilhas ≤ 10 art.; artigos em 1-3 trilhas |

### A.10.2 — Dashboard mensal

Artigos publicados/revisados no mês · score médio · % "revisão pendente" · top 5 buscas sem resultado · top 10 mais acessados · taxa "Foi útil" · próximas revisões obrigatórias · alertas de saúde de composição.

> **Feedback é "Foi útil / Não foi útil" em texto, sem emojis (Decisão 12).**

---
---

# PARTE B — SPEC WORDPRESS (ACIONÁVEL)

> Tradução da Parte A em configuração técnica para a Fase 3. Cada item aponta a decisão/camada de origem.
>
> **Status global:** DRAFT estrutural. Itens marcados ⏳ dependem de decisões ainda abertas (URLs semânticas, 6ª categoria, 25 tópicos, tipos de callout).

---

## B.1 — Modelo de dados: 3 Custom Post Types

| CPT | Slug | Representa | Decisão |
|---|---|---|---|
| **Artigo** | `artigo` | Unidade soberana de conteúdo | 17, 18 |
| **Trilha** | `trilha` | Micro-jornada ordenada de artigos | 18, 25 |
| **Percurso** | `percurso` | Agregação curada de trilhas + artigos soltos | 18, 27 |

**Relações (many-to-many, com ordem onde indicado):**

```
Percurso ──< contém (passos, sem ordem fixa) >── Trilha
Percurso ──< contém (artigos complementares) >── Artigo
Trilha   ──< contém (artigos, ORDEM IMPORTA) >── Artigo
Artigo   ──< pré-requisitos (links) >── Artigo
Artigo   ──< próximos passos (plural) >── Artigo
```

> Recomendação técnica: relações via plugin de relacionamento (ex.: ACF Relationship / Pods / JetEngine). A relação **Trilha→Artigo precisa de ordenação persistida** (a posição "Artigo X de Y" é estrutural — Decisão 29). A relação **Artigo→Trilha é derivada** (consulta reversa) — o box de trilha aparece por vínculo estrutural, sem referrer (Decisão 28).

---

## B.2 — Custom Fields do CPT `artigo`

| Campo | Tipo | Obrigatório | Origem | Observação |
|---|---|---|---|---|
| `subtitulo` | text | ✅ | Decisão 16 | 10-25 palavras; abaixo do H1 |
| `autores` | relationship (user/CPT autor), múltiplo | ✅ | Decisão 14 | Nome **exibido** na interface |
| `tempo_leitura` | number (min) | auto | Decisão 4 | 200 palavras/min PT-BR |
| `data_publicacao` | date | ✅ | Decisão 14 | Exibida |
| `data_revisao_interna` | date | ✅ | Decisão 14, 21 | **NÃO exibida no cabeçalho**; usada na ABNT e na depreciação |
| `produzido_com_ia` | boolean | — | Decisão 14, Princípio 8 | Marcação de compliance |
| `video_libras_url` | url | — | Decisão 13, 19 | Bloco Libras (accordion), 1º lugar |
| `audio_url` | url/media | — | Decisão 13, 19 | "Ouvir" — narração; 2º lugar |
| `podcast_url` | url | — | Decisão 13 | "Outros formatos" |
| `infografico` | media/url | — | Decisão 13 | Imagem-resumo opcional |
| `prerequisitos` | relationship (artigo) + texto livre | — | Camada 4.5 | Linkados, não pressupostos |
| `proximos_passos` | relationship (artigo), múltiplo | — | Camada 4.5 | Lista plural (≥2 ou nenhum) |

**Taxonomias (não custom fields — ver B.3):** `tipo`, `categoria`, `topico`.

**ABNT (gerada automaticamente — Decisão 20):**
`SOBRENOME, Nome. {título}. Base de Conhecimento CEFOR/IFes, {ano de data_publicacao}. Revisado em {data_revisao_interna}.`
Múltiplos autores seguem norma ABNT.

### Imagens dentro do conteúdo (bloco customizado)

| Campo da imagem | Origem | Observação |
|---|---|---|
| `alt` | acessibilidade | Padrão WCAG |
| `audiodescricao` | Decisão 13 | **Texto visível para todos**, não só no alt |
| `legenda` | Decisão 13 | Opcional |

---

## B.3 — Taxonomias (os 4 eixos — Decisão 17)

| Taxonomia | Eixo | Slug | Cardinalidade | Hierárquica? | Valores |
|---|---|---|---|---|---|
| **Tipo** | 1 | `tipo` | 1 por artigo | Não | Tutorial · Referência · Conceitual · Solução de Problema · Recurso |
| **Categoria** | 2 | `categoria` | 1 por artigo | Não | 6 valores (✅ fechados — 2026-05-21): Ferramentas e Recursos · Gestão e Operação do Moodle · Pedagogia e Planejamento · Acessibilidade · Conduta e Conformidade · Identidade |
| **Tópico** | 3 | `topico` | 2 a 4 por artigo | Não | ✅ 25 tópicos controlados (fechados — 2026-05-21). **Tags livres abolidas** |
| **Trilha** | 4 | (CPT `trilha`, não taxonomia) | 0 ou mais | — | Relação artigo↔trilha |

### As 6 categorias (Eixo 2) — com slug de URL

| Categoria | Slug | Domínio | Consolida (antigas) |
|---|---|---|---|
| Ferramentas e Recursos | `ferramentas` | Atividades/recursos Moodle (Questionário, Tarefa, Fórum, H5P, Rótulo, Webconf.) + ferramentas externas + GPTs | Recurso Educacional, Ferramentas de autoria/comunicação |
| **Gestão e Operação do Moodle** | `gestao-moodle` | Operação do AVA: config de curso, matrícula, notas/livro de notas, backup, navegação, Moodle Codes | AVA, Ambiente virtual, Moodle |
| Pedagogia e Planejamento | `pedagogia` | Planejamento, design educacional, fundamentos pedagógicos | Aspectos/Conhecimentos Pedagógicos, Tecnologias Educacionais |
| Acessibilidade | `acessibilidade` | Libras, audiodescrição, inclusão, desenho universal | (transversal antes) |
| Conduta e Conformidade | `conduta` | Direitos autorais, segurança, netiqueta, procedimentos | Direitos Autorais, Netiqueta, Segurança, Procedimentos |
| Identidade | `identidade` | Padrão visual, MOOC, ReLiCefor, templates institucionais | Padrão Visual, MOOC, Livros Digitais |

> **Por que "Moodle" não é categoria:** 60% do acervo (~78 artigos) era Moodle — uma categoria que abriga 60% não ajuda a navegar. O operacional de Moodle vai para *Gestão e Operação*; as atividades, para *Ferramentas e Recursos*; "avaliação" atravessa as duas e é unificada pelos **tópicos**.

### Os 25 tópicos (Eixo 3) — lista fechada

`Questionário · Banco de Questões · Tarefa · Fórum · Livro de Notas · H5P · Rótulo · Webconferência · Vídeo · Áudio e Podcast · Livro Digital · Configuração de Curso · Matrícula e Inscrição · Backup e Restauração · Moodle Codes · Sala Virtual · IA Generativa · GPT Customizado · Libras · Audiodescrição · Inclusão e Desenho Universal · Planejamento e Design Educacional · Padrão Visual · MOOC · Direitos Autorais e Segurança`

> Definições e sinônimos em `vocabulario-controlado.json` → `topicos_controlados`. "Prova" é sinônimo popular de *Questionário*, não tópico. Status `a_validar` — refinamento pedagógico fino pendente com Rute.

**Regras de validação no editor:**
- `tipo` e `categoria`: exatamente 1 (campo obrigatório, select único).
- `topico`: mínimo 2, máximo 4 (validação no save).
- `topico` **não permite digitação livre** — escolha entre os 25 termos controlados.

---

## B.4 — Custom Fields dos CPTs `trilha` e `percurso`

### `trilha`

| Campo | Tipo | Origem |
|---|---|---|
| `subtitulo` | text | Padrão 4.4 |
| `descricao_pedagogica` | wysiwyg (2-3 parágrafos) | Padrão 4.4 |
| `para_quem` / `o_que_vai_dominar` | text/lista | Padrão 4.4 |
| `prerequisitos` | relationship (artigo) + texto | Padrão 4.4 |
| `artigos` | relationship (artigo), **ordenado** | Decisão 18, 25, 29 |
| `checkpoints` | repeater (posição + texto curado) | Padrão 4.4.1 |
| `resultado_esperado` | wysiwyg | Padrão 4.4 |
| `como_foi_pensada` | text | Padrão 4.4 |
| `percursos` | relationship (percurso) — derivado | Decisão 31 |

> Validação: mínimo 3 artigos (bloqueante — Decisão 25). Alerta de saúde acima de 10 (não bloqueante).

### `percurso`

| Campo | Tipo | Origem |
|---|---|---|
| `subtitulo` | text | Padrão 4.5 |
| `descricao_pedagogica` | wysiwyg | Padrão 4.5 |
| `para_quem` / `o_que_vai_dominar` | text/lista | Padrão 4.5 |
| `como_percorrer` | repeater (3 rotas por perfil) | Decisão 31, Padrão 4.5 |
| `trilhas` | relationship (trilha) | Decisão 27 |
| `artigos_complementares` | relationship (artigo) | Decisão 27 |
| `curadoria` / `data_criacao` | text/date | Padrão 4.5 |

> **Sem campos de progresso/certificado/conclusão** (Decisões 27, 29).

---

## B.5 — Componentes/blocos do tema (Gutenberg + template)

### B.5.1 — Anatomia do artigo (Decisões 16, 19, 22, 23, 24, 32)

**Cabeçalho (template, ordem fixa):**
1. Categoria · Tipo (ex.: "Pedagogia e Planejamento · Tutorial")
2. Título (H1)
3. Subtítulo (obrigatório)
4. Autor + Tempo de leitura
5. Blocos multimodais — **ordem: Libras → Ouvir → Outros** (Decisão 19)
6. Índice "Neste artigo" — **sticky com scroll-tracking** (Decisão 4)

**Corpo:** miolo + blocos editoriais (callouts, checkpoint, infográfico, imagem com audiodescrição).

**Sidebar:** **Box de trilha multi-trilha** (acordeão) — aparece sempre que o artigo pertence a ≥1 trilha (Decisão 28, 30).

**Rodapé (ordem — Decisão 24, atualizada pela 32):**
1. Artigos relacionados (obrigatório em todos — Decisão 9)
2. "Foi útil / Não foi útil" + campo "O que faltou?" (Decisão 12)
3. Citação ABNT automática (Decisão 20)

> **Removido (Decisão 32):** botões prev/next da trilha no rodapé. Navegação entre artigos da trilha é **exclusiva do acordeão na sidebar**.

### B.5.2 — Blocos customizados (Gutenberg)

| Bloco | Origem | Campos |
|---|---|---|
| `Bloco Libras` (accordion) | Decisão 13, 19 | `video_libras_url` |
| `Player Ouvir` | Decisão 13, 19 | `audio_url` ou TTS |
| `Infográfico-resumo` | Decisão 13 | `infografico` |
| `Imagem com audiodescrição` | Decisão 13 | imagem + `audiodescricao` (visível) + `legenda` |
| `Callout / Destaque` | Decisão 5 ⏳ | tipo (⏳ a fechar) + texto; cores do DS (Fase 2) |
| `Checkpoint` | Camada 4 | texto verificável visualmente |
| `Bloco de pré-requisitos` | Camada 4.5 | lista linkada |
| `Bloco de saída` | Camada 4.5 | "o que você sabe fazer agora" + próximos passos plurais |

### B.5.3 — Componentes de trilha/percurso

| Componente | Padrão 4.5 | Cor |
|---|---|---|
| `BoxTrilhaAcordeao` (sidebar) | 4.2 | Verde IFES |
| `ChipPercurso` | 4.3 | Dourado |
| Página de trilha (`/trilhas/{slug}`) | 4.4 / 4.4.1 | Verde |
| Página de percurso (`/percursos/{slug}`) | 4.5 | Dourado |
| Card de trilha em percurso | 4.6 | Borda verde |
| Listagem `/percursos` | 4.7 | Borda dourada 4px |

> Tokens já definidos no `prototipo-artigo.html`: `--gold #b08544`, `--gold-soft #f3e7d0`, `--gold-deep #8c6a36`, `--accent #1f5142` (verde IFES), `--accent-soft #e3ecdf`. Detalhamento dos tokens visuais é responsabilidade do Design System (Fase 2).

---

## B.6 — URLs semânticas · ⏳ pendente (Sprint 3)

Padrão proposto (a confirmar com Elton + Marquito):

```
/artigos/{slug}          (ou /{categoria}/{slug} — a decidir)
/trilhas/{slug}
/percursos/{slug}
```

> A estratégia completa de URLs + SEO/GEO + busca interna é entregável do Sprint 3 (`output/taxonomia.md` e `output/descoberta-seo-geo.md`), ainda não produzido.

---

## B.7 — Estados de conteúdo e depreciação (Camada 8, Decisão 21)

| Estado | Visível ao leitor? | Comportamento |
|---|---|---|
| Publicado | Sim | Normal |
| Revisão pendente | **Não — badge admin-only** | 12 meses sem revisão |
| Depreciado (com substituto) | Sim | Redirect 301 + banner |
| Depreciado (sem substituto) | Sim | Banner com data de remoção |
| Arquivado | Por URL direta | Fora da navegação após 90 dias |

> Implementar como meta de estado + capability check (badge só renderiza para `manage_options`/editor).

---

## B.8 — Busca, feedback e acessibilidade (V1)

| Recurso | Decisão | Spec |
|---|---|---|
| Busca | 11 | Modal Ctrl+K, full-text, filtros por taxonomia, atalhos visíveis. IA fica para V2. Índice consome `sinonimos_aceitos` + `termo_popular` do Vocabulário (Camada 3) |
| Feedback | 12 | "Foi útil / Não foi útil" (texto, sem emoji) + campo "O que faltou?" + copiar link/âncora/ABNT + compartilhar (incl. WhatsApp formatado) |
| Acessibilidade | 10 | VLibras, A-/A+, alto contraste (WCAG AAA), fonte para dislexia, atalhos de teclado, "pular para conteúdo", semântica HTML rigorosa. Modo escuro via CSS custom properties (Decisão 8) |

---

## B.9 — Linter de conteúdo (Fase 3, consome a Parte A)

| Regra | Origem |
|---|---|
| Termos `sinonimos_rejeitados` do Vocabulário → warning | Camada 3 |
| Checklist de Encadeabilidade — critérios 1, 2, 3, 5, 6 automatizáveis | Camada 4.5 |
| Limites de legibilidade (palavras/frase, voz passiva, Flesch) | Camada 6 |
| Subtítulo presente e 10-25 palavras | Decisão 16 |
| Próximos passos plurais (≥2 ou nenhum) | Camada 4.5 |

---

## B.10 — Checklist de aceitação do template de artigo (Fase 3)

- [ ] Subtítulo obrigatório (campo + validação 10-25 palavras)
- [ ] Autor obrigatório e exibido
- [ ] Cabeçalho na ordem: Categoria·Tipo → H1 → Subtítulo → Autor+Tempo → Multimodal → Índice
- [ ] Blocos multimodais na ordem Libras → Ouvir → Outros
- [ ] Índice sticky com scroll-tracking
- [ ] Box de trilha multi-trilha (acordeão) na sidebar, vínculo estrutural
- [ ] Sem prev/next no rodapé (removido — Decisão 32)
- [ ] Rodapé: Relacionados → Feedback → ABNT
- [ ] Artigos relacionados obrigatórios
- [ ] ABNT gerada automaticamente
- [ ] Audiodescrição visível disponível por imagem
- [ ] `tipo` e `categoria` = 1; `topico` = 2-4 (sem tag livre)
- [ ] Badge de revisão pendente só para admins
- [ ] Marcação "Produzido com IA" quando aplicável
- [ ] Modo escuro + pacote de acessibilidade

---

## Pendências que travam a finalização

| Pendência | Bloqueia | Responsável |
|---|---|---|
| Validação pedagógica das Camadas 1, 2, 4, 5, 6, 7 (e 4.5) | Camadas viram fonte canônica definitiva | Rute |
| ~~6ª categoria do Eixo 2~~ ✅ **Decidida (2026-05-21):** Gestão e Operação do Moodle | — | — |
| ~~Lista dos 25 tópicos do Eixo 3~~ ✅ **Decidida (2026-05-21)** — refinamento fino pendente Rute | — | Rute (refino) |
| Mapear os 131 artigos antigos nos novos eixos | Valida categorias/tópicos na prática + insumo da triagem (Fase 4.1) | Elton + Juliana |
| Tipos de callout (Decisão 5) | Bloco `Callout` no WP | Camada 4 + DS (Fase 2) |
| URLs semânticas + SEO/GEO + busca | `output/taxonomia.md`, `output/descoberta-seo-geo.md` | Sprint 3 |
| Preenchimento das 6 categorias pendentes do Vocabulário | Linter + busca completos | Juliana + Rute + Elton |
| Validação das Decisões 25-32 com Rute e Marquito | Arquitetura Trilha/Percurso definitiva | Reunião a marcar |

---

## Histórico de versões

| Versão | Data | Mudança | Por |
|---|---|---|---|
| 1.0 | 2026-05-21 | Documento mestre consolidado: Parte A (10+ camadas, drafts redigidos das faltantes) + Parte B (spec WordPress). Camadas 1, 3, 4.5 por referência; 2, 4, 5, 6, 7, 8, 9, 10 redigidas em draft. | Elton + Claude |
| 1.1 | 2026-05-21 | Taxonomia fechada: 6ª categoria (Gestão e Operação do Moodle) + 25 tópicos do Eixo 3, com slugs. B.3 atualizada; pendências de categoria/tópico resolvidas. Sincronizado com `vocabulario-controlado.json` v1.1. | Elton + Claude |

---

*Content System (mestre consolidado) · Base de Conhecimento CEFOR/IFes · Fase 1 — Fundações*
