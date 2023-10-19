# DjangoRestFramework
[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Django+Rest+Framework)](https://git.io/typing-svg)

### Реализовано:
- регистрация по номеру телефона
- методы сериализаторов
- unit тесты
- оптимизирация запросов
- сортировка
- фильтрация
- поиск

### Запуск на локальной машине
- создать файл .env в директории service с данными базы postgres
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver
