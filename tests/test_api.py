from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    assert client.get("/api/health").status_code == 200

def test_assessment():
    r = client.post("/api/assess", json={"symptoms": [{"name": "fever"}, {"name": "cough"}]})
    assert r.status_code == 200
    assert r.json()["hypotheses"]

def test_red_flag():
    r = client.post("/api/assess", json={"symptoms": [{"name": "difficulty breathing"}]})
    assert r.json()["safety_level"] == "emergency"

def test_labs():
    r = client.post("/api/labs/parse", json={"text": "Hemoglobin 13.5 g/dL"})
    assert r.json()["results"]["hemoglobin"]["value"] == 13.5

def test_models():
    r = client.get("/api/models")
    assert r.status_code == 200
    assert r.json()[0]["clinical_use"] is False
