# BleVaettirDbPlot

Генерация графиков из SQLite базы данных показаний сенсоров BleVaettir.

## Установка

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

## Использование

```bash
.venv/bin/python chart.py --db data.db --sensor-name "SensorName" --type temperature --output chart.png
```

### Аргументы

| Аргумент | Описание | По умолчанию |
|----------|----------|--------------|
| `--db` | Путь к SQLite базе | `readings.db` |
| `--sensor-name` | Имя сенсора для фильтрации | (обязательно) |
| `--type` | Тип показаний | (обязательно) |
| `--output` | Путь для сохранения изображения | `chart.png` |
| `--width` | Ширина изображения в пикселях | 2000 |
| `--height` | Высота изображения в пикселях | 600 |

## Структура таблицы

Программа ожидает sqlite базу от BleVaettir:

## Пример

```bash
.venv/bin/python chart.py --db data --sensor-name "TempSensor1" --type temperature --output temp_chart.png
```

Выведет:
```
Chart saved to temp_chart.png
Min: <min_value>, Max: <max_value>, Points: <count>
```


Смотри примеры: temp1.bash и hum1.bash

Примеры графиков см. в директории ./examples/charts/