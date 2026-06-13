import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(BASE_DIR, '..')))

try:
    from src.preprocess import clean_data
except ModuleNotFoundError:
    from preprocess import clean_data

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

DATA_PATH = os.path.abspath(os.path.join(BASE_DIR, '..', 'data', 'raw'))
MODEL_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'models'))
MODEL_PATH = os.path.join(MODEL_DIR, 'model.pkl')


def main():
    df = clean_data(DATA_PATH)
    X = df.drop("Dataset", axis=1)
    y = df["Dataset"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    os.makedirs(MODEL_DIR, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"✅ Model saved to {MODEL_PATH}")


if __name__ == "__main__":
    main()

