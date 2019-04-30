from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

# Configure the baseURL
baseUrl = "https://www.expedia.es"

# Create a webDriver instance and maximize window
driver = webdriver.Firefox()
driver.maximize_window()

# Navigage to URL and put a 10 seconds implicit wait
driver.get(baseUrl)

# Find and click on element "Flights"
travelType = driver.find_element(By.ID, "tab-flight-tab-hp")
travelType.click()

# Find departure textbox and type "Barcelona"
originBox = driver.find_element(By.ID, "flight-origin-hp-flight")
originBox.clear()
originBox.send_keys("Barcelona")

# Find departure textbox and type "Madrid"
destinationBox = driver.find_element(By.ID, "flight-destination-hp-flight")
destinationBox.clear()
destinationBox.send_keys("Madrid")

# Find departure time and type "23/05/2019"
departTime = driver.find_element(By.ID, "flight-departing-hp-flight")
departTime.clear()
departTime.send_keys("23/05/2019")

# Close Calendar
close_button = driver.find_element_by_css_selector('.datepicker-close-btn.close.btn-text')
close_button.click()


# Find the "Find" button and click on
findButtons = driver.find_elements(By.XPATH, "//span[text()='Buscar']")

for button in findButtons:
    if button.is_displayed():
        button.click()
        break

# Wait the element that contain the first price and print it. Wait it 15 seconds with 0.5 polling frequency
# You can use the CSS Selector ".offer-price>span" to get the first price
element = WebDriverWait(driver, timeout=15,
                        poll_frequency=0.5).until(EC.presence_of_element_located((By.ID,
                                                                                  "filter-container")))
print(element.text)
sleep(3)


driver.quit()
