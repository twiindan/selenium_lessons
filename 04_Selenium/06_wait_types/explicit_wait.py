from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


'''
An explicit wait is a code you define to wait for a certain condition to occur before proceeding further in the code.
The extreme case of this is time.sleep(), which sets the condition to an exact time period to wait.
There are some convenience methods provided that help you write code that will wait only as long as required.
WebDriverWait in combination with ExpectedCondition is one way this can be accomplished.

'''

baseUrl = "https://forum-testing.herokuapp.com/v1.0"
driver = webdriver.Firefox()
driver.maximize_window()
driver.get(baseUrl)

listUsers = driver.find_element_by_id('list_users')
listUsers.click()

try:
    element = WebDriverWait(driver, timeout=15, poll_frequency=0.5, ignored_exceptions=NoSuchElementException).until(
        EC.presence_of_element_located((By.ID, "userlist"))
    )
    if element is not None:
        print('Element found')
except:
    print('Element not found')

driver.quit()

'''
Expected Conditions

- title_is
- title_contains
- presence_of_element_located ***
- visibility_of_element_located ***
- visibility_of
- presence_of_all_elements_located
- text_to_be_present_in_element
- text_to_be_present_in_element_value
- frame_to_be_available_and_switch_to_it
- invisibility_of_element_located
- element_to_be_clickable ***
- staleness_of
- element_to_be_selected
- element_located_to_be_selected
- element_selection_state_to_be
- element_located_selection_state_to_be
- alert_is_present
'''