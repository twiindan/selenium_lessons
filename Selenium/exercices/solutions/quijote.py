# Import webdriver
from selenium import webdriver

# Define baseURL
baseUrl = "https://forum-testing.herokuapp.com/v1.0/demo"

# Open browser
driver = webdriver.Firefox()

# Open baseUrl
driver.get(baseUrl)

# Find the element using absolute XPATH
webElement = driver.find_element_by_xpath('//*[@id="product"]/tbody/tr[3]/td[2]')

# Print text of the element
print(webElement.text)

# Find the element using relative XPATH (using contains)
webElement = driver.find_element_by_xpath('//td[contains(text(), "El Quijote")]')

# Print text of the element
print(webElement.text)