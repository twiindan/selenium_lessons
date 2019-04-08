from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('http://www.google.com')
sleep(2)

loginTextBox = driver.find_element_by_css_selector('.gLFyf.gsfi')
searchButton = driver.find_element_by_xpath('//input[@name="btnK"]')


loginTextBox.clear()
loginTextBox.send_keys("python")
sleep(2)
searchButton.click()

driver.quit()