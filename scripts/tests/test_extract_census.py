import pandas as pd
import pytest
import yaml
from pathlib import Path
from scripts.extract_census import fetch_census_data

# Load config
CONFIG_PATH = Path(__file__).parents[2] / "configs" / "series_config.yml"
with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

census_vars = config["census"]["variables"]
census_metros = config["census"]["metros"]

def get_latest_year(var_code, geo_id):
    """Fetch the most recent year available for a given Census var + metro."""
    START_YEAR = 2000
    END_YEAR = pd.Timestamp.today().year
    for year in range(END_YEAR, START_YEAR, -1):
        try:
            df = fetch_census_data(year, var_code, geo_id)
            if not df.empty:
                return year
        except Exception:
            continue
    raise ValueError(f"No data found for {var_code}, {geo_id}")

@pytest.mark.smoke
def test_census_smoke():
    """Quick smoke test for CI with just 1 metro + 1 variable."""
    metro_name, geo_id = next(iter(census_metros.items()))
    var_name, var_code = next(iter(census_vars.items()))
    latest_year = get_latest_year(var_code, geo_id)
    
    df = fetch_census_data(latest_year, var_code, geo_id)
    
    assert isinstance(df, pd.DataFrame)
    assert not df.empty, f"No data for {var_name} in {metro_name} ({geo_id}) at {latest_year}"
    assert {"year", "geo_id"}.issubset(df.columns)

@pytest.mark.parametrize("metro_name,geo_id", census_metros.items())
@pytest.mark.parametrize("var_name,var_code", census_vars.items())
def test_census_full(metro_name, geo_id, var_name, var_code):
    """Full validation: all metros + all variables (slower)."""
    latest_year = get_latest_year(var_code, geo_id)
    
    df = fetch_census_data(latest_year, var_code, geo_id)
    
    assert isinstance(df, pd.DataFrame)
    assert not df.empty, f"No data for {var_name} in {metro_name} ({geo_id}) at {latest_year}"
    assert {"year", "geo_id"}.issubset(df.columns)
