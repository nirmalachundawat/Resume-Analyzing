import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Dummy dataset (we’ll improve later)
data = {
    "text": [
        "python machine learning deep learning",
        "data analysis excel sql",
        "java spring backend development",
        "python pandas data science",
        "deep learning tensorflow pytorch",
        "sql data visualization power bi"
    ],
    "role": [
        "ML Engineer",
        "Data Analyst",
        "Backend Developer",
        "Data Scientist",
        "ML Engineer",
        "Data Analyst"
    ]
}

df = pd.DataFrame(data)

# Convert text → numerical
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])

# Train model
model = LogisticRegression()
model.fit(X, df["role"])

# Save model + vectorizer
joblib.dump(model, "app/models/model.pkl")
joblib.dump(vectorizer, "app/models/vectorizer.pkl")

print("Model trained and saved!")