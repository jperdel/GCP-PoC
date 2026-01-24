from utils.metadata import generate_metadata, save_metadata
from utils.gsc_io import upload_json_to_gcs
import pandas as pd
import tempfile
import os


def create_raw_metadata(
    df: pd.DataFrame,
    bucket_name: str,
    gcs_path: str,
    source: str,
    query: str,
):
    metadata = generate_metadata(
        df,
        extra_metadata={
            "source": source,
            "query": query,
            "format": "parquet",
            "compression": "snappy",
        },
    )

    with tempfile.TemporaryDirectory() as tmpdir:
        local_metadata_path = os.path.join(tmpdir, "metadata.json")
        save_metadata(metadata, local_metadata_path)

        print(local_metadata_path)

        upload_json_to_gcs(
            bucket_name=bucket_name,
            local_path=local_metadata_path,
            gcs_path=gcs_path,
        )