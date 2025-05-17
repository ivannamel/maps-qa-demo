# tests/ui/test_search_ui.py

import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_search_and_marker(driver):
    wait = WebDriverWait(driver, 10)

    # ждём, пока на странице станет доступно поле поиска
    inp = wait.until(EC.presence_of_element_located((By.ID, "search-input")))
    inp.clear()
    inp.send_keys("Statue of Liberty")

    btn = driver.find_element(By.ID, "search-btn")
    btn.click()

    # ждём появления хотя бы одного маркера
    start = time.time()
    marker = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".leaflet-marker-icon")))
    assert marker.is_displayed(), "Маркер не отображается"
    assert time.time() - start < 5, "Рендер карты слишком долгий"
