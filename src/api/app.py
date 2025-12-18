from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

from src.ingestion.load_data import load_csv
from src.preprocessing.clean import clean_data
from src.features.build_features import build_features
from src.inference.predict import predict_completion
from src.insights.risk import detect_risk
from src.insights.chapter_difficulty import chapter_difficulty
from src.insights.summary import generate_summary

app = FastAPI(title="AI Learning Intelligence Tool API")


class PredictionRequest(BaseModel):
    csv_path: str


@app.get("/")
def root():
    return {"message": "AI Learning Intelligence Tool API is running"}


@app.post("/predict")
def predict(request: PredictionRequest):
    df = load_csv(request.csv_path)
    df = clean_data(df)
    features = build_features(df)

    predictions = predict_completion(features[['avg_time', 'avg_score']])
    df['prediction'] = predictions

    risk_df = detect_risk(features)
    chapter_df = chapter_difficulty(df)
    summary = generate_summary(risk_df, chapter_df)

    return {
        "predictions": predictions.tolist(),
        "insights": summary
    }

