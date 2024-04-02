# test/routers/post_test.py
from fastapi.testclient import TestClient
from processor.routers.dataset_router import dataset_api
from starlette.datastructures import UploadFile
import os

client = TestClient(dataset_api)

def test_hello_dataset():
    response = client.get("/hello_dataset")
    assert response.status_code == 200
    # assert response.json() == [{"name": "item1"}, {"name": "item2"}]


def test_make_dataset():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 테스트 파일의 절대 경로
    test_file_path = os.path.join(current_dir, "test.mp3")
    
    with open(test_file_path, "rb") as f:
        test_file_content = f.read()
    
    # 파일 내용을 기반으로 dict 구성
    test_file = {"file": ("test.mp3", test_file_content, "audio/mpeg")}
    
    data = {"hz": 16000, "interval_seconds": 10}
    
    response = client.post("/make_dataset/", data=data, files=test_file)
    
    assert response.status_code == 200
    # assert response.json() == {"message": "Dataset created successfully."}

# def test_make_dataset():
#     test_file_path = "test.mp3"
#     test_file = UploadFile(filename="test.mp3", file=test_file_path, content_type="audio/mpeg")
#     data = {"hz": 16000, "interval_seconds": 10}
    
#     # FastAPI 엔드포인트 호출
#     response = client.post("/make_dataset/", data=data, files={"file": ("test.mp3", test_file, "audio/mpeg")})
    
#     # 예상되는 응답 상태 코드 확인
#     assert response.status_code == 200