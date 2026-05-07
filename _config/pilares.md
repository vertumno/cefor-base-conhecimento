# Pilares do Sistema — Base de Conhecimento CEFOR/IFes

> **Documento de orientação de escopo**
> Este documento registra os 11 pilares que estruturam o projeto da nova Base de Conhecimento do CEFOR/IFes.
> Cada pilar representa um sistema a ser **detalhado e especificado em etapa futura**, após benchmarking e pesquisa.

---

## Como usar este documento

1. Os pilares foram definidos antes do benchmarking — intencionalmente
2. O benchmarking vai **alimentar as decisões** dentro de cada pilar
3. Após a pesquisa, cada pilar receberá seu próprio documento de especificação
4. A unidade atômica principal do sistema é o **Artigo** — um organismo composto por moléculas e átomos menores que serão mapeados durante a especificação

---

## Os 11 Pilares

---

### 1. Sistema Visual (Visual System)

**O que é:**
Define como o sistema se apresenta visualmente — a linguagem estética da Base de Conhecimento.

**O que precisamos definir:**
- Paleta de cores (incluindo modo escuro)
- Escala tipográfica (famílias, tamanhos, pesos, alturas de linha)
- Sistema de espaçamento (margens, paddings, grid)
- Tokens de design como fonte única de verdade para todos os valores visuais
- Estilo de ícones e ilustrações
- Padrão visual para elementos de código, tabelas, citações e destaques

**Insumos esperados do benchmarking:**
- Como plataformas de conhecimento técnico tratam a identidade visual
- Referências de sistemas de tokens bem implementados

---

### 2. Sistema de Interação (Interaction System)

**O que é:**
Define o que o usuário pode **fazer** em um artigo — as ações disponíveis e como elas se comportam.

**O que precisamos definir:**
- Ações do leitor: curtir, compartilhar, copiar referência ABNT, comentar trecho
- Comportamento de cada ação (feedback visual, estado de carregamento, confirmação)
- Ações para usuários autenticados vs não autenticados
- Interações com trilhas/percursos (marcar como lido, avançar, retomar)
- Microinterações e estados de hover, foco, ativo

**Insumos esperados do benchmarking:**
- Quais interações são padrão vs diferenciais em bases de conhecimento
- Padrões de UX para anotação e comentário de texto

---

### 3. Modelo de Conteúdo (Content Model)

**O que é:**
Define a **estrutura interna de um artigo** — como ele é escrito, organizado e formatado textualmente. É o pilar central que alimenta a produção por IA generativa.

**O que precisamos definir:**
- Tipos de artigo (tutorial, template, referência, guia rápido, etc.)
- Estrutura obrigatória e opcional de cada tipo (resumo, TL;DR, seções, destaques, glossário, referências)
- Tom e linguagem por tipo de artigo
- Regras para títulos, subtítulos e hierarquia textual
- Padrão para blocos especiais (alertas, dicas, avisos, exemplos)
- Template de prompt por tipo de artigo para geração via IA
- Checklist de qualidade estrutural que toda IA deve seguir

**Insumos esperados do benchmarking:**
- Modelos de conteúdo de plataformas de EaD e knowledge bases técnicas
- Boas práticas editoriais para conteúdo técnico educacional

---

### 4. Sistema de Taxonomia (Taxonomy System)

**O que é:**
Define como os artigos são **categorizados, classificados e conectados** — tanto para administradores quanto para mecanismos de busca e trilhas de aprendizagem.

**O que precisamos definir:**
- Estrutura de categorias (árvore, flat, mista)
- Sistema de tags (controlado vs livre vs híbrido)
- Modelo de trilhas e percursos (como artigos se conectam em sequência)
- Artigos relacionados (manual, automático ou híbrido)
- Campos de metadados obrigatórios e opcionais por tipo de artigo
- Estrutura de URL semântica

**Insumos esperados do benchmarking:**
- Como EaD e plataformas educacionais organizam conteúdo em percursos
- Padrões de taxonomia em knowledge bases técnicas

---

### 5. Sistema de Acessibilidade (Accessibility System)

**O que é:**
Garante que o sistema esteja em conformidade com legislação brasileira e padrões internacionais de acessibilidade — não é opcional para uma instituição pública federal.

**O que precisamos definir:**
- Nível de conformidade alvo (WCAG 2.2 AA como mínimo; AAA onde possível)
- Aderência ao e-MAG (Modelo de Acessibilidade em Governo Eletrônico)
- Padrões de contraste de cor para texto e componentes
- Navegação completa por teclado
- Semântica HTML e uso correto de ARIA
- Suporte a leitores de tela
- Acessibilidade em modo escuro
- Checklist de acessibilidade por componente

**Insumos esperados do benchmarking:**
- Auditorias de acessibilidade em portais governamentais brasileiros
- Boas práticas de acessibilidade em plataformas de leitura técnica

---

### 6. Sistema de Leitura (Reading Experience System)

**O que é:**
Define a qualidade da **experiência de leitura sustentada** — diferente do visual, que cuida da estética, este pilar cuida do conforto e da retenção durante a leitura de artigos longos.

**O que precisamos definir:**
- Largura ideal de coluna de texto (caracteres por linha)
- Altura de linha e espaçamento entre parágrafos para leitura técnica
- Contraste específico para leitura prolongada (distinto do contraste mínimo de acessibilidade)
- Suporte a preferências do usuário: tamanho de fonte, modo escuro, fonte para dislexia
- Indicador de progresso de leitura
- Estimativa de tempo de leitura
- Índice de seções com navegação âncora
- Comportamento de imagens e blocos de código em leitura

**Insumos esperados do benchmarking:**
- Pesquisas sobre tipografia e leitura em telas
- Referências de plataformas com excelência em reading experience (Medium, Substack, GitBook)

---

### 7. Ciclo de Vida do Conteúdo (Content Lifecycle System)

**O que é:**
Define os **estados e processos** que um artigo percorre desde sua criação até sua eventual depreciação — essencial para manter a base de conhecimento confiável ao longo do tempo.

**O que precisamos definir:**
- Estados de um artigo: rascunho, em revisão, publicado, desatualizado, arquivado, depreciado
- Fluxo de transição entre estados (quem autoriza, quais critérios)
- Política de revisão periódica (frequência por tipo de artigo)
- Sinalização visual de conteúdo desatualizado para o leitor
- Processo de depreciação com redirecionamento para conteúdo atualizado
- Versionamento de artigos (histórico de alterações)
- Responsabilidades de curadoria por área temática

**Insumos esperados do benchmarking:**
- Como plataformas de documentação técnica gerenciam obsolescência de conteúdo
- Políticas editoriais de knowledge bases institucionais

---

### 8. Sistema de Estados (State System)

**O que é:**
Mapeia todos os **estados possíveis** de conteúdos e de usuários em relação ao conteúdo — afeta design, funcionalidade e metadados simultaneamente.

**O que precisamos definir:**

**Estados do conteúdo:**
- Rascunho / Em revisão / Publicado / Desatualizado / Arquivado / Depreciado

**Estados do usuário em relação ao artigo:**
- Não lido / Em progresso / Lido / Salvo / Recomendado

**Estados do usuário em relação a uma trilha:**
- Não iniciada / Em andamento / Concluída / Certificada

**Estados de componentes de interface:**
- Default / Hover / Foco / Ativo / Desabilitado / Carregando / Erro / Sucesso

**Insumos esperados do benchmarking:**
- Sistemas de progresso e gamificação em plataformas educacionais
- Padrões de UX para estados de leitura e progresso

---

### 9. Sistema Responsivo (Responsive Behavior System)

**O que é:**
Define como cada componente do artigo se comporta em diferentes tamanhos de tela — não é apenas adaptar o layout, mas repensar a experiência por dispositivo.

**O que precisamos definir:**
- Breakpoints do sistema
- Comportamento do índice de seções em mobile (drawer? oculto? fixo?)
- Comportamento da barra de ações (curtir, compartilhar) em mobile
- Tratamento de blocos de código longos em telas pequenas
- Tratamento de tabelas em mobile
- Comportamento de imagens e diagramas
- Navegação por trilhas em mobile
- Tipografia responsiva (escala fluida vs breakpoints fixos)

**Insumos esperados do benchmarking:**
- Analytics de dispositivos do público-alvo (professores de EaD usam mobile?)
- Padrões de responsive design em plataformas de leitura técnica

---

### 10. Sistema de Autoria (Authorship System)

**O que é:**
Define como o conteúdo é **criado, revisado e publicado** — cobrindo tanto autoria humana quanto produção assistida por IA generativa. É o pilar que operacionaliza a produção da base de conhecimento.

**O que precisamos definir:**
- Perfis de autor: servidor humano, especialista convidado, conteúdo assistido por IA
- Fluxo de criação humana: editor, campos, validações, submissão
- Fluxo de criação assistida por IA: prompt template → geração → revisão humana → publicação
- Sistema de validação automática de estrutura (artigo está completo? segue o modelo?)
- Mecanismo de feedback para refinamento de prompts ao longo do tempo
- Identificação clara de conteúdo gerado com assistência de IA (transparência editorial)
- Guia de estilo editorial por tipo de artigo
- Permissões e papéis no sistema de publicação

**Insumos esperados do benchmarking:**
- Fluxos editoriais de knowledge bases institucionais
- Boas práticas de uso de IA generativa em produção de conteúdo educacional
- Políticas de transparência sobre conteúdo gerado por IA

---

### 11. Sistema de Descoberta (Discoverability System)

**O que é:**
Garante que os artigos sejam encontrados — tanto por buscadores tradicionais (SEO) quanto por motores generativos como ChatGPT, Perplexity e Google AI Overview (GEO).

**O que precisamos definir:**

**SEO:**
- Estrutura de URLs semânticas
- Meta tags e Open Graph por tipo de artigo
- Sitemap e estratégia de indexação
- Core Web Vitals como requisito de performance
- Canonical tags e gestão de conteúdo duplicado

**GEO (Generative Engine Optimization):**
- Schema.org `EducationalArticle` e tipos relacionados
- Estrutura de conteúdo citável por IAs (definições explícitas, formato Q&A)
- Sinais de autoridade: autoria identificada, data de revisão, titulação do autor
- Seções de FAQ estruturadas por artigo
- Política de atualização de conteúdo para manutenção de relevância generativa

**Busca interna:**
- Estratégia de busca full-text vs semântica
- Filtros e facetas de busca
- Relevância e ranking de resultados internos

**Insumos esperados do benchmarking:**
- Análise de como knowledge bases institucionais são citados em respostas de IA
- Padrões de Schema.org para conteúdo educacional
- Ferramentas de busca semântica para conhecimento técnico

---

## Próximos passos sugeridos

```
1. Benchmarking e pesquisa (alimenta decisões em todos os pilares)
        ↓
2. Especificação de cada pilar (um documento por pilar)
        ↓
3. Definição da hierarquia atômica completa (átomos → moléculas → organismos)
        ↓
4. Design System e Modelo de Conteúdo (implementação)
```

---

*Documento criado em: 2026-04-07*
*Versão: 0.1 — Escopo inicial, pré-benchmarking*
*Projeto: Base de Conhecimento CEFOR/IFes — Reformulação*
