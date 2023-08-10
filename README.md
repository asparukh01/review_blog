# Review_Blog
## Для запуска проекта

1) Скачате проект

2) Создайте виртуальное окружение python -m venv venv

3) Установите все зависимости pip install -r requirements.txt

4) Сделайте миграции python manage.py migrate

5) Примените их python manage.py migrations

6) Загрузите данные для БД python manage.py loaddata fixtures/auth.json, python manage.py loaddata fixtures/dump.json

7) Извлеките фотографии

8) И запустите сервер python manage.py runserver


## Данные по БД
'NAME': 'postgress',
'USER': 'postgress',
'PASSWORD': 'postgress',
'HOST': 'localhost',
'PORT': 5432,
