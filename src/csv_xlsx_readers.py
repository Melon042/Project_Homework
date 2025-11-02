import pandas as pd


def read_csv(file_path):
    """Считывает csv-файл и возвращает список словарей"""
    df = pd.read_csv(file_path, sep=";")
    return df.to_dict(orient='records')


def read_xlsx(file_path):
    """Считывает Excel-файл и возвращает список словарей"""
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')
