from selenium import webdriver
import time

baseUrl = "https://forum-testing.herokuapp.com/v1.0/demo"
driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(baseUrl)

element = driver.find_element_by_id("name")
result = element.get_attribute("type")

print("Value of attribute is: " + result)
time.sleep(1)
result = element.get_attribute("placeholder")
print("Value of attribute is: " + result)

driver.quit()
