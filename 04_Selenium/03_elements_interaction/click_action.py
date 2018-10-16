from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('http://www.gmail.com')

nextButton = driver.find_element_by_id('identifierNext')

sleep(5)

nextButton.click()