from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage
from fixtures.constants import LoginNotice


class OrderPage(BasePage):
    LOGIN_LINK = (By.XPATH, "//li[@class='nav-item'][2]/a[@class='nav-link']")
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//form[@class='form-horizontal']/input[@class='form-control']")
    INDEX_TEXT = (By.CLASS_NAME, "card")
    LOGIN_TEXT = (By.CLASS_NAME, "dropdown-toggle")
    SEE_ACCOMMODATION = (By.CLASS_NAME, "btn-danger")
    BUTTON = (By.CLASS_NAME, "btn-danger")
    BASKET_LINK = (By.XPATH, "//a[@class='dropdown-item'][2]")
    BOOKED_TEXT = (By.CLASS_NAME, "basket_summary")

    def open_login_page(self):
        self.open_page(self.app.url)
        self.click(locator=self.LOGIN_LINK)

    def login(self):
        self.fill(locator=self.USERNAME_FIELD, value=LoginNotice.login)
        self.fill(locator=self.PASSWORD_FIELD, value=LoginNotice.password)
        self.click(locator=self.LOGIN_BUTTON)

    def success_log_in_text(self) -> str:
        element = self.text(locator=self.LOGIN_TEXT)
        return element

    def click_button_see_accommodation(self):
        self.click(locator=self.SEE_ACCOMMODATION)

    def find_button_more(self) -> str:
        element = self.text(locator=self.BUTTON)
        return element

    def click_button_more(self):
        self.click(locator=self.BUTTON)

    def find_button_book(self) -> str:
        element = self.text(locator=self.BUTTON)
        return element

    def click_button_book(self):
        self.click(locator=self.BUTTON)

    def open_basket_page(self):
        self.click(locator=self.LOGIN_TEXT)
        self.click(locator=self.BASKET_LINK)

    def check_book(self) -> str:
        element = self.text(locator=self.BOOKED_TEXT)
        return element
