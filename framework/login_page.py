from appium.webdriver.common.appiumby import AppiumBy
from .page import Page

TO_LOGIN_PAGE_BUTTON_ID = "com.ajaxsystems:id/authHelloLogin"
EMAIL_FIELD_ID = "com.ajaxsystems:id/authLoginEmail"
PASSWORD_FIELD_ID = "com.ajaxsystems:id/authLoginPassword"
LOGIN_BUTTON_ID = "com.ajaxsystems:id/authLogin"


class LoginPage(Page):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_page(self):
        el = self.find_element(by=AppiumBy.ID, value=TO_LOGIN_PAGE_BUTTON_ID)
        self.click_element(el)

    def login(self, email: str, password: str) -> None:
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()

    def set_email(self, email: str) -> None:
        el = self.find_element(by=AppiumBy.ID, value=EMAIL_FIELD_ID)
        self.send_keys(el, email)

    def set_password(self, password):
        el = self.find_element(by=AppiumBy.ID, value=PASSWORD_FIELD_ID)
        self.send_keys(el, password)

    def click_login_button(self):
        el = self.find_element(by=AppiumBy.ID, value=LOGIN_BUTTON_ID)
        self.click_element(el)
