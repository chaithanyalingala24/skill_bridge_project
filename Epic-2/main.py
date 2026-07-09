from fastapi import FastAPI

from app.database import Base, engine
from app.routers import user, loan, ai

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI application
app = FastAPI(
    title="FinRelief AI Backend",
    description="AI-powered Financial Assistance System",
    version="1.0"
)

# Home Route
@app.get("/")
def home():
    return {
        "message": "Welcome to FinRelief AI Backend"
    }

# Include Routers
app.include_router(user.router)
app.include_router(loan.router)
app.include_router(ai.router)