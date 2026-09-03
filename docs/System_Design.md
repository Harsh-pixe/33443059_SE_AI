# System Design

## Overall Architecture
The system has three stages: hand detection (MediaPipe), feature preparation (landmark normalization), and classification (a trained ML model). No cloud services or GPU are used; everything runs locally on CPU.

## Workflow
```
  Webcam Frame
       |
       v
  MediaPipe Hand Detection
       |
       v
  Extract 21 Landmarks (x, y, z)
       |
       v
  Normalize Landmarks
       |
       v
  Trained Classifier (SVM / MLP)
       |
       v
  Predicted Letter
       |
       v
  Display on Screen
```

## Main Modules

**Hand Detection Module (MediaPipe):** Detects a hand in each webcam frame and returns 21 key points (fingertips, knuckles, wrist).

**Landmark Extraction Module (`utils.py`):** Converts MediaPipe's output into a flat list of 63 numbers (x, y, z for each of the 21 points).

**Normalization Module (`utils.py`):** Shifts landmarks relative to the wrist and scales them, so the prediction works regardless of hand position or distance from the camera.

**Data Collection Module (`collect_data.py`):** Lets the developer record labeled samples (landmarks + letter) to build the training dataset.

**Training Module (`train_model.py`):** Trains and compares two classifiers (SVM and a small Neural Network), evaluates accuracy, and saves the better one along with a confusion matrix.

**Recognition Module (`recognize.py`):** Loads the trained model and runs real-time inference on the webcam feed for the live demo.

## Input
- Live webcam video feed.
- (During training only) Labeled hand landmark samples collected by the developer.

## Output
- The predicted alphabet letter, displayed on screen in real time.
- A trained model file (`sign_model.pkl`) and a confusion matrix image for the report.
