from fastapi.testclient import TestClient
from api.main import app

testClient = TestClient(app)

def test_api_health():
    response = testClient.get("/api/health")
    assert response.status_code == 200
    assert response.status == "healthy"
    assert response.checks.fastAPI == "running"