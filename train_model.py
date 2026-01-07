from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# 1. Training Data (In a real project, this would be thousands of rows)
data = [
    ("I love this project", "Positive"),
    ("This is amazing", "Positive"),
    ("Docker is great", "Positive"),
    ("I hate bugs", "Negative"),
    ("This is terrible", "Negative"),
    ("I am feeling sad", "Negative")
]

texts, labels = zip(*data)

# 2. Vectorization: Converting words to numbers (Features)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# 3. Training the Naive Bayes Model
model = MultinomialNB()
model.fit(X, labels)

# 4. Save the "Brain" to files
joblib.dump(model, 'mood_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("Model trained and saved!")