from fastapi import FastAPI
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version


app = FastAPI()

@app.get("/")
def home():
    return {"working":"Ok","model_version":model_version}

@app.post("/predict")
def predict(text : str):
    language = predict_pipeline(text.text)
    return {"Language":language}
