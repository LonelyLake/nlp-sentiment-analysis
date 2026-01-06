from textblob import TextBlob

# Let's test some sentences
sentences = [
    "I love studying ML at Polsl, it is absolutely amazing!",
    "The weather in Gliwice is quite gray and depressing today.",
    "This is a neutral sentence about a computer."
]

for text in sentences:
    blob = TextBlob(text)
    sentiment = blob.sentiment
    print(f"Text: {text}")
    print(f"Polarity: {sentiment.polarity:.2f}, Subjectivity: {sentiment.subjectivity:.2f}")
    print("-" * 30)