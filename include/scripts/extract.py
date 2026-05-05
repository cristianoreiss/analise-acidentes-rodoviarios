import os
import pandas as pd


def extract_from_csv(nome_arquivo_csv) -> pd.DataFrame:

    path_csv = f'/usr/local/airflow/include/datasets/{nome_arquivo_csv}.csv'
    if os.path.exists(path_csv):
        df = pd.read_csv(path_csv)
        return df
    else:
        raise FileNotFoundError(f"Arquivo não encontrado: {path_csv}")


