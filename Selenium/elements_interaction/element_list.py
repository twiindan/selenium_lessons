from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
baseUrl = "https://forum-testing.herokuapp.com/v1.0/demo"
driver = webdriver.Firefox()
driver.maximize_window()
driver.get(baseUrl)
driver.implicitly_wait(10)


CheckboxList = driver.find_elements(By.XPATH, "//input[contains(@type,'checkbox') and contains(@name,'so')]")
size = len(CheckboxList)
print("Size of the list: " + str(size))

for checkbox in CheckboxList:

    checkbox.click()
    sleep(2)

driver.quit()