from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health_check():
    """Test if API is running."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_predict_positive():
    """Test positive sentiment detection."""
    payload = {"text": "I love this movie, it was amazing!"}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert response.json()["sentiment_label"] == "Positive"

def test_predict_negative():
    """Test negative sentiment detection."""
    payload = {"text": "This was terrible and boring."}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert response.json()["sentiment_label"] == "Negative"

def test_missing_field():
    """Test validation error for bad input."""
    response = client.post("/predict", json={})
    assert response.status_code == 422
