import uuid
import time


class SessionManager:

    def __init__(self):

        self.sessions = {}

    def create_session(self):

        session_id = str(uuid.uuid4())

        self.sessions[session_id] = {
            "history": [],
            "last_active": time.time()
        }

        return session_id

    def get_history(self, session_id):

        return self.sessions[session_id]["history"]

    def add_message(self, session_id, role, message):

        self.sessions[session_id]["history"].append(
            {"role": role, "message": message}
        )

        self.sessions[session_id]["last_active"] = time.time()