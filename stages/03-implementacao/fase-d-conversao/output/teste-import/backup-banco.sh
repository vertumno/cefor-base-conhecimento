#!/usr/bin/env bash
# Snapshot do banco do DESTINO-LOCAL antes do import de teste (Fase D).
# Servidor MySQL ativo no Laragon: 5.7.33. Banco: baseconhecimento2026 (root, sem senha).
set -euo pipefail
DUMP="/c/laragon/bin/mysql/mysql-5.7.33-winx64/bin/mysqldump.exe"
DEST="$(dirname "$0")/backup-banco-ANTES-import.sql"
"$DUMP" -u root --default-character-set=utf8mb4 --single-transaction --routines --triggers \
  baseconhecimento2026 > "$DEST"
echo "Snapshot salvo em: $DEST"
