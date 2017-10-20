from exercices.framework.core.base import BasePage



class userListPage(BasePage):
    url = "https://forum-testing.herokuapp.com/v1.0/users/"

    def search_user(self, username):
        print (username)
        return self.driver.find_element_by_xpath('//td[contains(text(), "{}")]'.format(username))
