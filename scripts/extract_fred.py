import os
import requests
import pandas as pd
import yaml
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API configuration
FRED_API_KEY = os.environ["FRED_API_KEY"]
FRED_API_URL = os.environ["FRED_API_URL"]

# Set collection start date for historical data
START_DATE = "1995-01-01"

# Load metropolitan area configuration with FRED series IDs
with open("../configs/series_config.yml", "r") as f:
    config = yaml.safe_load(f)

metros = config["fred"]["metros"]
rates = config["fred"]["rates"]

# Fetch raw FRED series given a series_id
def fetch_fred_series(series_id: str) -> pd.DataFrame:
    params = {
        "series_id": series_id,
        "api_key": FRED_API_KEY,
        "file_type": "json",
        "observation_start": START_DATE,
    }
    
    response = requests.get(FRED_API_URL, params=params)
    response.raise_for_status()
    data = response.json()

    if "observations" not in data or not data["observations"]:
        return pd.DataFrame()

    # Convert API response to DataFrame
    df = pd.DataFrame(data["observations"])
    df["value"] = pd.to_numeric(df["value"], errors="coerce")

    # Standardized bronze schema
    df = df[["date", "value"]].copy()
    df["series_id"] = series_id

    return df[["date", "series_id", "value"]]

# Extract raw FRED series for all metros, keep geo_id + series_id only.
def extract_fred_metros() -> pd.DataFrame:
    total_data = []
    for metro, series_dict in metros.items():
        for _, series_id in series_dict.items():
            df = fetch_fred_series(series_id)
            if not df.empty:
                df["geo_id"] = metro
                total_data.append(df)
    if total_data:
        return pd.concat(total_data, ignore_index=True)
    else:
        return pd.DataFrame(columns=["date", "series_id", "geo_id", "value"])

# Extract raw FRED rate series, keep rate_type + series_id only.
def extract_fred_rates() -> pd.DataFrame:
    total_data = []
    for rate_name, series_id in rates.items():
        df = fetch_fred_series(series_id)
        if not df.empty:
            df["rate_type"] = rate_name
            total_data.append(df)
    if total_data:
        return pd.concat(total_data, ignore_index=True)
    else:
        return pd.DataFrame(columns=["date", "series_id", "rate_type", "value"])

# Collect metros and rates df to be stored in BigQuery "raw"
metros_df = extract_fred_metros()
rates_df = extract_fred_rates()