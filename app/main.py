from fastapi import FastAPI
from app import sensors

app = FastAPI()

app.include_router(sensors.router, prefix="/sensors", tags=["Sensors"])

@app.get("/")
def root():
    return {"message": "IoT API is running"}
