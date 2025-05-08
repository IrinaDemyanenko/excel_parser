"""
convertor.py - преобразование типов данных в колонках.
"""

import pandas as pd



def split_column_two_float_string(df: pd.DataFrame, col_name: str) -> pd.DataFrame:
    """Делит колонку col_name на две колонки - float и string.

    Сохраняем в первоначальной колонке только числа типа float.
    Для строковых значений создаём новую колонку с припиской _na.

    '1,0' останется в col_name
    'n/a' попадёт в col_name_na

    Возвращает DataFrame обновлённой, с новой колонкой.
    Использую для колонки Labour.
    """
    # если опечатка в названии колонки
    if col_name not in df.columns:
        print(f'Колонки {col_name} нет в таблице, проверьте правильность написания.')
        return df

    col_cleaned = df[col_name].astype(str).str.strip()  # без лишних пробелов

    col_float = pd.to_numeric(
        col_cleaned.str.replace(',', '.', regex=False),
        errors='coerce'
        )  # regex=False как обычный текст, без регулярных выражений

    condition = col_float.isna()
    col_string = col_cleaned.where(condition)  # оставить значение из col_cleaned, если col_float.isna() равно True

    df[col_name] = col_float
    df[f'{col_name}_na'] = col_string

    return df


def format_chptr(x):
    """Меняет тип с int на string, при этом форматирует строку так,
    чтобы она состояла из двух символов. Для односимвольных строк добавляет
    к символу ведущий ноль.
    7 -> '07'
    45 -> '45'
    """
    if pd.notna(x):
        return f'{int(x):02}'  # два символа, при необходимости добавл. 0
    return pd.NA


# колонка B
def convert_chptr_column(df: pd.DataFrame) -> pd.DataFrame:
    """Преобразует колонку 'Chptr' в строку, добавляет ведущие нули
    (например, 7 → '07').

    Возвращает DataFrame с отформатированной колонкой 'Chptr'.
    """
    df['Chptr'] = df['Chptr'].apply(format_chptr).astype('string')
    return df


# преобразование в строку
def convert_column_to_string(df: pd.DataFrame, col_name: str) -> pd.DataFrame:
    """Преобразование колонки в строку, если она есть в таблице.

    df: pd.DataFrame таблица
    col_name: имя колонки
    Возвращает DataFrame с отформатированной колонкой 'col_name'.
    """
    if col_name in df.columns:
        df[col_name] = df[col_name].astype('string')
    else:
        print(f'{col_name} нет в таблице.')

    return df


def mass_convert_column_to_string(df: pd.DataFrame, list_name: list[str]):
    """Массовое преобразование списка колонок в строки."""
    for col in list_name:
        df = convert_column_to_string(df, col)
    return df


# преобразование в целое число
def convert_column_to_int64(df: pd.DataFrame, col_name: str) -> pd.DataFrame:
    """Преобразование колонки в Int64, если она есть в таблице.

    df: pd.DataFrame таблица
    col_name: имя колонки
    Возвращает DataFrame с отформатированной колонкой 'col_name'.
    """
    if col_name in df.columns:
        #print(f'{col_name} начало преобразовани к Int64.')
        df[col_name] = pd.to_numeric(df[col_name], errors='coerce').astype('Int64')
        #print(f'{col_name} преобразовани к Int64.')
    else:
        print(f'{col_name} нет в таблице.')
    return df


def mass_convert_column_to_int64(df: pd.DataFrame, list_name: list[str]) -> pd.DataFrame:
    """Массовое преобразование списка колонок в Int64."""
    for name in list_name:
        df = convert_column_to_int64(df, name)
    return df


# преобразование в datetime64[ns]
def convert_column_to_datetime64ns(df: pd.DataFrame, col_name: str) -> pd.DataFrame:
    """Преобразование колонки в datetime64[ns], если она есть в таблице.

    df: pd.DataFrame таблица
    col_name: имя колонки
    Возвращает DataFrame с отформатированной колонкой 'col_name'.
    """
    if col_name in df.columns:
        df[col_name] = pd.to_datetime(df[col_name], errors='coerce')  # заменит невалидные даты на NaT
    else:
        print(f'{col_name} нет в таблице.')
    return df


def mass_convert_column_to_datetime64ns(
        df: pd.DataFrame,
        list_name: list[str]
) -> pd.DataFrame:
    """Массовое преобразование списка колонок в Int64."""
    for name in list_name:
        df = convert_column_to_datetime64ns(df, name)
    return df


# преобразование в целое число Rem CAL, потребовала округления, видимо где-то в формуле float
def convert_RemCAL_to_int64(df: pd.DataFrame) -> pd.DataFrame:
    """Преобразование колонки Rem CAL в Int64.

    df: pd.DataFrame таблица
    Возвращает DataFrame с отформатированной колонкой 'Rem CAL'.
    """
    df['Rem CAL'] = pd.to_numeric(df['Rem CAL'], errors='coerce').round().astype('Int64')
    return df
