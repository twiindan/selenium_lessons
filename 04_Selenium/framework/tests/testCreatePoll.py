from framework.pages.loginPage import loginPage
from framework.core.webdriverfactory import WebDriverFactory
from framework.core.configuration import webdriver_configuration

import random


class testLogin():

    baseUrl = "http://twiindan.pythonanywhere.com/admin"

    @classmethod
    def setup_class(self):
        wdf = WebDriverFactory(webdriver_configuration)
        self.driver = wdf.getWebDriverInstance()
        self.login_page = loginPage(self.driver)

    def setup(self):
        self.login_page.navigate()

    def testCreatePoll(self):
        self.login_page.locate_elements()
        main_page = self.login_page.login(username='user1', password='selenium')

        main_page.locate_elements()
        add_question_page = main_page.addQuestion()
        add_question_page.locate_elements()

        random_number = random.randint(1, 100000)
        questionText = "Question {}".format(random_number)
        add_question_page.setQuestionText(questionText)
        add_question_page.setNow()

        add_question_page.setChoicesText("Selenium", "Python", "Webpages")
        add_question_page.setChoiceVotes(0, 3, 1)
        add_question_page.savePoll()

    @classmethod
    def teardown_class(self):
        self.driver.quit()




