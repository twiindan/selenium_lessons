from framework.pages.base import BasePage



class headerPage (BasePage):

    url = "http://twiindan.pythonanywhere.com/admin"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locate_elements()

    def locate_elements(self):
        self.logoutLink = self.driver.find_element_by_link_text('Log out')
        self.changePassworkdLink = self.driver.find_element_by_link_text('Change password')


    def logout(self):
        self.logoutLink.click()

    def change_password(self):
        self.change_password.click()