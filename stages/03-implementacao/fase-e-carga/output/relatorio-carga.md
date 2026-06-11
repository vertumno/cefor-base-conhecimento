# Fase E — Relatório da carga no DESTINO-LOCAL

> **Data:** 2026-06-10
> **Destino:** `C:\laragon\www\conhecimento` (plugin cgte-estrutura v0.3.0 ativo)
> **Backup pré-carga:** `C:\laragon\www\migracao-base-conhecimento\backup-banco-ANTES-media-library.sql`

## E.1 — Media Library

| Métrica | Valor |
|---|---|
| Anexos do WXR | 430 |
| Registrados | **423** (os 7 restantes = mídia já perdida no legado, ver Fase C) |
| Metadados preservados | título, slug, datas, caption, descrição, alt |
| Meta de rastreio | `_cgte_url_legada` (URL original) em todos |

Script: `scripts/reconstruir-media-library.php` (idempotente, dry-run; exige
`-d memory_limit=2048M` — PNGs gigantes no corpus estouram 512M no GD).

## E.2 — Artigos

| Métrica | Valor |
|---|---|
| Inseridos como `cgte_base` | **139/139** (zero erros) |
| Status | 132 publish · 4 draft · 3 private (idêntico ao corpus, DP-1) |
| URLs de mídia reescritas p/ local | 222 (zero restantes apontando pro legado) |
| Colisão com slugs reservados | **nenhuma** |
| Metas gravados | `_cgte_slug_legado` + `_cgte_id_legado` em todos |
| Taxonomias | nenhuma atribuída (curadoria, Fase G) |

Script: `scripts/carregar_artigos.php` (idempotente por `_cgte_id_legado`;
roda como admin para o kses não mutilar blocos `wp:html` com iframe; usa
`slugs_reservados()` do plugin como fonte única). Links internos `/base/{slug}`
ficaram intactos de propósito — o redirect 301 do plugin os resolve.

**QA executado:** URL plana 200 em 9 artigos (1 dirigido + 8 aleatórios),
imagens dos corpos servindo local (200), `/base/{slug}` → 301 → URL plana,
contagens no banco conferidas.

## E.3 — Autores (decisão pendente)

Censo dos autores do legado (artigos por login). Hoje todos os artigos estão
**sem autor** (post_author 0) porque nenhum login existe no destino — exibição
fica vazia (DP-9). Quem a equipe quiser creditar precisa de conta criada e
re-atribuição (o `_cgte_id_legado` permite re-rodar a atribuição por script):

| Login legado | Artigos |
|---|---|
| juliana.cris | 68 |
| elton | 39 |
| marquito | 12 |
| andreia | 7 |
| leonardo | 5 |
| cgti.cefor@ifes.edu.br | 5 |
| admin | 1 |
| tiago | 1 |
| monia.vignati | 1 |

## E.4 — Comentários

Nenhum migrado (DP-10), por construção: o loader não toca em comentários.

## Replicação no servidor de testes

A mesma sequência roda lá: copiar `extraido\uploads` → rodar
`reconstruir-media-library.php` → rodar `carregar_artigos.php`. Os scripts
calculam as URLs pelo `home_url`/`upload_dir` do ambiente, então os corpos
saem com as URLs certas do servidor. Pré-requisitos: plugin v0.3.0 ativo
(já deployado) e os dois arquivos de entrada (uploads extraídos + WXR
convertido da Fase D).
