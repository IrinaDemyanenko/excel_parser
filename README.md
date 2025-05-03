# excel_parser
### Как запустить проект:

1. Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone https://github.com/IrinaDemyanenko/excel_parser.git
```

```
cd excel_parser/excel_parser_project/
```

2. Создайте виртуальное окружение и активируйте его:

```
python -m venv venv
venv/Scripts/activate
```

3. Установите зависимости:
```
pip install -r requirements.txt
```

4. Запустите скрипт для подготовки файла-excel. Выполнение скрипта создаст копию файла в директории excel_parser_project/data/raw/:
```
python prepare.py
```

5. Откройте копию файла в папке, сохраните изменения,  закройте файл. Этот шаг необходим для расчёта формул внутри файла-excel и получения вычисленных значений формул.

6. Теперь можно запускать основной скрипт:
```
python main.py
```

7. Итоговый .json-файл будет расположен в директории excel_parser_project/data/processed/json/.
