from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key
API_KEY = os.getenv("NEWS_API_KEY")

# Initialize NewsAPI
newsapi = NewsApiClient(api_key=API_KEY)

# Fetch financial news
articles = newsapi.get_everything(
    q="gold OR XAUUSD OR Federal Reserve OR inflation",
    language="en",
    sort_by="publishedAt",
    page_size=20
)

# Extract articles
news_data = articles["articles"]

# Save news to TXT
with open("data/raw/financial_news.txt", "w", encoding="utf-8") as file:

    for article in news_data:

        file.write(f"Title: {article['title']}\n")

        file.write(f"Source: {article['source']['name']}\n")

        file.write(f"Published At: {article['publishedAt']}\n")

        file.write(f"Description: {article['description']}\n")

        file.write("\n" + "=" * 80 + "\n\n")

print("Financial news saved successfully.")