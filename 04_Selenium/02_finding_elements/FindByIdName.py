from selenium import webdriver


baseUrl = "https://forum-testing.herokuapp.com/v1.0/demo"
driver = webdriver.Firefox()
driver.get(baseUrl)
elementById = driver.find_element_by_id("name")

if elementById is not None:
    print("We found an element by Id")

elementByName = driver.find_element_by_name("show-hide")

if elementByName is not None:
    print("We found an element by Name")

