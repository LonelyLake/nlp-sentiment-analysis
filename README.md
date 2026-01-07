# 🚀 Professional NLP Mood Tracker

A containerized sentiment analysis microservice that transitions from rule-based NLP to a probabilistic **Naive Bayes** model.

## 🏗️ Architecture & Features

* **API First:** Powered by **FastAPI**, featuring an interactive **Swagger UI** for testing.
* **Custom ML Model:** Replaced `TextBlob` with a custom-trained **Multinomial Naive Bayes** classifier.
* **MLOps Foundation:** - **Containerization:** Fully Dockerized with optimized `python:3.13-slim` image.
* **Orchestration:** Managed via **Docker Compose** for seamless environment setup.
* **Data Persistence:** Uses **Docker Volumes** to sync sentiment logs (`mood_history.csv`) between the container and the host machine.


* **Resource Optimized:** Configured for high performance even on 8GB RAM systems.

## 📐 Mathematical Perspective

The core of this project is the transition from **Rule-based analysis** to **Statistical Probability**.
The model utilizes **Bayes' Theorem**:



This allows the system to learn from data patterns rather than fixed dictionaries.

## 🛠️ Tech Stack

* **Backend:** Python 3.13, FastAPI, Uvicorn
* **Machine Learning:** Scikit-Learn (Naive Bayes), Joblib (Serialization)
* **DevOps:** Docker, Docker Compose
* **Environment:** Miniconda (ds env), WSL2

## 🚀 How to Run

1. **Clone & Navigate:**
```bash
git clone https://github.com/LonelyLake/NLP-Sentiment-Tracker.git
cd NLP-Sentiment-Tracker

```


2. **Train the Model (Optional):**
```bash
python train_model.py

```


3. **Launch the Microservice:**
```bash
docker-compose up -d

```


4. **Access the API:** Open `http://localhost:8000/docs` to use the Swagger UI.
