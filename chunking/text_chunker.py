from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(
    text,
    source="unknown",
    chunk_size=500,
    chunk_overlap=100
):
    """
    Split research paper text into smaller chunks.

    Args:
        text: Extracted text from the research paper.
        source: Name of the original research paper.
        chunk_size: Maximum chunk size.
        chunk_overlap: Overlap between consecutive chunks.

    Returns:
        List of chunks with metadata.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=[
            "\n\n",
            "\n",
            ". ",
            "? ",
            "! ",
            " ",
            ""
        ]
    )

    chunks = splitter.split_text(text)

    chunk_data = []

    for index, chunk in enumerate(chunks):

        chunk_data.append({
            "chunk_id": f"{source}_chunk_{index + 1}",
            "text": chunk,
            "source": source
        })

    return chunk_data


if __name__ == "__main__":

    sample_text = """
    Artificial intelligence is a branch of computer science.
    It focuses on creating systems capable of performing tasks
    that normally require human intelligence.

    Machine learning is a subset of artificial intelligence.
    It enables computers to learn patterns from data without
    being explicitly programmed.

    Deep learning is a specialized area of machine learning.
    It uses neural networks with multiple layers to learn
    complex patterns from large amounts of data.
    """

    chunks = split_text(
        sample_text,
        source="sample_research_paper.pdf",
        chunk_size=500,
        chunk_overlap=100
    )

    print("Total chunks:", len(chunks))

    for chunk in chunks:
        print("\n-----------------------------")
        print("Chunk ID:", chunk["chunk_id"])
        print("Source:", chunk["source"])
        print("Text:")
        print(chunk["text"])