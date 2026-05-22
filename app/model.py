import joblib
import pandas as pd

from datetime import datetime
import os

# Load trained pipeline once
model = joblib.load("loan_default_model.pkl")

THRESHOLD = 0.3

def classify_risk(probability):

    if probability < 0.3:
        return "Low Risk"

    elif probability < 0.6:
        return "Medium Risk"

    else:
        return "High Risk"

def log_prediction(input_data, result):

    log_entry = {
        **input_data, #unpacks all request fields
        **result, #adds probability, prediction and risk level
        "timestamp": datetime.now() #stores timestamp
    }

    df = pd.DataFrame([log_entry])

    if os.path.exists("logs.csv"):
        df.to_csv("logs.csv", mode="a", header=False, index=False) #mode="a" is append mode i.e. add new rows instaed of overwriting the file

    else:
        df.to_csv("logs.csv", index=False)

def predict_loan(data):

    # Convert input to DataFrame
    df = pd.DataFrame([data])

    # Predict probability
    probability = model.predict_proba(df)[0][1]

    # Threshold decision
    prediction = 1 if probability >= THRESHOLD else 0

    # Risk category
    risk_level = classify_risk(probability)

    
    result = {
    "default_probability": float(probability),
    "prediction": prediction,
    "risk_level": risk_level
    }

    log_prediction(data, result)

    return result
    