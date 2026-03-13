import ollama
from server.config import OLLAMA_MODEL


class RiskAgent:

    def analyze(self, query, context):

        context_text = "\n\n".join([c["text"] for c in context])

        prompt = f"""
You are a legal risk analysis assistant.

Analyze the document contract clauses and identify potential risks such as:

- Liability
- Accountability
- Loss due to weak clause
- Weak indemnification
- Missing breach notification
- Weak confidentiality protection
- Financial exposure

Context:
{context_text}

User Question:
{query}

Return:

Risk Level: LOW / MEDIUM / HIGH

Reason:
Short explanation.
"""

        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[{"role": "user", "content": prompt}]
        )

        return response["message"]["content"]