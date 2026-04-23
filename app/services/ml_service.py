import joblib
import os

model = joblib.load(os.path.join("app/models/model.pkl"))
vectorizer = joblib.load(os.path.join("app/models/vectorizer.pkl"))

SKILLS_DB = {
    "ML Engineer": ["python", "machine learning", "deep learning", "tensorflow", "pytorch"],
    "Data Scientist": ["python", "pandas", "numpy", "statistics", "machine learning"],
    "Data Analyst": ["excel", "sql", "power bi", "tableau", "data analysis"],
    "Backend Developer": ["java", "spring", "api", "database"]
}

def analyze_resume_text(text: str):
    text_lower = text.lower()

    X = vectorizer.transform([text])
    predicted_role = model.predict(X)[0]

    found_skills = []
    for skill in SKILLS_DB.get(predicted_role, []):
        if skill in text_lower:
            found_skills.append(skill)

    missing_skills = list(set(SKILLS_DB[predicted_role]) - set(found_skills))

    score = int((len(found_skills) / len(SKILLS_DB[predicted_role])) * 100)

    return {
        "predicted_role": predicted_role,
        "score": score,
        "skills_found": found_skills,
        "missing_skills": missing_skills
    }