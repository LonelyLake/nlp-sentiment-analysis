import os
import pandas as pd
from datasets import load_dataset


def ingest_data():
    print("🔄 Downloading IMDB dataset from Hugging Face...")
    # Load only 2000 examples to keep things fast for development
    dataset = load_dataset("imdb", split="train[:2000]")
    
    print("✅ Data downloaded. Converting to CSV...")
    df = pd.DataFrame(dataset)
    
    # Ensure the directory exists
    output_path = os.path.join("data", "raw")
    os.makedirs(output_path, exist_ok=True)
    
    # Save file
    file_path = os.path.join(output_path, "dataset.csv")
    df.to_csv(file_path, index=False)
    print(f"📂 Data saved to: {file_path}")
    print(df.head())

if __name__ == "__main__":
    ingest_data()
    