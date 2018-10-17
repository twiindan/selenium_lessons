from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

baseUrl = "https://forum-testing.herokuapp.com/v1.0/demo"
driver = webdriver.Firefox()
driver.maximize_window()
driver.get(baseUrl)
driver.implicitly_wait(10)

element = driver.find_element_by_id("soselect")
sel = Select(element)

sel.select_by_value("apple")
print("Select Apple by value")
time.sleep(2)

sel.select_by_index("2")
print("Select Windows by index")
time.sleep(2)

sel.select_by_visible_text("Linux")
print("Select Linux by visible text")
time.sleep(2)

