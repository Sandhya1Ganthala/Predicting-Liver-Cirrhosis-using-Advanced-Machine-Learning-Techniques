import joblib
import numpy as np

def predict_risk(features: list):
    model = joblib.load("models/model.pkl")
    prediction = model.predict([features])
    return prediction[0]
