# diabetes-prediction-ml


# 🩺 Diabetes Prediction API

A machine learning API built with **FastAPI** to predict the likelihood of diabetes based on medical attributes. The model is trained on the **PIMA Indians Diabetes Dataset** using **XGBoost**.

---

## Project Overview

This project includes the full machine learning pipeline:
- Data preprocessing
- Model training and evaluation
- Model serialization
- API development using FastAPI
- Local testing via Swagger UI

---

##  Model Details

- **Model:** XGBoost Classifier
- **Dataset:** PIMA Indians Diabetes Dataset
- **Features Used:**
  - `pregnancies`
  - `glucose`
  - `blood_pressure`
  - `skin_thickness`
  - `insulin`
  - `bmi`
  - `diabetes_pedigree_function`
  - `age`

---

## Project Structure

```

diabetes-prediction-ml/
│
├── app/
│   ├── main.py              # FastAPI app with POST /predict endpoint
│   └── models/
│       └── model.py         # Prediction function using the trained model
│
├── model/
│   └── diabetes\_model.pkl   # Trained XGBoost model (serialized)
│
├── notebooks/
│   └── training.ipynb       # Jupyter Notebook for data exploration & model training
│
├── requirements.txt         # Python dependencies
├── .gitignore
└── README.md                # Project description and usage

````

---

##  How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Sandrakimiring/diabetes-prediction-ml.git
cd diabetes-prediction-ml
````

### 2. Create and Activate a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate      # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI App

```bash
uvicorn app.main:app --reload
```

### 5. Open in Browser

Go to:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
Here, you can test the `POST /predict` endpoint using Swagger UI.

---

## Example Request

### Endpoint

`POST /predict`

### Sample JSON Body

```json
{
  "pregnancies": 2,
  "glucose": 130,
  "blood_pressure": 70,
  "skin_thickness": 20,
  "insulin": 79,
  "bmi": 25.0,
  "diabetes_pedigree_function": 0.5,
  "age": 31
}
```

### Sample Response

```json
{
  "prediction": 1
}
```

> `1` means diabetes is likely.
> `0` means diabetes is unlikely.

---

## 🪪 License

MIT License — feel free to use and adapt.

