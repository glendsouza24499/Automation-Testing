"""
This page will consist of method for "ALL COURSES" page
"""

from Base.base_page import BasePageClass
import time


class AllCourseClass(BasePageClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.custom_logger.debug("Initializing Class: AllCourseClass")


    #Locators
    loc_selectAllCourses = "//a[@href='/courses']"
    loc_searchBar = '//input[@id="search"]'
    loc_searchBttn = '//form[@id="search"]/div/button'
    loc_courseToSelect = '//div[@id="course-list"]/div'

    #This method will be used after login is completed to navigate to "All Courses" page
    def clickAllCourses(self):
        element = self.elementClick(locator=self.loc_selectAllCourses,locatorType="xpath")
        if element:
            self.custom_logger.info("Navigating to ALL COURSES page")
        else:
            self.custom_logger.info("Failed to navigate to ALL COURSES page")
        return element

    #This method is used to search for courses on the provided search bar of the page
    def searchCourse(self, data=None):
        search_bar = self.isElementDisplayed(locator=self.loc_searchBar,locatorType="xpath")
        confirmReturn = None
        if search_bar:
            self.custom_logger.info("Sending text "+data+" to search bar")
            self.sendTextToElement(locator=self.loc_searchBar, locatorType="xpath",data=str(data))
            time.sleep(2)
            self.custom_logger.info("Performing Mouse hover action to get "+data)
            self.mouseHoverAction(locator=self.loc_searchBttn, locatorType="xpath")
            time.sleep(2)
            courseList = self.getElementList(locator=self.loc_courseToSelect,locatorType="xpath")
            if len(courseList) == 1:
                self.elementClick(locator=self.loc_courseToSelect,locatorType="xpath")
                self.custom_logger.info("Successfully found " + data + " course element and selected it.")
                time.sleep(2)
                confirmReturn = True
                return confirmReturn
            else:
                self.custom_logger.warning("Failed to confirm registration of a course")
                confirmReturn = False
                return confirmReturn
        else:
            self.custom_logger.warning("Failed to confirm registration of a course")
            confirmReturn = False
            return confirmReturn