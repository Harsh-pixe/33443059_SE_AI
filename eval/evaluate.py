"""
evaluate.py
Evaluation harness for the RAG system. Runs a fixed set of test questions
through the existing retrieval + generation pipeline and measures:
  - Response time
  - Keyword-based answer accuracy
  - Retrieval precision (did the expected source page come back?)
  - Faithfulness (is the answer actually supported by the retrieved context?)

Kept deliberately lightweight (small model, small top_k, small question set)
so it runs quickly on a laptop with no GPU.

EDIT the constants below to match your existing project's config.py values
before running.

Usage:
    python eval/evaluate.py
"""
import json
import time
import csv
import os
import sys

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama

sys.path.append(os.path.dirname(__file__))
from faithfulness import faithfulness_score, flag_hallucination

# ---- EDIT THESE TO MATCH YOUR EXISTING config.py ----
PERSIST_DIR = "chroma_db"
COLLECTION_NAME = "academic_docs"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "phi3"          # lightweight local model, swapped from llama3.2
TOP_K = 3
# ------------------------------------------------------

EVAL_SET_PATH = os.path.join(os.path.dirname(__file__), "eval_questions.json")
RESULTS_PATH = os.path.join(os.path.dirname(__file__), "results.csv")

PROMPT_TEMPLATE = """Use the following context to answer the question.
If the answer isn't in the context, say you don't know.

Context:
{context}

Question: {question}

Answer:"""


def load_eval_set(path=EVAL_SET_PATH):
    with open(path) as f:
        return json.load(f)


def run_pipeline(vectordb, llm, question, k=TOP_K):
    docs = vectordb.similarity_search(question, k=k)
    context = "\n\n".join(d.page_content for d in docs)
    prompt = PROMPT_TEMPLATE.format(context=context, question=question)

    start = time.time()
    answer = llm.invoke(prompt)
    elapsed = time.time() - start

    sources = [d.metadata.get("page") for d in docs]
    return answer, sources, context, elapsed


def score_keywords(answer, expected_keywords):
    if not expected_keywords:
        return None
    answer_lower = answer.lower()
    hits = sum(1 for kw in expected_keywords if kw.lower() in answer_lower)
    return round(hits / len(expected_keywords), 2)


def main():
    print(f"Loading embeddings ({EMBEDDING_MODEL}) and vector store...")
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    vectordb = Chroma(
        persist_directory=PERSIST_DIR,
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
    )
    print(f"Loading local LLM via Ollama: {LLM_MODEL}...")
    llm = Ollama(model=LLM_MODEL, temperature=0.1)

    eval_set = load_eval_set()
    results = []

    for item in eval_set:
        answer, sources, context, elapsed = run_pipeline(vectordb, llm, item["question"])
        keyword_score = score_keywords(answer, item.get("expected_keywords"))

        retrieval_hit = None
        expected_page = item.get("expected_source_page")
        if expected_page is not None:
            retrieval_hit = expected_page in sources

        f_score = faithfulness_score(embeddings, answer, context)
        hallucination_flag = flag_hallucination(f_score)

        row = {
            "id": item.get("id"),
            "question": item["question"],
            "answer": answer.replace("\n", " ").strip(),
            "sources": sources,
            "response_time_sec": round(elapsed, 2),
            "keyword_score": keyword_score,
            "retrieval_hit": retrieval_hit,
            "faithfulness_score": round(f_score, 2),
            "possible_hallucination": hallucination_flag,
        }
        results.append(row)
        print(f"[{row['id']}] {item['question'][:45]:45} "
              f"time={row['response_time_sec']}s  kw={keyword_score}  "
              f"retrieval_hit={retrieval_hit}  faithfulness={row['faithfulness_score']}")

    with open(RESULTS_PATH, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(results[0].keys()))
        writer.writeheader()
        writer.writerows(results)
    print(f"\nSaved detailed results to {RESULTS_PATH}")

    avg_time = sum(r["response_time_sec"] for r in results) / len(results)
    kw_scores = [r["keyword_score"] for r in results if r["keyword_score"] is not None]
    avg_kw = sum(kw_scores) / len(kw_scores) if kw_scores else None
    hits = [r["retrieval_hit"] for r in results if r["retrieval_hit"] is not None]
    retrieval_precision = sum(hits) / len(hits) if hits else None
    avg_faithfulness = sum(r["faithfulness_score"] for r in results) / len(results)
    hallucination_count = sum(1 for r in results if r["possible_hallucination"])

    print("\n--- Summary ---")
    print(f"Average response time:      {avg_time:.2f}s")
    print(f"Average keyword score:      {avg_kw}")
    print(f"Retrieval precision:        {retrieval_precision}")
    print(f"Average faithfulness score: {avg_faithfulness:.2f}")
    print(f"Possible hallucinations:    {hallucination_count} / {len(results)}")


if __name__ == "__main__":
    main()
