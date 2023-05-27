import random


# Класс для хранения тестовых данных
class Data:
    NEW_USER_NAME = "Christina Lebedeva"
    NEW_USER_EMAIL = f"christina_lebedeva_10_{random.randint(111, 999)}@ya.ru"
    NEW_USER_PASSWORD = random.randint(111111, 999999)
    NEW_WRONG_PASSWORD = random.randint(11111, 99999)

    EXISTING_USER_NAME = "Chris Swan"
    EXISTING_USER_EMAIL = "christina_lebedeva_10_575@ya.ru"
    EXISTING_USER_PASSWORD = "/mzPf(?(W]x!]!Z{pb57f#LYF2fptz"
