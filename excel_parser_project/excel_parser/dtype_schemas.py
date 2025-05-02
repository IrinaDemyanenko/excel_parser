"""
dtype_schemas.py - словари с типами данных для таблиц, техническое задание
"""

sample_dtype_map = {
    "Chptr": "string",  #
    "Chaprer name": "string",
    "Task number": "string",
    "Item name": "string",  # убрать знак переноса строки /n
    "Task description": "string",
    "Notes": "string",
    "Interval": "string",
    "Data Module Reference": "string",
    "Package": "string",
    "Skill": "string",
    "Effectivity": "string",
    "Revision": "string",
    "Control": "string",
    "Labor": "object",  # разделить на две колонки float64, string
    "Tools": "string",
    "Materials": "string",
    "№ для WPSS": "string",
    "Название для WPSS": "string",
    "F.H.": "Int64",  # привести к int но есть значения, где нужно обрезать  op.hrs и оставить число (приводит preprocessor)
    "LND": "Int64",
    "MON": "Int64",
    "Last F.H.": "Int64",
    "Last LND": "Int64",
    "Last CAL": "datetime64[ns]",
    "Next F.H.": "Int64",  # есть формулы, нужно считать значения, а не формулы (исправляет preprocessor)
    "Next LND": "Int64",
    "Next CAL": "datetime64[ns]",
    "Rem F.H.": "Int64",  # есть формулы, нужно считать значения, а не формулы (исправляет preprocessor)
    "Rem LND": "Int64",
    "Rem CAL": "Int64",
    "Примечания": "string"
}

# Список колонок, которые нужно привести к строке
STRING_COLUMNS = [
    'Chaprer name',
    'Task number',
    'Item Name',
    'Task Description',
    'Notes',
    'Interval',
    'Data Module Reference',
    'Package',
    'Skill',
    'Effectivity',
    'Revision',
    'Control',
    'Tools',
    'Materials',
    '№ для WPSS',
    'Название для WPSS',
    'Примечания'
]

# Список колонок, которые нужно привести к Int64
INT64_COLUMNS = [
    'F.H.',
    'LND',
    'MON',
    'Last F.H.',
    'Last LND',
    'Next  F.H.',
    'Next LND',
    'Rem F.H.',
    'Rem LND',
]

# Список колонок, которые нужно привести к datetime64[ns]
DATETIME64NS_COLUMNS = [
    'Last CAL',
    'Next CAL',
]
