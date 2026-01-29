from utils.metadata import generate_metadata, save_metadata
from utils.gsc_io import upload_json_to_gcs
import pandas as pd
import tempfile
import os

def create_features_metadata(
    df: pd.DataFrame,
    bucket_name: str,
    gcs_path: str,
    source: str,
    encoding_steps: dict,
    scaling_steps: dict,
    target_encoding: dict
):
    metadata = generate_metadata(
        df,
        extra_metadata={
            "stage": "features",
            "source": source,
            "encoding_steps": encoding_steps,
            "scaling_steps": scaling_steps,
            "target_encoding": target_encoding,
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