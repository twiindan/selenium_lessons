from selenium import webdriver


baseUrl = "http://arnaumarch.com/"
driver = webdriver.Firefox()
driver.get(baseUrl)


'''
One method to find resources in DOM is using XPATH. The idea is use different techniques
and tips to obtain a unique element in the webpage using Xpath selectors.
'''

'''Syntax for XPATH
    / --> Look for the element immdiately inside the parent element
    // --> Loof for any child or nested-child element inside the parent element

    //tag[@attribute=value]

Example

//div[@id="main-content"]/section[1]/header/menu/a
     vs

//div[@id="main-content"]//menu/a

'''

elementByXpath = driver.find_element_by_xpath('//div[@id="main-content"]/section[1]/header/menu/a')
print(elementByXpath.text)

elementByXpath = driver.find_element_by_xpath('//div[@id="main-content"]//menu/a')
print(elementByXpath.text)

'''
Be careful:

//div[@id="main-content"]/section[2]/div/article[2]/header
//div[@id="main-content"]/section[2]//header
'''


elementsByXpath = driver.find_elements_by_xpath('//div[@id="main-content"]/section[2]/div/article[2]/header')
print(len(elementsByXpath))

elementsByXpath = driver.find_elements_by_xpath('//div[@id="main-content"]/section[2]//header')
print(len(elementsByXpath))


'''
Using Text of the element to build an effective XPATH

//tag[text()=<element_text>]

//div[@id="main-content"]/section[2]/div/article[2]/header  -> Text "About me"

//header[text()='About me']

Also can use hierarchy:

//div[@id="main-content"]//header[text()="About me"]
'''

elementByXpath = driver.find_element_by_xpath('//header[text()="About me"]')

if elementByXpath is not None:
    print("Element found")


elementByXpath = driver.find_element_by_xpath('//div[@id="main-content"]//header[text()="About me"]')

if elementByXpath is not None:
    print("Element found")


'''
Another utility to serch elements is using another attributes with the command "Contains"

//tag[contains(attribute, 'value')]

//div[@id="main-content"]//header[contains(text(), "About me")]
//div[@id="main-content"]//a[contains(@class, "button")]

Several conditions can be used to matching:

//div[@id="main-content"]//a[contains(@class, "button") and contains(@href, "https://twitter.com/rnowm/")]


'''

elementByXpath = driver.find_element_by_xpath('//div[@id="main-content"]//header[contains(text(), "About me")]')

if elementByXpath is not None:
    print("Element found")


elementsByXpath = driver.find_elements_by_xpath('//div[@id="main-content"]//a[contains(@class, "button")]')
print(len(elementsByXpath))


elementsByXpath = driver.find_elements_by_xpath('//div[@id="main-content"]//a[contains(@class, "button") and '
                                                'contains(@href, "https://twitter.com/rnowm/")]')

print(len(elementsByXpath))
print(elementsByXpath[0].text)


'''
Similar to contains function, XPATH also provide the starts-with function.

//tag[starts-with(attribute, value)]

//div[@id="main-content"]//header[starts-with(text(), "About")]
//div[@id="main-content"]//a[starts-with(@class, "butt")]
'''

elementsByXpath = driver.find_elements_by_xpath('//div[@id="main-content"]//header[starts-with(text(), "About")]')
print(len(elementsByXpath))

for element in elementsByXpath:
    print(element.text)

