from src.retrieval import search_chromadb

question = input("Ask a question about the research paper: ")

results = search_chromadb(question)

print("\nRelevant chunks:\n")

for i, document in enumerate(results["documents"][0]):
    print(f"\n--- Result {i + 1} ---")
    print(document)