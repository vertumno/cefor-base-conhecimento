#!/usr/bin/env bash
# Restaura o banco ao estado ANTERIOR ao import de teste (desfaz tudo).
# O dump traz DROP TABLE + CREATE TABLE por tabela; o import WXR nao cria tabelas
# novas, entao restaurar as tabelas do snapshot remove os posts importados.
set -euo pipefail
MYSQL="/c/laragon/bin/mysql/mysql-5.7.33-winx64/bin/mysql.exe"
SRC="$(dirname "$0")/backup-banco-ANTES-import.sql"
[ -f "$SRC" ] || { echo "ERRO: snapshot nao encontrado em $SRC"; exit 1; }
"$MYSQL" -u root --default-character-set=utf8mb4 baseconhecimento2026 < "$SRC"
echo "Banco restaurado ao estado do snapshot. Import de teste desfeito."
