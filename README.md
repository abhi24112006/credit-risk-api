# Credit Risk Prediction API

A full-stack machine learning application for predicting loan default risk using FastAPI backend and Streamlit frontend. This system integrates advanced ML models with a user-friendly interface for real-time credit risk assessment in fintech applications.

## 🎯 Features

- **ML-Powered Predictions**: Machine learning-based credit risk classification model
- **REST API Backend**: FastAPI with automatic API documentation and validation
- **Interactive Frontend**: Streamlit web application for real-time predictions
- **Risk Classification**: Threshold-based risk level determination
- **Data Validation**: Pydantic schemas for robust input validation
- **Prediction Logging**: CSV-based logging of all predictions for audit trails
- **Production Ready**: Deployed on Render with automatic scaling
- **Real-time Communication**: Live API integration between frontend and backend

## 🚀 Live Deployment

- **API Endpoint**: [https://credit-risk-api-zycq.onrender.com](https://credit-risk-api-zycq.onrender.com)
- **Streamlit App**: Available through the repository

## 📋 Input Parameters

The model accepts the following borrower and loan information:

| Parameter | Type | Description |
|-----------|------|-------------|
| `person_age` | Integer | Age of the loan applicant (minimum 18) |
| `person_income` | Float | Annual income of the applicant |
| `person_home_ownership` | String | Home ownership status (RENT, OWN, MORTGAGE) |
| `person_emp_length` | Float | Years of employment history |
| `loan_intent` | String | Purpose of loan (PERSONAL, EDUCATION, MEDICAL, VENTURE) |
| `loan_grade` | String | Loan grade classification (A-G) |
| `loan_amnt` | Float | Requested loan amount |
| `loan_int_rate` | Float | Interest rate offered |
| `loan_percent_income` | Float | Loan amount as percentage of income |
| `cb_person_default_on_file` | String | Previous default history (Y/N) |
| `cb_person_cred_hist_length` | Float | Years of credit history |

## 📊 Output

The API returns comprehensive prediction results:

```json
{
  "default_probability": 0.25,
  "prediction": "No Default",
  "risk_level": "Low"
}
```

- **default_probability**: Probability of loan default (0-1 scale)
- **prediction**: Binary prediction (Default/No Default)
- **risk_level**: Categorical risk assessment (Low/Medium/High)

## 🛠️ Tech Stack

### Backend
- **Framework**: FastAPI 0.133.1
- **Server**: Uvicorn 0.41.0
- **Model Serialization**: joblib 1.5.3
- **Data Processing**: Pandas 2.3.3, NumPy 2.4.0
- **Validation**: Pydantic 2.12.5
- **ML Framework**: scikit-learn 1.8.0

### Frontend
- **UI Framework**: Streamlit 1.53.1
- **HTTP Client**: Requests 2.32.5

### Deployment
- **Platform**: Render (Web Services)
- **Web Server**: Uvicorn with Procfile configuration

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip or conda

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/abhi24112006/credit-risk-api.git
   cd credit-risk-api
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the FastAPI Backend**
   ```bash
   uvicorn app.main:app --reload
   ```
   The API will be available at `http://localhost:8000`

4. **Run the Streamlit Frontend** (in a new terminal)
   ```bash
   streamlit run frontend.py
   ```
   The frontend will open at `http://localhost:8501`

## 🔌 API Usage

### Using cURL
```bash
curl -X POST "https://credit-risk-api-zycq.onrender.com/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "person_age": 35,
    "person_income": 75000,
    "person_home_ownership": "MORTGAGE",
    "person_emp_length": 10,
    "loan_intent": "PERSONAL",
    "loan_grade": "B",
    "loan_amnt": 15000,
    "loan_int_rate": 8.5,
    "loan_percent_income": 0.20,
    "cb_person_default_on_file": "N",
    "cb_person_cred_hist_length": 8
  }'
```

### Using Python
```python
import requests

url = "https://credit-risk-api-zycq.onrender.com/predict"
data = {
    "person_age": 35,
    "person_income": 75000,
    "person_home_ownership": "MORTGAGE",
    "person_emp_length": 10,
    "loan_intent": "PERSONAL",
    "loan_grade": "B",
    "loan_amnt": 15000,
    "loan_int_rate": 8.5,
    "loan_percent_income": 0.20,
    "cb_person_default_on_file": "N",
    "cb_person_cred_hist_length": 8
}

response = requests.post(url, json=data)
print(response.json())
```

## 📁 Project Structure

```
credit-risk-api/
├── app/
│   ├── main.py           # FastAPI application entry point
│   ├── model.py          # ML model prediction logic
│   └── schemas.py        # Pydantic data validation schemas
├── frontend.py           # Streamlit web interface
├── loan_default_model.pkl # Trained machine learning model
├── requirements.txt      # Python dependencies
├── Procfile             # Render deployment configuration
└── logs.csv             # Prediction audit logs
```

## 📝 Logging

All predictions are automatically logged to `logs.csv` with timestamps for audit trails and performance monitoring. Each record includes:
- Input features
- Prediction output
- Default probability
- Risk classification
- Timestamp

## 🔐 Error Handling

The API includes comprehensive error handling:
- **HTTP 422**: Validation errors for invalid input
- **HTTP 500**: Server-side prediction failures with detailed error messages
- Input validation using Pydantic before model inference

## 🚀 Deployment on Render

The application is configured for deployment on Render:

1. **Backend**: Deployed as a Web Service running `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
2. **Auto-scaling**: Enabled for handling variable loads
3. **Environment Variables**: Configured for production settings

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Abhishek** - [GitHub Profile](https://github.com/abhi24112006)

## 📞 Support

For issues, questions, or feedback, please open a GitHub issue in the repository.

---

**Last Updated**: May 2026
