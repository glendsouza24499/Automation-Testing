
from traceback import print_stack
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from pynput.keyboard import Key, Controller
import logging
import time
import os
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
            self.custom_logger.info("Element found:. Locator"+locator+" Locator Type: "+locatorType)
        except:
            self.custom_logger.warning("Element not found:. Locator"+locator+" Locator Type: "+locatorType)
            self.custom_logger.debug("*" * 10 + "Error in execution " + "*" * 10)
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

    def singleElementPresenceCheck(self, locator, locatorType="id", element=None):
        """
        Check if a single element is present
        Either provide directly thr element itself or a combination of locator and locator type
        """
        try:
            if locator:
                element = self.getElement(locator, locatorType)

            if element is not None:
                self.custom_logger.info("Element Presence Check : Element Found")
                return True
            else:
                self.custom_logger.info("Element Presence Check : Element Not Found")
                self.custom_logger.debug("*" * 10 + "Error in execution" + "*" * 10)
                return False
        except NoSuchElementException:
            self.custom_logger.critical("Element Presence Check Except Block :  Element Not Found")
            self.custom_logger.debug("*" * 10 + "Critical Error in execution" + "*" * 10)
            return False

    def listOfElementsPresenceCheck(self, locator, locatorType):
        try:
            elementsList = self.driver.find_elements(locatorType, locator)
            if len(elementsList) > 1:
                self.custom_logger.info("List of Elements Presence Check : List of Elements Found")
                return True
            else:
                self.custom_logger.info("List of Elements Presence Check : List of Elements Not Found")
                self.custom_logger.debug("*" * 10 + "Error in execution" + "*" * 10)
                return False
        except NoSuchElementException:
            self.custom_logger.critical("List of Elements Presence Check Except block :  List of Elements Not Found")
            self.custom_logger.debug("*" * 10 + "Critical Error in execution" + "*" * 10)
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
        except :
            self.custom_logger.warning("Element not appeared on the webpage")
            self.custom_logger.debug("*" * 10 + "Error in execution " + "*" * 10)
            print_stack()
        return element

    #This will click the element
    def elementClick(self, locator, locatorType="id", element=None):
        """
        Click on an element
        Either provide directly thr element itself or a combination of locator and locator type
        """
        try:
            if element is None:
                element = self.getElement(locator=locator, locatorType=locatorType)
            element.click()
            self.custom_logger.info("Element click was successful:. Locator"+locator+" Locator Type: "+locatorType)
            return True
        except:
            self.custom_logger.warning("Element not clicked on the webpage:. Locator:"+locator+" Locator type: "+locatorType)
            self.custom_logger.debug("*" * 10 + "Error in execution of login_test.py" + "*" * 10)
            print_stack()
            return  False

    #This will send text to element
    def sendTextToElement(self,data , locator, locatorType="id", element=None, dataType=str):
        """
        send text to an element
        Either provide directly thr element itself or a combination of locator and locator type
        """
        try:
            if locator:
                element = self.getElement(locatorType=locatorType, locator=locator)
            element.clear()       #clear the text field before sending data
            element.send_keys(dataType(data))
            self.custom_logger.info("Element text was added successful:. Locator" + locator + " Locator Type: " + locatorType)
            return True
        except:
            self.custom_logger.warning("Element text was not added on the webpage:. Locator:" + locator + " Locator type: " + locatorType)
            self.custom_logger.debug("*" * 10 + "Error in execution" + "*" * 10)
            print_stack()
            return False

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

    #to get list of elements
    def getElementList(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getLocatorType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.custom_logger.info("Element list found:. Locator:"+locator+" Locator Type:"+locatorType)
        except NoSuchElementException:
            self.custom_logger.warning("Element list not found on the webpage:. Locator:"+locator+" Locator Type:"+locatorType)
        return element

    #This will get the text from and element
    def getText(self, locator, locatorType="id", element=None, info=""):
        """
        Either provide element directly or  a combination of locator and locator type
        """
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            text = element.text     #this will find the text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            elif len(text) != 0:
                self.custom_logger.info("Getting text on element :: "+ info)
                text = text.strip()
        except:
            self.custom_logger.error("Failed to get text on the element " + info)
            self.custom_logger.debug("*" * 10 + "Error in execution " + "*" * 10)
            print_stack()
            text = None
        return text

    #This will check if a element is displayed on th webpage
    def isElementDisplayed(self, locator, locatorType="id",element=None):
        """
        Check if element is displayed
        Either provide element directly or  a combination of locator and locator type
        """
        is_displayed = False
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                is_displayed = element.is_displayed()
                self.custom_logger.info("Element is displayed:. Locator:"+locator+" Locator Type:"+locatorType)
            else:
                self.custom_logger.info("Element is not displayed:. Locator:"+locator+" Locator Type:"+locatorType)
            return is_displayed
        except:
            self.custom_logger.info("Element is not found:. Locator:" + locator + " Locator Type:" + locatorType)
            self.custom_logger.error("*" * 10 + "Error in execution" + "*" * 10)
            print_stack()
            return False

    #This method is used to screen the browser
    def webBrowserScroll(self,locator,locatorType="id"):
        if locator:
            element = self.getElement(locator, locatorType)
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        else:
            self.custom_logger.warning("Enter Valid locator")

    #Mouse hover and action method
    def mouseHoverAction(self, locator, locatorType="id", element=None,actionType="move"):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            action = ActionChains(self.driver)
            if actionType == "move":
                action.move_to_element(element).click().perform()
            elif actionType == "click":
                self.driver.execute_script("arguments[0].click();", element)
            self.custom_logger.info("Mouse hover action successful:. Locator:" + locator + " Locator Type:" + locatorType)
            return True
        except:
            self.custom_logger.error("Mouse hover action failed:. Locator:" + locator + " Locator Type:" + locatorType)
            self.custom_logger.error("*" * 10 + "Error in execution " + "*" * 10)
            print_stack()
            return False

    #use keyboard to type
    def keyboardType(self, data):
        try:
            keyboard = Controller()
            keyboard.type(data)
            self.custom_logger.info("Entered data "+data+" using keyboard")
        except:
            self.custom_logger.warning("Failed to enter data using keyboard")
            self.custom_logger.error("*" * 10 + "Error in execution " + "*" * 10)
            print_stack()

    def switchIframes(self,num=None,switch=True):
        """
        Switch to iframe and then back to parent
        :param num: Number of the frame
        :param switch: Condition for frame True = iframe False = Parent
        :return: current_frame
        """
        current_frame = None
        try:
            if switch:
                if num is not None:
                    current_frame = "iframe"
                    self.driver.switch_to.frame(num)
                    self.custom_logger.info("Switched to frame:. Number:"+str(num))
                else:
                    self.custom_logger.warning("Switching Failed to frame:. Number:"+str(num))
                return current_frame
            else:
                current_frame = "parent"
                self.driver.switch_to.default_content()
                self.custom_logger.info("Switched back to parent frame")
            return current_frame
        except:
            self.custom_logger.warning("Failed switch iframes:. Number:"+str(num))
            self.custom_logger.error("*" * 10 + "Error in execution " + "*" * 10)
            print_stack()