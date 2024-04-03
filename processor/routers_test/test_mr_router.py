from fastapi.testclient import TestClient
from routers.mr_router import mr_api
from routers_test.filepath import filepath
import os

client = TestClient(mr_api)

def test_make_mr():
    testfile = filepath()
    testfile = os.path.join(testfile, "test.mp3")

    with open(testfile, "rb") as f:
        testfile = f.read()

    testfile = {"file": ("test.mp3", testfile, "audio/mpeg")}
    response = client.post("/make_mr/",files=testfile)
    assert response.status_code == 200