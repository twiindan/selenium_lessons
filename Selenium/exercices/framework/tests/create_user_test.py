
from exercices.solutions.framework.core.webdriverfactory import WebDriverFactory
from exercices.solutions.framework.core.configuration import webdriver_configuration
from exercices.solutions.framework.pages.homePage import homePage
import random
from nose.tools import assert_equals

class testCreateUser():

    baseUrl = "https://forum-testing.herokuapp.com/v1.0/"

    @classmethod
    def setup_class(self):
        wdf = WebDriverFactory(webdriver_configuration)
        self.driver = wdf.getWebDriverInstance()
        self.home_page = homePage(self.driver)

    def setup(self):
        pass
        # Navigate to home page

        # Locate all Home page elements



    def test_create_user(self):

        user_id = random.randint(100, 10000000)
        username = 'username-{}'.format(user_id)
        password = 'password-{}'.format(user_id)
        name = 'name-{}'.format(user_id)
        email = 'email-{}@email.com'.format(user_id)
        role = 'DEVELOPER'

        # Click on Navigate New User Page

        # Locate all the New User Page elements

        # Fill name TextBox

        # Fill password TextBox

        # Fill username TextBox

        # Fill email TextBox

        # Fill role TextBox

        # Click on Save Button

        # Find the username element created (using the username variable)

        # Assert element text from the username element is the same than username variable
