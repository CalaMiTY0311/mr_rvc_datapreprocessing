#export PATH=$PATH:/c/Users/axels/OneDrive/바탕\ 화면/translation_AI/ff_path
# current_directory = os.path.dirname(os.path.abspath(__file__))
# ff_path = os.path.join(current_directory, "ff_path")
# os.environ["PATH"] = f'{os.environ["PATH"]};{ff_path}'

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from routers.dataset_router import dataset_api
from routers.mr_router import mr_api

app = FastAPI()
app.include_router(dataset_api)
app.include_router(mr_api)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return {"message": "Hello world"}

# # 음원들에 대해 하나의 음악으로 섞어 하나의 결과물로 만들 수 있도록함
# async def mix_mr(file: UploadFile):
#     id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
#     separation_mix = mr('audio_processor/mr', id)
#     return_path, delete_path = separation_mix.mix(file)
#     return return_path, delete_path

# @app.post("/mix_mr/")
# async def mix_song_mr(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
#     return_path, delete_path = await mix_mr(file)
#     background_tasks.add_task(after_delete, delete_path)
#     return FileResponse(return_path, media_type="audio/wav")


# uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4

