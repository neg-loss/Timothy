import ollama
from server.config import OLLAMA_MODEL


class MemoryAgent:

    def rewrite_query(self, query, history):

        if not history:
            return query

        history_text = ""

        for turn in history[-4:]:
            history_text += f"{turn['role']}: {turn['message']}\n"

        prompt = f"""
You are a query rewriting assistant.

Use conversation history and user query to form a standalone question.

Conversation history:
{history_text}

User query:
{query}

Rewrite the query so that it is self-contained.
Return ONLY the rewritten query.
"""

        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[{"role": "user", "content": prompt}]
        )

        rewritten = response["message"]["content"].strip()

        return rewritten