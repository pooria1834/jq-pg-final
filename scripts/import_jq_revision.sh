#!/usr/bin/env bash
set -euo pipefail
REF="${1:?Usage: scripts/import_jq_revision.sh FULL_JQ_SHA}"
UPSTREAM="${JQ_UPSTREAM:-$(pwd)/../jq-upstream}"
if ! git -C "$UPSTREAM" cat-file -e "${REF}^{commit}"; then
  echo "Upstream revision not available in $UPSTREAM: $REF" >&2
  exit 1
fi
rm -rf jq-src
mkdir -p jq-src
git -C "$UPSTREAM" archive "$REF" | tar -x -C jq-src
cp tooling/PGMakefile jq-src/PGMakefile
printf 'Imported jq %s
' "$REF"
