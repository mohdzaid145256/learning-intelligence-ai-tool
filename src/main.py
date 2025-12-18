import sys

from src.ingestion.load_data import load_csv
from src.preprocessing.clean import clean_data
from src.features.build_features import build_features
from src.inference.predict import predict_completion
from src.insights.risk import detect_risk
from src.insights.chapter_difficulty import chapter_difficulty
from src.insights.summary import generate_summary


def main():
    if len(sys.argv) < 3 or sys.argv[1] != "--data":
        print("Usage: python -m src.main --data <path_to_csv>")
        sys.exit(1)

    data_path = sys.argv[2]

    print("🚀 AI Learning Intelligence Tool Started")

    df = load_csv(data_path)
    print(f"✅ Loaded {len(df)} records")

    df = clean_data(df)
    features = build_features(df)

    predictions = predict_completion(features[['avg_time', 'avg_score']])
    df['prediction'] = predictions

    risk_df = detect_risk(features)
    chapter_df = chapter_difficulty(df)
    summary = generate_summary(risk_df, chapter_df)

    print("\n📊 Predictions:")
    print(predictions.tolist())

    print("\n🧠 Insights:")
    print(summary)

    print("\n✅ Execution completed successfully")


if __name__ == "__main__":
    main()

