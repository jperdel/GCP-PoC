from google.cloud import storage

from io import BytesIO
import pandas as pd

from config.settings import BUCKET_NAME, DATASETS

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
    df.to_parquet(buffer, index=False)
    buffer.seek(0)

    # Subir el contenido a GCS
    blob.upload_from_file(buffer, content_type="application/octet-stream")
    print(f"Archivo subido correctamente a gs://{bucket_name}/{destination_blob_name}")

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