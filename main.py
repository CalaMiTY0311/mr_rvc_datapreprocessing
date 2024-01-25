from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse, FileResponse
import uvicorn
import aiofiles
import shutil
import os

from audio_processor.setting_dataset import data_processing

app = FastAPI()

async def make_dataset(file: UploadFile):
    dataset_dir = os.path.join('audio_processor', 'dataset')
    file_path = os.path.join(dataset_dir, file.filename)
    
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    
    processor = data_processing(dataset_dir, 15)
    processor.processing()

    return {"filename": file.filename, "dataset_path": os.path.join(dataset_dir, 'dataset.zip')}

@app.post("/make_dataset/")
async def processing(file: UploadFile = File(...)):
    result = await make_dataset(file)
    return JSONResponse(content=result, status_code=200)

@app.get("/download_dataset/")
async def download_dataset():
    dataset_path = os.path.join('audio_processor', 'dataset', 'dataset.zip')
    
    if not os.path.exists(dataset_path):
        raise HTTPException(status_code=404, detail="Dataset not found")
    
    return FileResponse(dataset_path, filename="dataset.zip", media_type="application/zip")





















@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__=='__main__': 
    uvicorn.run(app, host='0.0.0.0', port = 8000)
