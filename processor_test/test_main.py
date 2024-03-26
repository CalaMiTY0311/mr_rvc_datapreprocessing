from fastapi.testclient import TestClient
from mr_rvc_datapreprocessing.main import app

client = TestClient(app)

def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg" : "Hello World"}