from fredapi import Fred
from dotenv import load_dotenv
import pandas as pd
import os

# Load environment variables
load_dotenv()

# Get API key
FRED_API_KEY = os.getenv("FRED_API_KEY")

# Initialize FRED
fred = Fred(api_key=FRED_API_KEY)

# Fetch Federal Funds Rate data
data = fred.get_series("FEDFUNDS")

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Interest_Rate"])

# Reset index
df.reset_index(inplace=True)

# Rename columns
df.columns = ["Date", "Interest_Rate"]

# Save CSV
df.to_csv("data/raw/fred_interest_rates.csv", index=False)

# Preview data
print(df.head())

print("Economic data saved successfully.")