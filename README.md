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
