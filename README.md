# 🎓 AI Learning Intelligence Tool

> An end-to-end **AI-powered learning analytics system** that predicts learner completion outcomes and generates actionable insights through a live interactive web interface.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![ML](https://img.shields.io/badge/Machine%20Learning-Enabled-orange)
![Deployment](https://img.shields.io/badge/Deployment-Render-purple)
![Status](https://img.shields.io/badge/Status-Live-success)

---

## 🚀 Live Demo & Links

- 🌐 **Live Application**  
  👉 https://learning-intelligence-ai-tool-c2g6.onrender.com

- 📘 **API Documentation (Swagger UI)**  
  👉 https://learning-intelligence-ai-tool-c2g6.onrender.com/docs

- 💻 **GitHub Repository**  
  👉 https://github.com/mohdzaid145256/learning-intelligence-ai-tool

---

## 🎯 Project Overview

The **AI Learning Intelligence Tool** is designed to analyze learner behavior data and provide:

- 📊 **Completion Predictions** (Completed vs At Risk)
- ⚠️ **High-Risk Student Detection**
- 📚 **Most Difficult Chapter Identification**
- 🖥️ **Interactive UI for non-technical users**
- 🔌 **REST API for programmatic access**

This project demonstrates **production-ready AI engineering**, not just model training.

---

## 🧠 High-Level Architecture

This project follows a clean, layered AI system design, separating data processing, machine learning, insights generation, and presentation.

1. CSV Learner Data


2. Data Cleaning & Preprocessing


3. Feature Engineering


4. ML Model (Binary Classification)


5. Inference Engine


6. Insights Generator


7. API + Interactive Web UI


### Architecture Highlights
- Modular and scalable design
- Clear separation between ML logic and presentation layer
- Production-style API and UI integration
- Easily extensible for additional insights or models

---



## 🏗️ Project Architecture (Directory Structure)

The project is organized using a **clean, modular structure** commonly used in production ML systems.

```text
learning-intelligence-ai-tool/
│
├── src/
│   ├── api/                     # FastAPI app & UI
│   │   ├── app.py               # API routes and UI serving
│   │   └── templates/
│   │       └── index.html       # Interactive Web UI
│   │
│   ├── ingestion/               # Data loading & validation
│   ├── preprocessing/           # Data cleaning logic
│   ├── features/                # Feature engineering
│   ├── inference/               # Model prediction logic
│   └── insights/                # Risk & chapter analysis
│
├── models/                      # Trained ML model artifacts
├── data/                        # Input datasets
├── sample_learning_data.csv     # Demo CSV for testing
├── requirements.txt
└── README.md

🧪 Sample Input Data
A sample CSV file is provided for quick testing and demonstration of the system.

student_id,course_id,chapter,time_spent,score,completed
101,C1,1,45,85,1
102,C1,2,30,78,1
103,C1,3,20,55,0
104,C2,1,60,90,1
105,C2,2,25,65,0
106,C2,3,15,40,0

🖥️ Web UI Usage
Follow these simple steps to use the interactive interface:

* Open the Live Application
* Upload a learner CSV file

Click Run Prediction
1.View results:

✔ Completion status per learner
⚠ High-risk student count
📘 Most difficult chapter(s)


🔌 API Endpoints

## Health Check
* GET /health

## Predict (CSV Upload – UI)
* POST /predict-ui

## Swagger documentation is available at:
/docs

## 🛠️ Tech Stack

The project leverages a modern and reliable technology stack to build, deploy, and serve an end-to-end AI system.

### 🔹 Backend & API
- **Python 3** – Core programming language
- **FastAPI** – High-performance REST API framework
- **Uvicorn** – ASGI server for serving the API

### 🔹 Machine Learning & Data Processing
- **Scikit-learn** – Machine learning model training and inference
- **Pandas** – Data manipulation and preprocessing
- **NumPy** – Numerical computations
- **Joblib** – Model serialization and loading

### 🔹 Frontend (UI)
- **HTML5** – UI structure
- **CSS3** – Styling and layout
- **Vanilla JavaScript** – Client-side interactivity and API calls

### 🔹 Deployment & DevOps
- **Render** – Cloud deployment platform
- **Git & GitHub** – Version control and collaboration

---

## ✨ Key Features

- ✅ **End-to-End Machine Learning Pipeline**  
  From raw CSV ingestion to predictions and insights.

- 📊 **Learner Completion Prediction**  
  Binary classification to identify *Completed* vs *At Risk* learners.

- ⚠️ **High-Risk Student Detection**  
  Automatically identifies students who may need intervention.

- 📘 **Most Difficult Chapter Analysis**  
  Highlights chapters where learners struggle the most.

- 🖥️ **Interactive Web UI (Level-2)**  
  Upload CSV files and visualize predictions without technical knowledge.

- 🔌 **REST API Access**  
  Enables programmatic integration via well-defined endpoints.

- 🛡️ **Robust Error Handling**  
  Graceful handling of invalid input and server-side failures.

- ☁️ **Live Cloud Deployment**  
  Publicly accessible and production-ready application.

- 🧩 **Modular & Maintainable Codebase**  
  Clean separation of concerns for scalability and readability.

---
## Run Locally

git clone https://github.com/mohdzaid145256/learning-intelligence-ai-tool.git
cd learning-intelligence-ai-tool
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn src.api.app:app --reload

## Then open in browser:
http://127.0.0.1:8000

## CLI Usage 

The tool can also be executed from the command line without using the web interface.

### Example Command
```bash
python -m src.main --data sample_learning_data.csv

🚀 AI Learning Intelligence Tool Started
✅ Loaded 6 records

📊 Predictions:
[1, 1, 1, 1, 1, 0]

🧠 Insights:
{'high_risk_students_count': 0, 'most_difficult_chapter': [3]}

✅ Execution completed successfully

👤 Author
Mohd Zaid
AI / Machine Learning / Data Engineering Enthusiast









