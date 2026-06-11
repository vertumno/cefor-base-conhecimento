# Fase C — Relatório da extração de mídia

> **Data:** 2026-06-10
> **Fonte:** `BASE ANTIGA - conhecimento-cefor-ifes-edu-br-20260521-103813-9qnt6u1otcrd.wpress`
> (All-in-One WP Migration, 1,48 GB, em `C:\laragon\www\migracao-base-conhecimento\`)
> **Destino:** `C:\laragon\www\migracao-base-conhecimento\extraido\uploads\`
> **Ferramentas:** `scripts/extrair_wpress.py` + `scripts/verificar_uploads.py` (stdlib, Python 3)

## Resultado

| Métrica | Valor |
|---|---|
| Arquivos no container | 9.647 (1.371 MiB) |
| Arquivos em `uploads/` | **1.835 (1.245,7 MiB) — todos extraídos** |
| Attachments do WXR | 430 URLs |
| Attachments encontrados na extração | **423 (98,4%)** |
| URLs `wp-content/uploads` citadas em corpos | 461 — 453 encontradas |
| Integridade | amostra visual OK; mtimes preservados |

O `.wpress` é um container sequencial próprio do All-in-One WP Migration
(cabeçalho de 4377 bytes por entrada — por isso 7-Zip não abre). O DP-11 do
roadmap ("extração pela equipe, com orientação") está resolvido por script:
qualquer pessoa reproduz com

```
python scripts/extrair_wpress.py ARQUIVO.wpress -o PASTA --somente uploads
python scripts/verificar_uploads.py WXR.xml PASTA/uploads
```

## Mídia faltante conhecida (8 arquivos — NÃO é falha da extração)

Os 8 arquivos abaixo constam no WXR mas **não existem no backup nem no
legado-vivo (HTTP 404 verificado em 2026-06-10)** — já estavam quebrados no
site antigo. Afetam principalmente 1 artigo de 2020/04. A curadoria (Fase G)
decide recapturar as telas ou remover as referências.

```
2020/04/1-3.png        2020/04/1-7.png
2020/04/1-5.png        2020/04/1-8.png
2020/04/1-6.png        2020/04/chave.png
2020/04/tela-1.png     2021/03/webconferencia-moodle.jpg  (citada em corpo)
```

## Conteúdo restante do container (não extraído, disponível se precisar)

`themes/` (3.703), `plugins/` (3.681), `wp-all-export/` (353), `languages/` (72)
e 3 arquivos na raiz (12,6 MiB, inclui `database.sql` do legado). Nada disso
migra (roadmap: "não migrar tema zero, plugins do legado").

## Próximo passo (Fase E.1)

Copiar `extraido\uploads\*` para `wp-content\uploads\` do destino, reconstruir
a Media Library e só então reescrever as URLs `conhecimento.cefor.ifes.edu.br`
nos corpos — na ordem que o roadmap define (mídia antes dos artigos).
