# Mapa de Trilhas e Percursos — Base de Conhecimento CEFOR/Ifes

> **Versão:** 1.0
> **Status:** ⏳ **Proposta** — validação pedagógica das sequências (ordem + começo/meio/fim) pendente com **Rute + Juliana** antes da Fase 4 (Produção de Conteúdo).
> **Base de análise:** 131 artigos reais do inventário (`data/base-antiga/base-conhecimento-cefor-inventario.json`) + 12 percursos antigos.
> **Referência cruzada:** `taxonomia.md` §6 (regras de Trilha/Percurso, Decisões 18, 25–32) · `convencao-titulos.md` (regra de nomeação) · insumo da Fase 4.1 (Triagem por Rubrica).

---

## 1. Diagnóstico dos 12 percursos antigos

A análise do acervo mostrou por que o modelo antigo não funcionava como jornada:

| Problema | Evidência no inventário |
|---|---|
| Percurso virou **depósito de categoria**, não jornada | "Professor Moodle" declarava **44 artigos**; "Planejamento e Design Educacional" 21 (e já em **404**) |
| **Sem começo/meio/fim** | "Dúvidas & Sugestões" abria **todos** os 12 percursos |
| **Sobreposição com categoria** | "Gestão e Config", "Ferramentas educacionais", "Moodle Codes" eram percurso **e** categoria |
| **Volume insuficiente** | "Gamificação" (5), "Direitos Autorais" (5) — sem massa para jornada própria |

**Correção:** trilha só existe onde há **sequência didática real** e nome que passa nos dois testes da convenção. O resto vira Categoria (eixo 2) ou Tópico (eixo 3).

---

## 2. Filtro — o que NÃO virou trilha

Conteúdo que vive como **referência da categoria** ou **descoberta por tópico**, nunca como trilha:

| Descartado como trilha | Por quê | Destino |
|---|---|---|
| Recursos do Moodle (URL, Arquivo, Página, Livro, Pasta, Rótulo) | Fichas de consulta, não jornada | Categoria `ferramentas` + tópicos |
| Atividades (Tarefa, Fórum, Glossário, Wiki, Escolha, Base de Dados) | Consulta avulsa | Categoria `ferramentas` + tópicos |
| Padrão Visual (orientações 32/55/46/49/50) | Conjunto de orientações, sem passo-a-passo sequencial | Categoria `identidade` |
| Ferramentas externas (Canva, Padlet, PowToon, +45…) | Recursos avulsos | Tipo `Recurso` |
| Direitos autorais, Netiqueta, Segurança do navegador | Leitura única, sem jornada | Categoria `conduta` |

---

## 3. Trilhas (nomeadas pela convenção)

> Cada trilha = uma **capacidade composta**, nome que passa nos dois testes (não vira categoria sem o qualificador; não cabe como título de um artigo). Número entre parênteses = `id` do artigo no inventário. `[C]` marca a âncora conceitual de abertura.

### Núcleo Moodle → integram o percurso *Dominando o Moodle*

#### T1 · Da sala vazia ao primeiro dia de aula
`categoria: gestao-moodle` · ~6 artigos · *jornada*

1. `[C]` Conheça o Moodle do Ifes (129)
2. Criar / importar a sala virtual (82 / 56)
3. Definir a data de início da sala (89)
4. Organizar seções e semanas (111)
5. Rodar o checklist de abertura de curso (66)

#### T2 · Avaliação online de ponta a ponta
`categoria: gestao-moodle` · ~10 artigos · ⚠️ *no limite do alerta de 10 (Decisão 25) — revisar promoção a percurso na V2*

1. `[C]` Prova online: entenda o que é (127)
2. Planejar a prova online (125)
3. Criar e configurar o questionário (120)
4. Elaborar as questões e conhecer os tipos (121 / 116)
5. Montar o banco de questões com sorteio automático (107 / 122 / 119)
6. Montar e publicar a prova no AVA (123 / 124 / 108)
7. Atribuir notas/pesos e embaralhar questões (118 / 106)
8. Proteger o acesso: senha, IP e Safe Exam Browser (104 / 103 / 34 / 126)

#### T3 · Do Livro de Notas ao Sistema Acadêmico
`categoria: gestao-moodle` · ~5 artigos · *jornada*

1. `[C]` Entender o Livro de Notas (85)
2. Configurar o Livro de Notas passo a passo (57)
3. Calcular a média com recuperação (16)
4. Acompanhar as notas no quadro (113)
5. Exportar as notas para o Sistema Acadêmico (47)

### Trilhas-destaque (autônomas)

#### T4 · Conteúdo interativo com H5P, do básico ao avançado
`categoria: ferramentas` · ~3 artigos

1. `[C]` Conhecer o potencial do H5P (17)
2. Inserir conteúdo H5P na sala virtual (18)
3. Montar um conteúdo interativo no AVA com H5P (19)

#### T5 · Aulas ao vivo por Webconferência
`categoria: ferramentas` · ~4 artigos

1. `[C]` Preparar-se para participar de uma webconferência (53)
2. Realizar uma aula ou reunião por webconferência (54)
3. Usar a Conferência Web da RNP integrada ao Moodle (27)
4. Transmitir a webconferência para o YouTube (58)

#### T6 · Acompanhamento e gamificação do progresso
`categoria: ferramentas` · ~3 artigos

1. Configurar a conclusão de atividades (44)
2. Ativar a barra de progresso (43)
3. Configurar o LevelUp (45)

#### T7 · Avaliação acessível para todos os estudantes
`categoria: acessibilidade` · ~3 artigos

1. `[C]` Cuidados de acessibilidade ao inserir recursos (15)
2. Configurar tempo ampliado no questionário (2)
3. Adicionar audiodescrição em imagens (26)

#### T8 · Conteúdo em Libras no AVA, do vídeo ao termo técnico
`categoria: acessibilidade` · ~3 artigos · *jornada*

1. Inserir vídeo em Libras no AVA (35)
2. Ativar a visualização VLibras (62)
3. Usar o videobook de termos da EaD em Libras (14)

#### T9 · Avaliações com IA generativa
`categoria: pedagogia` · ~3 artigos

1. `[C]` Fundamento — Taxonomia de Bloom 2.0 (5)
2. Gerar questionários com o GPT (8)
3. Gerar rubricas com o GPT (6)

#### T10 · Administração da sala virtual ao longo do curso *(candidata — confirmar com Rute)*
`categoria: gestao-moodle` · ~6 artigos

1. Fazer backup da sala virtual (92)
2. Restaurar a sala virtual (86)
3. Fazer backup e restauração de usuários (63)
4. Conceder acesso a usuários (59)
5. Habilitar acesso de visitante (48)
6. Criar atividade com acesso restrito (87)

---

## 4. Percurso V1

### Dominando o Moodle
`cor: verde escuro` (`--verde-profundo`; Decisão 31, revisada 2026-06-02 — dourado abandonado) · gerúndio aspiracional — *do zero ao curso avaliado no ar*

- **Passos (trilhas):** T1 → T2 → T3 (+ T10 se confirmada)
- **Artigos complementares soltos:** Criação de certificados no Moodle (93) · O que é mapa de atividades e como preencher (130)
- **3 rotas de entrada por perfil** (Decisão 31 — percurso não tem ordem linear obrigatória):
  - "Nunca dei aula no Moodle" → **T1**
  - "Vou aplicar uma prova" → **T2**
  - "Preciso fechar as notas" → **T3**

> As demais trilhas (T4–T9) ficam **autônomas e em destaque**. Graduam para percurso temático na V2 quando houver volume e ≥2 trilhas que formem uma formação real (candidatos, nomeados pelo gerúndio aspiracional da `convencao-titulos.md` §4: "Enriquecendo aulas com mídia" = T4+T5+T6; "Tornando o ensino acessível" = T7+T8).

---

## 5. Cobertura e fora de escopo

- **~55 artigos** entram em trilha; o restante vive como referência (categoria/tópico) ou recurso — **por desenho**, não por sobra.
- **Fora da base (remover/arquivar):** Dúvidas & Sugestões (1), START 2023 (20), Manual GLPI (64), divulgação de IA — Oficinas (10), Grupo WhatsApp (11), Papo IA.IÁ (12).
- **Mapeamento artigo-a-artigo dos 131 artigos** é entregável da Fase 4.1 (Triagem por Rubrica) — Juliana + Elton.

---

## Histórico de versões

| Versão | Data | Mudança | Por |
|---|---|---|---|
| 1.0 | 2026-06-01 | Proposta criada a partir da análise dos 131 artigos. 9 trilhas firmes + 1 candidata, nomeadas pela `convencao-titulos.md`. Percurso V1 "Dominando o Moodle". Substitui as 5 trilhas-piloto estimadas de `taxonomia.md` §6.4. | Elton + Claude |
| 1.1 | 2026-06-07 | Candidatos a percurso V2 renomeados para o padrão de gerúndio aspiracional (§4): "Conteúdo interativo e multimídia" → **Enriquecendo aulas com mídia**; "Ensino acessível" → **Tornando o ensino acessível**. Sincroniza com os protótipos da Fase 2 (home, listagem e página de percurso). | Elton + Claude |
