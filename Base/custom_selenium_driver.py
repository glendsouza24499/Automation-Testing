import time
import os
from traceback import print_stack
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import logging
import Utilities.custom_logger as CL


class CustomSeleniumDriver:

    custom_logger = CL.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getElement(self,locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()       #To make sure you compare locators sent her without case sensitivity issues
            byType = self.getLocatorType(locatorType)
            element = self.driver.find_element(byType,locator)
            self.custom_logger.info("Element found")
        except NoSuchElementException:
            self.custom_logger.warning("Element not found")
            self.custom_logger.debug("*" * 10 + "Error in execution of login_test.py" + "*" * 10)
        return element

    def getLocatorType(self, locatorType):
        locatorType = locatorType.lower()   #To make sure you compare locators sent her without case sensitivity issues

        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.custom_logger.warning("Locator Type "+locatorType+" not correct/supported")
            self.custom_logger.debug("*" * 10 + "Error in execution of login_test.py" + "*" * 10)
        return False

    def singleElementPresenceCheck(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.custom_logger.info("Element Presence Check : Element Found")
                return True
            else:
                self.custom_logger.info("Element Presence Check : Element Not Found")
                self.custom_logger.debug("*" * 10 + "Error in execution of login_test.py" + "*" * 10)
                return False
        except NoSuchElementException:
            self.custom_logger.critical("Element Presence Check Except Block :  Element Not Found")
            self.custom_logger.debug("*" * 10 + "Critical Error in execution of login_test.py" + "*" * 10)
            return False

    def listOfElementsPresenceCheck(self, locator, locatorType):
        try:
            elementsList = self.driver.find_elements(locatorType, locator)
            if len(elementsList) > 1:
                self.custom_logger.info("List of Elements Presence Check : List of Elements Found")
                return True
            else:
                self.custom_logger.info("List of Elements Presence Check : List of Elements Not Found")
                self.custom_logger.debug("*" * 10 + "Error in execution of login_test.py" + "*" * 10)
                return False
        except NoSuchElementException:
            self.custom_logger.critical("List of Elements Presence Check Except block :  List of Elements Not Found")
            self.custom_logger.debug("*" * 10 + "Critical Error in execution of login_test.py" + "*" * 10)
            return False

    #This will make elements explicitly wait before getting an element
    def waitForElement(self, locator, locatorType='id', timeout=10, pollFrequency=0.5):
        element = None
        try:
            locator_Type = self.getLocatorType(locatorType)
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency, ignored_exceptions=[NoSuchElementException,
                                                                                   ElementNotVisibleException,
                                                                                   ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((locator_Type, locator)))

            self.custom_logger.info("Wait for maximum :: " + str(timeout) + " :: seconds for element to be visible")
            self.custom_logger.info("Element appeared on the webpage")
        except NoSuchElementException:
            self.custom_logger.warning("Element not appeared on the webpage")
            self.custom_logger.debug("*" * 10 + "Error in execution of login_test.py" + "*" * 10)
            print_stack()
        return element

    #This will click the element
    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.custom_logger.info("Element click was successful:. Locator"+locator+" Locator Type: "+locatorType)
        except NoSuchElementException:
            self.custom_logger.warning("Element not clicked on the webpage:. Locator:"+locator+" Locator type: "+locatorType)
            self.custom_logger.debug("*" * 10 + "Error in execution of login_test.py" + "*" * 10)
            print_stack()

    #This will send text to element
    def sendTextToElement(self,data , locator, locatorType="id"):
        try:
            element = self.driver.find_element(locatorType, locator)
            element.clear()       #clear the text field before sending data
            element.send_keys(data)
            self.custom_logger.info("Element text was added successful:. Locator" + locator + " Locator Type: " + locatorType)
        except NoSuchElementException:
            self.custom_logger.warning("Element text was not added on the webpage:. Locator:" + locator + " Locator type: " + locatorType)
            self.custom_logger.debug("*" * 10 + "Error in execution of login_test.py" + "*" * 10)
            print_stack()

    #To take a screenshot of the current open webpage
    def takeScreenShot(self, resultMessage):
        fileName = resultMessage + "." + str(round(time.time()*1000)) + ".png"
        screenshotDir = "../Screenshots/"   #this will go back one directory
        relativeFileName = screenshotDir + fileName
        currentDir = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDir, relativeFileName)
        destinationDir = os.path.join(currentDir, screenshotDir)

        try:
            #this makes sure if the director Screenshots doesn't exist it will create it
            if not os.path.exists(destinationDir):
                os.makedirs(destinationDir)
                self.driver.save_screenshot(destinationFile)
                self.custom_logger.info("Screenshot saved successfully to : " + destinationFile)
            else:
                self.driver.save_screenshot(destinationFile)
                self.custom_logger.info("Screenshot saved successfully to : " + destinationFile)
        except NotADirectoryError:
            self.custom_logger.critical("Exception error : custom_selenium_driver.py-> takeScreenShot()")
            print_stack()

    #to get the title of the driver page
    def getTitle(self):
        return self.driver.title
