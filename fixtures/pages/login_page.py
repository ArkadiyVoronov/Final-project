import logging
from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage
from fixtures.constants import LoginNotice

logger = logging.getLogger("TravelMarket")


class LoginPage(BasePage):
    LOGIN_LINK = (By.XPATH, "//li[@class='nav-item'][2]/a[@class='nav-link']")
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//form[@class='form-horizontal']/input[@class='form-control']")
    LOGIN_TEXT = (By.CLASS_NAME, "dropdown-toggle")
    ERROR_TEXT = (By.CLASS_NAME, "errorlist")
    SING_IN = (By.XPATH, "//li[@class='nav-item'][2]/a[@class='nav-link']")

    def open_login_page(self):
        self.open_page(self.app.url)
        self.click(locator=self.LOGIN_LINK)

    def entry_data_login(self):
        self.fill(locator=self.USERNAME_FIELD, value=LoginNotice.login)
        self.fill(locator=self.PASSWORD_FIELD, value=LoginNotice.password)
        self.click(locator=self.LOGIN_BUTTON)

    def success_log_in_text(self) -> str:
        element = self.text(locator=self.LOGIN_TEXT)
        return element

    def error_text(self) -> str:
        element = self.text(locator=self.ERROR_TEXT)
        return element

    def index_page_text(self) -> str:
        element = self.text(locator=self.SING_IN)
        return element
