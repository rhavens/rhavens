import requests
import json
from datetime import datetime, timezone

COINS = ["bitcoin", "ethereum", "solana"]
API_URL = "https://api.coingecko.com/api/v3/simple/price"

def fetch_prices():
    params = {
        "ids": ",".join(COINS),
        "vs_currencies": "usd",
        "include_market_cap": "true",
        "include_24hr_vol": "true",
        "include_24hr_change": "true",
        "include_last_updated_at": "true"
    }
    response = requests.get(API_URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json()

def save_snapshot(data):
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
    filename = f"prices_{timestamp}.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Saved {filename}")
    return filename

if __name__ == "__main__":
    data = fetch_prices()
    save_snapshot(data)
