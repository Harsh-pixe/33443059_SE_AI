"""
chunking_experiment.py
Tests two chunk sizes against the same evaluation question set, to answer
the proposal's research question: "How does the quality of document
chunking affect retrieval?"

Kept to 2 chunk sizes (not more) to keep runtime short on a laptop.

EDIT the constants below before running.

Usage:
    python eval/chunking_experiment.py
"""
import os
import sys
import json
import csv

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama

sys.path.append(os.path.dirname(__file__))
from faithfulness import faithfulness_score

# ---- EDIT THESE ----
SOURCE_PDF = "data/sample.pdf"          # path to one representative test PDF
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "phi3"
CHUNK_SIZES = [300, 800]                # characters; small vs large chunks
CHUNK_OVERLAP = 50
TOP_K = 3
# ---------------------

EVAL_SET_PATH = os.path.join(os.path.dirname(__file__), "eval_questions.json")
RESULTS_PATH = os.path.join(os.path.dirname(__file__), "chunking_results.csv")

PROMPT_TEMPLATE = """Use the following context to answer the question.
If the answer isn't in the context, say you don't know.

Context:
{context}

Question: {question}

Answer:"""


def load_eval_set():
    with open(EVAL_SET_PATH) as f:
        return json.load(f)


def build_temp_vectorstore(chunk_size, embeddings):
    loader = PyPDFLoader(SOURCE_PDF)
    pages = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=CHUNK_OVERLAP)
    chunks = splitter.split_documents(pages)
    vectordb = Chroma.from_documents(
        chunks, embeddings, collection_name=f"chunk_test_{chunk_size}"
    )
    return vectordb


def score_keywords(answer, expected_keywords):
    if not expected_keywords:
        return None
    answer_lower = answer.lower()
    hits = sum(1 for kw in expected_keywords if kw.lower() in answer_lower)
    return round(hits / len(expected_keywords), 2)


def run_for_chunk_size(chunk_size, eval_set, embeddings, llm):
    print(f"\n=== Chunk size: {chunk_size} characters ===")
    vectordb = build_temp_vectorstore(chunk_size, embeddings)

    kw_scores, faith_scores = [], []
    for item in eval_set:
        docs = vectordb.similarity_search(item["question"], k=TOP_K)
        context = "\n\n".join(d.page_content for d in docs)
        prompt = PROMPT_TEMPLATE.format(context=context, question=item["question"])
        answer = llm.invoke(prompt)

        kw = score_keywords(answer, item.get("expected_keywords"))
        if kw is not None:
            kw_scores.append(kw)
        faith_scores.append(faithfulness_score(embeddings, answer, context))

    avg_kw = sum(kw_scores) / len(kw_scores) if kw_scores else None
    avg_faith = sum(faith_scores) / len(faith_scores) if faith_scores else None
    print(f"Average keyword score: {avg_kw}")
    print(f"Average faithfulness:  {avg_faith:.2f}" if avg_faith is not None else "N/A")
    return {"chunk_size": chunk_size, "avg_keyword_score": avg_kw, "avg_faithfulness": avg_faith}


def main():
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    llm = Ollama(model=LLM_MODEL, temperature=0.1)
    eval_set = load_eval_set()

    results = [run_for_chunk_size(size, eval_set, embeddings, llm) for size in CHUNK_SIZES]

    with open(RESULTS_PATH, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["chunk_size", "avg_keyword_score", "avg_faithfulness"])
        writer.writeheader()
        writer.writerows(results)

    print(f"\nSaved comparison to {RESULTS_PATH}")
    print("\n--- Chunking Experiment Summary ---")
    for r in results:
        print(r)


if __name__ == "__main__":
    main()
