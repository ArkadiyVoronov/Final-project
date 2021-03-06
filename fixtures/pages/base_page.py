from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, app):
        self.app = app

    def _find_element(self, locator, wait_time=5):
        element = WebDriverWait(self.app.driver, wait_time) \
            .until(expected_conditions.presence_of_element_located(locator),
                   message=f"Can't find element by locator {locator}")
        return element

    def _find_elements(self, locator, wait_time=5):
        elements = WebDriverWait(self.app.driver, wait_time) \
            .until(expected_conditions.presence_of_all_elements_located(locator),
                   message=f"Can't find elements by locator {locator}")
        return elements

    def click(self, locator, wait_time=20):
        element = self._find_element(locator, wait_time)
        element.click()

    def clear(self, locator, wait_time=20):
        element = self._find_element(locator, wait_time)
        element.clear()

    def fill(self, locator, value: str, wait_time=20):
        element = self._find_element(locator, wait_time)
        if value:
            element.send_keys(value)

    def text(self, locator, wait_time=20) -> str:
        element = self._find_element(locator, wait_time)
        return element.text

    def open_page(self, url: str):
        self.app.driver.get(url)
