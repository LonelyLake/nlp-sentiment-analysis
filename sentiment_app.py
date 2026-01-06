import csv
from datetime import datetime
from textblob import TextBlob

def save_to_history(text, mood, polarity):
    # Check if file exists to add header only once
    file_exists = False
    try:
        with open('mood_history.csv', 'r') as f:
            file_exists = True
    except FileNotFoundError:
        file_exists = False

    with open('mood_history.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Timestamp', 'Text', 'Mood', 'Polarity']) # Header
        
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), text, mood, round(polarity, 2)])

def analyze_mood(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0.5: mood = "Very Positive"
    elif polarity > 0: mood = "Positive"
    elif polarity == 0: mood = "Neutral"
    elif polarity > -0.5: mood = "Negative"
    else: mood = "Very Negative"
    
    return mood, polarity

# --- Main Program ---
print("--- Mood Tracker ---")
user_text = input("What's on your mind? ")
mood, score = analyze_mood(user_text)

print(f"Result: {mood} ({score})")

# Saving to "Database" (CSV)
save_to_history(user_text, mood, score)
print("Data saved to mood_history.csv")