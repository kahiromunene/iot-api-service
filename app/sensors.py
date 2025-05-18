from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Simulated in-memory DB
sensor_data = []

class SensorReading(BaseModel):
    id: int
    temperature: float
    humidity: float

@router.post("/", response_model=SensorReading)
def add_sensor_reading(reading: SensorReading):
    sensor_data.append(reading)
    return reading

@router.get("/", response_model=List[SensorReading])
def list_readings():
    return sensor_data
