"""
utils.py
Shared helper functions for hand landmark extraction and normalization,
used by collect_data.py, train_model.py, and recognize.py.
"""
import numpy as np
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils


def get_hand_landmarks(results):
    """Extract 21 (x, y, z) landmarks from a MediaPipe Hands result as a
    flat list of 63 floats. Returns None if no hand was detected."""
    if not results.multi_hand_landmarks:
        return None
    hand = results.multi_hand_landmarks[0]
    landmarks = []
    for lm in hand.landmark:
        landmarks.extend([lm.x, lm.y, lm.z])
    return landmarks


def normalize_landmarks(landmarks):
    """Normalize landmarks relative to the wrist point (landmark 0) and
    scale so the classifier is less sensitive to hand position/size on screen."""
    landmarks = np.array(landmarks).reshape(21, 3)
    wrist = landmarks[0].copy()
    landmarks = landmarks - wrist
    max_val = np.max(np.abs(landmarks))
    if max_val == 0:
        max_val = 1.0
    landmarks = landmarks / max_val
    return landmarks.flatten().tolist()
