from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import engine, Base, get_db

# Create tables on startup (for MVP)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="IT Troubleshooting CMS")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Troubleshooting API"}

@app.get("/articles")
def get_articles(db: Session = Depends(get_db)):
    # Logic to fetch articles from DB will go here
    return []