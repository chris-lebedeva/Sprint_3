from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from urls import Urls
from data import Data
import time


# Проверка перехода в личный кабинет
def test_personal_account_loading(driver):
    driver.get(Urls.MAIN_PAGE_URL)
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
    current_url = driver.current_url

    assert current_url == Urls.LOGIN_URL


# Проверка перехода из личного кабинета в конструктор по клику на кнопку «Конструктор»
def test_constructor_loading_by_button_clicking(driver):
    driver.get(Urls.LOGIN_URL)
    driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

    assert driver.find_element(*Locators.MAIN_PAGE_HEADING).text == 'Соберите бургер'


# Проверка перехода из личного кабинета в конструктор по клику на логотип Stellar Burgers
def test_constructor_loading_by_logo_clicking(driver):
    driver.get(Urls.LOGIN_URL)
    driver.find_element(*Locators.CONSTRUCTOR_LOGO).click()

    assert driver.find_element(*Locators.MAIN_PAGE_HEADING).text == 'Соберите бургер'


# Проверка выхода из личного кабинета
def test_personal_account_logout(driver):
    driver.get(Urls.LOGIN_URL)
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(Data.EXISTING_USER_EMAIL)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Data.EXISTING_USER_PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    time.sleep(1)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT))
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON))
    driver.find_element(*Locators.LOGOUT_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))

    assert driver.find_element(*Locators.LOGIN_BUTTON).text == 'Войти'
