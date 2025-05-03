"""
cleaner.py:

- превращает прочерки, пустые значения в pd.NA
- удаляет все переносы строк '\n' из DataFrame
"""

import pandas as pd
from excel_parser.inspector import inspect




def strip_strings(x):
    """Убирает пробелы вначале и в конце строки, если полученное
    значение строка, если не строка - возвращает переданное значение.
    """
    if isinstance(x, str):
        return x.strip()
    return x


def clean_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Проходит по каждой ячейке таблицы, если находит прочерки, пустые строки,
    лишние пробелы - заменяет на pd.NA (универсальный пропуск).

    Возвращает очищенную таблицу.
    """
    print("\nДО очистки\n")
    inspect(df)  # таблица до

    to_find = {'', ' ', '  ', '   ', '-', '--', '---'}  # обозначения пустых значений

    df = df.applymap(strip_strings)  # во всех строках удаляем лишние пробелы

    df.replace(to_find, pd.NA, inplace=True)  # заменяем условные пропуски на NA

    print("\nПОСЛЕ очистки\n")
    inspect(df)  # таблица после

    return df


def remove_newlines_n_(x):
    """Удаляет символы переноса строки из строки.

    Применим до массового преобразования в строки.
    Т. к. функция сработает только для строк (числа и даты пропустит),
    не будет лишней нагрузки.
    """
    if isinstance(x, str):
        return x.replace('\n', ' ')
    return x


def remove_new_lines_from_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Удаляет все переносы строк '\n' из DataFrame.

    Применяется после очистки таблицы от прочерков и пустых значений.
    """
    df = df.applymap(remove_newlines_n_)
    return df
