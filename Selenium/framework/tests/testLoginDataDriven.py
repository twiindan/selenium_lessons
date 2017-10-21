
from framework.pages.loginPage import loginPage
from framework.pages.headerPage import headerPage
from framework.core.webdriverfactory import WebDriverFactory
from framework.core.configuration import webdriver_configuration
from framework.utilities.read_data import get_csv_data

from ddt import ddt, data, unpack
from nose.tools import assert_equals


@ddt
class testLogin():

    baseUrl = "http://twiindan.pythonanywhere.com/admin"

    @classmethod
    def setup_class(self):
        wdf = WebDriverFactory(webdriver_configuration)
        self.driver = wdf.getWebDriverInstance()
        self.login_page = loginPage(self.driver)

    def setup(self):
        self.login_page.navigate()

    @data(*get_csv_data('/Users/arobres/PycharmProjects/selenium_lessons/Selenium/framework/data/login_data.csv'))
    @unpack
    def test_incorrect_login(self, username, password):
        self.login_page.locate_elements()
        self.login_page.fillUsername(username)
        self.login_page.fillPassword(password)
        self.login_page.submitClick()
        errorUrl = self.login_page.verifyURL()
        assert_equals('http://twiindan.pythonanywhere.com/admin/login/?next=/admin/', errorUrl)



    @classmethod
    def teardown_class(self):
        self.driver.quit()


