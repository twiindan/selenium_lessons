from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('https://google.com')

driver.set_window_size(800, 600)
sleep(5)

driver.maximize_window()


