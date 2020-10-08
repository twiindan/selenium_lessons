# import webdriver
from selenium import webdriver

# define baseURL
baseUrl = "https://www.browserstack.com/"

# Open browser
driver = webdriver.Firefox()

# Open baseUrl
driver.get(baseUrl)

# Get the element with lastprice
get_started_button = driver.find_element_by_id("signupModalButton")

# Print the Bitcoin price
print(get_started_button.text)

