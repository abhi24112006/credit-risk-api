from fastapi import FastAPI
from app.schemas import LoanData, PredictionResponse
from app.model import predict_loan
from fastapi import HTTPException

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Credit Risk API Running"
    }

@app.post("/predict", response_model=PredictionResponse)
def predict(data: LoanData):

    try: #attempts normal execution

        input_data = data.dict()

        result = predict_loan(input_data)

        return result

    except Exception as e: #catches unexpected backend failures

        print(f"Prediction Error: {e}")

        raise HTTPException(
            status_code=500,
            detail="Prediction failed. Please try again later."
        )