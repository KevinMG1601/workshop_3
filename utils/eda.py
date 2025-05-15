import pandas as pd

def comparation(dfs, years):
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
