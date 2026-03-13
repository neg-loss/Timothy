import ollama
from server.config import OLLAMA_MODEL


class GuardrailAgent:

    def check(self, query):

        prompt = f"""
You are a guardrail agent for a legal contract analysis system.

Determine whether the query is within scope.

IN SCOPE:
- Questions about clauses in contracts
- Risk analysis
- Contract comparisons
- Contract summaries
- Question about interpretaion
- Terms and conditions

OUT OF SCOPE:
- Drafting new contracts
- Legal advice
- Litigation strategies
- Anything unrelated to provided contracts

Query:
{query}

Return ONLY one label:

IN_SCOPE
OUT_OF_SCOPE
"""

        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[{"role": "user", "content": prompt}]
        )

        label = response["message"]["content"].strip()

        return label