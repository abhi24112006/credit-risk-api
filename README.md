# Credit Risk API

A full-stack machine learning system for predicting loan default risk in real-time using a Random Forest classifier. The project combines a FastAPI backend with a Streamlit frontend to deliver scalable and production-oriented credit risk assessment.

---

## 🎯 Overview

The Credit Risk API helps financial institutions evaluate lending risk by predicting the probability of loan default and classifying applicants into different risk categories.

The system is designed with production-oriented ML engineering concepts including:
- API-based model serving
- Pydantic validation
- Threshold-based decision making
- Prediction logging
- Cloud deployment
- Frontend-backend communication

---

## 🚀 Key Features

- 🚀 **FastAPI Backend** for scalable ML inference
- 🎨 **Streamlit Frontend** for interactive predictions
- 🤖 **Random Forest ML Model** for loan default prediction
- 📊 **Risk Classification** into Low, Medium, and High risk
- 📝 **Prediction Logging System** for monitoring and auditing
- 🔒 **Pydantic Validation** for safe and structured inputs
- ☁️ **Cloud Deployment** using Render
- 📡 **REST API Communication** using JSON requests/responses

---

## 🏗 System Architecture

```text
Streamlit Frontend
        ↓
HTTP POST Request
        ↓
FastAPI Backend
        ↓
Pydantic Validation
        ↓
ML Pipeline
        ↓
Prediction + Risk Logic
        ↓
Logging System