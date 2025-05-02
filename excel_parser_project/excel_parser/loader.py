"""
loader.py - загружает  excel в DataFrame
"""
import pandas as pd
from excel_parser.config import RAW_FILE


def load_data(path: str = RAW_FILE, dtype_map: dict = None) -> pd.DataFrame:
    """Эта функция отвечает за загрузку excel-файла
    и превращение его в объект DataFrame.

    path: путь к файлу excel
    dtype_map: словарь с типами данных для таблицы

    Возвращает таблицу — объект DataFrame.
    """

    df = pd.read_excel(
        path,
        engine='openpyxl',
        header=2,
        usecols='B:AF',
        )
    return df
