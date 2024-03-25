from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement


class Page:

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver

    def find_element(
        self, by: str = "id", value: str | dict | None = None
    ) -> WebElement:
        return self.driver.find_element(by=by, value=value)

    def click_element(self, element: WebElement) -> None:
        element.click()

    def send_keys(self, element: WebElement, value: str) -> None:
        element.send_keys(value)

    def press_keycode(self, keycode: int) -> None:
        self.driver.press_keycode(keycode)
