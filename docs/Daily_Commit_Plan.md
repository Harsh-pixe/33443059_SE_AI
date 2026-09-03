# Daily Commit Plan

Presentation date: **16 September 2026**
Target completion: **12 September 2026** (4 days of buffer)

Commit at the end of each day, even if the feature is only partly working — this builds a genuine commit history showing steady progress, which matters for the "quality of work and reporting on GitHub" 40%.

| Date | What to Add/Change | Suggested Commit Message |
|---|---|---|
| Sep 3 (Thu) | Add `docs/Evaluation_Methodology.md` and this `Daily_Commit_Plan.md` | `Add evaluation methodology and daily commit plan` |
| Sep 4 (Fri) | Switch LLM in `llm_config.py` to Phi-3 (see `docs/Model_Switch_Note.md`), run `ollama pull phi3`, confirm app still works | `Switch LLM from Llama 3.2 to Phi-3 for lighter local inference` |
| Sep 5 (Sat) | Fill in real questions/keywords/pages in `eval/eval_questions.json` based on your test PDF | `Add evaluation question set based on test document` |
| Sep 6 (Sun) | Add `eval/faithfulness.py` | `Add lightweight faithfulness scoring module` |
| Sep 7 (Mon) | Add `eval/evaluate.py`, run it, commit the generated `eval/results.csv` | `Add evaluation harness and initial evaluation results` |
| Sep 8 (Tue) | Add `eval/chunking_experiment.py`, run it, commit `eval/chunking_results.csv` | `Add chunking size experiment and results` |
| Sep 9 (Wed) | Write `docs/Findings.md` summarizing what the results show (accuracy, response time, faithfulness, best chunk size) | `Document evaluation and chunking findings` |
| Sep 10 (Thu) | Run through 10-15 test questions manually, fix any bugs found, update `logs/LOG.md` | `Bug fixes found during manual testing` |
| Sep 11 (Fri) | Update `README.md` to reference the evaluation results, prepare presentation slides | `Update README with evaluation summary, prep for presentation` |
| Sep 12 (Sat) | Final check: fresh clone test, confirm everything runs end to end, final commit | `Final polish and verification before presentation` |
| Sep 13-15 | Buffer: rehearse the live demo, no new code changes expected | (no commits required, or minor fixes only) |
| Sep 16 | Presentation day | — |

## Daily Commit Checklist (repeat each day)
1. Make your change.
2. Test that the app still runs (`streamlit run app.py`) without errors.
3. `git add .`
4. `git commit -m "..."` (use the suggested message above, or your own if it differs)
5. `git push`
6. Add 3-4 lines to `logs/LOG.md` for the day (Date, Work Completed, Challenges, Solutions, Next Plan).
