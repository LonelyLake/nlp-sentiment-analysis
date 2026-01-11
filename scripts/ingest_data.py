import os
import pandas as pd
from datasets import load_dataset


def ingest_data():
    print("🔄 Downloading IMDB dataset from Hugging Face...")
    
    # LOAD, SHUFFLE, THEN SELECT
    # This ensures we get a mix of positive(1) and negative(0) reviews
    dataset = load_dataset("imdb", split="train").shuffle(seed=42).select(range(2000))
    
    print("✅ Data downloaded. Converting to CSV...")
    df = pd.DataFrame(dataset)
    
    # Ensure the directory exists
    output_path = os.path.join("data", "raw")
    os.makedirs(output_path, exist_ok=True)
    
    # Save file
    file_path = os.path.join(output_path, "dataset.csv")
    df.to_csv(file_path, index=False)
    print(f"📂 Data saved to: {file_path}")
    print(df['label'].value_counts()) # Print stats to verify balance

if __name__ == "__main__":
    ingest_data()
