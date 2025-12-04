import requests
import pandas as pd
import logging
import re

logging.basicConfig(
    filename="api_fetcher.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def clean_text(text):
    """General text cleaner."""
    if not text:
        return None
    return re.sub(r"\s+", " ", str(text)).strip()


def fetch_api_data():
    """Fetch JSON data from the API with error handling."""
    try:
        response = requests.get(API_URL, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logging.error(f"API fetch error: {e}")
        return None


def prepare_dataframe(json_data):
    """Convert API JSON into a DataFrame."""
    if not json_data:
        return pd.DataFrame()

    try:
        base_currency = json_data.get("base")
        date = json_data.get("date")
        rates = json_data.get("rates", {})

        rows = []
        for currency, value in rates.items():
            rows.append({
                "Base Currency": base_currency,
                "Target Currency": currency,
                "Rate": value,
                "Date": date
            })

        df = pd.DataFrame(rows)
        return df

    except Exception as e:
        logging.error(f"Data preparation error: {e}")
        return pd.DataFrame()
