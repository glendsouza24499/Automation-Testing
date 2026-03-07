"""
@package base
use example :
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""

from selenium import webdriver
import logging
import Utilities.custom_logger as CL

class WebdriverFactory:
    custom_logger = CL.customLogger(logging.DEBUG)

    def __init__(self, browser):
        self.browser = browser

    #this will get the web drivers based on the instances on the browser configurations
    def getWebdriverInstance(self):
        baseURL = "https://www.letskodeit.com/"
        if self.browser == "chrome":
            driver = webdriver.Chrome()
            self.custom_logger.debug("Test initiated on chrome webdriver instance")
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
            self.custom_logger.debug("Test initiated on firefox webdriver instance")
        elif self.browser == "msedge":
            # set ie driver
            driver = webdriver.Edge()
            self.custom_logger.debug("Test initiated on microsoft edge webdriver instance")
        else:
            driver = webdriver.Chrome()

        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseURL)
        return driver