from faker import Faker


# Класс для генерации рандомных тестовых данных
class GeneratedData:

    def generate_random_name():
        fake = Faker()
        name = fake.name()
        return name

    def generate_random_email():
        fake = Faker()
        email = fake.email()
        return email

    def generate_random_password(length=6):
        fake = Faker()
        password = fake.password(length)
        return password

    def generate_wrong_password(length=5):
        fake = Faker()
        wrong_password = fake.password(length)
        return wrong_password
