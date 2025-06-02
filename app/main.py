from fastapi import FastAPI
from pydantic import BaseModel
from models.model import predict_diabetes

app = FastAPI()

class DiabetesInput(BaseModel):
    pregnancies: int
    glucose: float
    blood_pressure: float
    skin_thickness: float
    insulin: float
    bmi: float
    diabetes_pedigree_function: float
    age: int

@app.get("/")
async def root():
    return {"message": "Diabetes prediction API is running. Use POST /predict to get predictions."}

@app.post("/predict")
def predict(input_data: DiabetesInput):
    features = [
        input_data.pregnancies,
        input_data.glucose,
        input_data.blood_pressure,
        input_data.skin_thickness,
        input_data.insulin,
        input_data.bmi,
        input_data.diabetes_pedigree_function,
        input_data.age,
    ]
    prediction = predict_diabetes(features)
    return {"prediction": prediction}
