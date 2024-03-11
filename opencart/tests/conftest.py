import pytest
import os

from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()
OPENCART_URL = os.getenv("OPENCART_LINK")


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--drivers", default=os.path.expanduser("~/Downloads/drivers"))


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception("Driver not supported")

    request.addfinalizer(driver.quit)

    # driver.maximize_window()

    driver.get(OPENCART_URL)

    return driver
