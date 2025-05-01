"""
main.py - основной скрипт
"""
from excel_parser.loader import load_data
from excel_parser.inspector import inspect
from excel_parser.config import RAW_FILE


def main():
    """Основной сценарий запуска парсера."""

    # создаём таблицу DataFrame
    df = load_data(RAW_FILE)

    # оценим данные в таблице
    inspect(df)


if __name__ == '__main__':
    main()
