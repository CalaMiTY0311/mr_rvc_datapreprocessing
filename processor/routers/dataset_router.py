from fastapi import APIRouter
from fastapi import File, Form, UploadFile, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
from .dataset_processor.setting_dataset import data_processing
import random
import string
import shutil

dataset_api = APIRouter()

def after_delete(path):
    shutil.rmtree(path)

def make_dataset(hz: Form, interval_seconds: Form, file: UploadFile):
    wav_id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    processor = data_processing('routers/dataset_processor', interval_seconds, hz, wav_id)
    zip_path, delete_path = processor.processing(file)

    return zip_path, delete_path

import time

@dataset_api.post("/make_dataset/")
def processing(
                    background_tasks: BackgroundTasks, 
                    hz: int = Form(None), 
                    interval_seconds: int = Form(None), 
                    file: UploadFile = File(...)
                    ):
    start = time.time()
    # default hz and interval_seconds
    if hz is None:
        hz = 16000
    if interval_seconds is None:
        interval_seconds = 15

    try:
        file_check = ['mp3','wav']
        if file.filename.split('.')[-1].lower() not in file_check:
            raise HTTPException(status_code=400, detail = "not song file")
                            # await
        path, delete_path = make_dataset(hz, interval_seconds, file)
        background_tasks.add_task(after_delete, delete_path)

        end = time.time()
        print(end - start)
        return FileResponse(path, 
                            # filename="dataset.zip", 
                            media_type="application/zip")
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
