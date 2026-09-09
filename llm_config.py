"""
llm_config.py
Configures the local LLM used for answer generation, served via Ollama.
Uses Phi-3, as listed in the approved project proposal, chosen for its
lighter footprint (runs without lag on a laptop with no dedicated GPU).
"""
from langchain_community.llms import Ollama
from config import LLM_MODEL, LLM_TEMPERATURE


def get_llm():
    return Ollama(model=LLM_MODEL, temperature=LLM_TEMPERATURE)
