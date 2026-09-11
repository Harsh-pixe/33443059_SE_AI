"""
ingest.py
Loads uploaded PDF files, splits them into chunks, generates embeddings,
and stores/retrieves them from the local ChromaDB vector store.
"""
import os
import tempfile
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

from config import PERSIST_DIR, COLLECTION_NAME, EMBEDDING_MODEL, CHUNK_SIZE, CHUNK_OVERLAP

_embeddings = None


def get_embeddings():
    global _embeddings
    if _embeddings is None:
        _embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    return _embeddings


def get_vector_store():
    return Chroma(
        persist_directory=PERSIST_DIR,
        collection_name=COLLECTION_NAME,
        embedding_function=get_embeddings(),
    )


def ingest_pdfs(uploaded_files):
    """uploaded_files: list of Streamlit UploadedFile objects."""
    all_chunks = []
    splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)

    for uploaded_file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        loader = PyPDFLoader(tmp_path)
        pages = loader.load()
        for page in pages:
            page.metadata["source"] = uploaded_file.name

        chunks = splitter.split_documents(pages)
        all_chunks.extend(chunks)
        os.remove(tmp_path)

    vectordb = Chroma.from_documents(
        all_chunks,
        get_embeddings(),
        persist_directory=PERSIST_DIR,
        collection_name=COLLECTION_NAME,
    )
    return vectordb


def reset_vector_store():
    vectordb = get_vector_store()
    try:
        vectordb.reset_collection()
    except AttributeError:
        vectordb.delete_collection()
