"""
prepare.py - запускается перед main.py, готовит копию excel для дальнейшей обработки.
"""

from excel_parser.config import RAW_FILE
from excel_parser.preprocessor import clean_column_and_save_copy


def prepare():
    """Очищает исходный Excel-файл и сохраняет копию с чистыми значениями."""

    cleaned_file = clean_column_and_save_copy(input_path=RAW_FILE, sheet_name='РЕГЛАМЕНТ')



if __name__ == '__main__':
    prepare()
