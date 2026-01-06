# NLP Mood Tracker 🔍

A lightweight Natural Language Processing (NLP) application that analyzes text sentiment and logs results for historical tracking.

## 🎯 Purpose
To demonstrate basic NLP concepts and **Data Persistence** (MLOps foundation). This project maps human emotions to mathematical values (Polarity).

## 🛠️ Features
- **Sentiment Analysis:** Uses `TextBlob` to calculate polarity (-1 to 1).
- **Negation Handling:** Correctively interprets phrases like "not bad".
- **Data Logging:** Automatically saves every entry to `mood_history.csv` with a timestamp.

## 📈 Tech Stack
- **Python 3.13**
- **TextBlob** (NLP Library)
- **Pandas** (for history analysis)
- **CSV Module** (Persistence)
