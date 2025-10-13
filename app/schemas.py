from pydantic import BaseModel

class ResumeBase(BaseModel):
    name: str | None = None
    email: str | None = None
    phone: str | None = None
    core_skills: str | None = None
    soft_skills: str | None = None
    experience: str | None = None
    education: str | None = None
    improvement_areas: str | None = None
    upskill_suggestions: str | None = None

class ResumeCreate(ResumeBase):
    file_name: str

class ResumeOut(ResumeBase):
    id: int
    file_name: str

    class Config:
        orm_mode = True
