from fastapi import APIRouter
from fastapi import File, Form, UploadFile, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse

from .mr_processor.setting_mr import mr
import shutil, random, string

mr_api = APIRouter()

def after_delete(path):
    shutil.rmtree(path)

def make_mr(stems: Form, file: UploadFile):
    id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    separation = mr('routers/mr_processor',id)
    send_path,path = separation.separating(stems, file)
    # print(send_zip, name)
    return send_path,path

import time

@mr_api.post("/make_mr/")             
def song_mr(
            background_tasks: BackgroundTasks, 
            stems: int = Form(None), 
            file: UploadFile = File(...)):
    start = time.time()

    
    if stems is None:
        stems = 2

    try:
        file_check = ['mp3','wav']
        if file.filename.split('.')[-1].lower() not in file_check:
            raise HTTPException(status_code=400, detail = "not song file")
                        #await
        send_path,path = make_mr(stems, file)
        background_tasks.add_task(after_delete, path)

        end = time.time()
        print(end - start)

        # print(file.file)
        # print(FileResponse(send_path,  media_type="application/zip"))

        return FileResponse(send_path,  media_type="application/zip")

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def mix_mr(file: UploadFile):
    id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    separation_mix = mr('routers/mr_processor', id)
    return_path, delete_path = separation_mix.mix(file)
    return return_path, delete_path

@mr_api.post("/mix_mr/")
def mix_song_mr(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    return_path, delete_path = mix_mr(file)
    background_tasks.add_task(after_delete, delete_path)
    return FileResponse(return_path, media_type="audio/wav")