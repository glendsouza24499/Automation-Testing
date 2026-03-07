"""
This page will consist all methods related to enroll/register page
"""
from Base.base_page import BasePageClass
import time

class RegisterPage(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.custom_logger.debug("Initializing Class: RegisterPage")

    #Locators
    loc_registerButton = '//button[text()="Enroll in Course"]'

    def confirmRegisterPage(self):
        self.custom_logger.info("Confirming RegisterPage is open...")
        conf_regPage = self.isElementDisplayed(locator=self.loc_registerButton,locatorType="xpath")
        if conf_regPage:
            self.custom_logger.info("RegisterPage is open")
        else:
            self.custom_logger.warning("RegisterPage is not open")
        return conf_regPage

    def enrollACoursePage(self):
        self.custom_logger.info("Click enroll/register button")
        self.elementClick(locator=self.loc_registerButton,locatorType="xpath")
        time.sleep(2)