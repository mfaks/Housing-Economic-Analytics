import os
import requests
import pandas as pd
import yaml
from google.cloud import bigquery
import functions_framework

# Get the config path
config_path = os.environ.get("CONFIG_PATH", "configs/series_config.yml")

# API Configuration
CENSUS_API_KEY = os.environ["CENSUS_API_KEY"]
CENSUS_API_URL = os.environ["CENSUS_API_URL"]
CENSUS_API_DATASET = os.environ["CENSUS_API_DATASET"]

# Set collection start year and end year
START_YEAR = 2005
END_YEAR = 2023

# Load metros and variables from config
with open(config_path, "r") as f:
    config = yaml.safe_load(f)

metros = config["census"]["metros"]
variables = config["census"]["variables"]

# Fetch raw Census data for a given year, variable, and metro geo_id
def fetch_census_data(year: int, variable: str, geo_id: str) -> pd.DataFrame:
    url = f"{CENSUS_API_URL}/{year}/{CENSUS_API_DATASET}"
    params = {
        "get": f"NAME,{variable}",
        "for": f"metropolitan statistical area/micropolitan statistical area:{geo_id}",
        "key": CENSUS_API_KEY,
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code == 204 or not response.text.strip():
            return pd.DataFrame()
        data = response.json()
    except Exception:
        return pd.DataFrame()

    df = pd.DataFrame(data[1:], columns=data[0])
    df["year"] = year
    df["geo_id"] = geo_id
    df["var_code"] = variable
    df["value"] = pd.to_numeric(df[variable], errors="coerce")

    return df[["year", "geo_id", "var_code", "NAME", "value"]]

# Loop through all metros and variables, return combined raw dataset
def extract_census_variables() -> pd.DataFrame:
    total_data = []
    for year in range(START_YEAR, END_YEAR + 1):
        for metro, geo_id in metros.items():
            for _, var_code in variables.items():
                df = fetch_census_data(year, var_code, geo_id)
                if not df.empty:
                    total_data.append(df)
    if total_data:
        return pd.concat(total_data, ignore_index=True)
    else:
        return pd.DataFrame(columns=["year", "geo_id", "var_code", "NAME", "value"])

# Define BigQuery dataset and table names
project_id = os.environ["GCP_PROJECT"]
dataset_id = os.environ["BIGQUERY_DATASET_BRONZE"]

# Create cloud function for scheduled raw data extraction
@functions_framework.http
def main(request):
    # Initialize BigQuery connection client
    client = bigquery.Client(project=project_id)

    # Collect census df
    census_df = extract_census_variables()
    census_table_id = f"{project_id}.{dataset_id}.census"

    # Load census dataframe
    job_config = bigquery.LoadJobConfig(
        write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE,
        schema = [
            bigquery.SchemaField("year", "INTEGER"),
            bigquery.SchemaField("geo_id", "STRING"),
            bigquery.SchemaField("var_code", "STRING"),
            bigquery.SchemaField("NAME", "STRING"),
            bigquery.SchemaField("value", "FLOAT"),
        ]
    )
    job = client.load_table_from_dataframe(census_df, census_table_id, job_config=job_config)
    job.result()