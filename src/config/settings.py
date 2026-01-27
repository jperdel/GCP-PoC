# DATASET SETTINGS
DATASETS = {
    "penguins": {
        "raw": "datasets/penguins/raw/data.parquet",
        # "interim": "datasets/penguins/interim/data.parquet",
        "processed": "datasets/penguins/processed/data.parquet",
        "features": "datasets/penguins/features/data.parquet"
    }
}

METADATA = {
    "penguins": {
        "raw": "datasets/penguins/raw/metadata.json",
        # "interim": "datasets/penguins/interim/metadata.json",
        "processed": "datasets/penguins/processed/metadata.json",
        "features": "datasets/penguins/features/metadata.json"
    }
}

PENGUINS_SOURCE = "bigquery-public-data.ml_datasets.penguins"

PENGUINS_QUERY = """
SELECT *
FROM `bigquery-public-data.ml_datasets.penguins`
"""

# SPLIT AND  VALIDATION SETTINGS
TEST_SIZE = 0.2
K_FOLDS = 5
SK_SEED = 42

# MODEL SETTINGS
TARGET = "sex"
FEATURES = ['species', 'island', 'culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g']