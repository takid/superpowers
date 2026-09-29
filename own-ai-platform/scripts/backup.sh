#!/usr/bin/env bash
# Back up models, keys/usage DB and chat history to ./backups (copy that folder off-machine too).
set -euo pipefail
cd "$(dirname "$0")/.."; mkdir -p backups
for v in ollama gateway webui; do
  docker run --rm -v "own-ai-platform_${v}:/d:ro" -v "$PWD/backups:/b" alpine \
    tar czf "/b/${v}-$(date +%F).tgz" -C /d .
done
echo "Backups in ./backups"
