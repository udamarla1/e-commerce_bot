from pathlib import Path

import pandas as pd


DATA_FILE = Path(__file__).parents[1] / "src" / "prod_small2.csv"
REQUIRED_COLUMNS = {"TITLE", "DESCRIPTION"}


def test_product_catalog_exists():
    assert DATA_FILE.is_file()


def test_product_catalog_has_required_columns_and_rows():
    catalog = pd.read_csv(DATA_FILE)

    assert REQUIRED_COLUMNS.issubset(catalog.columns)
    assert not catalog.empty
    assert catalog["TITLE"].notna().any()
    assert catalog["DESCRIPTION"].notna().any()
