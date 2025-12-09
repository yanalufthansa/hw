import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # Размеры экрана
    driver.set_window_size(1000, 1000)
    yield driver
    driver.quit()