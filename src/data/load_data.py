from google.cloud import bigquery

import pandas as pd

def load_penguins(query: str) -> pd.DataFrame:

    client = bigquery.Client()

    df = client.query(query).to_dataframe()

    return df