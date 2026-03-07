"""
This Page will consist all the methods related to card details
"""
from Base.base_page import BasePageClass
from pynput.keyboard import Key, Controller
import time

class CardDetailsPage(BasePageClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.custom_logger.debug("Initializing Class: CardDetailsPage")

    #Fake card details
    card_number = "5186001700008785"
    expiry_date = "05 28"
    security_code = "007"

    #Locators
    _loc_CdInfo = '//*[contains(text(),"Payment Information")]//parent::div'
    _loc_cardNum = '//div[@id="card-number"]//input'
    _loc_expiryDate = '//div[@id="card-expiry"]//input'
    _loc_securityCode = '//div[@id="card-cvc"]//input'
    _loc_buyBttn = '//form[@id="checkout-form"]//button[contains(@class, "submit checkout-button")]'
    _loc_invalidCheck = '//div[@id="header19"]//p[contains(@class , "dynamic-text")]//button'

    def confirmCdPage(self):
        #first scroll the element in view
        self.webBrowserScroll(locator=self._loc_CdInfo,locatorType="xpath")
        element = self.isElementDisplayed(locator=self._loc_CdInfo,locatorType="xpath")
        if element:
            self.custom_logger.info("Enter card details")
        else:
            self.custom_logger.warning("Element not in View")
        return element

    def enterCardDetails(self):
        validity = None
        self.mouseHoverAction(locator=self._loc_cardNum,locatorType="xpath",actionType="click")
        self.keyboardType(data=self.card_number)
        time.sleep(1)
        self.mouseHoverAction(locator=self._loc_expiryDate, locatorType="xpath", actionType="click")
        self.keyboardType(data=self.expiry_date)
        time.sleep(1)
        self.mouseHoverAction(locator=self._loc_securityCode, locatorType="xpath", actionType="click")
        self.keyboardType(data=self.security_code)
        time.sleep(1)
        self.elementClick(locator=self._loc_buyBttn, locatorType="xpath")
        self.custom_logger.info("Card details entered and submitted")

        validity = self.waitForElement(locator=self._loc_invalidCheck, locatorType="xpath")
        if validity:
            self.takeScreenShot(resultMessage="Invalid Card details")
        else:
            self.custom_logger.info("Card details entered and submitted")
        return validity



