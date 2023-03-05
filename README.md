# Модуль фитнес-трекера
## _Расчет и отображение результатов тренировки_
Модуль выполнен в парадигме ООП.

Этот модуль выполняет следующие функции:
- принимает от блока датчиков информацию о прошедшей тренировке;
- определяет вид тренировки;
- рассчитывает результаты тренировки;
- выводит информационное сообщение о результатах тренировки.

Информационное сообщение включает такие данные:
- тип тренировки (бег, ходьба или плавание);
- длительность тренировки;
- дистанция, которую преодолел пользователь, в километрах;
- средняя скорость на дистанции, в км/ч;
- расход энергии, в килокалориях.
## Установка и настройки из терминала VS Code в MS Windows
### Клонировать репозиторий
```
git clone git@github.com:azhuravlev1001/hw_python_oop.git
```
### Активация виртуального окружения:
```
cd hw_python_oop
source venv/Scripts/activate
```
### Установка зависимостей из файла requirements.txt:
```
pip install -r requirements.txt
```
### Запуск тестов:
```
pytest
```
### Запуск проекта:
```
py homework.py
```
## Разработчик:
- Журавлев Алексей
