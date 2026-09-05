from src.embeddings import create_query_embedding
from src.chromadb_store import collection


def search_chromadb(question, n_results=5):

    # Convert question into embedding
    query_embedding = create_query_embedding(question)

    # Search ChromaDB
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results