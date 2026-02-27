from selenium.webdriver.common.by import By
from Base.custom_selenium_driver import CustomSeleniumDriver
import logging
import Utilities.custom_logger as CL
import time

class LoginPage(CustomSeleniumDriver):

    custom_logger = CL.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)    #sending the driver to the super i.e.CustomSeleniumDriver
        self.driver = driver

#Creating all locators for elements
    #locators
    _loginLink = '//a[@href="/login"]'
    _emailField = '//input[@id="email"]'
    _passwordField = '//input[@id="login-password"]'
    _loginBtn = '//button[@id="login"]'
    _confirmLoggedIn = '//button[@id="dropdownMenu1"]'
    _failedLogInConfirm = '//span[@id="incorrectdetails"]'

#Creating all elements
    # Instead of calling the login link again and again, this will make the locator "_loginLink" available to be found throughout the method
    def clickLoginLink(self):
        #return self.driver.find_element(By.XPATH, self._loginLink)
        self.elementClick(locator=self._loginLink,locatorType="xpath")

    # Instead of calling the email field again and again, this will make the locator "_emailField" available to be found throughout the method
    def enterInEmailField(self, username):
        #return self.driver.find_element(By.XPATH, self._emailField)
        self.sendTextToElement(data=username, locator=self._emailField, locatorType="xpath")

    # Instead of calling the password field again and again, this will make the locator "_passwordField" available to be found throughout the method
    def enterInPasswordField(self, password):
        #return self.driver.find_element(By.XPATH, self._passwordField)
        self.sendTextToElement(data=password, locator=self._passwordField, locatorType="xpath")

    # Instead of calling the login or submit button again and again, this will make the locator "_passwordField" available to be found throughout the method
    def clickLoginBtn(self):
        self.elementClick(locator=self._loginBtn,locatorType="xpath")

    def validateLogIn(self):
        #Check after click submit of it failed
        confirm_failed_login = self.singleElementPresenceCheck(locator=self._failedLogInConfirm, locatorType="xpath")
        if confirm_failed_login is False:
            # Called only if login details entered were correct and it passed through
            confirm_login = self.singleElementPresenceCheck(locator=self._confirmLoggedIn, locatorType="xpath")
            if confirm_login is True:
                self.custom_logger.info("Login Successful")
                self.custom_logger.debug("*" * 20 + "End of login_test.py execution" + "*" * 20)
            else:
                self.custom_logger.info("Login Confirmation element not found")
                self.custom_logger.debug("*" * 20 + "End of login_test.py execution" + "*" * 20)
        else:
            print("Login Failed : Please check your login details or internet connection")
            self.custom_logger.info("Login Failed : Please check your login details or internet connection")
            self.custom_logger.debug("*" * 20 + "End of login_test.py execution" + "*" * 20)


# #PART 1#Creating all action methods for elements
#     def goToLoginPage(self):
#         self.clickLoginLink().click()     #.clickLoginLink() will get the element and then .click() will perform click action on it
#
#     def enterInEmailField(self, username):
#         self.getEmailField().send_keys(username)    #.getEmailField() will find the element and then .send_keys() will enter text in the field
#
#     def enterInPasswordField(self, password):
#         self.getPasswordField().send_keys(password)    #.getPasswordField() will find the element and then .send_keys() will enter text in the field
#
#     def clickLoginBtn(self):
#         self.getLoginBtn().click()      #.getLoginBtn() will get the element and then .click() will perform click action on it


#This function will be called in the test file
    def login(self,username,password):
        self.clickLoginLink()

        self.enterInEmailField(username)

        self.enterInPasswordField(password)

        time.sleep(2)
        self.clickLoginBtn()
        time.sleep(2)
        self.validateLogIn()
        time.sleep(3)