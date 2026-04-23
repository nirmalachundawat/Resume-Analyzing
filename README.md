# Resume Analyzer API

An end-to-end **Machine Learning powered API** that analyzes PDF resumes and provides intelligent insights such as **job role prediction, skill extraction, and improvement suggestions**.

This project demonstrates the integration of **FastAPI + NLP + Machine Learning + Docker deployment** in a real-world use case.

---

## Tech Stack

* **Backend:** FastAPI
* **Machine Learning:** Scikit-learn (TF-IDF + Logistic Regression)
* **Language:** Python
* **File Processing:** pdfplumber
* **Deployment:** Docker
* **API Testing:** Swagger UI (/docs)

---

## Features

* Upload PDF resumes
* Predict job role using ML model
* Extract relevant skills from resume text
* Generate resume score based on skills
* Identify missing skills for improvement
* Fast and scalable REST API
* Dockerized for production deployment

---

## Project Structure

```
resume-analyzer/
│
├── app/
│   ├── main.py                # FastAPI app entry point
│   ├── routes/               # API routes
│   ├── services/             # ML logic
│   ├── models/               # Trained ML model & vectorizer
│   ├── utils/                # PDF processing
│   └── schemas/              # Request/response schemas
│
├── notebooks/
│   └── train_model.py        # Script to train ML model
│
├── Dockerfile                # Docker configuration
├── .dockerignore             # Docker ignore file
├── .gitignore                # Git ignore file
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

---

## API Endpoint

### POST `/analyze-resume`

Upload a PDF resume and receive analysis.

---

## Sample Response

```json
{
  "predicted_role": "ML Engineer",
  "score": 60,
  "skills_found": ["python", "tensorflow"],
  "missing_skills": ["deep learning"],
  "message": "Analysis complete"
}
```

---

## Run Locally

```bash
git clone https://github.com/nirmalachundawat/Resume-Analyzing.git
cd Resume-Analyzing

pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open: http://127.0.0.1:8000/docs

---

## Run with Docker

```bash
docker build -t resume-analyzer.
docker run -p 8000:8000 resume-analyzer
```

---

## Live Demo

(Add your Render deployment link here after hosting)

---

## How It Works

1. Upload PDF resume
2. Extract text using pdfplumber
3. Convert text → TF-IDF features
4. Predict job role using ML model
5. Match skills from predefined database
6. Generate score and suggestions

---

## Future Improvements

* 🔹 Use advanced NLP models (BERT / Transformers)
* 🔹 Add authentication (JWT)
* 🔹 Store results in database
* 🔹 Build frontend UI (Streamlit/React)
* 🔹 Improve skill extraction using NLP

---

## Use Case

This system can be used for:

* Resume screening automation
* Career guidance tools
* HR tech platforms
* Skill gap analysis

---

## Author

**Nirmala Chundawat**

---
