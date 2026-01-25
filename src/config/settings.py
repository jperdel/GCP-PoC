# DATASET SETTINGS
DATASETS = {
    "penguins": {
        "raw": "datasets/penguins/raw/data.parquet",
        "interim": "datasets/penguins/interim/data.parquet",
        "procesed": "datasets/penguins/procesed/data.parquet",
        "features": "datasets/penguins/features/data.parquet"
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

# MODEL SETTINGS
TARGET = "sex"
FEATURES = ['species', 'island', 'culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g']