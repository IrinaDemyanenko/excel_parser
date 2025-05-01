"""
dtype_schemas.py - словари с типами данных для таблиц
"""

sample_dtype_map = {
    "Chptr": "string",
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
    "F.H.": "int64",  # но есть значения, где нужно обрезать  op.hrs и оставить число
    "LND": "int64",
    "MON": "int64",
    "Last F.H.": "int64",
    "Last LND": "int64",
    "Last CAL": "datetime64[ns]",
    "Next F.H.": "int64",  # есть формулы, нужно считать значения, а не формулы
    "Next LND": "int64",
    "Next CAL": "datetime64[ns]",
    "Rem F.H.": "int64",  # есть формулы, нужно считать значения, а не формулы
    "Rem LND": "int64",
    "Rem CAL": "int64"
}
