from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('http://www.gmail.com')

driver.find_element_by_id('identifierNext').click()

sleep(5)

