# Evaluation Findings

*(Fill this in after running `eval/evaluate.py` and `eval/chunking_experiment.py`.)*

## Test Setup
- Test document: `data/sample.pdf`
- Number of test questions: (fill in)
- LLM used: Phi-3 (via Ollama)
- Embedding model: sentence-transformers/all-MiniLM-L6-v2

## Overall Results (from `eval/results.csv`)
| Metric | Value |
|---|---|
| Average response time (s) | |
| Average keyword score | |
| Retrieval precision | |
| Average faithfulness score | |
| Possible hallucinations flagged | |

## Chunking Experiment Results (from `eval/chunking_results.csv`)
| Chunk Size | Avg Keyword Score | Avg Faithfulness |
|---|---|---|
| 300 | | |
| 800 | | |

## Discussion
(Write 3-5 sentences: which chunk size performed better and why you think that is; whether the system correctly said "I don't know" on the unanswerable question; any surprising results.)

## Limitations Observed
(Note anything that went wrong during testing — slow responses, wrong retrievals, etc.)
