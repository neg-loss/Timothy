
# Legal RAG

This repository contains a Retrieval Augmented Generation (RAG) application for legal documents. The application uses a vector store of legal contract clauses to answer user questions.

## Architecture

The application is built with a modular architecture, with different agents responsible for specific tasks. The `Orchestrator` class in `server/agents/orchestrator.py` coordinates the workflow between these agents.

The main components are:

- **Flask Server**: The main entry point of the application is a Flask server defined in `app.py`. It exposes endpoints for starting a session and asking questions.
- **Ingestion Pipeline**: The `ingest.py` script is responsible for reading legal documents from the `data/` directory, splitting them into clauses, and storing them in a Chroma vector store.
- **Embedding Model**: The `server/rag/embeddings.py` file defines the `EmbeddingModel` class, which uses a sentence-transformer model to create vector embeddings of the text.
- **Vector Store**: The `server/rag/vector_store.py` file defines the `VectorStore` class, which provides an interface to the Chroma vector store.
- **Agents**: The `server/agents/` directory contains several agents that perform specific tasks in the RAG pipeline:
    - `GuardrailAgent`: Checks if the user's query is within the scope of the application.
    - `MemoryAgent`: Rewrites the user's query based on the conversation history.
    - `QueryAgent`: Classifies the user's query.
    - `RetrievalAgent`: Retrieves relevant context from the vector store.
    - `RerankAgent`: Reranks the retrieved contexts.
    - `RiskAgent`: Analyzes the risk associated with the user's query.
    - `AnswerAgent`: Generates an answer based on the user's query and the retrieved context.
- **Evaluation**: The `evaluation/` directory contains scripts for evaluating the performance of the RAG application.

## How to run

1. **Install dependencies**:
```bash
pip install -r requirements.txt
```

2. **Ingest data**:
```bash
python ingest.py
```

3. **Run Ollama Server**:
```bash
ollama run llama3
```

4. **Run the application**:
```bash
python app.py
```

The server will start on port 5000.

5. **Use the application**:

You can use the `client/cli.py` script to interact with the application from the command line.

## Evaluation

To evaluate the performance of the application, run the `evaluator.py` script:

```bash
python evaluator.py
```

This will run the evaluation queries from `evaluation/eval_queries.json` and print the results. This might take some time depending on the number of queries.
