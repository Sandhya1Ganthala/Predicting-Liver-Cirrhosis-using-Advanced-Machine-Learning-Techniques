import os
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "models", "model.pkl"))

# Ensure the model file exists before predicting
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at: {MODEL_PATH}")

def predict_risk(features: list):
    model = joblib.load(MODEL_PATH)
    prediction = model.predict([features])
    return prediction[0]
