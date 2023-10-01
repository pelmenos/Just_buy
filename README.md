# Установка
Проект написан на python 3.10

1. Клонируйте репозиторий: `https://github.com/pelmenos/Just_buy.git`.
2. Перейдите в созданную директорию `cd Just_buy`.
3. Создайте виртуальное окружение: `python -m venv venv`.
4. Активируйте его: `venv\Scripts\activate.bat`.
5. Перейдите в папку project: `cd project`.
6. Установите зависимости: `pip install -r requirements.txt`.
7. Запустить код `python manage.py runserver`.

В бд уже хранятся некоторые данные: админ и пользователь, с данными указанными в тех. задании, несколько продуктов.

Но можно использовать команду `python manage.py create_origin_data`, которая создаст админа, пользователя и 3 продукта.

Если нужно создать нового админа: `python manage.py createsuperuser`.

###Запуск с докером
1. Клонируйте репозиторий: `https://github.com/pelmenos/Just_buy.git`.
2. Перейдите в папку project: `cd Just_buy/project`.
3. Выполните миграции: `docker-compose run web python manage.py migrate`.
4. Создать записи в бд: `docker-compose run web python manage.py create_origin_data` (если их нет).
5. Запустить сервер: `docker-compose up`.

Запуск из папки deploy не получился, только из папки с django проектом


