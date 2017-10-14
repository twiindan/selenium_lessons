from selenium import webdriver

baseUrl = "https://forum-testing.herokuapp.com/v1.0/"
driver = webdriver.Firefox()
driver.get(baseUrl)

elementByLinkText = driver.find_element_by_link_text("List users")

if elementByLinkText is not None:
    print("We found an element by Link Text")

elementByPartialLinkText = driver.find_element_by_partial_link_text("Create new")

if elementByPartialLinkText is not None:
    print("We found an element by Partial Link Text")
