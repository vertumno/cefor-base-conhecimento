# Relatório — Replicação do DESTINO-LOCAL no servidor de testes

**Data:** 2026-06-11
**Executor:** Marcos + Claude (sessão assistida)
**Status:** ✅ concluída — https://testes.cefor.ifes.edu.br/ navegável com o conteúdo completo

Fecha a pendência adiada da Fase E ("Replicação no servidor de testes") e serve de
**ensaio do procedimento de promoção da Fase I** (DESTINO-LOCAL → SERVIDOR-NOVO com
search-replace de domínio).

## Método: clone de banco ("Caminho A")

Em vez de re-rodar o pipeline de carga/curadoria no servidor (onde os `wp_id` mudariam e o
`mapeamento-curadoria.json`, chaveado por ID, não valeria), o estado final do banco local —
já validado — foi promovido por dump + import. Restrição de acesso: sem shell no servidor;
apenas banco de dados (via VPN) e aplicação pela URL. Foi suficiente.

## Pré-condições verificadas

1. **Código no servidor**: MR `feature/cgte-tema` mergeado na main do GitLab (merge
   `6a706ef`) → deploy automático via CI; tema `cgte` e plugin `cgte-estrutura` já ativos
   no destino (options `template`/`stylesheet`/`active_plugins` conferidas no banco).
2. **Banco remoto era descartável**: só 2 artigos de teste (confirmado por Marcos).
3. **Uploads**: já existiam no servidor (cópia prévia — provavelmente CGTI). Amostra de
   1 arquivo por ano (2016–2026) respondeu 200. O passo de cópia de 1,2 GiB não foi
   necessário.

## Passo a passo executado

1. **Backup do banco remoto** (antes de qualquer escrita):
   `mysqldump --single-transaction --no-tablespaces --add-drop-table` →
   `backup-testes-ANTES-import-2026-06-11.sql` (em `C:\laragon\www\migracao-base-conhecimento\`).
   O usuário do banco não tem privilégio PROCESS → `--no-tablespaces` é obrigatório.
2. **Dump local transformado** com wp-cli (substituição segura para dados serializados):
   ```
   php wp-cli.phar search-replace 'http://localhost/conhecimento' 'https://testes.cefor.ifes.edu.br' \
     wp_commentmeta wp_comments wp_links wp_options wp_postmeta wp_posts \
     wp_term_relationships wp_term_taxonomy wp_termmeta wp_terms \
     --export=dump-local-para-testes-2026-06-11.sql
   ```
   730 substituições (siteurl/home, post_content, guids). **`wp_users` e `wp_usermeta`
   ficaram de fora** — os logins do servidor (administrador/elton/marquito) foram
   preservados; o usuário local não foi promovido.
3. **Conferência do dump**: DROP+CREATE das 10 tabelas presentes; zero ocorrências
   residuais de `localhost/conhecimento`; 2 menções a "laragon" inofensivas (option
   `recently_edited` e texto legítimo de artigo).
4. **Import no remoto**: o MySQL do servidor roda em sql_mode estrito e rejeita as datas
   zero do dump (`Invalid default value for 'comment_date'`). Importar com:
   ```
   mysql --init-command="SET SESSION sql_mode='';" --default-character-set=utf8mb4 ... < dump.sql
   ```
5. **Pós-import** (SQL direto):
   - `DELETE` das options `rewrite_rules` (regenera no primeiro hit, já com as regras do
     plugin — a option versionada `cgte_estrutura_rewrite_version` veio no dump e bate com
     a versão do código, então não haveria flush automático) e `recently_edited` (caminhos
     locais).
   - `active_plugins` reescrito para conter só `cgte-estrutura/cgte-estrutura.php` (o
     dump trazia também o `wordpress-importer`, que não existe no servidor).

## QA (tudo pela URL pública, via VPN)

| Rota | Resultado |
|---|---|
| `/` (home com vitrine) | 200 |
| `/artigos/` (catálogo) | 200 |
| `/trilhas/` | 200 |
| `/percursos/dominando-o-moodle/` | 200 |
| Artigo em URL plana | 200 |
| `/buscar/?q=moodle` | 200 |
| `/base/{slug}` (legado) | 301 → URL plana |
| Uploads (amostra 2016–2026) | 200 |

Estado final do banco: 132 `cgte_base` publish (+3 draft, +3 private), 424 attachments,
9 trilhas publish (+1 draft), 1 percurso. Usuários remotos intactos.

Ressalva conhecida: 1 attachment com guid apontando para permalink (não para arquivo)
responde 301 — cosmético, sem mídia faltando.

## Procedimento repetível (promoções futuras local → testes)

O mesmo trio resolve qualquer promoção de conteúdo: **backup remoto → dump local com
search-replace → import com sql_mode permissivo → limpar `rewrite_rules`**. Artefatos e
wp-cli.phar ficam em `C:\laragon\www\migracao-base-conhecimento\`. Credenciais do banco:
com Marcos/CGTI (não versionadas aqui).

Para a **Fase I** (go-live no domínio definitivo), o procedimento é idêntico, trocando o
domínio-alvo do search-replace — somado aos itens próprios da fase (redirects 301 da base
antiga, DP-8, DP-12).
