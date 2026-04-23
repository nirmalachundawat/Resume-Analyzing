from fastapi import APIRouter, UploadFile, File
from app.services.ml_service import analyze_resume_text
from app.utils.pdf_reader import extract_text_from_pdf

router = APIRouter()

@router.post("/analyze-resume")
async def analyze_resume(file: UploadFile = File(...)):
    text = extract_text_from_pdf(file.file)

    result = analyze_resume_text(text)

    return {
        "predicted_role": result["predicted_role"],
        "score": result["score"],
        "skills_found": result["skills_found"],
        "missing_skills": result["missing_skills"],
        "message": "Analysis complete"
    }