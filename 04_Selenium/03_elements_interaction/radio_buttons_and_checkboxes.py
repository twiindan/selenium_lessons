from selenium import webdriver
from time import sleep

baseUrl = "https://forum-testing.herokuapp.com/v1.0/demo"
driver = webdriver.Firefox()
driver.maximize_window()
driver.get(baseUrl)
driver.implicitly_wait(10)

windowsRadioBtn = driver.find_element_by_id("windowsradio")
windowsRadioBtn.click()

sleep(2)
appleRadioBtn = driver.find_element_by_id("appleradio")
appleRadioBtn.click()

sleep(2)
linuxCheckbox = driver.find_element_by_id("linuxcheck")
linuxCheckbox.click()

sleep(2)
windowsCheckbox = driver.find_element_by_id("windowscheck")
windowsCheckbox.click()

# True if selected, False is not selected
print("Windows Radio button is selected? " + str(windowsRadioBtn.is_selected()))
print("Apple Radio button is selected? " + str(appleRadioBtn.is_selected()))
print("Linux Checkbox is selected? " + str(linuxCheckbox.is_selected()))
print("Windows Checkbox is selected? " + str(windowsCheckbox.is_selected()))

driver.quit()




