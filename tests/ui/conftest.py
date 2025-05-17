# tests/ui/conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import UI_URL

@pytest.fixture(scope="session")
def driver():
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless")
    # если хотите видеть, как оно рендерится — уберите headless
    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=opts)
    # Навигируем к нашей странице
    drv.get(UI_URL)
    yield drv
    drv.quit()
