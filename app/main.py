from fastapi import FastAPI
from pydantic import BaseModel
from app.config import settings

app = FastAPI(
    title="Enterprise Document Intelligence System",
    version="1.0.0"
)


# ---------- Request Model ----------
class QueryRequest(BaseModel):
    question: str


# ---------- Health Check ----------
@app.get("/")
def root():
    return {
        "message": "Document Intelligence System is running 🚀",
        "production_mode": settings.PRODUCTION
    }


# ---------- Simple Test Endpoint ----------
@app.post("/echo")
def echo(data: QueryRequest):
    return {
        "your_question": data.question,
        "environment": "PRODUCTION" if settings.PRODUCTION else "DEVELOPMENT"
    }


# ---------- Health Endpoint ----------
@app.get("/health")
def health():
    return {"status": "healthy"}
