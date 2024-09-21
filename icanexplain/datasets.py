from __future__ import annotations

import pathlib

import pandas as pd

DATASETS_DIR = pathlib.Path(__file__).parent / "datasets"


def load_product_footprints():
    return pd.read_csv(DATASETS_DIR / "product_footprints.csv.gz")


def load_us_general_election_popular_vote():
    return pd.read_csv(DATASETS_DIR / "us_general_election_popular_vote.csv.zip")


def load_world_demography():
    return pd.read_csv(DATASETS_DIR / "world_demography.csv")


def load_iowa_whiskey_sales():
    """Iowa whiskey sales.

    This dataset contains the sales of whiskey in the state of Iowa, USA. The data comes from
    Iowa's Open Data Portal.

    For the sake of example, the data is limited to 2012, 2016, and 2020. The data is also limited
    to a sample of 50,000 sales records.

    References
    ----------
    [1] https://data.iowa.gov/Sales-Distribution/Iowa-Liquor-Sales/m3tr-qhgy/about_data

    """
    return pd.read_csv(DATASETS_DIR / "iowa_whiskey_sales.csv.zip")
