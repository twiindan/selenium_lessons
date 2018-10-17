from exercices.solutions.framework.core.base import BasePage



class userListPage(BasePage):
    url = "https://forum-testing.herokuapp.com/v1.0/users/"

    # Find a username
    def search_user(self, username):
        return self.driver.find_element_by_xpath('//td[contains(text(), "{}")]'.format(username))

