# models/model.py

import joblib
import numpy as np

# Load the saved model 
model = joblib.load("models/xgb_diabetes_model.joblib")

def predict_diabetes(features):
    """
    features: list of input features in the correct order
    Returns: prediction (0 or 1)
    """
    data = np.array(features).reshape(1, -1)  # Convert to 2D array for model
    prediction = model.predict(data)
    return int(prediction[0])
