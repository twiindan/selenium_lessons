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
        pass

    # Navigate to the new user page
    def navigate_new_user_page(self):
        pass

    # Navigate to the new forum message page
    def navigate_new_forum_message_page(self):
        pass

    # Navigate to the user list
    def navigate_user_list_page(self):
        pass

    # Navigate to the forum message list
    def navigate_forum_messages_list_page(self):
        pass

