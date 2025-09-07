import os
import requests
import pandas as pd
import yaml
from dotenv import load_dotenv

load_dotenv()

FRED_API_KEY = os.environ["FRED_API_KEY"]
FRED_API_URL = os.environ["FRED_API_URL"]
START_DATE = "1995-01-01"

with open("../configs/series_config.yml", "r") as f:
    config = yaml.safe_load(f)

metros = config["fred"]["metros"]

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

    df = pd.DataFrame(data["observations"])
    df = df[["date", "value"]].copy()
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    return df

def extract_indicator(indicator: str) -> pd.DataFrame:
    
    total_data = []
    for metro, series_dict in metros.items():
        series_id = series_dict.get(indicator)
        if not series_id:
            continue
        df = fetch_fred_series(series_id)
        df["geo_id"] = metro
        df.rename(columns={"value": indicator}, inplace=True)
        total_data.append(df)
        
        if not total_data:
            return pd.DataFrame()
        
    result = pd.concat(total_data, ignore_index=True)       
    return result

housing_df = extract_indicator("housing")
cpi_df = extract_indicator("cpi")
unemployment_df = extract_indicator("unemployment")