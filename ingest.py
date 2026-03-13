import os
from server.rag.chunker import split_into_clauses
from server.rag.embeddings import EmbeddingModel
from server.rag.vector_store import VectorStore


DATA_DIR = "./data/"


def load_documents():

    docs = []

    for file in os.listdir(DATA_DIR):

        path = os.path.join(DATA_DIR, file)

        with open(path, "r") as f:
            text = f.read()

        clauses = split_into_clauses(text)

        for i, clause in enumerate(clauses):

            docs.append({
                "text": clause,
                "metadata": {
                    "document": file,
                    "clause_id": i
                }
            })

    return docs


def main():

    embedder = EmbeddingModel()

    vector_store = VectorStore(embedder)

    docs = load_documents()

    texts = [d["text"] for d in docs]

    metadatas = [d["metadata"] for d in docs]

    ids = [f"id_{i}" for i in range(len(docs))]

    vector_store.add_documents(texts, metadatas, ids)

    print("Ingestion complete.")


if __name__ == "__main__":
    main()