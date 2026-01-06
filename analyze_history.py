import pandas as pd

# Load the "database"
df = pd.read_csv('mood_history.csv')

print("--- Your Mood Statistics ---")
print(f"Number of entries: {len(df)}")
print(f"Average polarity: {df['Polarity'].mean():.2f}")

# Let's check the most common mood
print("\nMood distribution:")
print(df['Mood'].value_counts())