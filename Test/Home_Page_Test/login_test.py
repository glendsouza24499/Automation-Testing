from selenium import webdriver
from Pages.Home_Page.login_page import LoginPage
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.driver = oneTimeSetUp

    @pytest.mark.run(order=1)
    def test_CommenceLogin(self):
        callLoginPage = LoginPage(self.driver)
        callLoginPage.login(username = "test@email.com", password = "abcabc")

#this will execute only once.
if __name__ == "__main__":
    unittest.main(verbosity=2)

#This will cause the test to execute twice, if called from CMD or terminal, but without this the pycharm cant execute the test
# callTest = LoginTest()
# callTest.test_CommenceLogin()
