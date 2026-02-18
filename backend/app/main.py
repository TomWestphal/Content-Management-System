from app.upload import router as upload_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .schemas.routes import auth, articles  # ⚠️ GEÄNDERT!

# Create tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="IT Troubleshooting CMS",
    description="Content Management System for IT Support troubleshooting tips",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production: specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(articles.router)
app.include_router(upload_router)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the IT Troubleshooting API",
        "docs": "/docs",
        "version": "1.0.0"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}