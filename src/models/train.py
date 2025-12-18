from sklearn.linear_model import LogisticRegression
from joblib import dump

from src.ingestion.load_data import load_csv
from src.preprocessing.clean import clean_data
from src.features.build_features import build_features


def train():
    df = load_csv("data/learning_data.csv")
    df = clean_data(df)
    features = build_features(df)

    X = features[['avg_time', 'avg_score']]
    y = features['completed']

    model = LogisticRegression()
    model.fit(X, y)

    dump(model, "models/completion_model.joblib")
    print("Model trained and saved successfully")


if __name__ == "__main__":
    train()

