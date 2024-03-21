from fastapi import APIRouter
from fastapi import FastAPI, File, Form, UploadFile, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse, FileResponse
from .dataset_processor.setting_dataset import data_processing
import random
import string
import shutil

dataset_api = APIRouter()

async def after_delete(path):
    shutil.rmtree(path)

# 실시간 음성 변환을 하기 전 학습에 필요한 데이터셋을 hz와 interval_seconds에 맞게 변환
# interval_seconds <- 예를 들어 값이 15이면 학습시키기위한 데이터셋이 15초 간격으로 나뉘어질것이고
# hz의 값을 본인이 원하는대로 값으로 변경가능 ( 모델마다 특정 hz에 맞춰줘야하기에 필요로하여 구현 )
async def make_dataset(hz: Form, interval_seconds: Form, file: UploadFile):
    wav_id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    processor = data_processing('routers/dataset_processor', interval_seconds, hz, wav_id)
    zip_path, delete_path = processor.processing(file)

    return zip_path, delete_path

@dataset_api.post("/make_dataset/")
async def processing(
                        background_tasks: BackgroundTasks, 
                        hz: int = Form(...), interval_seconds: int = Form(...), 
                        file: UploadFile = File(...)):
    try:
        file_check = ['mp3','wav','m4a']
        if file.filename.split('.')[-1].lower() not in file_check:
            raise HTTPException(status_code=400, detail = "not song file")
        
        path, delete_path = await make_dataset(hz, interval_seconds, file)
        background_tasks.add_task(after_delete, delete_path)
        return FileResponse(path, filename="dataset.zip", media_type="application/zip")
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
