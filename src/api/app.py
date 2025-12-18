from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import pandas as pd
import os

from src.ingestion.load_data import load_csv
from src.preprocessing.clean import clean_data
from src.features.build_features import build_features
from src.inference.predict import predict_completion
from src.insights.risk import detect_risk
from src.insights.chapter_difficulty import chapter_difficulty
from src.insights.summary import generate_summary

# -------------------------------------------------
# App initialization
# -------------------------------------------------
app = FastAPI(title="AI Learning Intelligence Tool API")

# -------------------------------------------------
# Paths
# -------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UI_FILE_PATH = os.path.join(BASE_DIR, "templates", "index.html")

# -------------------------------------------------
# Request schema
# -------------------------------------------------
class PredictionRequest(BaseModel):
    csv_path: str

# -------------------------------------------------
# UI endpoint (FORCED FILE READ)
# -------------------------------------------------
@app.get("/", response_class=HTMLResponse)
def serve_ui():
    with open(UI_FILE_PATH, "r", encoding="utf-8") as f:
        return f.read()

# -------------------------------------------------
# Health check
# -------------------------------------------------
@app.get("/health")
def health():
    return {"message": "AI Learning Intelligence Tool API is running"}

# -------------------------------------------------
# API prediction (JSON)
# -------------------------------------------------
@app.post("/predict")
def predict_api(request: PredictionRequest):
    try:
        df = load_csv(request.csv_path)
        df = clean_data(df)
        features = build_features(df)

        preds = predict_completion(features[["avg_time", "avg_score"]])
        df["prediction"] = preds

        risk_df = detect_risk(features)
        chapter_df = chapter_difficulty(df)
        summary = generate_summary(risk_df, chapter_df)

        return {
            "predictions": preds.tolist(),
            "insights": summary
        }

    except Exception as e:
        return {
            "error": "API prediction failed",
            "details": str(e)
        }

# -------------------------------------------------
# UI prediction (CSV upload)
# -------------------------------------------------
@app.post("/predict-ui")
async def predict_ui(file: UploadFile = File(...)):
    try:
        df = pd.read_csv(file.file)

        required_columns = {
            "student_id",
            "time_spent",
            "score",
            "completed"
        }

        missing = required_columns - set(df.columns)
        if missing:
            return {
                "error": "Invalid CSV format",
                "missing_columns": list(missing),
                "required_columns": list(required_columns)
            }

        df = clean_data(df)
        features = build_features(df)

        preds = predict_completion(features[["avg_time", "avg_score"]])
        df["prediction"] = preds

        risk_df = detect_risk(features)
        chapter_df = chapter_difficulty(df)
        summary = generate_summary(risk_df, chapter_df)

        return {
            "predictions": preds.tolist(),
            "insights": summary
        }

    except Exception as e:
        return {
            "error": "Prediction failed on server",
            "details": str(e)
        }

