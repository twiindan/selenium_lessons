from selenium import webdriver

'''
An implicit wait tells WebDriver to poll the DOM for a certain amount of time when trying to find any
element (or elements) not immediately available. The default setting is 0.
Once set, the implicit wait is set for the life of the WebDriver object.'''

baseUrl = "https://forum-testing.herokuapp.com/v1.0"
driver = webdriver.Firefox()

#driver.implicitly_wait(15)
driver.maximize_window()
driver.get(baseUrl)

listUsers = driver.find_element_by_id('list_users')
listUsers.click()

noUsers = driver.find_element_by_id("userlist")
