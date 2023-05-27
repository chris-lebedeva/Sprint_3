import pytest
from selenium import webdriver


@pytest.fixture() # фикстура драйвера
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
