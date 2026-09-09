"""
retriever.py
Retrieves the most relevant chunks from the vector store for a given
question, and builds the prompt sent to the LLM.
"""
from config import TOP_K

PROMPT_TEMPLATE = """Use the following context to answer the question.
If the answer isn't in the context, say you don't know.

Context:
{context}

Question: {question}

Answer:"""


def get_relevant_chunks(vectordb, question, k=TOP_K):
    return vectordb.similarity_search(question, k=k)


def build_prompt(context, question):
    return PROMPT_TEMPLATE.format(context=context, question=question)
