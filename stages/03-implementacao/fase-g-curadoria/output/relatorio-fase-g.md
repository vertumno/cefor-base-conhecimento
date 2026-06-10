# Fase G — Relatório da curadoria aplicada no DESTINO-LOCAL

> **Data:** 2026-06-10
> **Destino:** `C:\laragon\www\conhecimento` (plugin cgte-estrutura v0.3.1 + tema cgte ativos)
> **Backup pré-curadoria:** `C:\laragon\www\migracao-base-conhecimento\backup-banco-ANTES-curadoria-fase-g.sql`
> **Status:** aplicado e validado · **proposta editorial** — validação pendente: Elton + Juliana (taxonomia), Rute + Juliana (sequências de trilha)

## O que foi feito

Nenhum mapeamento artigo-a-artigo da taxonomia nova existia (a carga da Fase E
deixou taxonomias zeradas de propósito). Esta fase derivou e aplicou:

| Entrega | Resultado |
|---|---|
| `cgte_tipo` (1 por artigo) | 129 artigos — Tutorial 60 · Referência 29 · Conceitual 19 · Recurso 17 · Solução de Problema 1 (contagens públicas: 126; 4 classificados não públicos) |
| `cgte_categoria` (1 por artigo) | ferramentas 65 · gestao-moodle 35 · identidade 10 · acessibilidade 6 · conduta 5 · pedagogia 5 |
| `cgte_topico` (0–4 por artigo) | 25 tópicos do vocabulário, atribuição honesta (sem tópico de enchimento) |
| `cgte_subtitulo` | 129 subtítulos novos (10–25 palavras, regra do contentsystem.md) |
| Trilhas (`cgte_trilha`) | T1–T9 criadas **publish**, T10 **draft** (candidata — confirmar com Rute), com `cgte_artigos` na ordem do mapa e subtítulo |
| Percurso (`cgte_percurso`) | "Dominando o Moodle" **publish**: 3 trilhas + 2 complementares + 3 rotas de entrada (`cgte_como_percorrer`) |
| Não classificados | 10 artigos (utilitários e fora-da-base, lista abaixo) |

## Fontes do mapeamento

1. **Inventário antigo** (`data/base-antiga/…inventario.json`) — categoria/tipo/temas antigos de cada artigo; junção com o WP via `_cgte_slug_legado`.
2. **Tabelas de correspondência** antigo→novo (`taxonomia.md` §7).
3. **Mapa de trilhas** (`trilhas-percursos-mapa.md`) — sequências por id de inventário, posições e âncoras.
4. **Revisão editorial artigo a artigo** (título + classificação antiga + trecho do corpo) para os 42 tipos "Outros"/evento, divisões AVA→ferramentas/gestão e todos os subtítulos.

Pipeline (reproduzível, nesta pasta):

```
scripts/gerar_esqueleto_mapeamento.py   inventário + WP → esqueleto (derivação por regras)
output/ajustes-editoriais.json          camada editorial (sobrepõe o esqueleto)
scripts/consolidar_mapeamento.py        valida vocabulários → mapeamento-curadoria.json (canônico)
scripts/aplicar_curadoria.php           aplica no WP (dry-run por padrão; idempotente)
```

Para replicar no servidor de testes (depois que a carga E.1/E.2 rodar lá): os
wp_ids serão outros — re-rodar a extração e o pipeline, ou adaptar
`aplicar_curadoria.php` para resolver por `_cgte_slug_legado` (os scripts daqui
usam wp_id + conferência de slug).

## QA executado

- Dry-run e execução com **0 erros**; todos os termos resolvidos nos vocabulários semeados pelo plugin.
- Artigo-amostra (3417): tipo, categoria, 2 tópicos, subtítulo no banco e renderizados na página (200).
- Breadcrumb taxonômico ativo: `Início › Gestão e Operação do Moodle › artigo`.
- Relacionados calculando por categoria/tópicos; catálogo `/artigos` com chips de tipo.
- Home: vitrine exibe trilhas e o percurso "Dominando o Moodle".
- Páginas de trilha (`/trilhas/{slug}`) e percurso (`/percursos/dominando-o-moodle/`) → 200.

## Pendências e achados

1. **Box de trilha no artigo + vínculo de percurso**: placeholders comentados no
   tema (`single-cgte_base.php` linhas ~75 e ~140, Decisões 30/31). Os dados
   agora existem — é o próximo marco da Fase F.
2. **Trilha-teste "Moodle Dominado Perfeito"** (publish, 4 artigos) encontrada no
   destino — não veio do mapa, nome fora da convenção. Candidata a remoção
   (criação manual de teste?).
3. **Déficit de tópicos**: 70 artigos com <2 tópicos (regra: 2–4). Atribuição
   preferiu precisão a cota — vários assuntos (Wiki, Glossário, Emblemas,
   Padlet, Medium, diploma digital…) não têm tópico no vocabulário de 25.
   Backlog da curadoria fina com Rute/Juliana: ou estender o vocabulário
   (decisão formal Elton+Rute) ou aceitar 1 tópico nesses casos. Lista completa
   no console do `consolidar_mapeamento.py`.
4. **Não classificados (10)** — utilitários e fora-da-base (mapa §5); decisão de
   arquivar (status `cgte_arquivado`) fica com a equipe:
   3335 processo CGTE (private) · 3336 listagem alfabética · 3341 orientações
   sobre a base (vira página /sobre) · 3391 dúvidas&sugestões · 3410 GLPI ·
   3422 todos os artigos · 3455 START 2023 · 3463/3464/3465 divulgações de IA.
5. **Categoria da trilha**: o mapa declara categoria por trilha, mas
   `cgte_categoria` só está registrada para `cgte_base` — se o tema precisar
   colorir cards de trilha por categoria, registrar a taxonomia também para
   `cgte_trilha` (mudança no plugin, MR separado).
6. **Subtítulo dos 4 drafts/private classificados** também foi gravado — quando
   forem publicados, já saem completos.
