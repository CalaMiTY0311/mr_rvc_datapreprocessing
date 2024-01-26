from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse, FileResponse
import uvicorn
import aiofiles
import shutil
import os
import random, string

from audio_processor.setting_dataset import data_processing

app = FastAPI()

async def make_dataset(file: UploadFile):
    wav_id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    processor = data_processing('audio_processor/dataset', 15, wav_id)
    dataset = processor.processing(file)

    return {"filename": file.filename}

@app.post("/make_dataset/")
async def processing(file: UploadFile = File(...)):
    result = await make_dataset(file)
    return JSONResponse(content=result, status_code=200)

# @app.get("/download_dataset/")
# async def download_dataset():
#     dataset_path = os.path.join('audio_processor', 'dataset', 'dataset.zip')
    
#     if not os.path.exists(dataset_path):
#         raise HTTPException(status_code=404, detail="Dataset not found")
    
#     return FileResponse(dataset_path, filename="dataset.zip", media_type="application/zip")





















@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__=='__main__': 
    uvicorn.run(app, host='0.0.0.0', port = 8000)
