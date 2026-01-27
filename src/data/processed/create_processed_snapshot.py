from utils.metadata import generate_metadata, save_metadata
from utils.gsc_io import upload_json_to_gcs
import pandas as pd
import tempfile
import os

def create_processed_metadata(
    df: pd.DataFrame,
    bucket_name: str,
    gcs_path: str,
    source: str,
    cleaning_steps: dict,
    train_idx: pd.Index,
    test_idx: pd.Index
):
    metadata = generate_metadata(
        df,
        extra_metadata={
            "stage": "processed",
            "source": source,
            "cleaning_steps": cleaning_steps,
            "train_size": len(train_idx),
            "test_size": len(test_idx),
            "train_idx": train_idx,
            "test_idx": test_idx,
            "format": "parquet",
            "compression": "snappy",
        },
    )

    with tempfile.TemporaryDirectory() as tmpdir:
        local_metadata_path = os.path.join(tmpdir, "metadata.json")
        save_metadata(metadata, local_metadata_path)

        upload_json_to_gcs(
            bucket_name=bucket_name,
            local_path=local_metadata_path,
            gcs_path=gcs_path,
        )