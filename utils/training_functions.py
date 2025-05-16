import pandas as pd

def create_dummy(df):
    """
    Crea dummy variables para las columnas categóricas especificadas.
    
    Parámetros:
    - df (pd.DataFrame): El dataframe que contiene las columnas categóricas.

    Retorna:
    - pd.DataFrame: El dataframe con las dummy variables agregadas.
    """
    dummies = pd.get_dummies(df["continent"], drop_first=True)
    
    df = df.drop(columns=["continent"])
    
    df = pd.concat([df, dummies], axis=1)
    
    return df