import json
from datetime import datetime
from typing import Dict, Any
import pandas as pd


def generate_metadata(
    df: pd.DataFrame,
    extra_metadata: Dict[str, Any] | None = None,
) -> Dict[str, Any]:
    """
    Generate basic metadata for a dataset.

    Parameters
    ----------
    df : pd.DataFrame
        Dataset dataframe.
    extra_metadata : dict, optional
        Additional metadata to include.

    Returns
    -------
    dict
        Metadata dictionary.
    """
    metadata = {
        "created_at": datetime.utcnow().isoformat(),
        "row_count": len(df),
        "column_count": len(df.columns),
        "columns": {
            col: str(dtype)
            for col, dtype in df.dtypes.items()
        },
    }

    if extra_metadata:
        metadata.update(extra_metadata)

    return metadata


def save_metadata(
    metadata: Dict[str, Any],
    local_path: str,
) -> None:
    """
    Save metadata dictionary as JSON.

    Parameters
    ----------
    metadata : dict
        Metadata to save.
    local_path : str
        Path where metadata.json will be written.
    """
    with open(local_path, "w") as f:
        json.dump(metadata, f, indent=2)