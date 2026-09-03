# Tools and Technologies

**Python** — Purpose: main programming language for the whole project. Why used: has strong, easy-to-use libraries for computer vision and machine learning.

**OpenCV** — Purpose: captures webcam frames and displays the live video window with the prediction overlay. Why used: it is the standard, lightweight library for real-time video in Python.

**MediaPipe** — Purpose: detects the hand in each frame and extracts 21 landmark points. Why used: it is highly optimized for CPU, so it runs smoothly on a MacBook without a GPU or lag.

**scikit-learn** — Purpose: provides the SVM and Neural Network (MLP) classifiers used to recognize letters from landmark data, plus tools for evaluation (accuracy, confusion matrix). Why used: simple to use, well documented, and lightweight compared to deep learning frameworks.

**pandas / NumPy** — Purpose: store and manipulate the landmark dataset before training. Why used: standard, reliable tools for handling tabular numeric data in Python.

**joblib** — Purpose: saves and loads the trained model file. Why used: the standard way to persist scikit-learn models.

**Matplotlib** — Purpose: generates the confusion matrix image used as evidence of model evaluation in the report. Why used: simple, widely used plotting library.

**Git / GitHub** — Purpose: version control and hosting the project repository. Why used: required by the course, and allows the commit history to show genuine progress over time.
