## Date
September 3, 2026

## Work Completed
- Decided to restart the project as a fresh, individually distinct build (moved away from the earlier sign-language prototype and back to the approved RAG proposal, with clearer differentiation from other student submissions).
- Set up `33443059_SE_AI` GitHub repository, added collaborator.
- Added `.gitignore` to exclude `.DS_Store`, `venv/`, `__pycache__/`, and `chroma_db/`.
- Added evaluation planning documentation (`Evaluation_Methodology.md`, `Daily_Commit_Plan.md`, `Model_Switch_Note.md`).
- Added the evaluation harness (`eval/evaluate.py`, `eval/faithfulness.py`, `eval/chunking_experiment.py`, `eval/eval_questions.json` template).
- Built the core RAG application from scratch: `config.py`, `ingest.py`, `llm_config.py`, `retriever.py`, `app.py`.
- Switched the local LLM to Phi-3 (via Ollama), matching the approved proposal.
- Fixed a LangChain import error (`RecursiveCharacterTextSplitter` moved to the `langchain-text-splitters` package) and confirmed the app runs end to end.

## Challenges
- LangChain has split several classes into smaller packages in recent versions, which broke the initial import in `ingest.py`.
- Needed to rebuild the core application from scratch rather than reusing an older codebase.

## Solutions
- Installed `langchain-text-splitters` and updated the import path.
- Wrote a minimal, self-contained app (config, ingestion, LLM config, retriever, UI) that matches the evaluation scripts already in `eval/`.

## Next Plan
- Fill `eval/eval_questions.json` with real questions based on a test PDF (see `docs/How_To_Write_Eval_Questions.md`).
- Add a representative test PDF to `data/`.
- Run `eval/evaluate.py` and commit the results.
