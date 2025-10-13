from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# connect SQLAlchemy with PostgreSQL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all database models
Base = declarative_base()

# function to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
