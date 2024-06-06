from __future__ import annotations

import pathlib

import pandas as pd

DATASETS_DIR = pathlib.Path(__file__).parent / "datasets"


def load_product_footprints():
    return pd.read_csv(DATASETS_DIR / "product_footprints.csv.gz")
