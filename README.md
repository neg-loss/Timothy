# Multi-Agent RAG System for Legal Contract Analysis

## Overview

This project implements a multi-agent Retrieval-Augmented Generation
(RAG) system that allows users to query and analyze legal contracts
through a console-based interactive interface.

The system enables users to ask natural language questions about contracts
and service agreements etc. It retrieves relevant clauses from the documents
and generates grounded answers with supporting references and risk indicators.

The architecture is designed as a multi-agent system where each agent performs
a specialized task such as query validation, context retrieval, risk detection, and answer generation.

The system runs using a client-server architecture:

Flask Server - Hosts the RAG system and agents - Loads models and vector database - Manages conversation sessions

CLI Client - Interactive console interface - Supports multiple independent sessions

# Problem Statement

Legal contracts contain critical clauses related to confidentiality, liability, termination, compliance, 
and governing law. Manually analyzing these documents is time-consuming and error-prone.

This system provides:

-   Natural language querying of contracts
-   Retrieval of relevant clauses
-   Grounded answers with citations
-   Detection of potential legal risks
-   Multi-turn conversation support

# System Architecture

User Query | Guardrail Agent | Memory Agent | Query Classification Agent | Retrieval Agent | Rerank 
Agent | Risk Analysis Agent | Answer Generation Agent | Final Response + Sources + Risk Indicators

![Architecture](new_architecture.png)


# Setup Instructions(works well on linux)

1.  Install dependencies(preferably in separate conda env)

`pip install -r requirements.txt`

2.  Install Ollama

```
curl -fsSL https://ollama.com/install.sh | sh
```

And then run it `ollama run ollama3` (Separate terminal)

3.  Ingest documents(One time activity)

`python ingest.py`

4.  Start server

`python app.py` (Separate terminal)

5.  Start client

`python client/cli.py` (Separate terminal)

### Warning:

For the first run, it would download models and hence require a good internet connection.


## Components

Client - CLI interface - Sends queries to server - Maintains session ID

Flask Server Responsible for: - Running agents - Managing sessions - Retrieval pipeline - Response orchestration

Vector Database Stores contract clause embeddings and metadata for retrieval.

# Multi-Agent Design

Each agent has a clear and isolated responsibility.

## 1. Guardrail Agent

Purpose: Ensures queries are within system scope.

Blocks queries related to: - Legal advice - Contract drafting - Non-legal questions

Example blocked queries:

`Who won the world cup?`

Output:

```
"Sorry, I can only answer questions related to legal contracts. Please ask a different question."
```

## 2. Memory Agent

Purpose: Enables multi-turn conversation.

It converts follow-up questions into standalone queries using conversation history.

Example:

```
User: What is the termination clause in the NDA?
User: What about notice period?
```

Memory Agent rewrites:

```
What is the notice period for termination in the NDA?
```

## 3. Query Classification Agent

Purpose: Classifies the intent of the user query. Helps during answer generation phase.

## 4. Retrieval Agent(Not really an agent but ...)

Responsible for retrieving relevant contract clauses using vector
similarity search.

Steps:

1.  Convert query to embedding
2.  Search vector database
3.  Retrieve top-K relevant clauses

## 5. Rerank Agent

Vector search may return approximate matches.

The Rerank Agent improves retrieval precision using a cross-encoder model.

Steps:

(query, clause) pairs → relevance scoring sort by relevance return best clauses

## 6. Risk Analysis Agent

Analyzes retrieved clauses for potential legal risks such as:

-   Unlimited liability
-   Weak confidentiality protections
-   Missing breach notification requirements
-   Vendor exposure

Outputs:

Related risks associated with the clause/section.

## 7. Answer Generation Agent

Generates the final answer using:

-   Retrieved clauses
-   Risk analysis
-   User query
-   Query type

The answer includes:

-   Natural language response
-   Clause references
-   Risk summary

# Retrieval-Augmented Generation (RAG) Design

## Document Chunking Strategy

Legal documents are structured into clauses and numbered sections.

Instead of naive chunking, the system performs clause-aware chunking by splitting 
documents based on section numbering patterns.

Example:

5.  Termination 5.1 Notice Period 5.2 Survival

Each clause becomes an independent chunk.

Benefits:

-   Preserves semantic meaning
-   Improves retrieval accuracy
-   Enables precise citations

## Embedding Model

Embedding model used:

`BAAI/bge-small-en`

Reasons for selection:

-   High-quality semantic embeddings
-   Lightweight and fast
-   Good performance for retrieval tasks

## Vector Database

Vector store used:

`ChromaDB`

Reasons:

-   Lightweight
-   Local deployment
-   Simple API
-   Good integration with Python

Stored metadata includes:

document name, section, title, clause text etc.

## LLM Model Choice

LLM used:

Llama 3 via Ollama

Reasons:

-   Runs locally
-   No API cost
-   Good reasoning capability
-   Supports streaming responses

## Prompt Design

Prompts are carefully designed to:

-   Enforce grounded answers
-   Avoid hallucinations
-   Produce structured outputs
-   Maintain determinism

# Multi-Turn Conversation

The system supports conversation sessions.

Features:

-   Each client session has unique ID
-   Conversation history stored server-side
-   History used by Memory Agent

# RAG Ingestion Workflow

Load contract documents | Clause-based chunking | Generate embeddings | Store in vector database

# Evaluation Approach

A small evaluation pipeline is implemented to assess system performance.

## What is Evaluated

1.  Retrieval Accuracy Measured by checking if expected keywords appear
    in retrieved clauses.

## Limitations of Evaluation

-   Small evaluation dataset
-   Keyword-based correctness
-   No human expert validation

# Example Queries

- What is the notice period for terminating the NDA? 
- Which law governs the Vendor Services Agreement?
- Do confidentiality obligations survive termination?
- Is liability capped for breach of confidentiality?
- Are there any legal risks related to liability exposure? Summarize all risks for Acme Corp.

# Known Limitations

-   Small document corpus
-   Limited evaluation dataset
-   Risk analysis relies on LLM reasoning
-   No hybrid retrieval
-   No legal fine-tuning

# Potential Production Enhancements

Better Legal Parsing Use advanced legal document parsers.

Larger Evaluation Benchmarks Create labeled datasets for retrieval and risk detection.

Guardrail Improvements Add stronger safety filters.

Scalable Architecture Move from Flask to a distributed microservice architecture.

# Conclusion

This project demonstrates a modular multi-agent RAG system for legal contract analysis with:

-   Interactive CLI interface
-   Clause-aware retrieval
-   Multi-turn conversations
-   Risk detection
-   Grounded responses with citations

The architecture emphasizes separation of responsibilities across agents, enabling maintainability and extensibility.
