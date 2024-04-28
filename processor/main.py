#export PATH=$PATH:/c/Users/axels/OneDrive/바탕\ 화면/translation_AI/ff_path
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
ff_path = os.path.join(current_directory, "ff_path")
os.environ["PATH"] = f'{os.environ["PATH"]};{ff_path}'

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

# uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4

