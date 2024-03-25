import logging

import pytest
from appium.webdriver.common.appiumby import AppiumBy

import conftest

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


@pytest.mark.parametrize(
    "email,password,expected_page_id",
    (
        ("wrong_email", "wrong_password", conftest.LOGIN_PAGE_ID),
        (conftest.EMAIL, conftest.PASSWORD, conftest.AFTER_LOGIN_PAGE_ID),
    ),
)
def test_user_login(
    user_login_fixture, email: str, password: str, expected_page_id: str
):
    logger.info(f"Test login: {email=}, {password=}")
    user_login_fixture.login(email, password)
    assert user_login_fixture.find_element(by=AppiumBy.ID, value=expected_page_id)
