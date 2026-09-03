# Dataset

## Type of Dataset
This project uses a self-collected dataset of hand landmark coordinates, not raw images. Each sample is a set of 21 (x, y, z) points describing one hand pose, labeled with the corresponding letter.

## Data Source
All data is recorded by the developer using `collect_data.py`, which captures the developer's own hand signing each letter of the alphabet in front of a webcam. Collecting original data (rather than only using a public dataset) supports the project's originality requirement.

## Supported Signs
Static letters of the ASL alphabet: A-Y, excluding J and Z, since those require hand motion rather than a single static pose.

## Data Preprocessing
For each captured frame, MediaPipe extracts 21 hand landmarks (63 numeric values). These are normalized relative to the wrist point and scaled, so that the hand's position and distance from the camera do not affect classification.

## Data Volume
Approximately 40-60 samples were collected per letter, varying hand angle and distance slightly during collection, to help the classifier generalize.

## Metadata
Each row in `landmarks.csv` stores the 63 normalized coordinate values plus the letter label, making the dataset simple, small (a few hundred KB), and fast to train on.

## Limitations
- The dataset reflects one person's hand shape and signing style; accuracy may be lower for other users without additional data collection.
- Only static letters are supported; motion-based letters (J, Z) and full words/sentences are out of scope.
- Performance may vary under poor lighting or unusual camera angles, since MediaPipe's hand detection can be less reliable in these conditions.
