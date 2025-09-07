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

def fetch_fred_series(series_id: str) -> pd.DataFrame:
    params = {
        "series_id": series_id,
        "api_key": FRED_API_KEY,
        "file_type": "json",
        "observation_start": START_DATE
    }
    
    response = requests.get(FRED_API_URL, params=params)
    response.raise_for_status()
    data = response.json()

    # Convert API response to DataFrame
    df = pd.DataFrame(data["observations"])
    
    # Keep only relevant columns
    df = df[["date", "value"]].copy()
    
    # Convert to numeric, invalid values become NaN
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    return df

def extract_indicator(indicator: str) -> pd.DataFrame:
    total_data = []
    
    for metro, series_dict in metros.items():
        series_id = series_dict.get(indicator)
        
        # Fetch data from FRED API
        df = fetch_fred_series(series_id)
        
        # Add metro identifier and rename value column
        df["geo_id"] = metro
        df.rename(columns={"value": indicator}, inplace=True)
        total_data.append(df)
        
    # Combine all metro data into a single DataFrame    
    result = pd.concat(total_data, ignore_index=True)       
    return result

def extract_rates() -> pd.DataFrame:
    total_data = []
    
    for rate_name, series_id in rates.items():
        
        # Fetch data from FRED API
        df = fetch_fred_series(series_id)
        
        # Add rate type identifier and rename value column
        df["rate_type"] = rate_name
        df.rename(columns={"value": "rate"}, inplace=True)
        total_data.append(df)
    
    # Combine all rate data into a single DataFrame    
    result = pd.concat(total_data, ignore_index=True)       
    return result

# Each DataFrame contains time series data with date, indicator value, and geo_id (for metros) or rate_type (for rates)
housing_df = extract_indicator("housing")
cpi_df = extract_indicator("cpi")
unemployment_df = extract_indicator("unemployment")
rates_df = extract_rates()