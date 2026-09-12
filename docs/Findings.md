# Evaluation Findings

## Test Setup
- Test document: `data/sample.pdf` (5-page overview of Retrieval-Augmented Generation)
- Number of test questions: 9 (8 answerable, 1 deliberately unanswerable)
- LLM used: Phi-3 (via Ollama)
- Embedding model: sentence-transformers/all-MiniLM-L6-v2

## Overall Results (`eval/results.csv`)
| Metric | Value |
|---|---|
| Average response time | 2.61s |
| Average keyword score | 0.82 |
| Retrieval precision | 1.00 (8/8 answerable questions correctly retrieved their source page) |
| Average faithfulness score | 0.60 |
| Possible hallucinations flagged | 1 / 9 |

## Chunking Experiment Results (`eval/chunking_results.csv`)
| Chunk Size | Avg Keyword Score | Avg Faithfulness |
|---|---|---|
| 300 characters | 0.54 | 0.67 |
| 800 characters | 0.78 | 0.56 |

## Discussion

**Retrieval was fully reliable on this test set.** All 8 answerable questions retrieved a chunk from the correct source page (retrieval precision = 1.00), and average keyword accuracy was high (0.82), suggesting the embedding + ChromaDB retrieval pipeline works well for this document.

**Response time was fast and practical.** At 2.61 seconds average (excluding the very first, unindexed run reported earlier), Phi-3 via Ollama is responsive enough for interactive use on a MacBook Air with no dedicated GPU — validating the choice of a lightweight local model.

**The system did not handle the unanswerable question correctly.** Question 9 ("What is the capital of France?") should have triggered an "I don't know" response, since the test document does not cover this topic. Instead, the keyword score was 0.0 and the faithfulness score was very low (0.05), and the system flagged this as a likely hallucination. This is a genuine limitation: the current prompt instructs the model to say it doesn't know when the answer isn't in the context, but Phi-3 did not reliably follow this instruction on unrelated questions. This is a worthwhile area for future improvement (e.g., a stricter prompt, or a similarity threshold that refuses to answer when no retrieved chunk is close enough to the question).

**Chunk size involves a real trade-off.** Smaller (300-character) chunks produced answers more tightly grounded in the retrieved text (higher faithfulness, 0.67) but with lower keyword accuracy (0.54), likely because each chunk contains less complete context. Larger (800-character) chunks produced more complete, accurate-sounding answers (keyword score 0.78) but were somewhat less faithful to the retrieved text (0.56), possibly because more unrelated surrounding text gets pulled in alongside the relevant passage. This directly answers the project proposal's research question on chunking: there is no single "best" chunk size — it is a trade-off between answer completeness and grounding, and the right choice depends on whether accuracy or faithfulness matters more for a given use case.

## Limitations Observed
- The keyword-matching accuracy score is a simple proxy for correctness, not a full semantic judgment of answer quality.
- The faithfulness score is based on embedding similarity, not a perfect hallucination detector.
- The test set is small (9 questions) and based on a single document; a larger, multi-document test set would give more statistically reliable results.
- The system does not reliably decline to answer questions outside the scope of the uploaded document.
