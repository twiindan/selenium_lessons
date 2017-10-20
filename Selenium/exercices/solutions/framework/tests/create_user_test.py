
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
        self.home_page.navigate()
        self.home_page.locate_elements()

    def test_create_user(self):

        user_id = random.randint(100, 10000000)
        username = 'username-{}'.format(user_id)
        password = 'password-{}'.format(user_id)
        name = 'name-{}'.format(user_id)
        email = 'email-{}@email.com'.format(user_id)

        user_page = self.home_page.navigate_new_user_page()
        user_page.locate_elements()
        user_page.fill_name(name)
        user_page.fill_password(password)
        user_page.fill_username(username)
        user_page.fill_email(email)
        user_page.fill_role("DEVELOPER")
        user_list_page = user_page.click_button()
        username_element = user_list_page.search_user(username)
        assert_equals(username_element.text, username)
