from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


baseUrl = "https://forum-testing.herokuapp.com/v1.0/demo"
driver = webdriver.Firefox()
driver.get(baseUrl)


'''
One method to find resources in DOM is using CSS Selectors. The idea is use different techniques
and tips to obtain a unique element in the webpage.
'''

'''Syntax for CSS Selectors
There are several possibilities to define a CSS Selector.
    - tag[attribute='value']
    - #Id
    - .Class
'''

'''
Example using Id's

input[id=displayed-text]
#displayed-text
input#displayed-text

'''


elementByCss = driver.find_element_by_css_selector("input[id=displayed-text]")
print(elementByCss.get_attribute('name'))

elementByCss = driver.find_element_by_css_selector("#displayed-text")
print(elementByCss.get_attribute('name'))

elementByCss = driver.find_element_by_css_selector("input#displayed-text")
print(elementByCss.get_attribute('name'))


'''
Example using Classes

input[class=displayed-class]
.displayed-class
input#displayed-class

'''


elementByCss = driver.find_element_by_css_selector(".displayed-class")
print(elementByCss.get_attribute('name'))

elementByCss = driver.find_element_by_css_selector("input.displayed-class")
print(elementByCss.get_attribute('name'))


try:
    elementByCss = driver.find_element_by_css_selector("input[class=displayed-class]")

except NoSuchElementException:
    print("The element is not found")


#There are more than one class in the Element

elementByCss = driver.find_element_by_css_selector(".inputs.displayed-class")
print(elementByCss.get_attribute('name'))


elementByCss = driver.find_element_by_css_selector(".btn-style.class1.class2")
print(elementByCss.get_attribute('href'))
