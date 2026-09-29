# Own AI Platform

Your own model host. Run any open model, fine-tune your own, serve it through an
OpenAI-compatible API with your own keys. No licence fees, no usage limits, no vendor.

```
Your apps / Zapier / Make ──► Gateway :8080 (API keys, usage log) ──► Ollama (models)
Browser chat ───────────────► Open WebUI :3000 ─────────────────────► Ollama
```

## Start

```bash
cp .env.example .env          # set ADMIN_KEY (openssl rand -hex 32)
make up                       # or: make up-gpu  (NVIDIA)
make pull MODEL=llama3.2:3b
make key NAME=website         # prints an API key, once
```

Chat: http://localhost:3000 · API: http://localhost:8080/v1 (any OpenAI SDK, `model="llama3.2:3b"`)

```bash
curl localhost:8080/v1/chat/completions -H "Authorization: Bearer sk-own-..." \
  -H "Content-Type: application/json" \
  -d '{"model":"llama3.2:3b","messages":[{"role":"user","content":"Hello"}]}'
```

## Train your own model

1. Put examples in JSONL (see `train/example-data.jsonl`): real enquiries and the replies you'd stand behind.
2. Run `train/finetune.py` on a GPU. No GPU? Free Colab or Kaggle notebooks work for 3B-class models.
3. Drop the `.gguf` into `models/`, then `make register NAME=my-model GGUF=my-model.gguf`.
4. Iterate: add data, retrain, register again under a new name, compare, keep the winner.

## Run it 24/7

- Machine: an always-on PC or mini PC at home or the office. A 16GB+ RAM box runs 3B–8B models on CPU; a used RTX 3060 12GB makes it fast.
- Remote access: set `CLOUDFLARE_TUNNEL_TOKEN` in `.env`, then `docker compose --profile tunnel up -d`. Free, no port forwarding.
- Auto-restart is on (`restart: unless-stopped`). `make backup` weekly and copy `backups/` off the machine.

## What "free" means here

Software: free forever (Ollama, Open WebUI, Unsloth are open source; this repo is yours).
Compute and electricity: yours to supply. Nobody offers free unlimited GPUs for life, so
anything claiming to is a trial with strings. Owning the box is the only version with none.

## Security

Only the gateway and web UI are exposed. Ollama is not published. Keep `.env` private,
give each app its own key, revoke with `DELETE /admin/keys/<name>`.
Open WebUI: first account created becomes admin, so create yours before exposing it.

## Test

`make test` (gateway auth, key lifecycle, usage logging).
