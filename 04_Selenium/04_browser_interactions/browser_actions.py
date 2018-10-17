from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('https://google.com')
driver.get('https://forum-testing.herokuapp.com/v1.0/demo')

sleep(2)
driver.back()

sleep(2)
driver.forward()

sleep(2)
driver.refresh()

sleep(2)
driver.get(driver.current_url)



