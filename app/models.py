from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.dialects.postgresql import JSON
from app.database import Base

class Resume(Base):
    __tablename__ = "resumes"
    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String, nullable=False)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    core_skills = Column(JSON)        # list of strings
    soft_skills = Column(JSON)        # list of strings
    experience = Column(JSON)         # list of {role, company, start, end, bullets}
    education = Column(JSON)          # list of {degree, school, year}
    projects = Column(JSON)           # list of project objects
    certifications = Column(JSON)
    resume_rating = Column(String)
    improvement_areas = Column(Text)
    upskill_suggestions = Column(Text)
