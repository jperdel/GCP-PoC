DATASETS = {
    "penguins": {
        "raw": "datasets/penguins/raw/data.parquet",
    }
}

METADATA = {
    "penguins": {
        "raw": "datasets/penguins/raw/metadata.json",
    }
}

PENGUINS_SOURCE = "bigquery-public-data.ml_datasets.penguins"

PENGUINS_QUERY = """
SELECT *
FROM `bigquery-public-data.ml_datasets.penguins`
"""