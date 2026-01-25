import pandas as pd

def clean_nulls(df: pd.DataFrame, target: str, features: list[str]) -> pd.DataFrame:

    '''
    Limpia los valores nulos del DataFrame dado
    
    Args:
        df: pandas.DataFrame con el dataset en raw
        target: columna target del dataset
        features: lista de columnas feature del dataset

    Returns:
        pandas.DataFrame
    '''

    # Chequea si hay nulos en la columna target. Si los hay, los elimina
    if df[target].isna().any():

        df.dropna(subset=target, inplace=True)

    # Chequea si hay nulos en el resto de columnas y elimina en caso afirmativo
    if df[features].isna().any().any():

        df.dropna(subset=features, inplace=True)

    # TODO: estrategias de imputación de nulos en features

    return df

def clean_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Elimina los registros duplicados del dataset

    Args:
        df: pandas.DataFrame con los datos

    Returns:
        pandas.DataFrame
    '''

    df.drop_duplicates(inplace=True)

    # TODO: estrategias de deduplicación avanzadas

    return df