import pandas as pd
import country_converter as cc

def comparation(dfs, years):
    """
    Compares the number of rows, columns, missing values, and duplicate values in each DataFrame.
    Parameters:
        dfs (list of pd.DataFrame): List of DataFrames to compare.
        years (list of str): List of years corresponding to each DataFrame.
    Returns:
        pd.DataFrame: A DataFrame summarizing the comparison results.
    """
    summary_data = []

    for df, year in zip(dfs, years):
        num_rows = df.shape[0]
        num_columns = df.shape[1]
        total_missing = df.isna().sum().sum()
        total_duplicates = df.duplicated().sum()
        
        summary_data.append({
            "Year": year,
            "Number of rows": num_rows,
            "Number of columns": num_columns,
            "All null values ": total_missing,
            "All duplicate values": total_duplicates
        })
    
    return pd.DataFrame(summary_data)


def country_code(dfs_to_rename, country_col="country"):
    """
    Asigna continentes a cada dataframe en el diccionario dfs_to_rename.
    
    Parámetros:
    - dfs_to_rename (dict): Diccionario con dataframes organizados por año.
    - country_col (str): Nombre de la columna que contiene los nombres de los países.
    
    Retorna:
    - dict: El mismo diccionario dfs_to_rename con la columna 'continent' agregada.
    """
    continent_mapping = {
        "Argentina": "South America",
        "Belize": "Central America",
        "Bolivia": "South America",
        "Brazil": "South America",
        "Canada": "North America",
        "Chile": "South America",
        "Colombia": "South America",
        "Costa Rica": "Central America",
        "Dominican Republic": "Central America",
        "Ecuador": "South America",
        "El Salvador": "Central America",
        "Guatemala": "Central America",
        "Honduras": "Central America",
        "Haiti": "Central America",
        "Jamaica": "Central America",
        "Mexico": "North America",
        "Panama": "Central America",
        "Paraguay": "South America",
        "Peru": "South America",
        "Puerto Rico": "Central America",
        "Trinidad and Tobago": "South America",
        "Trinidad & Tobago": "South America",
        "United States": "North America",
        "Uruguay": "South America",
        "Venezuela": "South America"
    }

    for year, df in dfs_to_rename.items():
        df["continent"] = cc.convert(names=df[country_col].tolist(), to="continent")

        df["continent"] = df[country_col].map(continent_mapping).fillna(df["continent"])
        
        dfs_to_rename[year] = df
        
    return dfs_to_rename