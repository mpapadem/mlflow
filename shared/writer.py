import pandas as pd

def read_files(file: str) -> pd.DataFrame:
    return pd.read_csv(file)