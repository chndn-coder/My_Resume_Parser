from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app.utils.pdf_extractor import extract_text_from_pdf, extract_basic_info
from app.utils.ai_analyzer import analyze_resume_with_ai
import os

router = APIRouter(prefix="/resume", tags=["Resume Parser"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save the uploaded file
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Extract text & info
    text = extract_text_from_pdf(file_path)
    info = extract_basic_info(text)

    # Analyze with Gemini
    ai_result = analyze_resume_with_ai(text)

    # Save to database
    new_resume = models.Resume(
        file_name=file.filename,
        name=info.get("name"),
        email=info.get("email"),
        phone=info.get("phone"),
        core_skills=info.get("core_skills"),
        improvement_areas=ai_result.get("improvement_areas"),
        upskill_suggestions=ai_result.get("upskill_suggestions")
    )

    db.add(new_resume)
    db.commit()
    db.refresh(new_resume)

    return {
        "message": "Resume uploaded and analyzed successfully!",
        "data": {
            "id": new_resume.id,
            "name": new_resume.name,
            "email": new_resume.email,
            "phone": new_resume.phone,
            "core_skills": new_resume.core_skills,
            "resume_rating": ai_result.get("resume_rating"),
            "improvement_areas": ai_result.get("improvement_areas"),
            "upskill_suggestions": ai_result.get("upskill_suggestions")
        }
    }

@router.get("/all")
def get_all_resumes(db: Session = Depends(get_db)):
    resumes = db.query(models.Resume).all()
    return resumes
