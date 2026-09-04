from src.pdf_extractor import extract_text_from_pdf
from src.chunking import chunk_text
from src.embeddings import create_embeddings
from src.chromadb_store import store_embeddings


def main():
    pdf_path = "data/papers/paper1.pdf"

    # 1. Extract text from PDF
    text = extract_text_from_pdf(pdf_path)

    # 2. Split text into chunks
    chunks = chunk_text(text)

    # 3. Create embeddings
    embeddings = create_embeddings(chunks)

    # 4. Store embeddings in ChromaDB
    store_embeddings(chunks, embeddings)

    print("Research paper successfully processed and stored.")


if __name__ == "__main__":
    main()
