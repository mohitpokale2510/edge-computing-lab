from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

log_file = "log.txt"

class SensorData(BaseModel):
    temperature: float

@app.post("/log")
async def log_data(data: SensorData):
    with open(log_file, "a") as f:
        f.write(f"Temperature: {data.temperature}\n")
    return {"status": "logged"}
