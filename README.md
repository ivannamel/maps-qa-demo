# Maps QA Demo

Пример проекта для демонстрации навыков QA Automation (API + UI) в контексте картографического сервиса.

## Структура проекта

maps-qa-demo/
├── api-server/
│ └── docker-compose.yml # (необязательно, заменён mock_server.py)
├── web-ui/
│ └── index.html # простой фронтенд на Leaflet
├── tests/
│ ├── api/
│ │ ├── test_geocode.py # API-тест геокодирования
│ │ └── test_reverse_geocode.py# API-тест обратного геокодирования
│ └── ui/
│ ├── conftest.py # фикстуры Selenium
│ └── test_search_ui.py # UI-тест поиска и рендера маркера
├── config.py # базовые URL и заголовки
├── mock_server.py # Flask-mock для /search и /reverse
├── requirements.txt # зависимости Python
└── README.md

bash
Копировать
Редактировать

## Предварительные требования

- Python 3.9+  
- pip  
- Google Chrome (или Chromium) для Selenium  
- (опционально) Docker, если хочется поднять настоящий Nominatim

## Установка и запуск

1. **Клонирование и виртуальное окружение**
   ```bash
   git clone https://github.com/<ваш-ник>/maps-qa-demo.git
   cd maps-qa-demo
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
Запуск mock-сервера геокодирования

bash
Копировать
Редактировать
python mock_server.py
— сервис доступен на http://localhost:8080

Запуск HTTP-сервера для фронтенда
(в новом терминале)

bash
Копировать
Редактировать
cd web-ui
python3 -m http.server 8000
— фронтенд на http://localhost:8000/index.html

Прогон автотестов
(в терминале с активным .venv, из корня проекта)

bash
Копировать
Редактировать
pytest -q
Что тестируется
API

Геокодирование адресов (/search)

Обратное геокодирование координат (/reverse)

UI

Поле поиска и кнопка на карте

Отображение маркера Leaflet после запроса

Смоук-проверка времени рендера маркера

Возможное расширение
Подключить настоящий Nominatim через Docker Compose

Добавить валидацию JSON-schema (jsonschema)

Интегрировать в GitHub Actions с поднятием mock-сервера и фронтенда как сервисов

Добавить сбор различных performance-метрик
