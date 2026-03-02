"""
@package utilities

Extra step in "assert". Instead of calling assert directly we use custom method like this to check the result multiple times
This will make sure to not stop execution of script directly like "assert" does

Example:
    self.check_point.markFinal("Test name", result, "Message"
"""

import logging
from Base.custom_selenium_driver import CustomSeleniumDriver
import Utilities.custom_logger as CL

class TestStatus(CustomSeleniumDriver):
    custom_logger = CL.customLogger(logging.DEBUG)

    def __init__(self, driver):

        super(TestStatus, self).__init__(driver)
        self.resultList = []        #Will keep track of all the results

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.custom_logger.info("## Verification successful :: "+resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.custom_logger.error("## Verification Failed :: " + resultMessage)
            else:
                self.resultList.append("FAIL")
                self.custom_logger.error("## Verification Failed :: " + resultMessage)
        except AssertionError:
            self.resultList.append("FAIL")
            self.custom_logger.error("## Exception occurred !!!")


    #this will just keep track of them
    def mark(self, result, resultMessage):
        self.setResult(result, resultMessage)

    #this will do the final assertions
    def markFinal(self, testName, result, resultMessage):
        self.setResult(result, resultMessage)

        if "FAIL" in self.resultList:
            self.custom_logger.error(testName+"## Test Failed")
            self.resultList.clear()
            assert True == False
        else:
            self.custom_logger.error(testName + "## Test Successful")
            self.resultList.clear()
            assert True == True
