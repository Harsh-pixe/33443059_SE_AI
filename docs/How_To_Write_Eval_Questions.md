# How To Write Evaluation Questions

Use this guide to fill in `eval/eval_questions.json` with real questions based on your own test PDF.

## Steps
1. Pick one PDF you'll use as your main test document (e.g., a lecture note or paper). Put a copy in `data/sample.pdf` — this is also used by `eval/chunking_experiment.py`.
2. Open the PDF and note the page number for each fact you'll turn into a question.
3. For each question, fill in:
   - `question`: a natural-language question a real user might ask.
   - `expected_keywords`: 1-3 words/phrases that MUST appear in a correct answer.
   - `expected_source_page`: the page number where that answer is found (use `null` if the question is designed to be unanswerable).

## Example
If page 3 of your PDF says *"Retrieval-Augmented Generation combines a retriever with a generative language model,"* a good entry is:
```json
{
  "id": 1,
  "question": "What does Retrieval-Augmented Generation combine?",
  "expected_keywords": ["retriever", "language model"],
  "expected_source_page": 3
}
```

## Tips
- Include at least one question the PDF **cannot** answer (set `expected_source_page` to `null`, and `expected_keywords` to something like `["don't know", "not mentioned"]`) — this tests whether the system correctly avoids guessing.
- Keep questions specific enough that keyword matching is meaningful (avoid yes/no questions).
- 8-10 questions is enough; more isn't necessary and will just make `evaluate.py` slower to run.
