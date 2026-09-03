"""
collect_data.py
Capture webcam frames, extract hand landmarks with MediaPipe, and save
labeled samples to data/landmarks.csv for training the sign language classifier.

Usage:
    python src/collect_data.py --label A

Controls:
    Press 'c' to capture a sample for the current label.
    Press 'q' to quit and move on to the next letter.

Tip: Record at least 40-60 samples per letter, varying hand angle and
distance slightly, for a more robust classifier.
"""
import argparse
import csv
import os
import cv2
from utils import get_hand_landmarks, normalize_landmarks, mp_hands, mp_drawing

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "landmarks.csv")


def main(label):
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    file_exists = os.path.isfile(DATA_PATH)

    cap = cv2.VideoCapture(0)
    hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

    with open(DATA_PATH, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            header = [f"c{i}" for i in range(63)] + ["label"]
            writer.writerow(header)

        print(f"Collecting samples for label '{label}'. Press 'c' to capture, 'q' to quit.")
        count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            cv2.putText(frame, f"Label: {label}  Samples: {count}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            cv2.putText(frame, "Press 'c' to capture, 'q' to quit", (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
            cv2.imshow("Collect Data", frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('c'):
                landmarks = get_hand_landmarks(results)
                if landmarks:
                    normalized = normalize_landmarks(landmarks)
                    writer.writerow(normalized + [label])
                    count += 1
                    print(f"Captured sample {count} for label {label}")
                else:
                    print("No hand detected, try again.")
            elif key == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--label", required=True, help="Letter label for this session, e.g. A")
    args = parser.parse_args()
    main(args.label.upper())
