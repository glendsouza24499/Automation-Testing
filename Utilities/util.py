"""
All commonly used utilities should be implemented in this class

usage Example:
    name = self.util.getUniqueName()
"""
import random, string, time, traceback, logging
import Utilities.custom_logger as CL

class Util(object):
    custom_logger = CL.customLogger(logging.DEBUG)

    def sleep(self, sec, info=""):
        """
        Put the program to wait for the specified amount of time
        """
        if info is not None:
            self.custom_logger.info("Wait :: '"+str(sec)+"' seconds for "+info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def getAlphaNumeric(self, length, typeAN='letters'):
        """
        Get random strong of characters
        :param length:  Length of string, number of characters string should have
        :param typeAN: Type of characters string should have Default is letters
        Provide lower/upper/digits for different types
        """
        alpha_num = ''
        if typeAN == 'lower':
            case = string.ascii_lowercase
        elif typeAN == 'upper':
            case = string.ascii_uppercase
        elif typeAN == 'digits':
            case = string.digits
        elif typeAN == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def getUniqueName(self, charCount=10):
        """
        Get unique name uses above method
        """
        return self.getAlphaNumeric(length=charCount, typeAN='lower')

    def getUniqueNameList(self, listSize=5, itemLength=None):
        """
        Get list pf valid email ids

        :param listSize: NUmber of email ids. Default is 5
        :param itemLength: It should be a list containing number of items equal to the listSize. This determines the length of each item in the list
        :return:
        """
        nameList = []
        for i in range(0, listSize):
            nameList.append(self.getUniqueName(itemLength[i]))

        return nameList


    def verifyTextContains(self, actualText, expectedText):
        """
        Verify that the actual text contains in the expected text
        """
        self.custom_logger.info("Actual Text From Application Web UI --> :: " + actualText)
        self.custom_logger.info("Expected Text From Application Web UI --> :: " + expectedText)
        if expectedText.lower() in actualText.lower():
            self.custom_logger.info("## verifyTextContains Passed!!!")
            return True
        else:
            self.custom_logger.info("## verifyTextContains Failed!!!")
            return False

    def verifyTextMatch(self, actualText, expectedText):
        """
        Verify that the actual text matches the expected text
        """
        self.custom_logger.info("Actual Text From Application Web UI--> :: " + actualText)
        self.custom_logger.info("Expected Text From Application Web UI--> :: " + expectedText)
        if expectedText.lower() == actualText.lower():
            self.custom_logger.info("## verifyTextMatch Passed!!!")
            return True
        else:
            self.custom_logger.info("## verifyTextMatch Failed!!!")
            return False

    def verifyListMatch(self, expectedList, actualList):
        """
        Verify that the actual list matches the expected list
        """
        return set(expectedList) == set(actualList)

    def verifyListContains(self, expectedList, actualList):
        """
        Verify actual list contains elements of the expected list
        """
        length = len(expectedList)
        for i in range(0, length):
            if expectedList[i] not in actualList[i]:
                return False
        else:
            return True