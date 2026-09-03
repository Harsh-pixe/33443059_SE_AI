# Model Switch Note: Llama 3.2 → Phi-3

## What Changed
The local LLM used by the system was switched from Llama 3.2 to **Phi-3**, matching the candidate models listed in the approved project proposal (Section 5).

## How to Apply This Change
1. Pull the new model once:
   ```bash
   ollama pull phi3
   ```
2. In your existing `llm_config.py`, change the model name passed to the Ollama client:
   ```python
   # Before
   llm = Ollama(model="llama3.2", temperature=0.2)

   # After
   llm = Ollama(model="phi3", temperature=0.2)
   ```
3. Restart the Streamlit app and confirm it still answers questions correctly.

## Why Phi-3
- It is smaller than Mistral 7B, so it runs noticeably faster with no lag on a laptop without a dedicated GPU.
- It is one of the two candidate models explicitly listed in the approved proposal.
- It keeps the project fully local and zero-cost, consistent with the proposal's aim.
