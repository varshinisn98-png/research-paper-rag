from fastapi import FastAPI
from pydantic import BaseModel

from src.retrieval import search_chromadb
from src.llm import generate_answer


app = FastAPI(
    title="Research Paper RAG API",
    description="Question answering system for research papers using Retrieval-Augmented Generation",
    version="1.0.0"
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

    # Step 1: Retrieve relevant chunks from ChromaDB
    results = search_chromadb(request.question)

    # Step 2: Extract retrieved text
    documents = results.get("documents", [[]])[0]

    # Step 3: Combine retrieved chunks into context
    context = "\n\n".join(documents)

    # Step 4: Generate answer using the LLM
    answer = generate_answer(
        request.question,
        context
    )

    return {
        "question": request.question,
        "answer": answer,
        "retrieved_chunks": documents
    }
