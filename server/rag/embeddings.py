from sentence_transformers import SentenceTransformer


class EmbeddingModel:

    def __init__(self, model_name="BAAI/bge-small-en"):
        self.model = SentenceTransformer(model_name)

    def __call__(self, input):
        # Chroma expects list[str] → list[list[float]]
        return self.model.encode(input).tolist()
    
    @staticmethod
    def name() -> str:
        return "my-embedding-model"
    
    def embed_query(self, input):
        # Chroma expects list[str] → list[list[float]]
        return self.model.encode(input).tolist()

    def name(self):
        return "bge-small-en"
    
    # What is the notice period for terminating the NDA?