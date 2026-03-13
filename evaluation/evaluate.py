import json

def evaluate(orchestrator):

    with open("evaluation/eval_queries.json") as f:
        queries = json.load(f)

    correct = 0

    print("Evaluation started...\n")
    for q in queries:

        result = orchestrator.run(q["query"], [])

        contexts = result["contexts"]

        text = " ".join([c["text"] for c in contexts]).lower()

        if q["expected_keyword"] in text:

            correct += 1

        print("Query:", q["query"])
        print("Retrieved:", text)
        print("===============================================\n")

    print("Retrieval accuracy:", correct / len(queries))