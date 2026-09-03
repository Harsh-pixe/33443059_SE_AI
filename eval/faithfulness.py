"""
faithfulness.py
Lightweight faithfulness check: measures how well a generated answer is
supported by the retrieved context, using the same embedding model already
loaded for retrieval (no extra model needed, so this stays fast/lightweight).

A LOW score suggests the answer may contain information not actually
present in the retrieved context (a possible hallucination).
"""
import numpy as np


def cosine_similarity(vec_a, vec_b):
    a = np.array(vec_a)
    b = np.array(vec_b)
    denom = (np.linalg.norm(a) * np.linalg.norm(b))
    if denom == 0:
        return 0.0
    return float(np.dot(a, b) / denom)


def faithfulness_score(embeddings, answer, context):
    """
    embeddings: a LangChain-compatible embeddings object with .embed_query()
    answer: the generated answer text (string)
    context: the retrieved context text used to generate the answer (string)
    Returns a float between -1 and 1 (higher = more faithful/supported).
    """
    if not answer.strip() or not context.strip():
        return 0.0
    answer_vec = embeddings.embed_query(answer)
    context_vec = embeddings.embed_query(context)
    return cosine_similarity(answer_vec, context_vec)


def flag_hallucination(score, threshold=0.35):
    """Returns True if the faithfulness score is below the threshold,
    suggesting the answer may not be well supported by the retrieved context."""
    return score < threshold
