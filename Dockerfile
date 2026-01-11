FROM python:3.13-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose API port
EXPOSE 8000

# Run the NEW app.py file
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]