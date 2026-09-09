"""
app.py
Streamlit interface for the local Academic RAG Assistant.
Upload PDF documents, index them into ChromaDB, and ask questions answered
using Retrieval-Augmented Generation with a local LLM (Phi-3 via Ollama).
"""
import streamlit as st
from ingest import ingest_pdfs, get_vector_store, reset_vector_store
from llm_config import get_llm
from retriever import get_relevant_chunks, build_prompt

st.set_page_config(page_title="Academic RAG Assistant", page_icon="📚")
st.title("📚 AI-Powered Academic Assistant")
st.caption("Fully local Retrieval-Augmented Generation over your own PDF documents.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.sidebar:
    st.header("Upload Documents")
    uploaded_files = st.file_uploader("Upload one or more PDF files", type="pdf", accept_multiple_files=True)
    if st.button("Index Documents") and uploaded_files:
        with st.spinner("Extracting text, chunking, and generating embeddings..."):
            ingest_pdfs(uploaded_files)
        st.success("Documents indexed. You can now ask questions.")

    st.divider()
    if st.button("Reset Knowledge Base"):
        reset_vector_store()
        st.session_state.chat_history = []
        st.success("Knowledge base cleared.")

st.subheader("Ask a Question")
question = st.text_input("Type your question about the uploaded documents:")

if st.button("Ask") and question:
    with st.spinner("Retrieving relevant content and generating answer..."):
        vectordb = get_vector_store()
        docs = get_relevant_chunks(vectordb, question)
        context = "\n\n".join(d.page_content for d in docs)
        prompt = build_prompt(context, question)
        llm = get_llm()
        answer = llm.invoke(prompt)
        sources = [
            f"{d.metadata.get('source', 'unknown')} (page {d.metadata.get('page', '?')})"
            for d in docs
        ]

    st.session_state.chat_history.append({"question": question, "answer": answer, "sources": sources})

for entry in reversed(st.session_state.chat_history):
    st.markdown(f"**Q: {entry['question']}**")
    st.write(entry["answer"])
    with st.expander("Sources"):
        for s in entry["sources"]:
            st.write(f"- {s}")
    st.divider()
