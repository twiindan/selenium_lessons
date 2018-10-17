from selenium import webdriver
from selenium.webdriver.common.by import By
import time


baseUrl = "https://forum-testing.herokuapp.com/v1.0/demo"
driver = webdriver.Firefox()
driver.maximize_window()
driver.get(baseUrl)

# Find parent handle -> Main Window
parentHandle = driver.current_window_handle
print("Parent Handle: " + parentHandle)

# Find open window button and click it
driver.find_element(By.ID, "openwindow").click()
time.sleep(2)

# Find all handles, there should two handles after clicking open window button
handles = driver.window_handles

# Switch to window and search course
for handle in handles:
    print("Handle: " + handle)
    if handle not in parentHandle:
        driver.switch_to.window(handle)
        print("Switched to window:: " + handle)
        searchBox = driver.find_element(By.ID, "create_user")
        searchBox.click()
        time.sleep(2)
        driver.close()
        break

# Switch back to the parent handle
driver.switch_to.window(parentHandle)
driver.find_element(By.ID, "name").send_keys("Test Successful")

time.sleep(2)

driver.quit()
