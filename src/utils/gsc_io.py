from google.cloud import storage

from io import BytesIO
import json
import pandas as pd

from typing import Dict, Any

def upload_dataframe_to_gcs(df: pd.DataFrame, bucket_name: str, destination_blob_name: str) -> None:
    """
    Sube un DataFrame de pandas a un bucket de GCS como archivo Parquet.
    
    Args:
        df: pandas.DataFrame que quieres subir.
        bucket_name: str, nombre del bucket (sin gs://)
        destination_blob_name: str, ruta completa dentro del bucket, ej: datasets/raw/v1/data.parquet
    """
    # Inicializa el cliente con las credenciales ADC
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    # Guardar DataFrame a un buffer en memoria como Parquet
    buffer = BytesIO()
    df.to_parquet(buffer, index=True)
    buffer.seek(0)

    # Subir el contenido a GCS
    blob.upload_from_file(buffer, content_type="application/octet-stream")

def read_parquet_from_gcs(bucket_name: str, blob_path: str) -> pd.DataFrame:
    """
    Lee un archivo Parquet desde un bucket de GCS y devuelve un DataFrame de pandas.
    
    Args:
        bucket_name: nombre del bucket (sin gs://)
        blob_path: ruta dentro del bucket, ej: datasets/penguins/raw/v1/data.parquet
        
    Returns:
        pandas.DataFrame
    """
    # Inicializa el cliente GCS
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_path)
    
    # Descargar el archivo a memoria
    buffer = BytesIO()
    blob.download_to_file(buffer)
    buffer.seek(0)
    
    # Leer Parquet desde memoria
    df = pd.read_parquet(buffer)
    return df

def upload_json_to_gcs(bucket_name: str, local_path: str, gcs_path: str) -> None:
    """
    Upload a local JSON file to a Google Cloud Storage bucket.

    Parameters
    ----------
    bucket_name : str
        Name of the GCS bucket.
    local_path : str
        Path to the local JSON file.
    gcs_path : str
        Destination path in the bucket (e.g., "datasets/penguins/v1/metadata.json").
    """
    # Inicializa el cliente
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    
    # Nombre del blob dentro del bucket
    blob = bucket.blob(gcs_path)
    
    # Sube el fichero JSON
    blob.upload_from_filename(local_path)


def read_json_from_gcs(bucket_name: str, gcs_path: str) -> Dict[str, Any]:
    """
    Read a JSON file from a Google Cloud Storage bucket.

    Parameters
    ----------
    bucket_name : str
        Name of the GCS bucket.
    gcs_path : str
        Origin path in the bucket (e.g., "datasets/penguins/processed/metadata.json").
    """
    # Inicializa el cliente
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    
    # Nombre del blob dentro del bucket
    blob = bucket.blob(gcs_path)
    
    # Lee y parsea el fichero json
    content = blob.download_as_text()
    metadata = json.loads(content)

    return metadata