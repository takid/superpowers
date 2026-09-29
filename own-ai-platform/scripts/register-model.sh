#!/usr/bin/env bash
# Register a local GGUF with Ollama so it is served through the gateway.
# usage: register-model.sh <name> <file.gguf inside ./models> ["system prompt"]
set -euo pipefail
NAME=${1:?name}; GGUF=${2:?gguf filename}; SYSTEM=${3:-"You are a helpful assistant."}
cd "$(dirname "$0")/.."
[ -f "models/$GGUF" ] || { echo "models/$GGUF not found"; exit 1; }
printf 'FROM /models/%s\nSYSTEM """%s"""\n' "$GGUF" "$SYSTEM" > "models/$NAME.Modelfile"
docker compose exec -T ollama ollama create "$NAME" -f "/models/$NAME.Modelfile"
echo "Ready: use model \"$NAME\" via http://localhost:8080/v1"
