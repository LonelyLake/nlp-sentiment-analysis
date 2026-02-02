# 🎭 NLP Sentiment Analysis API

ML-powered REST API for sentiment analysis, designed with a strong focus on clean architecture, reproducibility, and production-oriented ML engineering practices.

![CI Pipeline](https://github.com/LonelyLake/nlp-sentiment-analysis/actions/workflows/ci.yml/badge.svg)

## 📖 Description

This project demonstrates a production-ready machine learning system for sentiment analysis, showcasing best practices in MLOps, software engineering, and API design. The API analyzes text sentiment using a trained Multinomial Naive Bayes classifier on the IMDb movie reviews dataset from Hugging Face.

## ✨ Key Highlights

- **End-to-end ML pipeline**: Complete workflow from data ingestion → training → inference
- **FastAPI-based REST service**: Typed request/response models with automatic API documentation
- **Containerized deployment**: Docker and docker-compose for consistent environments
- **Automated CI pipeline**: Includes model training and API testing via GitHub Actions
- **Clear separation of concerns**: Distinct modules for training, inference, and data ingestion logic
- **Production-oriented design**: Health checks, error handling, and model artifact management

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

### Using pip

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

### Using uv (Alternative)

```bash
# 1. Install dependencies
uv add scikit-learn pandas datasets joblib fastapi uvicorn pydantic

# 2. Download data and train model
uv run python scripts/ingest_data.py
uv run python train_model.py

# 3. Run API
uv run uvicorn app:app --reload

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

### Example Request

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"text": "This movie was absolutely fantastic!"}'
```

### Example Response

```json
{
  "text": "This movie was absolutely fantastic!",
  "sentiment_label": "Positive",
  "confidence_score": 0.89
}
```

## 🎯 What This Project Demonstrates

This project showcases several important concepts in modern ML engineering:

1. **Applying software engineering principles to ML systems**: Clean code, modular design, type safety, and separation of concerns
2. **Building reproducible ML pipelines**: Consistent data ingestion, deterministic training, and versioned artifacts
3. **Serving ML models via production-oriented APIs**: RESTful design, input validation, error handling, and health monitoring
4. **Understanding the gap between experimentation and deployment**: Bridging research code and production-ready systems
5. **MLOps fundamentals**: CI/CD for ML, containerization, automated testing, and pipeline orchestration

## 🚀 Planned Improvements

Future enhancements to make this project even more production-ready:

- **Model versioning**: Integration with MLflow or DVC for experiment tracking and model registry
- **Advanced NLP models**: 
  - TF-IDF vectorization for better feature representation
  - Transformer-based models (BERT, DistilBERT) for state-of-the-art performance
- **Monitoring and observability**:
  - Inference logging and metrics collection
  - Model performance monitoring and drift detection
  - API latency and throughput tracking
- **Advanced features**:
  - Batch prediction endpoints
  - A/B testing infrastructure
  - Model explainability (LIME, SHAP)

## 🛠️ Tech Stack

### ML & Data Science
- **Scikit-learn**: Multinomial Naive Bayes classifier with CountVectorizer
- **Hugging Face Datasets**: Data ingestion from IMDb movie reviews
- **Pandas**: Data manipulation and preprocessing
- **joblib**: Model serialization and persistence

### Backend & API
- **FastAPI**: Modern web framework with automatic OpenAPI documentation
- **Uvicorn**: ASGI server for production-ready API serving
- **Pydantic**: Data validation and settings management with type hints

### MLOps Foundations
- **Docker**: Containerization for consistent deployment environments
- **GitHub Actions**: Automated CI pipeline with training and testing
- **pytest**: Unit and integration testing framework
- **httpx**: Testing HTTP endpoints
