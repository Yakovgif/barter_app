# Платформа обмена вещами (Barter_platform)

## Описание

Веб-приложение на Django для обмена вещами между пользователями с веб-интерфейсом и REST API.

## Установка

1. Клонировать репозиторий:
git clone https://github.com/yourusername/barter_platform.git
cd barter_platform
2. Создать виртуальное окружение и установить зависимости:
python -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows
pip install -r requirements.txt
3. Настроить базу данных PostgreSQL в `barter_platform/settings.py`.

4. Сделать миграции и запустить сервер:
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
5. Использование

- Веб-интерфейс доступен по адресу: `http://127.0.0.1:8000/`
- REST API доступен по адресу: `http://127.0.0.1:8000/api/`