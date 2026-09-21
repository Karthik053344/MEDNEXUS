from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/api/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_assessment():
    payload = {
        "age": 30,
        "sex": "unknown",
        "symptoms": [{"name":"fever"},{"name":"cough"},{"name":"fatigue"}],
        "history": [],
        "medications": [],
        "allergies": [],
        "vitals": {},
        "labs": {}
    }
    r = client.post("/api/assess", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert data["assessment_id"]
    assert data["hypotheses"]

def test_red_flag():
    payload = {"symptoms":[{"name":"difficulty breathing"}]}
    r = client.post("/api/assess", json=payload)
    assert r.status_code == 200
    assert r.json()["safety_level"] == "emergency"
