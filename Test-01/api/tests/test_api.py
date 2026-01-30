from fastapi.testclient import TestClient
from api.main import app
client = TestClient(app)

def test_healthcheck_endpoint():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert "application_status" in response.json()

def test_add_status_endpoint():
    payload = {
        "application_name": "rbcapp1",
        "service_name": "httpd",
        "service_status": "UP",
        "host_name": "testhost",
        "timestamp": "2026-01-30T12:00:00Z"
    }
    response = client.post("/add", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Document indexed successfully"

def test_service_status_endpoint():
    response = client.get("/healthcheck/httpd")
    assert response.status_code == 200
    assert "service_name" in response.json() or "status" in response.json()

def test_add_status_invalid_payload():
    payload = {
        "application_name": "rbcapp1",
        "service_name": "httpd"
    }
    response = client.post("/add", json=payload)
    assert response.status_code == 422
    assert response.json()["success"] is False or response.json().get("message") == "Validation error"