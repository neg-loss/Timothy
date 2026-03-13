import chromadb

class VectorStore:

    def __init__(self, embedding_model):

        self.client = chromadb.PersistentClient()

        # self.client = chromadb.PersistentClient(Settings(chroma_db_impl="duckdb+parquet", persist_directory=VECTOR_DB_PATH))

        print("collection list", self.client.list_collections())

        self.collection = self.client.get_or_create_collection(
            name="contracts",
            embedding_function=embedding_model
        )

    def add_documents(self, documents, metadatas, ids):

        self.collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )

    def search(self, query, k=5):

        results = self.collection.query(
            query_texts=[query],
            n_results=k
        )

        return results