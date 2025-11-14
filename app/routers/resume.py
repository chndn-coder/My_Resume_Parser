from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app.utils.pdf_extractor import extract_text_from_pdf, extract_basic_info
from app.utils.ai_analyzer import analyze_resume_with_ai
import os
import json

router = APIRouter(prefix="/resume", tags=["Resume Parser"])

# Upload folder
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """Upload a resume PDF, extract data, analyze with Gemini, and save to DB"""
    try:
        # Validate file type
        if not file.filename.lower().endswith(".pdf"):
            raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

        file_path = os.path.join(UPLOAD_DIR, file.filename)

        # Save uploaded file
        with open(file_path, "wb") as f:
            f.write(await file.read())

        # Extract text and basic info
        text = extract_text_from_pdf(file_path)
        info = extract_basic_info(text)

        # Analyze with Gemini AI
        ai_result = analyze_resume_with_ai(text)

        # Build new resume record
        new_resume = models.Resume(
            file_name=file.filename,
            name=info.get("name"),
            email=info.get("email"),
            phone=info.get("phone"),
            core_skills=json.dumps(info.get("core_skills", [])),  # store as JSON string
            soft_skills=json.dumps(ai_result.get("soft_skills", [])),
            experience=json.dumps(ai_result.get("experience", [])),
            education=json.dumps(ai_result.get("education", [])),
            projects=json.dumps(ai_result.get("projects", [])),
            certifications=json.dumps(ai_result.get("certifications", [])),
            resume_rating=str(ai_result.get("resume_rating", "N/A")),
            improvement_areas=ai_result.get("improvement_areas"),
            upskill_suggestions=json.dumps(ai_result.get("upskill_suggestions", []))
        )

        # Save to DB
        db.add(new_resume)
        db.commit()
        db.refresh(new_resume)

        # Response
        return {
            "message": "✅ Resume uploaded and analyzed successfully!",
            "data": {
                "id": new_resume.id,
                "name": new_resume.name,
                "email": new_resume.email,
                "phone": new_resume.phone,
                "core_skills": json.loads(new_resume.core_skills or "[]"),
                "soft_skills": json.loads(new_resume.soft_skills or "[]"),
                "resume_rating": new_resume.resume_rating,
                "improvement_areas": new_resume.improvement_areas,
                "upskill_suggestions": json.loads(new_resume.upskill_suggestions or "[]"),
            }
        }

    except Exception as e:
        print("❌ Upload or analysis failed:", e)
        raise HTTPException(status_code=500, detail=f"Error processing resume: {e}")



@router.get("/all")
def get_all_resumes(db: Session = Depends(get_db)):
    """Return all analyzed resumes"""
    resumes = db.query(models.Resume).all()
    result = []
    for r in resumes:
        result.append({
            "id": r.id,
            "file_name": r.file_name,
            "name": r.name,
            "email": r.email,
            "phone": r.phone,
            "core_skills": json.loads(r.core_skills or "[]"),
            "resume_rating": r.resume_rating,
        })
    return result



@router.get("/{resume_id}")
def get_resume_by_id(resume_id: int, db: Session = Depends(get_db)):
    """Fetch a single resume by ID"""
    resume = db.query(models.Resume).filter(models.Resume.id == resume_id).first()
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")

    return {
        "id": resume.id,
        "file_name": resume.file_name,
        "name": resume.name,
        "email": resume.email,
        "phone": resume.phone,
        "core_skills": json.loads(resume.core_skills or "[]"),
        "soft_skills": json.loads(resume.soft_skills or "[]"),
        "experience": json.loads(resume.experience or "[]"),
        "education": json.loads(resume.education or "[]"),
        "projects": json.loads(resume.projects or "[]"),
        "certifications": json.loads(resume.certifications or "[]"),
        "resume_rating": resume.resume_rating,
        "improvement_areas": resume.improvement_areas,
        "upskill_suggestions": json.loads(resume.upskill_suggestions or "[]"),
    }
