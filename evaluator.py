from evaluation import evaluate

from server.rag.embeddings import EmbeddingModel
from server.rag.vector_store import VectorStore
from server.agents.guardrail_agent import GuardrailAgent
from server.agents.query_agent import QueryAgent
from server.agents.memory_agent import MemoryAgent
from server.agents.retrieval_agent import RetrievalAgent
from server.agents.rerank_agent import RerankAgent
from server.agents.risk_agent import RiskAgent
from server.agents.answer_agent import AnswerAgent
from server.agents.orchestrator import Orchestrator

embedder = EmbeddingModel()
vector_store = VectorStore(embedder)
guardrail_agent = GuardrailAgent()
memory_agent = MemoryAgent()
query_agent = QueryAgent()
retrieval_agent = RetrievalAgent(vector_store)
rerank_agent = RerankAgent()
risk_agent = RiskAgent()
answer_agent = AnswerAgent()

orchestrator = Orchestrator(
    guardrail_agent=guardrail_agent,
    memory_agent=memory_agent,
    query_agent=query_agent,
    retrieval_agent=retrieval_agent,
    rerank_agent=rerank_agent,
    risk_agent=risk_agent,
    answer_agent=answer_agent
)

evaluate.evaluate(orchestrator)