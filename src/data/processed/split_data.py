import pandas as pd

from sklearn.model_selection import train_test_split

def split_data(df: pd.DataFrame, test_size: float, strat_by: str=None, random_seed: int=None) -> tuple[pd.Index]:

    '''
    Función para partir los datos en train y test

    Args:
        df: pandas.DataFrame con el dataset a dividir
        test_size: tamaño del conjunto de test. Debe ser una proporción entre 0 y 1
        strat_by: columna sobre la que estratificar los datos. Si no hay, no estratifica
    
    Returns:
        Devuelve una tupla consistente en:
            idx_train: pandas.Index con el conjunto de datos de entrenamiento
            idx_test: pandas.Index con el conjunto de datos de test
    '''

    df_train, df_test = train_test_split(df, test_size=test_size, stratify=strat_by, random_state=random_seed)

    return df_train.index, df_test.index
