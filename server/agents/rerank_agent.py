from sentence_transformers import CrossEncoder


class RerankAgent:

    def __init__(self):

        self.model = CrossEncoder(
            "cross-encoder/ms-marco-MiniLM-L-6-v2"
        )

    def rerank(self, query, contexts, top_k=3):

        pairs = [[query, c["text"]] for c in contexts]

        scores = self.model.predict(pairs)

        ranked = sorted(
            zip(contexts, scores),
            key=lambda x: x[1],
            reverse=True
        )

        return [r[0] for r in ranked[:top_k]]