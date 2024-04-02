# test/routers/post_test.py
from fastapi.testclient import TestClient
from processor.routers.dataset_router import dataset_api
import os

client = TestClient(dataset_api)

def test_hello_dataset():
    response = client.get("/hello_dataset")
    assert response.status_code == 200
    # assert response.json() == [{"name": "item1"}, {"name": "item2"}]


def test_make_dataset():
    now_dir = os.path.dirname(os.path.abspath(__file__))
    testfile = os.path.join(now_dir, "test.mp3")
    with open(testfile, "rb") as f:
        testfile = f.read()
    
    testfile = {"file": ("test.mp3", testfile, "audio/mpeg")}
    response = client.post("/make_dataset/",files=testfile)
    assert response.status_code == 200
