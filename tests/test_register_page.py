import random
import allure
from models.register import RegisterUserModel
from fixtures.constants import RegNotice


class TestRegisterPage:
    @allure.feature("register page")
    @allure.story("Successful registration with valid data.")
    def test_valid_registration(self, app):
        """
        Successful registration with valid data.
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        app.register_page.register_user(data=data)
        assert app.register_page.success_log_in_text() == RegNotice.LOG_IN

    @allure.feature("register page")
    @allure.story("Registration with different Password and Password confirmation.")
    def test_invalid_password(self, app):
        """
        Registration with different Password and Password confirmation.
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        data.password_2 = random.randint(100, 10000)
        app.register_page.register_user(data=data)
        assert app.register_page.error_text() == RegNotice.ERROR_PASSWORD

    @allure.feature("register page")
    @allure.story("Registration with an invalid email.")
    def test_invalid_email(self, app):
        """
        Registration with an invalid email.
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        data.email = data.domain
        app.register_page.register_user(data=data)
        assert app.register_page.success_log_in_text() != RegNotice.LOG_IN

    @allure.feature("register page")
    @allure.story("Registration with an incorrect age (under 18).")
    def test_invalid_age(self, app):
        """
        Registration with an incorrect age (under 18).
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        data.age = random.randint(0, 17)
        app.register_page.register_user(data=data)
        assert app.register_page.error_text() == RegNotice.ERROR_AGE

    @allure.feature("register page")
    @allure.story("Registration with a password consisting only of numbers.")
    def test_password_is_numeric(self, app):
        """
        Registration with a password consisting only of numbers.
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        data.password_1, data.password_2 = "04725596632", "04725596632"
        app.register_page.register_user(data=data)
        assert app.register_page.error_text() == RegNotice.ERROR_PASSWORD_NUMERIC

    @allure.feature("register page")
    @allure.story("Registration with a simple/common password.")
    def test_password_is_common(self, app):
        """
        Registration with a simple/common password.
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        data.password_1, data.password_2 = "password", "password"
        app.register_page.register_user(data=data)
        assert app.register_page.error_text() == RegNotice.ERROR_PASSWORD_COMMON

    @allure.feature("register page")
    @allure.story("Successful registration with not all fields filled in.")
    def test_valid_registration_incomplete_data(self, app):
        """
        Successful registration with not all fields filled in.
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        data.firstname = None
        data.email = None
        app.register_page.register_user(data=data)
        assert app.register_page.success_log_in_text() == RegNotice.LOG_IN

    @allure.feature("register page")
    @allure.story("Re-registration with an existing username in the database.")
    def test_re_registration(self, app):
        """
        Re-registration with an existing username in the database.
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        data.user = "qwerty"
        app.register_page.register_user(data=data)
        assert app.register_page.error_text() == RegNotice.ERROR_RE_REG
