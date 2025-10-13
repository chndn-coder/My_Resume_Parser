from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import resume
from app import models
from app.database import engine

# create database tables
models.Base.metadata.create_all(bind=engine)


# create FastAPI app
app = FastAPI(title="AI Resume Parser")

# allow frontend access (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for now allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include router
app.include_router(resume.router)

@app.get("/")
def home():
    return {"message": "Welcome to AI Resume Parser API 🚀"}
