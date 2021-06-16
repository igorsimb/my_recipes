# Домашнее задание homework_l34
И заодно тренировка написания readme.md

<img src="https://i.imgur.com/BthC3Sw.jpeg" alt='Лучшие рецепты мира' width='50%'/>

## Деплой
Рабочий деплой задания находится на [http://forshag.pythonanywhere.com](http://forshag.pythonanywhere.com)

## Задание

```
Создайте программу, которая организует работу с рецептами.

Программа должна состоять их трёх архитектурных частей, согласно паттерну MVC:

1. Модель (Model). Хранит данные и методы работы с ними
2. Представление (View). Отвечает за то, что видит пользователь
3. Контроллер (Controller). Связывает пользовательские действия (изменения) в
программе с Представлением и Моделью. Обрабатывает пользовательский ввод и
передаёт его Модели, и наоборот, передаёт данные от Модели в Представление, из-за
чего пользователь видит изменения в интерфейсе программы.

Модель должна хранить следующую информацию:
- название рецепта;
- автор рецепта;
- тип рецепта (первое, второе блюдо и т.д.);
- текстовое описание рецепта;
- список ингредиентов;
- название кухни (итальянская, французская, украинская и т.д.).

У пользователя должна быть возможность делать следующие действия:
- Добавить рецепт
- Удалить рецепт
- Посмотреть конкретный рецепт
- Посмотреть все рецепты

В качестве интерфейса программы можно выбрать простое консольное приложение, где
всё необходимое будет писаться текстом.

Создайте необходимые методы для осуществления заданного пользовательского функционала.
Каждая архитектурная часть программы должна быть представлена в отдельном файле.

В итоге структура проекта будет следующей:

RecipesApplication
    ├───controller.py (здесь функционал контроллера)
    ├───homework_l34.py (отсюда пользователь запускает программу, можно назвать как угодно)
    ├───model.py (здесь функционал модели)
    └───view.py (здесь функционал представления)
```

## Сделано с помощью
* Django
* Bootstrap 5
* django-crispy-forms

## Перед началом работы

Шаг 1. Клонируйте этот репозиторий

Шаг 2. Установите зависимости:


```
pip install django
pip install django-crispy-forms
pip install crispy-bootstrap5
```

Шаг 3. Убедитесь, что вы в папке ```shag``` (вместе с manage.py)

Шаг 4. Сделайте миграции:

```
python manage.py makemigrations
python manage.py migrate
```

Шаг 5. Запустите сервер:
```
python manage.py runserver
```

## Функционал
- Главная страница - просмотр всех текущих рецептов (у каждого видно название и первые 150 символов описания)
- Кликнуть на название рецепта для подробной информации
- Кликнуть на "+", чтобы добавить новый рецепт
- Кликнуть на значок карандаша для редактирования рецепта
- Кликнуть на "Х" для удаление (экран подтверждения даст возможность передумать)