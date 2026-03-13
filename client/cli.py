import requests


SERVER = "http://localhost:5000"


def main():

    r = requests.post(f"{SERVER}/start_session")

    session_id = r.json()["session_id"]

    print("Session started:", session_id)

    while True:

        query = input("\nYou: ")

        if query == "exit" or query == "quit" or query == "q":
            break

        r = requests.post(
            f"{SERVER}/query",
            json={
                "session_id": session_id,
                "message": query
            }
        )

        print("\nAssistant:", r.json()["answer"])


if __name__ == "__main__":
    main()