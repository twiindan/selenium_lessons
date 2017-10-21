from exercices.solutions.framework.core.base import BasePage
from exercices.solutions.framework.pages.userListPage import userListPage
from selenium.webdriver.support.ui import Select



class newUserPage(BasePage):
    url = "https://forum-testing.herokuapp.com/v1.0/users/new"

    _usernameTextBox = None
    _passwordTextBox = None
    _nameTextBox = None
    _emailTextBox = None
    _roleSelect = None

    # Locate all the elements of the New User Page
    def locate_elements(self):
        pass

    # Fill the name TextBox
    def fill_name(self, name):
        pass

    # Fill the username TextBox
    def fill_username(self, username):
        pass

    # Select the role in the dropdown (Remember use Select method in webdriver)
    def fill_role(self, role):
        pass

    # Fill the password TextBox
    def fill_password(self, password):
        pass

    # Fill the email TextBox
    def fill_email(self, email):
        pass

    # Click on Save button
    def click_button(self):
        pass


    # Optional: Fill all the Textboxes and click on save Button (you can do that using the methods of the class)
    def fill_all_form(self, username, password, role, email, name):

        pass