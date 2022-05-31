import random

from models.register import RegisterUserModel
from fixtures.constants import RegNotice


class TestRegisterPage:
    def test_valid_registration(self, app):
        """
        Successful registration with valid data.
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        app.register_page.register_user(data=data)
        assert app.register_page.success_log_in_text() == RegNotice.LOG_IN

    def test_invalid_password(self, app):
        """
        Registration with different Password and Password confirmation.
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        data.password_2 = random.randint(100, 10000)
        app.register_page.register_user(data=data)
        assert app.register_page.error_text() == RegNotice.ERROR_PASSWORD

    def test_invalid_email(self, app):
        """
        Registration with an invalid email.
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        data.email = data.domain
        app.register_page.register_user(data=data)
        assert app.register_page.success_log_in_text() != RegNotice.LOG_IN

    def test_invalid_age(self, app):
        """
        Registration with an incorrect age (under 18).
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        data.age = random.randint(0, 17)
        app.register_page.register_user(data=data)
        assert app.register_page.error_text() == RegNotice.ERROR_AGE

    def test_password_is_numeric(self, app):
        """
        Registration with a password consisting only of numbers.
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        data.password_1, data.password_2 = "04725596632", "04725596632"
        app.register_page.register_user(data=data)
        assert app.register_page.error_text() == RegNotice.ERROR_PASSWORD_NUMERIC

    def test_password_is_common(self, app):
        """
        Registration with a simple/common password.
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        data.password_1, data.password_2 = "password", "password"
        app.register_page.register_user(data=data)
        assert app.register_page.error_text() == RegNotice.ERROR_PASSWORD_COMMON

    def test_re_registration(self, app):
        """
        Re-registration with an existing username in the database.
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        data.user = "qwerty"
        app.register_page.register_user(data=data)
        assert app.register_page.error_text() == RegNotice.ERROR_RE_REG
