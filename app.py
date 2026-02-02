from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os


# Define the input schema
class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    text: str
    sentiment_label: str
    confidence_score: float

app = FastAPI(title="Sentiment Analysis API", version="1.0.0")

# Load model artifacts at startup
MODEL_PATH = os.path.join("models", "mood_model.pkl")
VECTORIZER_PATH = os.path.join("models", "vectorizer.pkl")

if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
    raise RuntimeError("Model files not found! Run train_model.py first.")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

# Map numeric labels back to strings
LABEL_MAP = {0: "Negative", 1: "Positive"}

@app.post("/predict", response_model=SentimentResponse)
def predict_sentiment(request: SentimentRequest):
    vec_text = vectorizer.transform([request.text])
    
    prediction = model.predict(vec_text)[0]
    prob = model.predict_proba(vec_text).max()
    
    return SentimentResponse(
        text=request.text,
        sentiment_label=LABEL_MAP.get(prediction, "Unknown"),
        confidence_score=round(float(prob), 4)
    )

@app.get("/health")
def health_check():
    return {"status": "ok", "model_loaded": True}
