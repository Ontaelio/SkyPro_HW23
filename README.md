**Homework 23**

Это решение должно правильно реагировать на прописанные в задании запросы.

В качестве дополнения - тут реализован парсер запросов, чтобы можно было принимать не только строгий список из пяти параметров, а выстраивать их как угодно.

В POST-запросе должны быть:
- file_name: имя файла в папке data
- cmdX: команда, X - ее номер в очереди на выполнение
- valueX: аргумент команды, X - номер в очереди на выполнение

Пар cmdX-valueX может быть сколько угодно, но они обязательно должны быть парами.
Команды выполняются по очереди согласно X, все элементы POST-запроса можно писать вперемешку как угодно.
Последовательность X необязательно консистентна, т.е. лучше давать командам номера 10-20-30 BASIC-стайл, чтобы оставалось место, куда что-нибудь вставить потом.

*Расширенная версия* добавляет команды filter_and, filter_or и filter_not, а также дает возможность выбирать несколько колонок с помощью map, передавая их номера одной строкой через пробелы (см пример ниже).

Пример запроса:

```json
{
    "cmd10": "filter",
    "value10": "POST",
    "cmd40": "sort",
    "value40": "asc",
    "cmd20": "map",
    "value20": "0 3 4 6",
    "cmd28": "unique",
    "value28": "",
    "cmd501": "limit",
    "value501": "2",
    "file_name": "apache_logs.txt"
}
```
