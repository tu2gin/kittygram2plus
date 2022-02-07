# backend_community_homework



C:\\Users\\*NAME USER*\\AppData\\Local\\Programs\\Python\\Python310\\python.exe -m venv venv

source venv/Scripts/activate

WARNING: You are using pip version 21.2.4;

python -m pip install --upgrade pip

pip install -r requirements.txt

pip install pytest --upgrade

pip install flake8-quotes

python manage.py runserver

python manage.py createsuperuser

Flake8

Выбрать и активировать нужный линтер можно с помощью командной строки VSC (Command Palette, вызывается через Ctrl+Shift+P).
Введите в командную строку Python: Select Linter и нажмите Enter.


 
yatube/static/



How to Use Python isort Library
https://simpleisbetterthancomplex.com/packages/2016/10/08/isort.html

Установка
Установите его через pip или возьмите код с GitHub:

pip install isort
Использование
Вы уже можете начать использовать его без какой-либо настройки:

Проверить и применить изменения везде
isort *

Показать изменения перед применением
isort * --diff

isort views.py urls.py

# show a diff before applying any change
isort views.py --diff

# just check for errors
isort urls.py --check-only


python manage.py test -v 2

python manage.py test posts.tests.test_views.PostContextTests.test_img

python manage.py test posts.tests.test_views.CommentAddTests.test_add_comment


Тестомерки Coverage
Проект не дымит. Что тестировать дальше?
Ответ на этот вопрос даст инструмент coverage (англ. «покрытие»). Он показывает, в какой степени код проекта проверен (покрыт) тестами.
Любимая игра программистов — увеличить coverage до 100%.
Установка пакета Coverage

pip3 install coverage

https://coverage.readthedocs.io/en/latest/index.html


# После выполнения команды 
coverage run --source='posts,users' manage.py test -v 2 
# coverage сформирует отчёт и сохранит его в корневой папке проекта, в файле .coverage.

# Самый простой способ — вывести результаты в консоль.
coverage report

# Для представления результатов есть и более удобный формат: отчёт можно сохранить в виде HTML.
coverage html

# Все команды отображения работают с созданным отчётом .coverage. После нового запуска 
coverage run 
# этот отчёт будет перезаписан.


Хозяйке на заметку: стандартный метод slugify из модуля django.utils.text не умеет работать с кириллицей. Нужно установить в виртуальное окружение пакет pytils (pip3 install pytils) и импортировать slugify именно из него, как это сделано в листинге deals/models.py


# ----------------
# Работа с графикой
# ----------------

# {Установка}
pip install pillow 
pip install sorl-thumbnail

# {Документация}
https://github.com/jazzband/sorl-thumbnail

# {Загрузка тегов библиотеки в шаблон}
<!-- Загрузка тегов библиотеки в шаблон -->
{% load thumbnail %}


<!-- Пример использования тега для пропорционального уменьшения и обрезки -->
<!-- картинки до размера 100x100px с центрированием -->
{% thumbnail item.image "100x100" crop="center" as im %}
  <img src="{{ im.url }}" width="{{ im.width }}" height="{{ im.height }}">
{% endthumbnail %}


# ---!---!---!---!---!---!---!---!---!---!---!---!---!---

# ----------------
# Ошибки
# ----------------
# ModuleNotFoundError: No module named 'pip'
python -m ensurepip

# ----------------
# Миграция Базы
# ----------------
# Первым делом запускается команда makemigrations, Django проверяет модели и таблицы в БД, анализирует их на соответствие друг другу, подготавливает скрипты миграций
#  и сообщает, какие миграции необходимо применить; однако никаких изменений в БД в этот момент не вносится.
# ----------------

python manage.py makemigrations

# Затем запускается команда migrate, и в этот момент все изменения вносятся в БД.

python manage.py migrate

# ----------------
# установка django-debug-toolbar
# ----------------
pip install django-debug-toolbar


Регистрация пользователя

POST
# на адрес
http://127.0.0.1:8000/auth/users/

# ---------------------------------------
{
    "username" : "cat_admin",
    "password": "adminadmin"
}


{
    "email": "",
    "username": "cat_admin",
    "id": 1
}

Токен  

access":

http://127.0.0.1:8000/auth/jwt/create/

{
    "username" : "cat_admin",
    "password": "adminadmin"
}

{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0NDMxNTkyOSwianRpIjoiY2ZjZWI5M2YyZWI4NGZkNmE0YjZjMWNjNzFjYzhlNWQiLCJ1c2VyX2lkIjoxfQ.WvqCtaAFjoeJyrvhspzBd6TgRy5kXiTBoZ3OTDIu10M",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ0MzE1OTI5LCJqdGkiOiI0MzI1ZDNlNGIwZTI0MTcxYmJiZTQ5NWJhYjA0ZTBiZiIsInVzZXJfaWQiOjF9.cUVD67NaelcxVqePOs2p4RUEAPT3iHUjzxKgHYLn-8Q"
}
# ---------------------------------------
{
    "username" : "cat_user2",
    "password": "adminadmin"
}

{
    "email": "",
    "username": "cat_user1",
    "id": 3
}

Токен

{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0NDMxODg2NiwianRpIjoiZjg3NmE2ZTYyNTM5NDJmMjk3MDNiYmRjYzU3Yzk5MWQiLCJ1c2VyX2lkIjozfQ.MXlCGDHaZVfAEwqnhNuC1GD7mLyu2KJ3rVyEhElzGns",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ0MzE4ODY2LCJqdGkiOiI0N2UyZmZhNWQyMmQ0ZDFmODk3NGUwNmM5MDhhMjZhZiIsInVzZXJfaWQiOjN9.q_86naz83b0KNPDnCyZDTGrCglCd0rNkUkd34K00YHQ"
}


# ---------------------------------------

{
    "username" : "cat_user2",
    "password": "adminadmin"
}

{
    "email": "",
    "username": "cat_user2",
    "id": 4
}

{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0NDMxODk0MCwianRpIjoiNmMzYjJiOWViNjI0NDZiZDk0NTBiMmYwZmU1OGUzYzQiLCJ1c2VyX2lkIjo0fQ.vEwQGk9hRpmwsxmI8UrppZatNd0r5qSDRO9s87m523Q",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ0MzE4OTQwLCJqdGkiOiIxYWI4MDU0ZmM0NjE0YTE5OTg2NTg4MjI0ZDQxYmJkZSIsInVzZXJfaWQiOjR9.d9nFrtbKKk4UYqTHaaQQ79ZnP8KUC8GXWsr80n5vyWM"
}



# ---------------------------------------
добавить кота
POST
http://127.0.0.1:8000/cats/

{
    "name" : "cat_admin",
    "color": "White",
    "birth_year": 1999
}

{
    "name" : "Пуфыстик",
    "color": "White",
    "birth_year": 2020
}

{
    "name" : "Чубайс",
    "color": "Ginger",
    "birth_year": 1999
}

ответ

{
    "id": 1,
    "name": "cat_admin",
    "color": "White",
    "birth_year": 1999,
    "achievements": [],
    "owner": 1,
    "age": 23
}






