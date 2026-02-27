import pytest
from selenium import webdriver

@pytest.fixture()
def setUp():
    print("Running confTest setup before every method")
    yield
    print("Running confTest teardown after every method")

@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    baseURL = "https://www.letskodeit.com/"
    print("Running confTest setUp once")
    if browser == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        print("Running test on chrome")
    else:
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        print("Running test on firefox")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running confTest tearDown once")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")