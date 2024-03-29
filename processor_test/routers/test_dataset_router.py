# test/routers/post_test.py
from fastapi.testclient import TestClient
from processor.routers.dataset_router import dataset_api
from starlette.datastructures import UploadFile

client = TestClient(dataset_api)

def test_hello_dataset():
    response = client.get("/hello_dataset")
    assert response.status_code == 200
    # assert response.json() == [{"name": "item1"}, {"name": "item2"}]

def test_make_dataset():
    test_file_path = "After_You.mp3"
    with open(test_file_path, "rb") as file:
        test_file_content = file.read()
    test_file = UploadFile(filename="data_processing.mp3", content=test_file_content, content_type="audio/mpeg")
    response = client.post("/make_dataset/", 
                           data={"hz": 16000, "interval_seconds": 15},
                           files={"file": ("data_processing.mp3", test_file, "audio/mpeg")})
    assert response.status_code == 200
