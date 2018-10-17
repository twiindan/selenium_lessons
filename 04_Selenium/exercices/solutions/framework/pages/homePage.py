from exercices.solutions.framework.core.base import BasePage
from exercices.solutions.framework.pages.newUserPage import newUserPage


class homePage(BasePage):
    url = 'https://forum-testing.herokuapp.com/v1.0/'
    _newUserLink = None
    _listUserLink = None
    _newForumMessageLink = None
    _listForumLink = None

    # Locate all the elements of the Home Page
    def locate_elements(self):
        self._newUserLink = self.driver.find_element_by_link_text('Create a new user')
        self._listUserLink = self.driver.find_element_by_link_text('List users')
        self._newForumMessageLink = self.driver.find_element_by_link_text('Create new forum message')
        self._listForumLink = self.driver.find_element_by_link_text('List forum message')

    # Navigate to the new user page
    def navigate_new_user_page(self):
        self._newUserLink.click()
        return newUserPage(self.driver)

    # Navigate to the new forum message page
    def navigate_new_forum_message_page(self):
        self._newForumMessageLink.click()

    # Navigate to the user list
    def navigate_user_list_page(self):
        self._listUserLink.click()

    # Navigate to the forum message list
    def navigate_forum_messages_list_page(self):
        self._listForumLink.click()

