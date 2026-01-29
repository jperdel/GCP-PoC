from sklearn.preprocessing import OneHotEncoder
import pandas as pd

def one_hot_encoder(df: pd.DataFrame, ohe_cols: list[str], train_idx: list[int]) -> pd.DataFrame:

    '''
    Función para obtener el OHE de las columnas indicadas. Además, elimina las columnas originales
    
    Params:
        df: dataframe con los datos preparados para aplicarles el OHE
        ohe_cols: columnas a las que queremos aplicar el OHE
        train_idx: índices de entrenamiento para ajustar el encoder

    Returns:
        pandas.DataFrame con las columnas ohe_cols codificadas mediante OHE
    '''

    enc = OneHotEncoder(handle_unknown='ignore', dtype=int)

    enc.fit(df.loc[train_idx, ohe_cols])

    df.loc[:, enc.get_feature_names_out()] = (
        enc.transform(df[ohe_cols])
        .toarray()
        .astype(float)
    )

    df.drop(columns=ohe_cols, inplace=True)

    return df

def encode_target(enc_dict: dict[str:int], target_col: str, df: pd.DataFrame) -> pd.Series:

    '''
    Función para codificar la columna target
    
    Params:
        enc_dict: diccionario con las clases del problema y su valor codificado correspondiente
        target_col: columna target a buscar en el pandas.DataFrame
        df: pandas.DataFrame con el dataset

    Returns:
        pandas.Series con la columna target codificada
    '''

    y_enc = df[target_col].map(enc_dict)

    return y_enc