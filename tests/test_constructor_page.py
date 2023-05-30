from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import time
from data import Data
from locators import Locators
from urls import Urls


# Проверка перехода к разделу "Соусы" в конструкторе
def test_constructor_sauces_section_switching(driver):
    driver.get(Urls.MAIN_PAGE_URL)
    driver.find_element(*Locators.CONSTRUCTOR_SAUCES_SECTION_SWITCHER).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_SAUCES_SECTION_HEADING))

    assert driver.find_element(*Locators.CONSTRUCTOR_SAUCES_SECTION_HEADING).text == 'Соусы'


# Проверка перехода к разделу "Начинки" в конструкторе
def test_constructor_toppings_section_switching(driver):
    driver.get(Urls.MAIN_PAGE_URL)
    driver.find_element(*Locators.CONSTRUCTOR_TOPPINGS_SECTION_SWITCHER).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_TOPPINGS_SECTION_HEADING))

    assert driver.find_element(*Locators.CONSTRUCTOR_TOPPINGS_SECTION_HEADING).text == 'Начинки'


# Проверка перехода к разделу "Булки" в конструкторе
def test_constructor_buns_section_switching(driver):
    driver.get(Urls.MAIN_PAGE_URL)
    driver.find_element(*Locators.CONSTRUCTOR_TOPPINGS_SECTION_SWITCHER).click()
    driver.find_element(*Locators.CONSTRUCTOR_BUNS_SECTION_SWITCHER).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUNS_SECTION_HEADING))

    assert driver.find_element(*Locators.CONSTRUCTOR_BUNS_SECTION_HEADING).text == 'Булки'


# Позитивный кейс создания заказа через конструктор
def test_order_burger_success(driver):
    driver.get(Urls.LOGIN_URL)
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(Data.EXISTING_USER_EMAIL)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Data.EXISTING_USER_PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUNS_SECTION_HEADING))
    bun = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BUN))
    drag_and_drop_to_basket(driver, bun)
    driver.find_element(*Locators.CONSTRUCTOR_TOPPINGS_SECTION_SWITCHER).click()
    time.sleep(0.40)
    patty = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PATTY))
    drag_and_drop_to_basket(driver, patty)
    driver.find_element(*Locators.CONSTRUCTOR_SAUCES_SECTION_SWITCHER).click()
    time.sleep(0.40)
    sauce = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.SAUCE))
    drag_and_drop_to_basket(driver, sauce)
    driver.find_element(*Locators.ORDER_BUTTON).click()
    time.sleep(0.01)

    assert driver.find_element(*Locators.CONFIRMATION_POPUP).is_displayed()


def drag_and_drop_to_basket(driver, element):
    action = ActionChains(driver)
    action.drag_and_drop_by_offset(element, 15, 15).perform()
    pyautogui.moveTo(None, 400)
    pyautogui.click()
