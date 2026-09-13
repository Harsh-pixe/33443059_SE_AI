# AI-Powered Academic Assistant (Local RAG)

**Student:** Harsh Dhiman
**Student ID:** 33443059
**Module:** Artificial Intelligence

Fully local Retrieval-Augmented Generation (RAG) system for question answering over user-uploaded PDF documents. No cloud APIs, no cost — everything runs on your own machine.

## How It Works
```
PDF Upload -> Text Extraction (PyPDF) -> Chunking -> Embeddings (Sentence-Transformers)
-> ChromaDB -> Retriever -> Phi-3 (via Ollama) -> Answer
```

## Repository Structure
```
33443059_SE_AI/
├── app.py              # Streamlit UI
├── config.py            # Shared settings (model names, chunk size, etc.)
├── ingest.py             # PDF loading, chunking, embeddings, vector store
├── llm_config.py         # Local LLM configuration (Phi-3 via Ollama)
├── retriever.py          # Retrieval + prompt construction
├── requirements.txt
├── data/                 # Place a sample PDF here for eval/chunking_experiment.py
├── eval/                 # Evaluation harness (see docs/Evaluation_Methodology.md)
├── docs/                 # Project documentation
├── logs/                 # Weekly development logs
└── .gitignore
```

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
ollama pull phi3
```

## Run the App
```bash
streamlit run app.py
```
Upload a PDF, click **Index Documents**, then ask a question.

## Run the Evaluation
See `docs/Evaluation_Methodology.md` for details.
```bash
python eval/evaluate.py
python eval/chunking_experiment.py
```

## Documentation
- `docs/Evaluation_Methodology.md` — how the system is evaluated
- `docs/Model_Switch_Note.md` — why Phi-3 was chosen
- `docs/Daily_Commit_Plan.md` — development schedule

## Results

The system was evaluated against a fixed set of 9 test questions (8 answerable, 1 deliberately unanswerable) using a 5-page test document. Full methodology in `docs/Evaluation_Methodology.md`, full results in `docs/Findings.md`.

| Metric | Value |
|---|---|
| Average response time | 2.61s |
| Retrieval precision | 100% (8/8 answerable questions) |
| Average keyword accuracy | 0.82 |
| Average faithfulness score | 0.60 |

**Chunking experiment:** smaller chunks (300 characters) produced more faithful answers (0.67) but lower keyword accuracy (0.54); larger chunks (800 characters) produced higher keyword accuracy (0.78) but lower faithfulness (0.56) — a real accuracy/grounding trade-off, not a single "best" size.

**Limitation found:** manual testing revealed the system does not reliably decline to answer questions outside the scope of the uploaded document, and can supplement retrieved context with outside general knowledge on broad, open-ended prompts. See `docs/Findings.md` and `screenshots/manual_test_hallucination_example.png` for a documented example.

Screenshots of the working application and manual test cases are available in `screenshots/`.
