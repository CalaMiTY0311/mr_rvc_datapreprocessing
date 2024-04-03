# test/routers/post_test.py
from fastapi.testclient import TestClient
from routers.dataset_router import dataset_api
from routers_test.filepath import filepath
import os

client = TestClient(dataset_api)

# mp3
def test_mp3():
    testfile = filepath()
    testfile = os.path.join(testfile,"test.mp3")
    with open(testfile, "rb") as f:
        testfile = f.read()
    
    testfile = {"file": ("test.mp3", testfile, "audio/mpeg")}
    response = client.post("/make_dataset/",files=testfile)
    assert response.status_code == 200

# wav
def test_wav():
    testfile = filepath()
    testfile = os.path.join(testfile,"test.wav")
    with open(testfile, "rb") as f:
        testfile = f.read()
    
    testfile = {"file": ("test.mp3", testfile, "audio/mpeg")}
    response = client.post("/make_dataset/",files=testfile)
    assert response.status_code == 200



# def test_hello_dataset():
#     response = client.get("/hello_dataset")
#     assert response.status_code == 200