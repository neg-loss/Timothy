from flask import Flask, request, jsonify

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

from server.sessions.session_manager import SessionManager


app = Flask(__name__)

print("Loading models...")

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

session_manager = SessionManager()

print("Server ready.")


@app.route("/start_session", methods=["POST"])
def start_session():

    session_id = session_manager.create_session()

    return jsonify({"session_id": session_id})


@app.route("/query", methods=["POST"])
def query():

    data = request.json

    session_id = data["session_id"]
    message = data["message"]

    history = session_manager.get_history(session_id)

    session_manager.add_message(session_id, "user", message)

    result = orchestrator.run(message, history)

    session_manager.add_message(session_id, "assistant", result["answer"])

    return jsonify(result)


if __name__ == "__main__":
    app.run(port=5000)