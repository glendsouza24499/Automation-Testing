"""
In this page you implement methods that are common to all pages throughout the application

THis class should not be created as an object instance rather it should be inherited by all pages
"""
from Base.custom_selenium_driver import CustomSeleniumDriver
from traceback import print_stack
from Utilities.util import Util

class BasePageClass(CustomSeleniumDriver):

    def __init__(self, driver):
        super(BasePageClass, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verifyPageTitle(self, titleToVerify):
        try:
            actual_title = self.getTitle()
            return self.util.verifyTextContains(str(actual_title), titleToVerify)
        except:
            self.custom_logger.error("Failed to get page title")
            print_stack()
            return False