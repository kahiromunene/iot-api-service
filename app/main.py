from fastapi import FastAPI
from app import sensors

app = FastAPI(title="IoT Sensor API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the IoT API"}

# Include sensor routes
app.include_router(sensors.router, prefix="/sensors", tags=["Sensors"])
