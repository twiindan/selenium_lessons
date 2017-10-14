from selenium import webdriver



baseUrl = "https://forum-testing.herokuapp.com/v1.0/demo"
driver = webdriver.Firefox()
driver.get(baseUrl)

elementByClassName = driver.find_element_by_class_name("displayed-class")

if elementByClassName is not None:
    print("We found an element by Class Name")

elementByTagName = driver.find_element_by_tag_name("h1")
text = elementByTagName.text

if elementByTagName is not None:
    print("We found an element by Tag Name and the text on element is: " + text)
