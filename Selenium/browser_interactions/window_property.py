from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://google.com')

print("CURRENT WEBPAGE TITTLE: {}".format(driver.title))
print("CURRENT URL: {}".format(driver.current_url))

source_page = driver.page_source

print(source_page)