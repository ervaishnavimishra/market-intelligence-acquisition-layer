import re

# Read raw news
with open("data/raw/financial_news.txt", "r", encoding="utf-8") as file:
    text = file.read()

print("Before Cleaning:")
print(f"Characters: {len(text)}")

def clean_text(text):

    text = text.lower()

    text = re.sub(r'http\S+|www\S+', '', text)

    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

    text = " ".join(text.split())

    return text

cleaned_text = clean_text(text)

print("\nAfter Cleaning:")
print(f"Characters: {len(cleaned_text)}")

# Save cleaned text
with open("data/processed/clean_news.txt", "w", encoding="utf-8") as file:
    file.write(cleaned_text)

print("\nCleaned news saved successfully!")