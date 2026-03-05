import time

import pytest
from Base.webdriver_factory import WebdriverFactory
from Pages.Home_Page.login_page import LoginPage
import logging
import Utilities.custom_logger as CL

custom_logger = CL.customLogger(logging.DEBUG)

@pytest.fixture()
def setUp():
    print("Running confTest setup before every method")
    yield
    print("Running confTest teardown after every method")

@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    custom_logger.debug("*" * 20 + "Start of execution" + "*" * 20)
    custom_logger.info("Running conftest.py oneTimeSetUp setup")
    wdf = WebdriverFactory(browser)
    driver = wdf.getWebdriverInstance()
    # if browser == "chrome":
    #     driver = webdriver.Chrome()
    #     driver.maximize_window()
    #     driver.implicitly_wait(3)
    #     driver.get(baseURL)
    #     print("Running test on chrome")
    # else:
    #     driver = webdriver.Firefox()
    #     driver.maximize_window()
    #     driver.implicitly_wait(3)
    #     driver.get(baseURL)
    #     print("Running test on firefox")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    custom_logger.info("Running conftest.py oneTimeSetUp teardown")
    custom_logger.debug("*" * 20 + "End of execution" + "*" * 20)
    time.sleep(3)
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")