FROM python:3.13-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m textblob.download_corpora

# Copy all project files
COPY . .

# FastAPI runs on port 8000 by default
EXPOSE 8000

# Run uvicorn inside the container
# 0.0.0.0 makes the server reachable outside the container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]