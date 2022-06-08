import allure
from fixtures.constants import LoginNotice


class TestLoginPage:
    @allure.feature("login page")
    @allure.story("Successful authorization with valid data.")
    def test_successful_login(self, app):
        """
        Successful authorization with valid data.
        """
        app.login_page.open_login_page()
        app.login_page.entry_data_login()
        assert app.login_page.success_log_in_text() == LoginNotice.login

    @allure.feature("login page")
    @allure.story("Authorization attempt with invalid password.")
    def test_login_with_invalid_password(self, app):
        """
        Authorization attempt with invalid password.
        """
        app.login_page.open_login_page()
        LoginNotice.password = "1234"
        app.login_page.entry_data_login()
        assert app.login_page.error_text() == LoginNotice.ERROR_LOGIN

    @allure.feature("login page")
    @allure.story("Trying to log in with a blank login.")
    def test_login_with_empty_username(self, app):
        """
        Trying to log in with a blank login.
        """
        app.login_page.open_login_page()
        LoginNotice.login = None
        app.login_page.entry_data_login()
        assert app.login_page.index_page_text() != LoginNotice.login

    @allure.feature("login page")
    @allure.story("Authorization attempt with a blank password.")
    def test_login_with_empty_password(self, app):
        """
        Authorization attempt with a blank password.
        """
        app.login_page.open_login_page()
        LoginNotice.password = None
        app.login_page.entry_data_login()
        assert app.login_page.index_page_text() != LoginNotice.login

    @allure.feature("login page")
    @allure.story("Attempting to authorize an unregistered user.")
    def test_non_existent_user(self, app):
        """
        Attempting to authorize an unregistered user.
        """
        app.login_page.open_login_page()
        LoginNotice.login = "qw"
        LoginNotice.password = "353453534"
        app.login_page.entry_data_login()
        assert app.login_page.error_text() == LoginNotice.ERROR_LOGIN

    @allure.feature("login page")
    @allure.story("Logging in with a blank login and password.")
    def test_login_with_empty_login_password(self, app):
        """
        Logging in with a blank login and password.
        """
        app.login_page.open_login_page()
        LoginNotice.login = None
        LoginNotice.password = None
        app.login_page.entry_data_login()
        assert app.login_page.index_page_text() != LoginNotice.login
