from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.database import get_connection

router = APIRouter()

class SensorReading(BaseModel):
    id: int
    temperature: float
    humidity: float

@router.post("/", response_model=SensorReading)
def add_sensor_reading(reading: SensorReading):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO sensor_readings (id, temperature, humidity) VALUES (%s, %s, %s)",
            (reading.id, reading.temperature, reading.humidity)
        )
        conn.commit()
        cur.close()
        conn.close()
        return reading
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=List[SensorReading])
def list_readings():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM sensor_readings")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
