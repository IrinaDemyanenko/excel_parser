"""
exporter.py - сохранение DataFrame в файл.
"""
import os
import pandas as pd
from excel_parser.config import JSON_OUT_FILE


def export_to_json(df: pd.DataFrame, output_path: str = JSON_OUT_FILE):
    """Экспоритрует данные из DataFrame, сохраняет в .json файл.

    df: отформатированная таблица pd.DataFrame
    output_path: путь для сохранения файла

    Особенности экспорта:
     - каждая строка будет отдельным объектом словаря;
     - без преобразования кирилицы;
     - даты в формате iso ("2022-03-25T00:00:00").
    """
    # защита от ошибки сохранения, если папки нет
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df.to_json(
        path_or_buf=output_path,
        orient='records',  # каждая строка будет отдельным объектом словаря
        force_ascii=False,  # без преобразования кирилицы
        indent=2,
        date_format='iso',  # "2022-03-25T00:00:00", иначе timestamp (1648166400000)
    )
