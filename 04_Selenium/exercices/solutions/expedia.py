from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Configure the baseURL
baseUrl = "https://www.expedia.es"

# Create a webDriver instance and maximize window
driver = webdriver.Firefox()
driver.maximize_window()

# Navigage to URL and put a 10 seconds implicit wait
driver.get(baseUrl)
driver.implicitly_wait(10)

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

# Find departure time and type "23/11/2018"
departTime = driver.find_element(By.ID, "flight-departing-hp-flight")
departTime.clear()
departTime.send_keys("23/11/2018")

# Find adult dropdown and select 5 adults
adultsDropdown = driver.find_element(By.ID, "flight-adults-hp-flight")
adultsSel = Select(adultsDropdown)
adultsSel.select_by_value("5")

# Find child dropdown and select 1 children
childDropdown = driver.find_element(By.ID, "flight-children-hp-flight")
childSel = Select(childDropdown)
childSel.select_by_value("1")

# Find the first option in the child age
oldDropdown = driver.find_element(By.ID, "flight-age-select-1-hp-flight")
oldSel = Select(oldDropdown)
oldSel.select_by_index(1)

# Find the "Find" button and click on
findButtons = driver.find_elements(By.XPATH, "//span[text()='Buscar']")

for button in findButtons:
    if button.is_displayed():
        button.click()
        break

#Quit Driver
driver.quit()
