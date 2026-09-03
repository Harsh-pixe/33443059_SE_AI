# Problem Analysis

## Introduction
Sign language is a primary means of communication for many deaf and hard-of-hearing individuals. However, most people who can hear do not know sign language, which creates a communication barrier. This project explores whether a simple, real-time computer vision system can recognize hand signs and display the corresponding letter, using only a standard webcam and lightweight machine learning.

## Existing Problem
Learning to read sign language takes time and practice, and there is no lightweight, offline tool that gives instant feedback on whether a hand sign is being formed correctly. Many existing sign language recognition systems rely on large, GPU-heavy deep learning models, making them impractical to run on an everyday laptop.

## Proposed Solution
This project builds a real-time sign language alphabet recognizer using MediaPipe for hand landmark detection and a lightweight machine learning classifier (trained on self-collected data) to predict the letter being signed. The entire system runs on CPU, with no internet connection or GPU required.

## Objectives
- To detect a hand and extract landmark points from a live webcam feed.
- To collect a labeled dataset of hand landmarks for each letter of the alphabet.
- To train and evaluate a machine learning classifier on this dataset.
- To recognize signed letters in real time and display the prediction on screen.
- To keep the system lightweight enough to run smoothly without a GPU.

## Scope
The project covers static ASL alphabet letters (A-Y, excluding J and Z, which require hand motion rather than a static pose). It does not cover full sign language sentence translation, motion-based letters, or multi-hand gestures.

## Expected Outcome
A working real-time application where a user can show a hand sign to their webcam and see the predicted letter displayed instantly on screen, backed by a trained and evaluated machine learning model.
