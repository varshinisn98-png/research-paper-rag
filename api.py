from fastapi import FastAPI
from pydantic import BaseModel

from src.retrieval import search_chromadb
from src.llm import generate_answer

app = FastAPI(
    title="Research Paper RAG API",
    description="Research Paper Question Answering using RAG",
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

    results = search_chromadb(
        request.question,
        n_results=5
    )

    documents = results["documents"][0]

    context = "\n\n".join(documents)

    answer = generate_answer(
        request.question,
        context
    )

    return {
        "question": request.question,
        "answer": answer,
        "retrieved_chunks": documents
    }