from pydantic import BaseModel

class LoanData(BaseModel):

    person_age: int
    person_income: float
    person_home_ownership: str
    person_emp_length: float

    loan_intent: str
    loan_grade: str

    loan_amnt: float
    loan_int_rate: float
    loan_percent_income: float

    cb_person_default_on_file: str
    cb_person_cred_hist_length: int

class PredictionResponse(BaseModel): #define exact api output structure

    default_probability: float
    prediction: int
    risk_level: str