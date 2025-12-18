from joblib import load

def predict_completion(features):
    model = load("models/completion_model.joblib")
    return model.predict(features)

