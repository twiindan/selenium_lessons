from selenium import webdriver
from selenium.webdriver.common.by import By


baseUrl = "https://forum-testing.herokuapp.com/v1.0/demo"
driver = webdriver.Firefox()
driver.get(baseUrl)

elementListByTagName = driver.find_elements(By.TAG_NAME, "td")
length1 = len(elementListByTagName)

if elementListByTagName is not None:
    print("TagName -> Size of the list is: " + str(length1))

for element in elementListByTagName:
    print(element.text)


elementListByClassName = driver.find_elements_by_class_name("inputs")
length2 = len(elementListByClassName)

for element in elementListByClassName:
    print(element.get_attribute('placeholder'))

if elementListByClassName is not None:
    print("ClassName -> Size of the list is: " + str(length2))


