from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


baseUrl = "https://letskodeit.teachable.com/pages/practice"
driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(baseUrl)

try:
    elementResult1 = driver.find_element_by_id("opentab")
    print "Element1 present"
except:
    print "Element1 not present"


try:
    elementResult2 = driver.find_element_by_id("opentab1")
    print "Element2 present"
except NoSuchElementException:
    print "Element2 not present"

driver.quit()