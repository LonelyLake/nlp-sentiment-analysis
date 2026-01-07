from fastapi import FastAPI
import joblib

app = FastAPI()

# Load our trained model
model = joblib.load('mood_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.get("/analyze")
def analyze_mood(text: str):
    # Transform input text to the same number format as training
    vectorized_text = vectorizer.transform([text])
    
    # Predict!
    prediction = model.predict(vectorized_text)[0]
    
    return {
        "text": text,
        "sentiment": prediction,
        "method": "Naive Bayes"
    }