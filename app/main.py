from fastapi import FastAPI
from fastapi.testclient import TestClient
from app import sensors

app = FastAPI()

app.include_router(sensors.router, prefix="/sensors", 
tags=["Sensors"])


@app.get("/")
def root():
    return {"message": "IoT API is running"}
