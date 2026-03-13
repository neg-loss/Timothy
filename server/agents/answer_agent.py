import ollama
from server.config import OLLAMA_MODEL


class AnswerAgent:

    def generate(self, query_type, query, context, risk_analysis):

        context_text = ""

        for c in context:

            meta = c["metadata"]

            context_text += f"""
Document: {meta['document']}
Clause: {meta['clause_id']}

{c['text']}
"""

        prompt = f"""
You are a legal contract assistant.

Answer the user's question using ONLY the context. You can drop information from the context if it is not relevant to the question.
You can also use the risk analysis as part of your answer if it is relevant.

Context:
{context_text}

Query Type: {query_type}

Question:
{query}

Risk Analysis:
{risk_analysis}

Provide:

Clear explanation to the user question. Cite relevant clauses/sources in your answer. Add risk analysis if relevant.
"""

        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[{"role": "user", "content": prompt}]
        )

        return response["message"]["content"]