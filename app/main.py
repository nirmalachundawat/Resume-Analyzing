from fastapi import FastAPI
from app.routes import predict

app = FastAPI()

app.include_router(predict.router)

@app.get("/")
def home():
    return {"message": "Resume Analyzer API is running "}