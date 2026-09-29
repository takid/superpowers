"""OpenAI-compatible gateway in front of Ollama.

- Per-app API keys (create/revoke with the admin key)
- Streams responses, passes /v1/* straight through to Ollama
- Logs usage per key + model in SQLite
Point any OpenAI SDK at http://<host>:8080/v1 with one of your keys.
"""
import hashlib
import json
import os
import secrets
import sqlite3
import time

import httpx
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, StreamingResponse
from starlette.background import BackgroundTask

UPSTREAM = os.environ.get("UPSTREAM_URL", "http://localhost:11434")
DB_PATH = os.environ.get("DB_PATH", "gateway.db")
ADMIN_KEY = os.environ.get("ADMIN_KEY", "")

app = FastAPI(title="Own AI Gateway")
client = httpx.AsyncClient(base_url=UPSTREAM, timeout=None)


def db():
    con = sqlite3.connect(DB_PATH)
    con.execute("CREATE TABLE IF NOT EXISTS keys(hash TEXT PRIMARY KEY, name TEXT, created REAL, revoked INT DEFAULT 0)")
    con.execute("CREATE TABLE IF NOT EXISTS usage(ts REAL, key_name TEXT, path TEXT, model TEXT, status INT)")
    return con


def h(key: str) -> str:
    return hashlib.sha256(key.encode()).hexdigest()


def bearer(req: Request) -> str:
    auth = req.headers.get("authorization", "")
    return auth[7:] if auth.lower().startswith("bearer ") else ""


def require_admin(req: Request):
    if not ADMIN_KEY or not secrets.compare_digest(bearer(req), ADMIN_KEY):
        raise HTTPException(401, "admin key required")


@app.get("/health")
async def health():
    return {"ok": True}


@app.post("/admin/keys")
async def create_key(req: Request, name: str):
    require_admin(req)
    key = "sk-own-" + secrets.token_urlsafe(32)
    with db() as con:
        con.execute("INSERT INTO keys VALUES(?,?,?,0)", (h(key), name, time.time()))
    return {"name": name, "key": key, "note": "shown once, store it now"}


@app.delete("/admin/keys/{name}")
async def revoke_key(req: Request, name: str):
    require_admin(req)
    with db() as con:
        con.execute("UPDATE keys SET revoked=1 WHERE name=?", (name,))
    return {"revoked": name}


@app.get("/admin/usage")
async def usage(req: Request):
    require_admin(req)
    with db() as con:
        rows = con.execute(
            "SELECT key_name, model, COUNT(*) FROM usage GROUP BY key_name, model ORDER BY 3 DESC"
        ).fetchall()
    return [{"key": k, "model": m, "requests": n} for k, m, n in rows]


def key_name(token: str):
    with db() as con:
        r = con.execute("SELECT name FROM keys WHERE hash=? AND revoked=0", (h(token),)).fetchone()
    return r[0] if r else None


@app.api_route("/v1/{path:path}", methods=["GET", "POST"])
async def proxy(path: str, req: Request):
    token = bearer(req)
    name = "admin" if ADMIN_KEY and secrets.compare_digest(token, ADMIN_KEY) else key_name(token)
    if not name:
        return JSONResponse({"error": {"message": "invalid API key"}}, status_code=401)

    body = await req.body()
    model = ""
    if body:
        try:
            model = json.loads(body).get("model", "")
        except ValueError:
            pass

    upstream = client.build_request(
        req.method, f"/v1/{path}", content=body,
        headers={"content-type": req.headers.get("content-type", "application/json")},
    )
    r = await client.send(upstream, stream=True)
    with db() as con:
        con.execute("INSERT INTO usage VALUES(?,?,?,?,?)", (time.time(), name, path, model, r.status_code))

    return StreamingResponse(
        r.aiter_bytes(), status_code=r.status_code,
        media_type=r.headers.get("content-type"), background=BackgroundTask(r.aclose),
    )
