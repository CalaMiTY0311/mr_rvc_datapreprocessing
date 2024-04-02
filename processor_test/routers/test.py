from starlette.datastructures import UploadFile

test_file_path = "test.mp3"
with open(test_file_path, "rb") as file:
    test_file = UploadFile(filename="test.mp3", file=file, content_type="audio/mpeg")

# test_file = UploadFile(filename="test.mp3", file=test_file_path , content_type="audio/mpeg")
print(test_file)