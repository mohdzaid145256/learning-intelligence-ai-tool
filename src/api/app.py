from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
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
# App Initialization
# -------------------------------------------------
app = FastAPI(title="AI Learning Intelligence Tool API")

# -------------------------------------------------
# Absolute paths (important for Render)
# -------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
UI_FILE_PATH = os.path.join(TEMPLATES_DIR, "index.html")

# -------------------------------------------------
# Request schema (JSON API usage)
# -------------------------------------------------
class PredictionRequest(BaseModel):
    csv_path: str

# -------------------------------------------------
# UI Endpoint (HTML page)
# -------------------------------------------------
@app.get("/", response_class=FileResponse)
def serve_ui():
    """
    Serves the minimal HTML UI
    """
    return FileResponse(UI_FILE_PATH)

# -------------------------------------------------
# Health check
# -------------------------------------------------
@app.get("/health")
def health_check():
    return {"message": "AI Learning Intelligence Tool API is running"}

# -------------------------------------------------
# API endpoint (JSON-based, CSV path)
# -------------------------------------------------
@app.post("/predict")
def predict_api(request: PredictionRequest):
    """
    Predict using CSV path (API usage)
    """
    try:
        df = load_csv(request.csv_path)
        df = clean_data(df)
        features = build_features(df)

        predictions = predict_completion(features[["avg_time", "avg_score"]])
        df["prediction"] = predictions

        risk_df = detect_risk(features)
        chapter_df = chapter_difficulty(df)
        summary = generate_summary(risk_df, chapter_df)

        return {
            "predictions": predictions.tolist(),
            "insights": summary
        }

    except Exception as e:
        return {
            "error": "Internal server error during API prediction",
            "details": str(e)
        }

# -------------------------------------------------
# UI endpoint (CSV upload with validation)
# -------------------------------------------------
@app.post("/predict-ui")
async def predict_ui(file: UploadFile = File(...)):
    """
    Predict using uploaded CSV (UI usage)
    Includes schema validation and safe error handling
    """
    try:
        df = pd.read_csv(file.file)

        # Required columns for ML pipeline
        required_columns = {
            "student_id",
            "time_spent",
            "score",
            "completed"
        }

        missing_columns = required_columns - set(df.columns)
        if missing_columns:
            return {
                "error": "Invalid CSV format",
                "missing_columns": list(missing_columns),
                "required_columns": list(required_columns)
            }

        df = clean_data(df)
        features = build_features(df)

        predictions = predict_completion(features[["avg_time", "avg_score"]])
        df["prediction"] = predictions

        risk_df = detect_risk(features)
        chapter_df = chapter_difficulty(df)
        summary = generate_summary(risk_df, chapter_df)

        return {
            "predictions": predictions.tolist(),
            "insights": summary
        }

    except Exception as e:
        return {
            "error": "Internal server error during UI prediction",
            "details": str(e)
        }

