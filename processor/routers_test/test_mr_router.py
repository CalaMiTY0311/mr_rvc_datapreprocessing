from fastapi.testclient import TestClient
from routers.mr_router import mr_api
from routers_test.filepath import filepath
import os

dir = os.path.dirname(os.path.abspath(__file__))
dir = os.path.dirname(dir)
ff_path = os.path.join(dir, "ff_path")
os.environ["PATH"] = f'{os.environ["PATH"]};{ff_path}'

client = TestClient(mr_api)

def test_make_mr():
    testfile = filepath()
    testfile = os.path.join(testfile, "test.mp3")

    with open(testfile, "rb") as f:
        testfile = f.read()

    testfile = {"file": ("test.mp3", testfile, "audio/mpeg")}
    response = client.post("/make_mr/",files=testfile)
    print(response)
    assert response.status_code == 200

def test_mix_mr():
    testfile = filepath()
    testfile = os.path.join(testfile, "test.zip")

    with open(testfile, "rb") as f:
        testfile = f.read()

    testfile = {"file": ("test.zip", testfile, "application/zip")}
    response = client.post("/mix_mr/",files=testfile)
    print(response)
    assert response.status_code == 200

