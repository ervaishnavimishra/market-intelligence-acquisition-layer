from transformers import pipeline
import pandas as pd
import os

print("Loading FinBERT model...")

classifier = pipeline(
    "text-classification",
    model="ProsusAI/finbert"
)

# Read cleaned news text
with open("data/processed/clean_news.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Split into news chunks
news_items = text.split("title")

results = []

for item in news_items:

    item = item.strip()

    if len(item) < 20:
        continue

    # FinBERT max input length handling
    result = classifier(item[:512])[0]

    results.append({
        "text": item[:200],  # preview
        "sentiment": result["label"],
        "score": result["score"]
    })

# Convert to DataFrame
df = pd.DataFrame(results)

# Create output folder if needed
os.makedirs("data/output", exist_ok=True)

# Save sentiment results
df.to_csv(
    "data/output/news_with_sentiment.csv",
    index=False
)

print(df.head())

print("\nSentiment analysis completed!")