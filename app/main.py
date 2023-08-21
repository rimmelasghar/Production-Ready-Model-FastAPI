from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version
from os import environ as env

app = FastAPI()

class DataIn(BaseModel):
    sepal_length: float
    sepal_width:  float
    petal_length: float
    petal_width: float

class PredictionOut(BaseModel):
    specie: str

@app.get("/")
def home():
    return {"status":"running","health_check": "OK","app_name": env['APP_NAME'],"model_version": model_version}

@app.post("/predict", response_model=PredictionOut)
def predict(payload: DataIn):
    print(payload)
    prediction = predict_pipeline(payload)
    return {"specie": prediction}

