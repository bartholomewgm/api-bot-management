# GPT Bot Constructor

## Описание

Django-приложение для создания и управления GPT-ботами с поддержкой сценариев и интеграции с Telegram.

## Стек

- Python
- Django
- Django REST Framework
- OpenAI GPT API
- Telegram Bot API

## Архитектура

- bots — управление ботами
- scenarios — сценарии диалогов (FSM)
- integrations — GPT и Telegram интеграции
- users — пользователи и сессии

## API endpoints

### Bots

- GET /bots/
- POST /bots/
- GET /bots/{id}/
- PUT /bots/{id}/
- DELETE /bots/{id}/

### Scenarios

- GET /scenarios/
- POST /scenarios/
- GET /scenarios/{id}/steps/

### Steps

- CRUD /scenarios/{id}/steps/

## Запуск проекта

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
