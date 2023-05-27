from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from urls import Urls
from data import Data
from generators import GeneratedData


# Позитивный кейс регистрации нового пользователя
def test_user_registration(driver):
    driver.get(Urls.REGISTRATION_URL)
    driver.find_element(*Locators.USER_NAME_INPUT).send_keys(Data.NEW_USER_NAME)
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(Data.NEW_USER_EMAIL)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Data.NEW_USER_PASSWORD)
    driver.find_element(*Locators.REGISTRATION_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))

    assert driver.find_element(*Locators.LOGIN_BUTTON).text == 'Войти'


# Позитивный кейс регистрации пользователя с рандомно сгенерированными данными
def test_random_user_registration(driver):
    driver.get(Urls.REGISTRATION_URL)
    driver.find_element(*Locators.USER_NAME_INPUT).send_keys(GeneratedData.generate_random_name())
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(GeneratedData.generate_random_email())
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(GeneratedData.generate_random_password())
    driver.find_element(*Locators.REGISTRATION_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))

    assert driver.find_element(*Locators.LOGIN_BUTTON).text == 'Войти'


# Негативный кейс регистрации пользователя с некорректным паролем
def test_user_registration_with_wrong_password(driver):
    driver.get(Urls.REGISTRATION_URL)
    driver.find_element(*Locators.USER_NAME_INPUT).send_keys(GeneratedData.generate_random_name())
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(GeneratedData.generate_random_email())
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(GeneratedData.generate_wrong_password())
    driver.find_element(*Locators.REGISTRATION_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.WRONG_PASSWORD_ERROR))

    assert driver.find_element(*Locators.WRONG_PASSWORD_ERROR).text == 'Некорректный пароль'
