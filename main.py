from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version

app = FastAPI()


class TextInput(BaseModel):
    text: str


class PredictionOutput(BaseModel):
    language: str


@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}


@app.post("/predict", response_model=PredictionOutput)
def predict(payload: TextInput):
    language = predict_pipeline(payload.text)
    return {"language": language}
