import os

# Базовый URL теперь наш Flask-mock
BASE_URL = "http://localhost:8080"

# UI остаётся на том же порту 8000
UI_URL = "http://localhost:8000/index.html"

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "MapsQA-Demo/1.0 (you@example.com)"
}
