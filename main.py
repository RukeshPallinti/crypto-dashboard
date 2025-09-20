import requests
import pandas as pd
from datetime import datetime

# CoinGecko API endpoint to fetch top 50 coins by market cap
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "inr",       # Prices in INR
    "order": "market_cap_desc",  # Sort by market cap
    "per_page": 50,             # Top 50 coins
    "page": 1,
    "sparkline": False
}

# Fetch data
response = requests.get(url, params=params)
data = response.json()

# Convert to DataFrame
df = pd.DataFrame(data)

# Select relevant columns
df = df[[
    "id", "symbol", "name", "current_price", "market_cap",
    "total_volume", "high_24h", "low_24h", "price_change_percentage_24h"
]]

# Add timestamp
df["last_updated"] = datetime.now()

# Save to CSV
df.to_csv("crypto_top50_inr.csv", index=False)

print("✅ Top 50 coin data saved to crypto_top50_inr.csv")
print(df)
