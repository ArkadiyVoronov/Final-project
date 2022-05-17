import logging
import random
from faker import Faker

fake = Faker()


class RegisterUserModel:
    """Генерация фейковых данных для успешной регистрации."""
    def __init__(self, user: str = None, firstname: str = None, password_1: str = None, password_2: str = None,
                 email: str = None, age: str = None, domain: str = None):
        self.user = user
        self.firstname = firstname
        self.password_1 = password_1
        self.password_2 = password_2
        self.email = email
        self.age = age
        self.domain = domain

    @staticmethod
    def random():
        user = f"{fake.first_name()}{random.randint(10, 100)}"
        firstname = fake.first_name()
        password = fake.password()
        email = fake.ascii_free_email()
        age = str(random.randint(18, 100))
        domain = fake.domain_name()
        logging.info(f"user: {user}, firstname: {firstname}, password: {password}, email: {email}, age: {age}")
        return RegisterUserModel(user=user, firstname=firstname, email=email, password_1=password, password_2=password,
                                 age=age, domain=domain)
