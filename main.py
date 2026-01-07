from fastapi import FastAPI
from textblob import TextBlob
import csv
from datetime import datetime

app = FastAPI()

# This is our "Home" endpoint
@app.get("/")
def home():
    return {"message": "Mood Tracker API is Online!"}

# This is where the magic happens
@app.get("/analyze")
def analyze_mood(text: str):
    analysis = TextBlob(text)
    sentiment = "Positive" if analysis.sentiment.polarity > 0 else "Negative" if analysis.sentiment.polarity < 0 else "Neutral"
    
    # Log to CSV (keeping your data persistence logic)
    with open('mood_history.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), text, sentiment])
        
    return {
        "text": text,
        "sentiment": sentiment,
        "score": analysis.sentiment.polarity
    }