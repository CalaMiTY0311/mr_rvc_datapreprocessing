from fastapi.testclient import TestClient
from processor.routers.mr_router import mr_api
import os

client = TestClient(mr_api)

def test_make_mr():
    now_dir = os.path.dirname(os.path.abspath(__file__))
    testfile = os.path.join(now_dir, "test.mp3")
    with open(testfile, "rb") as f:
        testfile = f.read()

    testfile = {"file": ("test.mp3", testfile, "audio/mpeg")}
    response = client.post("/make_mr/",files=testfile)
    assert response.status_code == 200