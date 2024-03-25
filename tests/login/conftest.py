from os import getenv

import pytest
from appium.webdriver.extensions.android.nativekey import AndroidKey

from framework.login_page import LoginPage


EMAIL = getenv("EMAIL")
PASSWORD = getenv("PASSWORD")

LOGIN_PAGE_ID = "com.ajaxsystems:id/auth_redesign_container"
AFTER_LOGIN_PAGE_ID = "com.ajaxsystems:id/coordinator"


@pytest.fixture(scope="function")
def user_login_fixture(driver):
    driver.implicitly_wait(10)
    page = LoginPage(driver)
    page.go_to_page()
    yield page
    page.press_keycode(AndroidKey.BACK)
