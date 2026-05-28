# Roadmap de Migração — Base de Conhecimento CEFOR/Ifes

> **Revisão 3 — 2026-05-21.** Incorpora a atualização do content-system feita pelo Elton.
> Sobre a revisão 2 (estratégia "migrar bruto, curar depois"), esta revisão: corrige o
> modelo de dados para **3 CPTs** (`cgte_base`, `cgte_trilha`, `cgte_percurso`) + **3
> taxonomias** — Trilha é CPT, não taxonomia; fecha DP-3 a DP-6 com a taxonomia já
> definida (6 categorias + 25 tópicos); adota o `design.md` do Elton como spec do tema
> (Fase F). Convenção de nomes: tudo prefixado com `cgte_` (o content-system será
> sincronizado pelo Elton para esses nomes).

## Contexto

A CGTE/CEFOR mantém uma base de conhecimento em WordPress (`conhecimento.cefor.ifes.edu.br`)
criada às pressas, numa versão antiga. Ela está degradada: REST API quebrada, corpo dos
artigos preso a um page builder legado (SiteOrigin), ~1.800 comentários de spam e ~20 contas
de usuário suspeitas.

Em paralelo, um workspace de design (`C:\laragon\www\cefor-base-conhecimento`) produziu a
especificação de uma base nova — nova taxonomia, nova interface, nova arquitetura de
conteúdo. Já existe uma instalação WordPress nova e limpa (`C:\laragon\www\conhecimento`,
WP 6.8.3) à espera desse conteúdo.

O objetivo é levar os artigos da base antiga para a instalação nova, dentro da estrutura
nova. Este documento é o **roadmap** dessa migração: estratégia, fases, dependências,
decisões e riscos. **Nada foi executado** — a execução das fases A-I é trabalho subsequente.

## Estratégia: migrar bruto, curar depois

A análise conjunta definiu a estratégia. Em vez de triar e fazer o trabalho editorial
**antes** da carga — o que punha o trabalho humano no caminho crítico e adiava o ambiente
funcional — **carrega-se tudo primeiro, cru, e cura-se depois.**

Os 139 registros do dump entram inteiros — inclusive rascunhos e lixo — na estrutura nova.
Subtítulo, autoria, mapeamento de eixos e blocos multimodais ficam **pendentes e
não-obrigatórios**. Assim que a carga termina, há um ambiente de testes navegável e
completo; a partir dele, uma pessoa humana cura os dados — decide o que fica e o que sai,
preenche o que falta, ajusta — enquanto o desenvolvimento do sistema continua em paralelo.

O objetivo é **desbloquear**: ter algo funcional e disponível rápido, e tratar a curadoria
como trabalho contínuo no ambiente de testes, não como pré-requisito da migração.

O que isso significa na prática:

- **Sem triagem de artigos.** Migram-se todos os 139, inclusive lixo e rascunho. Juntar,
  apagar, depreciar — depois, na curadoria.
- **Triagem só para usuários e comentários.** Comentários: **nenhum** migra (tudo é spam).
  Usuários: migram os autores legítimos, não as contas spam.
- **Campos obrigatórios viram opcionais nesta etapa.** O content-system (B.2/B.10) marca
  subtítulo e autor como obrigatórios; o plugin de estrutura registra os campos mas **não**
  força preenchimento agora. A obrigatoriedade volta como passo de endurecimento, depois da
  curadoria, antes do go-live.
- **Conversão de corpo com mínima fricção.** SiteOrigin → Gutenberg automático, aceitando
  imperfeição; humanos ajustam artigo a artigo no ambiente de testes.

## Decisões já tomadas

- **Estratégia:** migrar tudo bruto agora, curar depois no ambiente de testes.
- **Escopo deste documento:** roadmap. A execução das fases A-I é trabalho subsequente.
- **Conteúdo:** os 139 registros do dump migram inteiros para a estrutura nova (CPT
  `cgte_base` + taxonomias). A remodelagem editorial é curadoria pós-migração, humana.
- **Estrutura-alvo:** o content-system do workspace de design é a **referência canônica**
  da estrutura. A Parte B de `contentsystem.md` é o spec WordPress acionável.
- **Legado:** continua no ar (`conhecimento.cefor.ifes.edu.br`) e serve de consulta — **não**
  se monta um ambiente local de legado (versão de PHP antiga inviabiliza a recriação local).
- **Mídia:** os arquivos físicos estão no export All-in-One; a extração é feita pela equipe.
- **Handoff:** o roadmap aprovado será publicado também no workspace de design (ver final).

## Insumos disponíveis

### Fontes da migração — em `C:\laragon\www\migracao-base-conhecimento\`

| Arquivo | Tamanho | O que é | Uso |
|---|---|---|---|
| `basedeconhecimento.wordpress.2026-05-21.xml` | 2,56 MB | Export WXR nativo do WP (21/05). 584 itens: ~139 artigos `kbe_knowledgebase`, ~430 attachments, páginas, posts, termos. **Não** contém os binários de mídia. | Fonte estruturada para a carga de conteúdo. |
| `conhecimento-cefor-ifes-edu-br-...wpress` | 1,4 GB | Export All-in-One: site inteiro — banco + arquivos de mídia + plugins + tema. | Fonte dos binários de mídia. |
| `mysql-siena-conhecimento-2026-03-25...sql` | 11 MB | Dump do banco (estado de 25/03). | Redundante; serve de conferência. |
| `backup_vitrine_mooc20240821...sql` | 2,59 MB | Dump de **outro projeto** (Vitrine MOOC). | **Ignorar** — está na pasta por engano. |

**Atenção:** o `.wpress` tem 1,4 GB e **excede o limite de import gratuito** do All-in-One
(~256 MB). O caminho recomendado: extrair o `.wpress` manualmente (formato descompactável —
recupera o banco e a pasta `uploads` sem o plugin). Essa extração é feita pela equipe (DP-11).

### Referências de estrutura — no workspace de design (`C:\laragon\www\cefor-base-conhecimento\`)

| Arquivo | O que define | Usa em |
|---|---|---|
| `stages/01-fundacoes/output/contentsystem.md` | Parte A: governança editorial. Parte B: **spec WordPress** — CPTs, custom fields, taxonomias, blocos, estados, checklist de aceitação. | Fases B, E, F, H |
| `stages/01-fundacoes/output/vocabulario-controlado.json` | Vocabulário controlado; termos dos 5 Tipos, 4 eixos, 25 Tópicos. | Fases B, G |
| `stages/02-design-system/output/design.md` | Design System: tokens (CSS custom properties), 3 modos, componentes. **É a spec de tema em formato WordPress.** | Fase F |
| `stages/02-design-system/drafts/prototipos-paginas/prototipo-artigo.html` · `stages/02-design-system/drafts/kit-visual.html` | Interface canônica do artigo · style guide vivo dos tokens. | Fase F |

## O quadro: estrutura antiga ≠ estrutura nova

| | Base antiga (nos dumps) | Base nova (content-system) |
|---|---|---|
| Modelo de dado | post type `kbe_knowledgebase` (plugin WP Knowledgebase) + taxonomia custom "setor" | 3 CPTs: `cgte_base` (artigo), `cgte_trilha`, `cgte_percurso`. 3 taxonomias: `cgte_tipo` (5), `cgte_categoria` (6), `cgte_topico` (25) |
| Corpo do artigo | shortcodes do SiteOrigin Page Builder | blocos Gutenberg (core na carga; blocos editoriais inseridos na curadoria) |
| Estrutura | artigos soltos | artigos + Trilhas + Percursos |

A carga **copia tudo cru** para o esqueleto novo — o mapeamento estrutural
`kbe_knowledgebase` → `cgte_base` acontece no momento do import. A remodelagem editorial
(subtítulo, mapeamento de eixos, corpo em blocos editoriais) **não** acontece na carga: é
curadoria humana posterior, no ambiente de testes.

## Volume

O dump traz **139** registros `kbe_knowledgebase` (qualquer status — inclui rascunho e lixo).
**Todos os 139 migram** (DP-1). O crawl público via ~131 (≈ os publicados) e a estimativa de
~55-70 "editorialmente vivos" deixam de ser metas de migração: viram **resultado da curadoria
pós-migração** (Fase G).

## Dependência central: implementação × migração

Das 8 etapas do plano de implementação (`cefor-base-conhecimento/stages/03-implementacao/CONTEXT.md`),
**apenas uma bloqueia a carga**:

- **Etapa 2 — CPTs + metadados + taxonomias:** pré-requisito duro. É a Fase B deste roadmap,
  e o spec dela é a **Parte B de `contentsystem.md`**. Sem a estrutura nova registrada, não
  há onde carregar o conteúdo.

A Etapa 3 (blocos Gutenberg) **não bloqueia a carga**: com a conversão de mínima fricção
(DP-7), o corpo dos artigos vai para blocos *core* do Gutenberg, sem depender dos blocos
editoriais customizados (callout, Libras, audiodescrição, infográfico). Esses só são
necessários quando a **curadoria** (Fase G) for inserir conteúdo multimodal. As demais
etapas (tema, workflow, SEO, busca, acessibilidade, testes) correm em paralelo.

**Recomendação:** registrar a estrutura de dados (Fase B) num **plugin separado do tema** —
nunca dentro do tema. CPTs e taxonomias no tema fazem o conteúdo "sumir" ao trocar de tema.
Como o tema novo ainda nem existe, um plugin de estrutura destrava a carga sem esperar nada
do trilho visual.

## As 9 fases

Ambientes: **LEGADO-VIVO** = `conhecimento.cefor.ifes.edu.br` (no ar — consulta apenas) ·
**DESTINO-LOCAL** = `C:\laragon\www\conhecimento` (o ambiente de testes) · **SERVIDOR-NOVO**
(produção) · **WORKSPACE** = `C:\laragon\www\cefor-base-conhecimento` (só design).

### Fase A — Preparação e decisões de arquitetura
- **Objetivo:** travar as decisões e validar insumos. **Depende de:** nada.
- As decisões técnicas estão fechadas nesta revisão (ver tabela DP).
- Conferir a cobertura do WXR: quais dos 139 artigos ele traz e em que status — aqui é só
  **conferência**, não triagem (todos migram de qualquer forma).
- **Entrega:** este documento aprovado + DESTINO-LOCAL confirmado como ambiente de testes.

### Fase B — Plugin de estrutura no destino (= Etapa 2 da implementação)
- **Objetivo:** criar a estrutura de dados nova, independente do tema. **Depende de:** Fase A.
  **Spec:** Parte B de `contentsystem.md`.
- Plugin em `C:\laragon\www\conhecimento\wp-content\plugins\`.
- Registrar **3 CPTs:** `cgte_base` (artigo, `show_in_rest: true`), `cgte_trilha`,
  `cgte_percurso`.
- Registrar **3 taxonomias:** `cgte_tipo`, `cgte_categoria`, `cgte_topico`.
- Custom fields do artigo (`contentsystem.md` B.2): `subtitulo`, `autores`, `tempo_leitura`
  (auto), `data_publicacao`, `data_revisao_interna`, `produzido_com_ia`, `video_libras_url`,
  `audio_url`, `podcast_url`, `infografico`, `prerequisitos`, `proximos_passos`. Os que o
  content-system marca obrigatórios (subtítulo, autores, datas) são **registrados como
  opcionais — sem enforcement** nesta etapa.
- Custom fields de `cgte_trilha` e `cgte_percurso` (`contentsystem.md` B.4), incluindo a
  relação **ordenada** Trilha→Artigo.
- Post status de depreciação (`contentsystem.md` B.7): Revisão pendente (badge admin-only),
  Depreciado, Arquivado.
- Pré-cadastrar os termos: 5 Tipos, **6 Categorias** e **25 Tópicos** — todos fechados (ver
  DP-6).
- **Entrega:** estrutura nova ativa no admin. A partir daqui a carga é tecnicamente possível.

> **Modelo de Trilha e Percurso (DP-4 — `contentsystem.md` B.1/B.4):**
> - **Trilha** e **Percurso** são CPTs (`cgte_trilha`, `cgte_percurso`), não taxonomias —
>   têm página própria, descrição e lista de membros.
> - **Trilha→Artigo** é um campo de relação **ordenado** no CPT `cgte_trilha` (campo
>   `artigos`). A posição "Artigo X de Y" é estrutural e persistida.
> - **Artigo→Trilha** é **derivado** — consulta reversa; o box de trilha na sidebar aparece
>   por vínculo estrutural, sem referrer.
> - **Percurso** agrega via campos de relação `trilhas` + `artigos_complementares`, sem
>   ordem fixa.
> - Implementação: campos de relação via ACF Relationship / Pods / JetEngine, **ou** no
>   próprio plugin de estrutura, com interface drag-and-drop para a ordem (substitui o
>   plugin de ordenação de terceiros usado hoje).
> - Migração: carregar os artigos **sem vínculo de trilha/percurso**; montar e ordenar
>   trilhas e percursos é tarefa da curadoria (Fase G).

### Fase C — Mídia e legado de consulta
- **Objetivo:** ter a mídia em mãos e o legado disponível para apoio editorial. **Depende de:** Fase A.
- O **LEGADO-VIVO continua no ar** e serve de consulta editorial durante a curadoria — não
  se monta um WordPress local de legado (PHP antigo torna a recriação local inviável).
- Extrair o `.wpress` para obter a pasta `uploads` (~430 mídias). Extração **feita pela
  equipe**; orientamos o procedimento (DP-11).
- **Entrega:** pasta `uploads` disponível; LEGADO-VIVO confirmado como referência de consulta.

### Fase D — Conversão do conteúdo (SiteOrigin → Gutenberg)
- **Objetivo:** converter o corpo dos artigos para blocos Gutenberg. **Depende de:** Fase A
  (o WXR já está em mãos).
- O WXR traz o `post_content` cru, com shortcodes SiteOrigin.
- Conversão **automática e de mínima fricção** (DP-7): shortcodes → blocos *core* do Gutenberg
  (parágrafo, título, imagem, lista); onde não houver equivalente limpo, bloco Clássico/HTML.
  **Sem reescrita.** Aceita-se imperfeição.
- Os blocos editoriais novos (callout, Libras, audiodescrição, infográfico) **não** entram
  aqui — são inseridos por humanos na curadoria (Fase G), com os blocos da Fase F.
- **Entrega:** corpos convertidos, minimamente funcionais, prontos para a carga.

### Fase E — Carga no destino (migração bruta)
- **Objetivo:** popular a instalação nova com tudo. **Depende de:** Fase B + C + D.
- **E.1 Mídia primeiro:** copiar a pasta `uploads` para `wp-content\uploads`; reconstruir a
  Media Library. Mídia antes dos artigos, para os links resolverem.
- **E.2 Artigos:** importar **todos os 139** do WXR mapeado para `cgte_base` — qualquer
  status, inclusive lixo e rascunho (DP-1), via WP All Import ou script. Os artigos entram
  **sem termos de taxonomia** (Tipo/Categoria/Tópico são atribuídos na curadoria).
  *Opcional:* pré-preencher `cgte_categoria` por melhor esforço, usando a tabela de
  consolidação "antigas → novas" do `contentsystem.md` B.3, deixando o curador confirmar.
- **E.3 Autores:** criar só os autores legítimos referenciados; **excluir as contas spam**
  (DP-10). Artigo sem autor identificável fica **sem autor** — não exibe nada (DP-9).
- **E.4 Comentários:** **nenhum** migra (DP-10).
- **Não migrar:** revisions, comentários, contas spam, tema "zero", plugins do legado,
  taxonomia "setor".
- **Entrega:** **ambiente de testes completo e navegável** — o marco de desbloqueio.

### Fase F — Tema e camadas técnicas
- **Objetivo:** a camada visual e funcional. Corre **em paralelo**; **não bloqueia a carga**.
- **Insumos:** `design.md` (tokens normativos), `kit-visual.html` (style guide vivo),
  `prototipo-artigo.html` (interface canônica do artigo), `contentsystem.md` Parte B
  (anatomia do artigo B.5, blocos B.5.2, checklist de aceitação B.10).
- O tema é criado a partir desses insumos — os tokens do `design.md` viram CSS custom
  properties; trocar de tema é trocar variáveis.
- Inclui: tema, blocos Gutenberg editoriais (Libras, Ouvir, infográfico, imagem com
  audiodescrição, callout — 6 tipos, checkpoint, pré-requisitos, saída), workflow, SEO/GEO,
  busca Ctrl+K, widget de acessibilidade (3 modos), testes eMAG/CWV.
- Os blocos editoriais precisam existir antes de a curadoria (Fase G) inserir conteúdo
  multimodal.
- **Entrega:** tema + blocos + camadas técnicas no DESTINO-LOCAL.

### Fase G — Curadoria editorial pós-migração
- **Objetivo:** curar a base já carregada. **Depende de:** Fase E (ambiente de testes pronto).
  Corre **em paralelo** à Fase F e ao desenvolvimento contínuo do sistema.
- Uma pessoa humana, no ambiente de testes, cura os dados migrados:
  - decide o que fica e o que sai — usa a **Rubrica de Qualidade** (`contentsystem.md`
    Camada 5, 7 dimensões) como instrumento; funde duplicatas, depreca obsoletos, descarta lixo;
  - mapeia os 4 eixos por artigo (Tipo, Categoria, Tópicos, Trilha);
  - escreve os subtítulos e revisa a autoria;
  - insere os blocos multimodais usando os blocos da Fase F;
  - ajusta os corpos convertidos imperfeitamente na Fase D;
  - monta e ordena as trilhas e os percursos.
- **Não-bloqueante:** a base já está no ar (em testes) durante todo esse trabalho; nada disso
  é pré-requisito da migração.
- **Entrega:** base curada, progressivamente, no ambiente de testes.

### Fase H — Verificação e QA
- **Objetivo:** garantir correção em dois momentos. **Depende de:** Fase E e Fase G/F.
- **Logo após a Fase E** — verificação de integridade da carga (ver "Verificação").
- **Antes da Fase I** — QA de prontidão: o template de artigo passa pelo **checklist de
  aceitação B.10** do `contentsystem.md`, mais o passo de **endurecimento** (re-tornar
  subtítulo e autor obrigatórios).
- **Entrega:** relatório de verificação + mapa de redirects validado + sinal verde.

### Fase I — Go-live no servidor novo
- **Objetivo:** publicar em produção. **Depende de:** Fase H + DP-8 + DP-12.
- Promover do DESTINO-LOCAL para o SERVIDOR-NOVO; search-replace de domínio.
- Ativar os redirects 301 (a base antiga usa `/%postname%/`; a estrutura de URL muda).
- Beta interno CGTE/CEFOR → ajustes → lançamento público.
- Decidir domínio final e desligamento da base antiga — definido nesta etapa, com a TI (DP-12).
- Ativar ContentOps, revisão periódica e Política de Depreciação.
- **Entrega:** base nova no ar; antiga redirecionada/desativada.

## Diagrama de dependências

```
FASE A — decisões de arquitetura
   ├───────────────┬───────────────┬──────────────────────────────┐
   ▼               ▼               ▼                              ▼
FASE B           FASE C          FASE D                trilho paralelo:
plugin de        mídia +         SiteOrigin →          Design System (design.md)
estrutura        legado vivo     Gutenberg                     │
   │               │               │                          ▼
   └───────────────┴───────┬───────┘                         FASE F
                           ▼                          tema + blocos + SEO +
              FASE E — carga bruta                    busca + acessibilidade
              (mídia → 139 artigos → autores)                  │
                           │                                   │
                           ▼                                   │
            ╔═════════════════════════╗                        │
            ║ AMBIENTE DE TESTES NO AR ║ ◄── marco de desbloqueio
            ╚═════════════════════════╝                        │
                           │                                   │
            ┌──────────────┴──────────────┐                    │
            ▼                             ▼                     │
   FASE G — curadoria             FASE H — verificação          │
   editorial (humana,             da carga                      │
   contínua, paralela)                    │                     │
            │                             │                     │
            └──────────────┬──────────────┴─────────────────────┘
                           ▼
              FASE H — QA de prontidão + endurecimento
                           ▼
              FASE I — go-live no SERVIDOR-NOVO
```

Caminho crítico até o desbloqueio: **A → (B, C, D) → E**. Depois da Fase E o ambiente de
testes está no ar; **G** (curadoria), **F** (tema) e **H** (verificação) correm em paralelo,
e **I** fecha. O trabalho humano deixou de estar no caminho crítico da migração.

## Decisões técnicas — resolução

| ID | Decisão | Resolução |
|---|---|---|
| DP-1 | Número-alvo de artigos da V1 | **Migrar todos os 139**, inclusive lixo e rascunho. Sem triagem prévia; o conjunto final é resultado da curadoria (Fase G). |
| DP-2 | `post_type` keys dos CPTs | **`cgte_base`** (artigo), **`cgte_trilha`**, **`cgte_percurso`**. Tudo prefixado com `cgte_` (evita colisão com outros plugins). O Elton sincroniza o `contentsystem.md` para esses nomes. |
| DP-3 | `taxonomy` keys | **3 taxonomias:** `cgte_tipo`, `cgte_categoria`, `cgte_topico`. Trilha **não** é taxonomia — é o CPT `cgte_trilha`. |
| DP-4 | Modelo de Trilha/Percurso + ordem | 3 CPTs; Trilha→Artigo = relação **ordenada** no CPT trilha; Artigo→Trilha = derivada; Percurso agrega trilhas + artigos. Interface drag-and-drop para a ordem. Migrar sem vínculo; montar na curadoria. Ver "Modelo de Trilha e Percurso" na Fase B. |
| DP-5 | Slugs de URL públicos | Artigo: `/artigos/{slug}`. Trilha: `/trilhas/{slug}`. Percurso: `/percursos/{slug}`. Categoria: `/categoria/{slug}`. Tópico: `/topico/{slug}`. Escolha simples e funcional; a estratégia completa de SEO/URL é entregável do Sprint 3 do workspace — se mudar, o mapa de redirects (Fase H/I) se ajusta. |
| DP-6 | Lista dos Tópicos + 6ª Categoria | **Fechada** (`contentsystem.md` v1.1, 21/05). **6 categorias:** Ferramentas e Recursos (`ferramentas`), Gestão e Operação do Moodle (`gestao-moodle`), Pedagogia e Planejamento (`pedagogia`), Acessibilidade (`acessibilidade`), Conduta e Conformidade (`conduta`), Identidade (`identidade`). **25 tópicos** listados em `contentsystem.md` B.3 / `vocabulario-controlado.json` (refino pedagógico fino ainda pendente com a Ruti — não bloqueia). |
| DP-7 | Estratégia SiteOrigin → Gutenberg | Conversão automática de **mínima fricção**, sem reescrita. Humanos ajustam artigo a artigo na curadoria. |
| DP-8 | Relação DESTINO-LOCAL ↔ SERVIDOR-NOVO | Não é problema agora; verificar na Fase I. |
| DP-9 | Autoria | **Não-bloqueante.** Sem autor identificável, o artigo fica sem autor — não exibe nada. |
| DP-10 | Comentários e usuários spam | **Não migrar** comentário nenhum (tudo é spam). Não migrar contas spam; migram só os autores legítimos. |
| DP-11 | Contorno do limite do `.wpress` | Extração feita pela **equipe** (formato descompactável — recupera banco + `uploads`). Orientação na Fase C. |
| DP-12 | Domínio final e desligamento da base antiga | Etapa posterior, definida **com a TI** na Fase I. |

## Riscos

| Risco | Mitigação |
|---|---|
| `.wpress` de 1,4 GB excede o limite de import gratuito do All-in-One | Extração manual pela equipe (DP-11); não depender da reimportação pelo plugin. |
| REST API do legado quebrada | Não é bloqueante: temos WXR + `.wpress` + `.sql`; a extração não depende da API. |
| Mudança de estrutura de URL quebra links externos e SEO | Mapa de redirects 301 completo (Fase H), testado antes do go-live (Fase I). |
| Conversão SiteOrigin → Gutenberg imperfeita | Aceito por design (mínima fricção); a curadoria humana corrige no ambiente de testes. |
| A base vai ao ar crua porque a curadoria nunca acontece | O go-live (Fase I) tem o QA de prontidão como gate explícito (checklist B.10); a base só promove com sinal verde da Fase H. |
| Subtítulo e autor opcionais — artigos podem ir ao ar incompletos | Passo de endurecimento na Fase H: re-tornar os campos obrigatórios após a curadoria, antes de promover. |
| Links de imagem no corpo com caminho absoluto do domínio antigo | Carregar a mídia antes dos artigos (E.1 antes de E.2) + search-replace de domínio. |
| `contentsystem.md` ainda usa nomes sem prefixo (B.1/B.3) | O Elton sincroniza o content-system para os nomes `cgte_*` decididos aqui; até lá, este roadmap é a referência dos nomes. |
| Tema novo depende do Design System | O plugin de estrutura (Fase B) destrava a carga sem o tema; o tema segue trilho próprio (Fase F) a partir do `design.md`. |
| "Servidor novo" pode não estar realmente pronto | Validar o SERVIDOR-NOVO na Fase I; manter o DESTINO-LOCAL espelhando-o. |

## Verificação

**Após a Fase E — integridade da carga:**

- **Contagem:** os 139 registros do dump estão no destino como `cgte_base`.
- **Mídia:** os ~430 anexos foram carregados e as imagens do corpo resolvem.
- **Import limpo:** nenhum erro de import; os 3 CPTs e as 3 taxonomias presentes no admin,
  com os 5 Tipos / 6 Categorias / 25 Tópicos pré-cadastrados.
- **Autores:** autores legítimos criados, contas spam ausentes, comentários ausentes.

**Antes da Fase I — prontidão para o público:**

- **Checklist de aceitação B.10** do `contentsystem.md` aplicado ao template de artigo.
- **Taxonomia:** os artigos curados têm 1 Tipo, 1 Categoria e 2-4 Tópicos; trilhas ordenadas.
- **Endurecimento:** subtítulo e autor re-tornados obrigatórios; cobertura aferida.
- **Corpo:** nenhum shortcode SiteOrigin cru renderizando; blocos editoriais corretos.
- **Redirects:** o mapa 301 (URL antiga → nova) cobre os artigos e foi testado.
- **Testes técnicos:** eMAG (acessibilidade) e Core Web Vitals (performance) sobre conteúdo real.
- **Piloto:** 3-5 artigos validados ponta a ponta (conteúdo, taxonomia, mídia, interface).

## Handoff e sincronização com o design system

Após a aprovação, este roadmap será publicado no workspace de design para que o Elton
trabalhe o design system com o contexto da migração e sincronize o `contentsystem.md`
(nomes `cgte_*`).

- **Destino sugerido:** `C:\laragon\www\cefor-base-conhecimento\stages\03-implementacao\roadmap-migracao-conteudo.md`.
- A partir da publicação, a cópia em `cefor-base-conhecimento` passa a ser a versão
  viva/compartilhada; este arquivo em `solution-design/Plans/` permanece como registro do
  desenho da solução.

## O que será feito após a aprovação

Como o escopo é "roadmap, não executar a migração", a única execução pós-aprovação é:

1. Finalizar este documento como o roadmap definitivo.
2. Copiá-lo para `cefor-base-conhecimento/stages/03-implementacao/roadmap-migracao-conteudo.md`.

A execução das fases A-I é trabalho subsequente, fora do escopo deste roadmap.
