from framework.pages.base import BasePage



class addQuestionPage (BasePage):

    questionTextBox = None
    showMore = None
    todayLink = None
    nowLink = None
    choiceText1 = None
    choiceText2 = None
    choiceText3 = None
    choiceVotes1 = None
    choiceVotes2 = None
    choiceVotes3 = None
    addChoice = None
    saveButton = None

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def locate_elements(self):

        self.questionTextBox = self.driver.find_element_by_id("id_question_text")
        self.showMore = self.driver.find_element_by_id("fieldsetcollapser0")
        self.todayLink = self.driver.find_element_by_link_text("Today")
        self.nowLink = self.driver.find_element_by_link_text("Now")
        self.choiceText1 = self.driver.find_element_by_name("choice_set-0-choice_text")
        self.choiceText2 = self.driver.find_element_by_name("choice_set-1-choice_text")
        self.choiceText3 = self.driver.find_element_by_name("choice_set-2-choice_text")
        self.choiceVotes1 = self.driver.find_element_by_name("choice_set-0-votes")
        self.choiceVotes2 = self.driver.find_element_by_name("choice_set-1-votes")
        self.choiceVotes3 = self.driver.find_element_by_name("choice_set-2-votes")
        self.addChoice = self.driver.find_element_by_link_text("Add another Choice")
        self.saveButton = self.driver.find_element_by_name("_save")


    def setQuestionText(self, question_text=''):
        self.questionTextBox.send_keys(question_text)


    def setNow(self):
        self.showMore.click()
        self.todayLink.click()
        self.nowLink.click()

    def setChoicesText(self, choiceTextvalue1='', choiceTextvalue2='', choiceTextvalue3=''):


        self.choiceText1.send_keys(choiceTextvalue1)
        self.choiceText2.send_keys(choiceTextvalue2)
        self.choiceText3.send_keys(choiceTextvalue3)

    def setChoiceVotes(self, choiceVotesValue1=0, choiceVotesValue2=0, choiceVotesValue3=0):

        self.choiceVotes1.clear()
        self.choiceVotes2.clear()
        self.choiceVotes3.clear()

        self.choiceVotes1.send_keys(choiceVotesValue1)
        self.choiceVotes2.send_keys(choiceVotesValue2)
        self.choiceVotes3.send_keys(choiceVotesValue3)

    def savePoll(self):
        self.saveButton.click()
        #return mainPage(self.driver)
