from framework.pages.base import BasePage
from framework.pages.addQuestionPage import addQuestionPage


class mainPage(BasePage):

    pollsLink = None
    addPollLink = None
    changePollLink = None


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def locate_elements(self):
        self.pollsLink = self.driver.find_element_by_link_text("Questions")
        self.addPollLink = self.driver.find_element_by_link_text("Add")
        self.changePollLink = self.driver.find_element_by_link_text("Change")

    def addQuestion(self):
        self.addPollLink.click()
        return addQuestionPage(self.driver)

    def changeQuestion(self):
        self.changePollLink.click()

    def listQuestions(self):
        self.pollsLink.click()



