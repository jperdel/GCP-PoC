from google.cloud import bigquery

import pandas as pd

def load_penguins(query: str) -> pd.DataFrame:
    '''
    Lee los datos originales en crudo desde BigQuery

    Args:
        query: query para leer desde el cliente de BigQuery

    Returns:
        pandas.DataFrame
    '''

    client = bigquery.Client()

    df = client.query(query).to_dataframe()

    return df