import logging
from fixtures.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from models.register import RegisterUserModel

logger = logging.getLogger("TravelMarket")


class RegisterPage(BasePage):
    LOGIN_LINK = (By.XPATH, "//li[@class='nav-item'][2]/a[@class='nav-link']")
    REGISTER_LINK = (By.CLASS_NAME, "btn-round")
    REGISTER_BUTTON = (By.XPATH, "//input[@value='register']")
    USERNAME = (By.NAME, "username")
    FIRST_NAME = (By.NAME, "first_name")
    PASSWORD_1 = (By.NAME, "password1")
    PASSWORD_2 = (By.NAME, "password2")
    EMAIL = (By.NAME, "email")
    AGE = (By.NAME, "age")
    LOG_IN_TEXT = (By.CLASS_NAME, "h2")
    ERROR_TEXT = (By.XPATH, "//ul[@class='errorlist']/li")

    def open_register_page(self):
        self.open_page(self.app.url)
        self.click(locator=self.LOGIN_LINK)
        self.click(locator=self.REGISTER_LINK)

    def register_user(self, data: RegisterUserModel):
        logger.info(f"Registration data: user: {data.user}, firstname: {data.firstname}, password: {data.password_1}, "
                    f"password: {data.password_2}, email: {data.email}, age: {data.age}")
        self.fill(locator=self.USERNAME, value=data.user)
        self.fill(locator=self.FIRST_NAME, value=data.firstname)
        self.fill(locator=self.PASSWORD_1, value=data.password_1)
        self.fill(locator=self.PASSWORD_2, value=data.password_2)
        self.fill(locator=self.EMAIL, value=data.email)
        self.clear(locator=self.AGE)
        self.fill(locator=self.AGE, value=data.age)
        self.click(locator=self.REGISTER_BUTTON)

    def success_log_in_text(self) -> str:
        element = self.text(locator=self.LOG_IN_TEXT)
        return element

    def error_text(self) -> str:
        error = self.text(locator=self.ERROR_TEXT)
        return error
