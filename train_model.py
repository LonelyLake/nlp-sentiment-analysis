import pandas as pd
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
import os

def train():
    print("⏳ Loading data...")
    # Load the data we ingested earlier
    try:
        df = pd.read_csv(os.path.join("data", "raw", "dataset.csv"))
    except FileNotFoundError:
        print("❌ Data not found! Run 'python scripts/ingest_data.py' first.")
        return

    # Prepare features (X) and labels (y)
    # IMDB dataset usually has 'text' and 'label' columns
    X = df['text']
    y = df['label'] # 0 is Negative, 1 is Positive

    # Split data: 80% for training, 20% for validation (Standard ML Practice)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("🧠 Vectorizing text...")
    vectorizer = CountVectorizer(stop_words='english')
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    print("🏋️ Training model...")
    model = MultinomialNB()
    model.fit(X_train_vec, y_train)

    # Validate
    y_pred = model.predict(X_test_vec)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"✅ Model Accuracy: {accuracy:.4f}")
    print(classification_report(y_test, y_pred))

    # Save artifacts to the 'models' directory
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, os.path.join("models", "mood_model.pkl"))
    joblib.dump(vectorizer, os.path.join("models", "vectorizer.pkl"))
    print("💾 Model and vectorizer saved to 'models/' directory.")

if __name__ == "__main__":
    train()