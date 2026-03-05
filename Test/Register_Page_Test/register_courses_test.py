"""
This test is to register for a course from ALL COURSES page, enroll for that course and then enter invalid card details for error messages
"""

from Pages.AllCourses_Page.all_course_class import AllCourseClass
from Pages.Register_Page.register_course_page import RegisterPage
from Pages.Payment_Page.card_details_page import CardDetailsPage
from Pages.Home_Page.login_page import LoginPage
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp")
class RegisterCoursesTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.driver = oneTimeSetUp

    @pytest.mark.run(order=1)
    def test_registerCourses(self):
        #Step 1 Login and verify confirmation:
        callLoginPage = LoginPage(self.driver)
        validate_login = callLoginPage.login(username="test@email.com", password="abcabc")
        #Step 2 if Login is valid navigate to ALL COURSES Page
        if validate_login:
            callAllCoursesPage = AllCourseClass(self.driver)
            allCoursePage_Class = callAllCoursesPage.clickAllCourses()
            #Step 3 After navigating to ALL COURSES Page search for a course and press enter
            if allCoursePage_Class:
                findCourse = callAllCoursesPage.searchCourse(data="JavaScript")
                if findCourse:
                    # Step 4 After course is found, click enroll/register button
                    register_page = RegisterPage(self.driver)
                    confirm_regPage = register_page.confirmRegisterPage()
                    if confirm_regPage:
                        register_page.enrollACoursePage()

    @pytest.mark.run(order=2)
    def test_invalidDetails(self):
        # Step 5 After clicking enroll button check for payment page
        cardDet_Page = CardDetailsPage(self.driver)
        confPay_Page = cardDet_Page.confirmCdPage()
        #Step 6 Enter invalid card details
        if confPay_Page:
            cardDet_Page.enterCardDetails()


if __name__ == "__main__":
    unittest.main(verbosity=2)