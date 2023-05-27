from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from urls import Urls
from data import Data


# Проверка входа по кнопке «Войти в аккаунт» на главной странице
def test_user_login_on_main_page(driver):
    driver.get(Urls.MAIN_PAGE_URL)
    driver.find_element(*Locators.MAIN_PAGE_LOGIN_BUTTON).click()
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(Data.EXISTING_USER_EMAIL)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Data.EXISTING_USER_PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))

    assert driver.find_element(*Locators.ORDER_BUTTON).text == 'Оформить заказ'


# Проверка входа через кнопку «Личный кабинет»
def test_user_login_through_personal_account(driver):
    driver.get(Urls.MAIN_PAGE_URL)
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(Data.EXISTING_USER_EMAIL)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Data.EXISTING_USER_PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))

    assert driver.find_element(*Locators.ORDER_BUTTON).text == 'Оформить заказ'


# Проверка входа через кнопку в форме регистрации
def test_user_login_on_registration_page(driver):
    driver.get(Urls.REGISTRATION_URL)
    driver.find_element(*Locators.REG_PAGE_LOGIN_BUTTON).click()
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(Data.EXISTING_USER_EMAIL)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Data.EXISTING_USER_PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))

    assert driver.find_element(*Locators.ORDER_BUTTON).text == 'Оформить заказ'


# Проверка входа через кнопку в форме восстановления пароля
def test_user_login_on_password_recovery_page(driver):
    driver.get(Urls.LOGIN_URL)
    driver.find_element(*Locators.FORGOT_PASSWORD_BUTTON).click()
    driver.find_element(*Locators.REG_PAGE_LOGIN_BUTTON).click()
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(Data.EXISTING_USER_EMAIL)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Data.EXISTING_USER_PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))

    assert driver.find_element(*Locators.ORDER_BUTTON).text == 'Оформить заказ'
