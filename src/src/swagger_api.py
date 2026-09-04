from fastapi import FastAPI
from pydantic import BaseModel

from src.rag_pipeline import rag_pipeline


app = FastAPI(
    title="Research Paper RAG API",
    description="Question Answering API for a Research Paper using RAG",
    version="1.0"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Research Paper RAG API is running"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):
    result = rag_pipeline(request.question)
    return result
