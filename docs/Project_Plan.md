# Project Plan (Compressed Schedule)

Presentation date: **16 September 2026**
Target completion: **12 September 2026** (4 days of buffer before the demo)

| Date | Focus | Tasks |
|---|---|---|
| Sep 3 (Thu) | Setup | Rename GitHub repo to `33443059_<COURSE_SECTION>`, confirm collaborator added, set up Python virtual environment, install requirements, test webcam + MediaPipe with a quick hello-world script |
| Sep 4 (Fri) | Data Collection (Part 1) | Record landmark samples for letters A-M using `collect_data.py` (40-60 samples each) |
| Sep 5 (Sat) | Data Collection (Part 2) | Record landmark samples for letters N-Y (excluding J), clean up `landmarks.csv` |
| Sep 6 (Sun) | Model Training | Run `train_model.py`, compare SVM vs MLP accuracy, save the confusion matrix |
| Sep 7 (Mon) | Improve Accuracy | Identify letters with low accuracy from the confusion matrix, collect extra samples for those letters, retrain |
| Sep 8 (Tue) | Real-Time Testing | Run `recognize.py`, test recognition live, fix any bugs (lighting, hand distance, prediction lag) |
| Sep 9 (Wed) | Documentation | Finalize Problem Analysis, System Design, Tools, and Dataset docs; add screenshots to `screenshots/` |
| Sep 10 (Thu) | Repo Quality Pass | Clean up code comments, verify README instructions work from a fresh clone, write LOG.md entries covering the whole week |
| Sep 11 (Fri) | Presentation Prep | Prepare slides (Problem, Solution, Workflow, Demo, Results, Conclusion), rehearse the live demo at least twice |
| Sep 12 (Sat) | Final Buffer | Final commit, double-check repo is complete and collaborator access works; project considered complete |
| Sep 13-15 | Rehearsal Buffer | Extra practice runs of the live demo in different lighting/locations to make sure it works reliably on demo day |
| Sep 16 | Presentation | Live demo, presentation, and viva |

## Deliverables Checklist
- [ ] GitHub repo renamed correctly and collaborator (`data-boss`) added
- [ ] `landmarks.csv` with data for all supported letters
- [ ] Trained model (`sign_model.pkl`) with reported accuracy
- [ ] Confusion matrix image in `docs/`
- [ ] Working `recognize.py` live demo
- [ ] All documentation files completed in `docs/`
- [ ] `logs/LOG.md` updated throughout
- [ ] Presentation slides ready
