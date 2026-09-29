import os, importlib
os.environ.update(ADMIN_KEY="admin-secret", DB_PATH="/tmp/gw_test.db")
if os.path.exists("/tmp/gw_test.db"): os.remove("/tmp/gw_test.db")
import httpx
from fastapi.testclient import TestClient
import app as gw

def fake_upstream(request):
    return httpx.Response(200, json={"echo": request.url.path, "body": request.content.decode()})

gw.client = httpx.AsyncClient(base_url="http://up", transport=httpx.MockTransport(fake_upstream))
c = TestClient(gw.app)
A = {"Authorization": "Bearer admin-secret"}

def test_rejects_without_key():
    assert c.post("/v1/chat/completions", json={"model": "x"}).status_code == 401

def test_key_lifecycle_and_usage():
    key = c.post("/admin/keys?name=website", headers=A).json()["key"]
    r = c.post("/v1/chat/completions", json={"model": "mymodel"}, headers={"Authorization": f"Bearer {key}"})
    assert r.status_code == 200 and r.json()["echo"] == "/v1/chat/completions"
    assert {"key": "website", "model": "mymodel", "requests": 1} in c.get("/admin/usage", headers=A).json()
    c.delete("/admin/keys/website", headers=A)
    assert c.post("/v1/chat/completions", json={}, headers={"Authorization": f"Bearer {key}"}).status_code == 401

def test_admin_endpoints_locked():
    assert c.post("/admin/keys?name=x").status_code == 401
