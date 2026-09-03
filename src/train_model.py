"""
train_model.py
Train two candidate classifiers (SVM and a small Neural Network) on the
collected hand landmark data, evaluate both, keep the best one, and save
a confusion matrix image for the report.

Usage:
    python src/train_model.py
"""
import os
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "landmarks.csv")
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "sign_model.pkl")
REPORT_PATH = os.path.join(os.path.dirname(__file__), "..", "docs", "confusion_matrix.png")


def main():
    df = pd.read_csv(DATA_PATH)
    X = df.drop("label", axis=1).values
    y = df["label"].values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    candidates = {
        "SVM (RBF kernel)": SVC(kernel="rbf", probability=True),
        "MLP (Neural Network)": MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=1000, random_state=42),
    }

    best_model, best_name, best_acc = None, None, 0.0
    for name, model in candidates.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)
        print(f"\n{name} accuracy: {acc:.3f}")
        print(classification_report(y_test, preds, zero_division=0))
        if acc > best_acc:
            best_model, best_name, best_acc = model, name, acc

    print(f"\nBest model: {best_name} with accuracy {best_acc:.3f}")

    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(best_model, MODEL_PATH)
    print(f"Saved best model to {MODEL_PATH}")

    # Confusion matrix for the best model (useful evidence for the report)
    preds = best_model.predict(X_test)
    labels = sorted(df["label"].unique())
    cm = confusion_matrix(y_test, preds, labels=labels)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
    fig, ax = plt.subplots(figsize=(8, 8))
    disp.plot(ax=ax, cmap="Blues", colorbar=False)
    plt.title(f"Confusion Matrix - {best_name}")
    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    plt.savefig(REPORT_PATH, bbox_inches="tight")
    print(f"Saved confusion matrix to {REPORT_PATH}")


if __name__ == "__main__":
    main()
