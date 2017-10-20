from framework.pages.base import BasePage
from framework.pages.mainPage import mainPage



class loginPage (BasePage):

    url = "http://twiindan.pythonanywhere.com/admin"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    loginTextBox = None
    passwordTextBox = None
    logInButton = None

    def locate_elements(self):
        self.loginTextBox = self.driver.find_element_by_id("id_username")
        self.passwordTextBox = self.driver.find_element_by_id("id_password")
        self.logInButton = self.driver.find_element_by_xpath("//input[contains(@value, 'Log in')]")

    def fillUsername(self, username=''):
        self.loginTextBox.send_keys(username)

    def fillPassword(self, password=''):
        self.passwordTextBox.send_keys(password)

    def submitClick(self):

        self.logInButton.click()
        return mainPage(self.driver)

    def login(self, username='', password=''):
        self.loginTextBox.send_keys(username)
        self.passwordTextBox.send_keys(password)
        self.logInButton.click()
        return mainPage(self.driver)

    def verifyURL(self):
        return self.driver.current_url