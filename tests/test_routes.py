from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json()["message"] == "tldw server"

def test_summarize_route():
    resp = client.post("/summarize", json={"text": "one two three four five six"})
    assert resp.status_code == 200
    assert "summary" in resp.json()
