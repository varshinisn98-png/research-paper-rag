from src.retrieval import search_chromadb
from src.llm import generate_answer


def rag_pipeline(question, n_results=5):

    # Step 1: Retrieve relevant chunks from ChromaDB
    results = search_chromadb(
        question,
        n_results=n_results
    )

    # Step 2: Get retrieved documents
    documents = results["documents"][0]

    # Step 3: Combine chunks into context
    context = "\n\n".join(documents)

    # Step 4: Generate answer using the LLM
    answer = generate_answer(
        question,
        context
    )

    return {
        "question": question,
        "answer": answer,
        "retrieved_chunks": documents
    }
