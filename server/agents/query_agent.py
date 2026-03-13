import ollama
from server.config import OLLAMA_MODEL


class QueryAgent:

    def classify(self, query):

        prompt = f"""
You are a legal query classifier.

Classify the user query into one of the following categories:

CLAUSE_LOOKUP
AGREEMENT_LOOKUP
NDA
RISK_ANALYSIS
CONTRACT_COMPARISON
SUMMARY
INTERPRETATION
TERMS_AND_CONDITIONS
POLICY_SCOPE
INDEMNIFICATION
CONFIDENTIALITY
ACCOUNTABILITY
OUT_OF_SCOPE

Query:
{query}

Return ONLY the label.
"""

        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[{"role": "user", "content": prompt}]
        )

        label = response["message"]["content"].strip()

        return label