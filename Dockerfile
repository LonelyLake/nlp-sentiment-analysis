# Step 1: Use a lightweight Python image
FROM python:3.13-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy your requirements first (for better caching)
COPY requirements.txt .

# Step 4: Install the libraries
RUN pip install --no-cache-dir -r requirements.txt
# TextBlob needs a specific data download
RUN python -m textblob.download_corpora

# Step 5: Copy your Python script and the CSV history
COPY sentiment_app.py .
COPY mood_history.csv .

# Step 6: Tell Docker how to run your script
# We use -u to see the output in real-time
CMD ["python", "-u", "sentiment_app.py"]