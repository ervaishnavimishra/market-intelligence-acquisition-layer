import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("TWELVE_DATA_API_KEY")

url = "https://api.twelvedata.com/time_series"

params = {
    "symbol": "XAU/USD",
    "interval": "1h",
    "outputsize": 1000,
    "apikey": API_KEY
}

response = requests.get(url, params=params)

data = response.json()

values = data["values"]

market_data = []

for item in values:

    market_data.append({
        "Datetime": item["datetime"],
        "Open": item["open"],
        "High": item["high"],
        "Low": item["low"],
        "Close": item["close"],
        "Volume": item.get("volume", "N/A")
    })

df = pd.DataFrame(market_data)

df = df.iloc[::-1]

os.makedirs("data/raw", exist_ok=True)

df.to_csv("data/raw/market_data.csv", index=False)

print(df.head())

print("Market data saved successfully.")