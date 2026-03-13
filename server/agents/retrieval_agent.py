class RetrievalAgent:

    def __init__(self, vector_store):

        self.vector_store = vector_store

    def retrieve(self, query):

        results = self.vector_store.search(query)

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]

        context = []

        for doc, meta in zip(documents, metadatas):

            context.append({
                "text": doc,
                "metadata": meta
            })

        return context