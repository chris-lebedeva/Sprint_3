from selenium.webdriver.common.by import By


# Класс для хранения локаторов
class Locators:
    # Поле "Имя"
    USER_NAME_INPUT = By.XPATH, ".//label[contains(text(), 'Имя')]/following-sibling::input"
    # Поле "Email"
    EMAIL_INPUT = By.XPATH, ".//label[contains(text(), 'Email')]/following-sibling::input"
    # Поле "Пароль"
    PASSWORD_INPUT = By.XPATH, ".//label[contains(text(), 'Пароль')]/following-sibling::input"
    # Кнопка "Зарегистрироваться"
    REGISTRATION_BUTTON = By.XPATH, ".//button[contains(text(),'Зарегистрироваться')]"
    # Кнопка "Войти"
    LOGIN_BUTTON = By.XPATH, ".//button[contains(text(), 'Войти')]"
    # Сообщение о некорректном пароле
    WRONG_PASSWORD_ERROR = By.XPATH, ".//p[@class='input__error text_type_main-default']"
    # Сообщение, что пользователь уже существует
    EXISTING_USER_ERROR = By.XPATH, ".//p[contains(text(), 'Такой пользователь уже существует')]"
    # Кнопка "Войти в аккаунт" на главной странице
    MAIN_PAGE_LOGIN_BUTTON = By.XPATH, ".//button[contains(text(),'Войти в аккаунт')]"
    # Кнопка "Оформить заказ" на главной странице
    ORDER_BUTTON = By.XPATH, ".//button[contains(text(),'Оформить заказ')]"
    # Кнопка "Личный кабинет"
    PERSONAL_ACCOUNT = By.XPATH, ".//a[@href='/account']"
    # Кнопка "Войти" на странице регистрации
    REG_PAGE_LOGIN_BUTTON = By.XPATH, ".//a[@href='/login']"
    # Кнопка "Восстановить пароль"
    FORGOT_PASSWORD_BUTTON = By.XPATH, ".//a[@href='/forgot-password']"
    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = By.XPATH, ".//li/a[@href='/']"
    # Заголовок "Соберите бургер" на главной странице
    MAIN_PAGE_HEADING = By.XPATH, ".//h1[contains(text(), 'Соберите бургер')]"
    # Логотип "Stellar Burgers"
    CONSTRUCTOR_LOGO = By.XPATH, ".//div/a[@href='/']"
    # Кнопка "Выход" в личном кабинете
    LOGOUT_BUTTON = By.XPATH, ".//button[contains(text(), 'Выход')]"
    # Переключатель с названием "Соусы" в конструкторе
    CONSTRUCTOR_SAUCES_SECTION_SWITCHER = By.XPATH, ".//span[contains(text(), 'Соусы')]"
    # Переключатель с названием "Начинки" в конструкторе
    CONSTRUCTOR_TOPPINGS_SECTION_SWITCHER = By.XPATH, ".//span[contains(text(), 'Начинки')]"
    # Переключатель с названием "Булки" в конструкторе
    CONSTRUCTOR_BUNS_SECTION_SWITCHER = By.XPATH, ".//span[contains(text(), 'Булки')]"
    # Заголовок раздела "Соусы" в конструкторе
    CONSTRUCTOR_SAUCES_SECTION_HEADING = By.XPATH, ".//h2[contains(text(), 'Соусы')]"
    # Заголовок раздела "Начинки" в конструкторе
    CONSTRUCTOR_TOPPINGS_SECTION_HEADING = By.XPATH, ".//h2[contains(text(), 'Начинки')]"
    # Заголовок раздела "Булки" в конструкторе
    CONSTRUCTOR_BUNS_SECTION_HEADING = By.XPATH, ".//h2[contains(text(), 'Булки')]"
    # Флюоресцентная булка R2-D3
    BUN = By.XPATH, ".//img[@alt='Флюоресцентная булка R2-D3']"
    # Биокотлета из марсианской Магнолии
    PATTY = By.XPATH, ".//img[@alt='Биокотлета из марсианской Магнолии']"
    # Соус фирменный Space Sauce
    SAUCE = By.XPATH, ".//img[@alt='Соус фирменный Space Sauce']"
    # Поп-ап, подтверждающий успешно сделанный заказ
    CONFIRMATION_POPUP = By.XPATH, ".//div[@class='Modal_modal__contentBox__sCy8X pt-30 pb-30']"
