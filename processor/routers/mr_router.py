from fastapi import APIRouter
from fastapi import File, Form, UploadFile, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse

from .mr_processor.setting_mr import mr
import shutil, random, string

mr_api = APIRouter()

async def after_delete(path):
    shutil.rmtree(path)

async def make_mr(stems: Form, file: UploadFile):
    id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    separation = mr('routers/mr_processor',id)
    send_path, name, path = separation.separating(stems, file)
    # print(send_zip, name)
    return send_path, name, path

@mr_api.post("/make_mr/")             
async def song_mr(background_tasks: BackgroundTasks, stems: int = Form(...), file: UploadFile = File(...)):
    try:
        file_check = ['mp3','wav','m4a']
        if file.filename.split('.')[-1].lower() not in file_check:
            raise HTTPException(status_code=400, detail = "not song file")
        
        send_path, name, path = await make_mr(stems, file)
        background_tasks.add_task(after_delete, path)
        return FileResponse(send_path, filename=name, media_type="application/zip")
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# 음원들에 대해 하나의 음악으로 섞어 하나의 결과물로 만들 수 있도록함
async def mix_mr(file: UploadFile):
    id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    separation_mix = mr('routers/mr_processor', id)
    return_path, delete_path = separation_mix.mix(file)
    return return_path, delete_path

@mr_api.post("/mix_mr/")
async def mix_song_mr(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    return_path, delete_path = await mix_mr(file)
    background_tasks.add_task(after_delete, delete_path)
    return FileResponse(return_path, media_type="audio/wav")