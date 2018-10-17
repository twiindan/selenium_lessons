from exercices.solutions.framework.core.base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class userListPage(BasePage):
    url = "https://forum-testing.herokuapp.com/v1.0/users/"

    # Find a username
    def search_user(self, username):
        element = WebDriverWait(self.driver, timeout=15,
                                poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                                          '//td[contains(text(), "{}")]'.format(username))))

        return element
