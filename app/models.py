from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String, nullable=False)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    core_skills = Column(Text)
    soft_skills = Column(Text)
    experience = Column(Text)
    education = Column(Text)
    improvement_areas = Column(Text)
    upskill_suggestions = Column(Text)
