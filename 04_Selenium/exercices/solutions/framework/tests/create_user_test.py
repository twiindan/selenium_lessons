
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
        # Navigate to home page
        self.home_page.navigate()

        # Locate all Home page elements
        self.home_page.locate_elements()


    def test_create_user(self):

        user_id = random.randint(100, 10000000)
        username = 'username-{}'.format(user_id)
        password = 'password-{}'.format(user_id)
        name = 'name-{}'.format(user_id)
        email = 'email-{}@email.com'.format(user_id)
        role = 'DEVELOPER'

        # Click on Navigate New User Page
        user_page = self.home_page.navigate_new_user_page()

        # Locate all the New User Page elements
        user_page.locate_elements()

        # Fill name TextBox
        user_page.fill_name(name)

        # Fill password TextBox
        user_page.fill_password(password)

        # Fill username TextBox
        user_page.fill_username(username)

        # Fill email TextBox
        user_page.fill_email(email)

        # Fill role TextBox
        user_page.fill_role(role)

        # Click on Save Button
        user_list_page = user_page.click_button()

        # Find the username element created (using the username variable)
        username_element = user_list_page.search_user(username)

        # Assert element text from the username element is the same than username variable
        assert_equals(username_element.text, username)

    @classmethod
    def teardown_class(self):
        self.driver.quit()