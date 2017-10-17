from selenium import webdriver
from selenium.webdriver.common.by import By
import time


baseUrl = "http://www.mclibre.org/consultar/htmlcss/html/html_objetos.html#iframe"
driver = webdriver.Firefox()
driver.maximize_window()
driver.get(baseUrl)

# Switch to frame using numbers
driver.switch_to.frame(0)

# Switch to frame using element
iframe = driver.find_element(By.XPATH, '//*[@id="iframe"]/div[1]/div[2]/iframe')
driver.switch_to.frame(iframe)
time.sleep(2)

#Print text
elementText = driver.find_element(By.XPATH, "/html/head/title/")
print(elementText.text)
time.sleep(2)

# Switch back to the parent frame
driver.switch_to.default_content()
driver.execute_script("window.scrollBy(0, 1000);")
time.sleep(2)


# '//iframe[contains(@src,"ejemplo_iframe.html")]'