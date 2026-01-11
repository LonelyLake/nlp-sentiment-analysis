# 🎭 Sentiment Analysis API

A production-ready ML microservice for sentiment analysis, built with MLOps best practices.

![CI Pipeline](https://github.com/LonelyLake/nlp-sentiment-analysis/actions/workflows/ci.yml/badge.svg)

## 🚀 Features

- **FastAPI** REST API with automatic Swagger docs
- **Scikit-learn** Naive Bayes classifier trained on IMDB reviews
- **Docker** containerization for easy deployment
- **Automated testing** with pytest
- **CI/CD pipeline** with GitHub Actions

## 📁 Project Structure

```
├── app.py              # FastAPI application
├── train_model.py      # Model training pipeline
├── scripts/
│   └── ingest_data.py  # Data ingestion from HuggingFace
├── tests/
│   └── test_app.py     # Unit tests
├── Dockerfile          # Container configuration
└── .github/workflows/  # CI/CD automation
```

## ⚡ Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Download data and train model
python scripts/ingest_data.py
python train_model.py

# 3. Run API
uvicorn app:app --reload

# 4. Open browser
# http://127.0.0.1:8000/docs
```

## 🐳 Docker

```bash
docker-compose up --build
```

## 🧪 Run Tests

```bash
pytest --verbose
```

## 📊 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| POST | `/predict` | Analyze sentiment of text |
| GET | `/health` | Health check |

## 🛠️ Tech Stack

- Python 3.11
- FastAPI
- Scikit-learn
- Docker
- GitHub Actions
- pytest
