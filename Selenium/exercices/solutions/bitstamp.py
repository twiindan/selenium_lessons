#import webdriver
from selenium import webdriver

#define baseURL
baseUrl = "https://www.bitstamp.net/"

#Open browser
driver = webdriver.Firefox()

#Open baseUrl
driver.get(baseUrl)

#Get the element with lastprice
priceElement = driver.find_element_by_id("last-price")

#Print the Bitcoin price
print(priceElement.text)