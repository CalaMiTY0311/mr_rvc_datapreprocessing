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

ff_path = os.path.join(current_directory, "ff_path")

os.environ["PATH"] = f'{os.environ["PATH"]};{ff_path}'

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# mr과 dataset에 id 명으로된 폴더들이 쌓이지 않도록 반환이 완료되면 path경로 파일 삭제
async def after_delete(path):
    shutil.rmtree(path)

# 실시간 음성 변환을 하기 전 학습에 필요한 데이터셋을 hz와 interval_seconds에 맞게 변환
# interval_seconds <- 예를 들어 값이 15이면 학습시키기위한 데이터셋이 15초 간격으로 나뉘어질것이고
# hz의 값을 본인이 원하는대로 값으로 변경가능 ( 모델마다 특정 hz에 맞춰줘야하기에 필요로하여 구현 )
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


# MR (Music Recorded) 이란 노래반주 및 연주음 감상을 목적으로 가수의 목소리가 빠진 연주만으로 제작된 음원을 지칭한다.
# stems는 Form로 입력 받으며 2,4,5의 값 만 들어갈수있음 
# 2 : 보컬(노래하는 목소리) / 반주 (2음원)          4 : 보컬/드럼/베이스/나머지 (4음원)             5 : 보컬/드럼/베이스/피아노/나머지 (5음원)
# stems으로 나눠진 wav파일들은 zip으로 반환된다.
async def make_mr(stems: Form, file: UploadFile):
    id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    separation = mr('audio_processor/mr',id)
    zip_path, zip_name, delete_path = separation.separating(stems, file)
    print(zip_path, zip_name, delete_path)
    return zip_path, zip_name, delete_path

@app.post("/make_mr/")             
async def song_mr(background_tasks: BackgroundTasks, stems: int = Form(...), file: UploadFile = File(...)):

    zip_path, zip_name, delete_path = await make_mr(stems, file)
    background_tasks.add_task(after_delete, delete_path)
    return FileResponse(zip_path, filename=zip_name, media_type="application/zip")


# 음원들에 대해 하나의 음악으로 섞어 하나의 결과물로 만들 수 있도록함
async def mix_mr(file: UploadFile):
    id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    separation_mix = mr('audio_processor/mr', id)
    return_path, delete_path = separation_mix.mix(file)
    return return_path, delete_path

@app.post("/mix_mr/")
async def mix_song_mr(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    return_path, delete_path = await mix_mr(file)
    background_tasks.add_task(after_delete, delete_path)
    return FileResponse(return_path, media_type="audio/wav")

    
    




















# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


if __name__=='__main__': 
    uvicorn.run(app, host='0.0.0.0', port = 8000)
