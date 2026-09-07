"""
config.py
Shared configuration constants used by both the Streamlit app and the
evaluation scripts in eval/. Keep these values in sync — the eval scripts
already assume these exact defaults.
"""

PERSIST_DIR = "chroma_db"
COLLECTION_NAME = "academic_docs"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "phi3"
LLM_TEMPERATURE = 0.2
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
TOP_K = 3
