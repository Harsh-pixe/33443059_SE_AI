# Evaluation Methodology

This document describes how the RAG system is evaluated, directly following the methodology promised in the project proposal (Section 7).

## Why This Exists
Most similar student projects only demonstrate that the chatbot "works" by asking it a question live. This project goes further by measuring performance against a fixed test set, so claims about accuracy and reliability are backed by numbers, not just a working demo.

## Model Used
The system uses **Phi-3 (via Ollama)** as the local LLM, as proposed, chosen over larger models like Mistral 7B because it is lighter and runs without lag on a laptop with no dedicated GPU.

## Test Set
A fixed set of 8 questions (`eval/eval_questions.json`) was written against a representative test PDF, including:
- Questions with clear, findable answers in the document.
- One question the document cannot answer, to check the system correctly responds "I don't know" rather than guessing.

## Metrics Measured

**Response Time** — how long (in seconds) the system takes to answer each question, measured directly around the LLM call.

**Keyword-Based Answer Accuracy** — each test question has a small set of expected keywords; the score is the proportion of those keywords present in the generated answer. This is a lightweight substitute for manual grading of every answer.

**Retrieval Precision** — for questions with a known expected source page, whether that page number appears among the retrieved chunks' metadata.

**Faithfulness Score** — cosine similarity between the embedding of the generated answer and the embedding of the retrieved context. A low score flags a possible hallucination (the answer may contain information not actually present in the retrieved text).

## Chunking Experiment
To address the proposal's research question on chunking, the same test set is run twice against the same document indexed at two different chunk sizes (300 and 800 characters), comparing keyword accuracy and faithfulness between the two. Results are saved to `eval/chunking_results.csv`.

## Limitations of This Evaluation
- The keyword-matching accuracy score is a simple proxy for correctness, not a full semantic judgment of answer quality.
- The faithfulness score is based on embedding similarity, not a perfect hallucination detector.
- The test set is small (8 questions) to keep evaluation fast; a larger set would give more statistically reliable results.
