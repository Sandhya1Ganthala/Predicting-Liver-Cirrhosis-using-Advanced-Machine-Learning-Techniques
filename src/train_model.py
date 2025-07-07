from preprocess import clean_data
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib, os

df = clean_data("data/raw/liver_data.csv")
X = df.drop("Dataset", axis=1)
y = df["Dataset"]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/model.pkl")
print("✅ Model saved to models/model.pkl")

