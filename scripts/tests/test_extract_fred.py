import pandas as pd
import pytest
import yaml
from pathlib import Path
from scripts.extract_fred import fetch_fred_data

# Load config
CONFIG_PATH = Path(__file__).parents[2] / "configs" / "series_config.yml"
with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

fred_metros = config["fred"]["metros"]
fred_rates = config["fred"]["rates"]

@pytest.mark.parametrize("series_id", [m["housing"] for m in fred_metros.values()])
def test_fetch_fred_metro_housing(series_id):
    """Each metro housing series should return a non-empty DataFrame with expected cols."""
    df = fetch_fred_data(series_id)
    
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert {"date", "value"}.issubset(df.columns)

@pytest.mark.parametrize("series_id", fred_rates.values())
def test_fetch_fred_rates(series_id):
    """Each macro rate series should return a non-empty DataFrame with expected cols."""
    df = fetch_fred_data(series_id)
    
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert {"date", "value"}.issubset(df.columns)
