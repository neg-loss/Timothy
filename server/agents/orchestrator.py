from server.config import OUT_OF_SCOPE_RESPONSE

class Orchestrator:

    def __init__(
        self,
        guardrail_agent,
        memory_agent,
        query_agent,
        retrieval_agent,
        rerank_agent,
        risk_agent,
        answer_agent
    ):

        self.guardrail_agent = guardrail_agent
        self.memory_agent = memory_agent
        self.query_agent = query_agent
        self.retrieval_agent = retrieval_agent
        self.rerank_agent = rerank_agent
        self.risk_agent = risk_agent
        self.answer_agent = answer_agent

    def run(self, query, history):

        guardrail_label = self.guardrail_agent.check(query)

        if guardrail_label == "OUT_OF_SCOPE":
            return {"answer": OUT_OF_SCOPE_RESPONSE}

        rewritten_query = self.memory_agent.rewrite_query(query, history)

        query_type = self.query_agent.classify(rewritten_query)

        if query_type == "OUT_OF_SCOPE":
            return {"answer": OUT_OF_SCOPE_RESPONSE}

        contexts = self.retrieval_agent.retrieve(rewritten_query)

        contexts = self.rerank_agent.rerank(rewritten_query, contexts)

        risk = self.risk_agent.analyze(rewritten_query, contexts)

        answer = self.answer_agent.generate(query_type, rewritten_query, contexts, risk)

        return {
            "query_type": query_type,
            "rewritten_query": rewritten_query,
            "answer": answer,
            "contexts": contexts,
            "risk": risk
        }