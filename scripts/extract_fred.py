import os
import requests
import pandas as pd
import yaml
from google.cloud import bigquery
import functions_framework

# Get the config path
config_path = os.environ.get("CONFIG_PATH", "configs/series_config.yml")

# FRED API configuration
FRED_API_KEY = os.environ["FRED_API_KEY"]
FRED_API_URL = os.environ["FRED_API_URL"]

# Set collection start date for historical data
START_DATE = "1995-01-01"

# Load metropolitan area configuration with FRED series IDs
with open(config_path, "r") as f:
    config = yaml.safe_load(f)

metros = config["fred"]["metros"]
rates = config["fred"]["rates"]

# Fetch raw FRED series given a series_id
def fetch_fred_data(series_id: str) -> pd.DataFrame:
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
            df = fetch_fred_data(series_id)
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
        df = fetch_fred_data(series_id)
        if not df.empty:
            df["rate_type"] = rate_name
            total_data.append(df)
    if total_data:
        return pd.concat(total_data, ignore_index=True)
    else:
        return pd.DataFrame(columns=["date", "series_id", "rate_type", "value"])

# Define BigQuery dataset and table names
project_id = os.environ["GCP_PROJECT"]
dataset_id = os.environ["BIGQUERY_DATASET_BRONZE"]

# Create cloud function for scheduled raw data extraction
@functions_framework.http
def main(request):
    # Initialize BigQuery connection client
    client = bigquery.Client(project=project_id)

    # Collect metros df and construct table id path
    metros_df = extract_fred_metros()
    metros_table_id = f"{project_id}.{dataset_id}.fred_metros"

    # Collect rates df and construct table id path
    rates_df = extract_fred_rates()
    rates_table_id = f"{project_id}.{dataset_id}.fred_rates"

    # Load metros dataframe
    job_config = bigquery.LoadJobConfig(
        write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE,
        schema = [
            bigquery.SchemaField("date", "DATE"),
            bigquery.SchemaField("series_id", "STRING"),
            bigquery.SchemaField("geo_id", "STRING"),
            bigquery.SchemaField("value", "FLOAT")
        ]    
    )
    metros_df["date"] = pd.to_datetime(metros_df["date"], errors="coerce").dt.date
    job = client.load_table_from_dataframe(metros_df, metros_table_id, job_config=job_config)
    job.result()

    # Load rates dataframe
    job_config = bigquery.LoadJobConfig(
        write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE,
        schema = [
            bigquery.SchemaField("date", "DATE"),
            bigquery.SchemaField("series_id", "STRING"),
            bigquery.SchemaField("rate_type", "STRING"),
            bigquery.SchemaField("value", "FLOAT")
        ]
    )
    rates_df["date"] = pd.to_datetime(rates_df["date"], errors="coerce").dt.date
    job = client.load_table_from_dataframe(rates_df, rates_table_id)
    job.result()