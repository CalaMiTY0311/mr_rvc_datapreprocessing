from fastapi.testclient import TestClient
from processor.main import app

client = TestClient(app)

def test_main():
    response = client.get("/")
    assert response.status_code == 200
    # assert response.json() == {"msg" : "Hello World"}