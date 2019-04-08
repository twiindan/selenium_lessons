from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


baseUrl = "https://forum-testing.herokuapp.com/v1.0/demo"
driver = webdriver.Firefox()
driver.get(baseUrl)


'''
One method to find resources in DOM is using CSS Selectors. The idea is use different techniques
and tips to obtain a unique element in the webpage using CSS selectors.
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
input.displayed-class

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


'''
Is Possible is wildcards inside the CSS Selectors using the following syntax:

tag[attribute<special-character>=value]

The special characters used as wildcards are the following:

    - Represents the starting text --> ^
    - Represents the ending text --> $
    - Represents the text contained --> *
'''


'''
Examples using wildcards

input[class='inputs'] --> 1 matching element
input[class^='inputs'] --> 2 matching element
input[class$='inputs'] --> 1 matching element
input[class*='inputs'] --> 2 matching element

'''

elementsByCss = driver.find_elements_by_css_selector("input[class='inputs']")
print(len(elementsByCss))

elementsByCss = driver.find_elements_by_css_selector("input[class^='inputs']")
print(len(elementsByCss))

elementsByCss = driver.find_elements_by_css_selector("input[class$='inputs']")
print(len(elementsByCss))

elementsByCss = driver.find_elements_by_css_selector("input[class*='inputs']")
print(len(elementsByCss))


'''
Is possible also find the elements finding his children nodes using the character ">".

fieldset>table
fieldset>#product
fieldset>button
fieldset>input#name


'''

elementByCss = driver.find_element_by_css_selector("fieldset>table")
print(elementByCss.get_attribute('name'))


elementByCss = driver.find_element_by_css_selector("fieldset>#product")
print(elementByCss.get_attribute('name'))


elementByCss = driver.find_element_by_css_selector("fieldset>button")
print(elementByCss.get_attribute('name'))


elementByCss = driver.find_element_by_css_selector("fieldset>input#name")
print(elementByCss.get_attribute('name'))

