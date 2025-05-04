"""
main.py - основной скрипт
"""
from excel_parser.loader import load_data
from excel_parser.inspector import inspect
from excel_parser.config import CLEANED_FILE
from excel_parser.cleaner import clean_missing_values, remove_new_lines_from_dataframe
from excel_parser.dtype_schemas import STRING_COLUMNS, INT64_COLUMNS, DATETIME64NS_COLUMNS
from excel_parser.exporter import export_to_json
from excel_parser.convertor import (
    convert_chptr_column,
    mass_convert_column_to_string,
    mass_convert_column_to_int64,
    mass_convert_column_to_datetime64ns,
    convert_RemCAL_to_int64,
    split_column_two_float_string
    )



def parse():
    """Загружает очищенный файл и применяет схему типов."""

    df = load_data(CLEANED_FILE)  # создаём таблицу DataFrame

    df = split_column_two_float_string(df, 'Labor')  # разделить колонку Labor на две

    inspect(df)  # оценим данные в таблице, как считались

    df = clean_missing_values(df)  # очищаем таблицу от пустых значений и прочерков

    df = remove_new_lines_from_dataframe(df)  # очищаем таблицу от '\n'

    # преобразование колонок
    df = convert_chptr_column(df)
    df = mass_convert_column_to_string(df, STRING_COLUMNS)  # колонки в строки
    df = mass_convert_column_to_int64(df, INT64_COLUMNS)
    df = mass_convert_column_to_datetime64ns(df, DATETIME64NS_COLUMNS)
    df = convert_RemCAL_to_int64(df)

    inspect(df)  # оценим данные в таблице, преобразовались типы в колонках

    export_to_json(df)


if __name__ == '__main__':
    parse()      # потом можно запускать хоть сколько угодно раз
