from nose.tools import assert_equals
from selenium import webdriver
import random


class TestCreatePoll():

    baseUrl = "http://twiindan.pythonanywhere.com/admin"

    @classmethod
    def setup_class(self):

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)

    def setup(self):
        self.driver.get(self.baseUrl)

    def test_createPoll(self):
        loginTextBox = self.driver.find_element_by_id("id_username")
        passwordTextBox = self.driver.find_element_by_id("id_password")

        logInButton = self.driver.find_element_by_xpath("//input[contains(@value, 'Log in')]")

        loginTextBox.send_keys("user1")
        passwordTextBox.send_keys("selenium")
        logInButton.click()

        questionsLink = self.driver.find_element_by_link_text("Questions")
        assert_equals(questionsLink.get_attribute('href'), 'http://twiindan.pythonanywhere.com/admin/polls/question/')

        addLink = self.driver.find_element_by_class_name("addlink")
        addLink.click()

        questionText = self.driver.find_element_by_id("id_question_text")

        showMore = self.driver.find_element_by_id("fieldsetcollapser0")
        showMore.click()

        today_link = self.driver.find_element_by_link_text("Today")
        today_link.click()

        now_link = self.driver.find_element_by_link_text("Now")
        now_link.click()

        random_number = random.randint(1, 100000)
        questionText.send_keys("Question {}".format(random_number))

        choiceText1 = self.driver.find_element_by_name("choice_set-0-choice_text")
        choiceText2 = self.driver.find_element_by_name("choice_set-1-choice_text")
        choiceText3 = self.driver.find_element_by_name("choice_set-2-choice_text")

        choiceText1.send_keys("Selenium")
        choiceText2.send_keys("Python")
        choiceText3.send_keys("Webpages")

        choiceVotes = self.driver.find_element_by_name("choice_set-0-votes")
        choiceVotes.clear()
        choiceVotes.send_keys("3")

        saveButton = self.driver.find_element_by_name("_save")
        saveButton.click()

    def test_createPollWithOnlyTwoOptions(self):
        loginTextBox = self.driver.find_element_by_id("id_username")
        passwordTextBox = self.driver.find_element_by_id("id_password")

        logInButton = self.driver.find_element_by_xpath("//input[contains(@value, 'Log in')]")

        loginTextBox.send_keys("user1")
        passwordTextBox.send_keys("selenium")
        logInButton.click()

        questionsLink = self.driver.find_element_by_link_text("Questions")
        assert_equals(questionsLink.get_attribute('href'), 'http://twiindan.pythonanywhere.com/admin/polls/question/')

        addLink = self.driver.find_element_by_class_name("addlink")
        addLink.click()

        questionText = self.driver.find_element_by_id("id_question_text")

        showMore = self.driver.find_element_by_id("fieldsetcollapser0")
        showMore.click()

        today_link = self.driver.find_element_by_link_text("Today")
        today_link.click()

        now_link = self.driver.find_element_by_link_text("Now")
        now_link.click()

        random_number = random.randint(1, 100000)
        questionText.send_keys("Question {}".format(random_number))

        choiceText1 = self.driver.find_element_by_name("choice_set-0-choice_text")
        choiceText2 = self.driver.find_element_by_name("choice_set-1-choice_text")

        choiceText1.send_keys("Selenium")
        choiceText2.send_keys("Python")

        choiceVotes = self.driver.find_element_by_name("choice_set-0-votes")
        choiceVotes.clear()
        choiceVotes.send_keys("5")

        saveButton = self.driver.find_element_by_name("_save")
        saveButton.click()

    def teardown(self):
        logout_link = self.driver.find_element_by_link_text("Log out")
        logout_link.click()

    @classmethod
    def teardown_class(self):
        self.driver.quit()

