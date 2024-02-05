#export PATH=$PATH:/c/Users/axels/OneDrive/바탕\ 화면/translation_AI/ffmpeg-6.1.1-full_build/bin
#export PATH=$PATH:/c/Users/axels/OneDrive/바탕\ 화면/translation_AI/ff_path

from fastapi import FastAPI, File, Form, UploadFile, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import aiofiles
import shutil
import os
import random, string
import subprocess

from audio_processor.setting_dataset import data_processing
from audio_processor.setting_mr import mr

current_directory = os.path.dirname(os.path.abspath(__file__))

# ff_path를 포함한 전체 경로
ff_path = os.path.join(current_directory, "ff_path")

# 환경 변수에 현재 디렉토리의 ff_path 추가
os.environ["PATH"] = f'{os.environ["PATH"]};{ff_path}'

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def after_delete(path):
    shutil.rmtree(path)

async def make_dataset(hz: Form, interval_seconds: Form, file: UploadFile):
    wav_id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    processor = data_processing('audio_processor/dataset', interval_seconds, hz, wav_id)
    zip_path, delete_path = processor.processing(file)

    return zip_path, delete_path

@app.post("/make_dataset/")
async def processing(background_tasks: BackgroundTasks, hz: int = Form(...), interval_seconds: int = Form(...), file: UploadFile = File(...)):
    path, delete_path = await make_dataset(hz, interval_seconds, file)
    background_tasks.add_task(after_delete, delete_path)
    return FileResponse(path, filename="dataset.zip", media_type="application/zip")


async def make_mr(stems: Form, file: UploadFile):
    id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    separation = mr('audio_processor/mr',id)
    zip_path, zip_name, delete_path = separation.separating(stems, file)
    print(zip_path, zip_name, delete_path)
    return zip_path, zip_name, delete_path                  

@app.post("/make_mr/")             
async def song_mr(
                    background_tasks: BackgroundTasks, 
                    stems: int = Form(...), file: UploadFile = File(...)
                ):

    zip_path, zip_name, delete_path = await make_mr(stems, file)
    background_tasks.add_task(after_delete, delete_path)
    return FileResponse(zip_path, filename=zip_name, media_type="application/zip")

# async def add_mr(zip_file: UploadFile):
#     id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
#     separation_to_add = mr('audio_processor/mr', id)

# @app.post("/add_mr/")
# async def add_song_mr(background_tasks: BackgroundTasks, zip_file: UploadFile = File(...)):
    




















@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__=='__main__': 
    uvicorn.run(app, host='0.0.0.0', port = 8000)
