from selenium import webdriver
from selenium.webdriver.common.by import By
import time

baseUrl = "https://forum-testing.herokuapp.com/v1.0/demo"
driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(baseUrl)

openTabElement = driver.find_element(By.ID, "opentab")
elementText = openTabElement.text
print("Text on element is: " + elementText)
time.sleep(1)
driver.quit()
