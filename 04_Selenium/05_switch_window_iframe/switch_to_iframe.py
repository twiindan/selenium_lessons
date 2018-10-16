from selenium import webdriver
from selenium.webdriver.common.by import By
import time


baseUrl = "https://jqueryui.com/button/"
driver = webdriver.Firefox()
driver.maximize_window()
driver.get(baseUrl)

# Switch to frame using element
iframe = driver.find_element(By.XPATH, '//div[@id="content"]/iframe')
driver.switch_to.frame(iframe)
time.sleep(2)

#Print text
elementText = driver.find_element(By.XPATH, "/html/body/div/button")
print(elementText.text)
time.sleep(2)

# Switch back to the parent frame
driver.switch_to.default_content()
driver.execute_script("window.scrollBy(0, 1000);")
time.sleep(2)

driver.quit()
