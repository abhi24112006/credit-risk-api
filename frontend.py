import streamlit as st
import requests

st.title("Loan Default Risk Prediction")

# User Inputs
person_age = st.number_input("Person Age", min_value=18)

person_income = st.number_input("Person Income")

person_home_ownership = st.selectbox(
    "Home Ownership",
    ["RENT", "OWN", "MORTGAGE"]
)

person_emp_length = st.number_input("Employment Length")

loan_intent = st.selectbox(
    "Loan Intent",
    ["PERSONAL", "EDUCATION", "MEDICAL", "VENTURE"]
)

loan_grade = st.selectbox(
    "Loan Grade",
    ["A", "B", "C", "D", "E", "F", "G"]
)

loan_amnt = st.number_input("Loan Amount")

loan_int_rate = st.number_input("Loan Interest Rate")

loan_percent_income = st.number_input("Loan Percent Income")

cb_person_default_on_file = st.selectbox(
    "Previous Default",
    ["Y", "N"]
)

cb_person_cred_hist_length = st.number_input(
    "Credit History Length"
)

# Predict Button
# Predict Button
if st.button("Predict Risk"):

    input_data = {

        "person_age": person_age,
        "person_income": person_income,
        "person_home_ownership": person_home_ownership,
        "person_emp_length": person_emp_length,
        "loan_intent": loan_intent,
        "loan_grade": loan_grade,
        "loan_amnt": loan_amnt,
        "loan_int_rate": loan_int_rate,
        "loan_percent_income": loan_percent_income,
        "cb_person_default_on_file": cb_person_default_on_file,
        "cb_person_cred_hist_length": cb_person_cred_hist_length
    }

    # Send POST request to FastAPI
    response = requests.post(
        "https://credit-risk-api-zycq.onrender.com/predict",
        json=input_data
    )

    result = response.json()

    st.subheader("Prediction Result")

    st.write(
        f"Default Probability: {result['default_probability']:.2f}"
    )

    st.write(f"Prediction: {result['prediction']}")

    st.write(f"Risk Level: {result['risk_level']}")