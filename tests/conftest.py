import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService

from utils.android_utils import android_get_desired_capabilities


APPIUM_PORT = 4723
APPIUM_HOST = "127.0.0.1"


@pytest.fixture(scope="session")
def appium_service():
    service = AppiumService()
    service.start(
        args=["--address", APPIUM_HOST, "-p", str(APPIUM_PORT), "--base-path", "/wd/hub"],
        timeout_ms=20000,
    )
    yield service
    print("stoped")
    service.stop()


@pytest.fixture(scope="session")
def driver(appium_service):
    android_driver = webdriver.Remote(
        f"http://{APPIUM_HOST}:{APPIUM_PORT}/wd/hub",
        options=UiAutomator2Options().load_capabilities(
            android_get_desired_capabilities()
        ),
    )
    yield android_driver
    android_driver.quit()
