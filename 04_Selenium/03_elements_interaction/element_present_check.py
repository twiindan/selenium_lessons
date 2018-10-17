from selenium import webdriver
from selenium.common.exceptions import WebDriverException


baseUrl = "https://forum-testing.herokuapp.com/v1.0/demo"
driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(baseUrl)

try:
    elementResult1 = driver.find_element_by_id("opentab")
    print("Element1 present")
except:
    print("Element1 not present")


try:
    elementResult2 = driver.find_element_by_id("opentab1")
    print("Element2 present")
except WebDriverException:
    print("Element2 not present")

driver.quit()
