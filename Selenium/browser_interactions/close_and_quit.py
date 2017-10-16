from selenium import webdriver
from time import sleep


driver = webdriver.Firefox()
driver.get('https://google.com')

driver.execute_script("window.open('https://twitter.com')")
driver.execute_script("window.open('https://linkedin.com')")
driver.execute_script("window.open('https://facebook.com')")
sleep(5)
driver.close()

sleep(5)
driver.quit()
