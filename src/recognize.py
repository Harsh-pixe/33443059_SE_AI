"""
recognize.py
Real-time sign language alphabet recognition using the trained model.
This is the script you run for the live demo.

Usage:
    python src/recognize.py
Press 'q' to quit.
"""
import os
import cv2
import joblib
from utils import get_hand_landmarks, normalize_landmarks, mp_hands, mp_drawing

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "sign_model.pkl")


def main():
    model = joblib.load(MODEL_PATH)
    cap = cv2.VideoCapture(0)
    hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        prediction = "-"
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmarks = get_hand_landmarks(results)
            if landmarks:
                normalized = normalize_landmarks(landmarks)
                prediction = model.predict([normalized])[0]

        cv2.putText(frame, f"Prediction: {prediction}", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
        cv2.imshow("Sign Language Recognition", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
