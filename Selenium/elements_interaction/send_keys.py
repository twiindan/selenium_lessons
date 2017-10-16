from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('http://www.google.com')
sleep(2)

loginTextBox = driver.find_element_by_id('lst-ib')
searchButton = driver.find_element_by_xpath('//input[@name="btnK"]')

loginTextBox.send_keys("python")
sleep(2)
searchButton.click()

driver.quit()