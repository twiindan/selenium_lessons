from selenium import webdriver
from nose.tools import assert_equals
import random



baseUrl = "http://twiindan.pythonanywhere.com/admin"
driver = webdriver.Firefox()
driver.get(baseUrl)

loginTextBox = driver.find_element_by_id("id_username")
passwordTextBox = driver.find_element_by_id("id_password")

logInButton = driver.find_element_by_xpath("//input[contains(@value, 'Log in')]")

loginTextBox.send_keys("user1")
passwordTextBox.send_keys("selenium")
logInButton.click()

questionsLink = driver.find_element_by_link_text("Questions")
assert_equals(questionsLink.get_attribute('href'), 'http://twiindan.pythonanywhere.com/admin/polls/question/')

addLink = driver.find_element_by_class_name("addlink")
addLink.click()

questionText = driver.find_element_by_id("id_question_text")

showMore = driver.find_element_by_id("fieldsetcollapser0")
showMore.click()

today_link = driver.find_element_by_link_text("Today")
today_link.click()

now_link = driver.find_element_by_link_text("Now")
now_link.click()

random_number = random.randint(1, 100000)
questionText.send_keys("Question {}".format(random_number))

choiceText1 = driver.find_element_by_name("choice_set-0-choice_text")
choiceText2 = driver.find_element_by_name("choice_set-1-choice_text")
choiceText3 = driver.find_element_by_name("choice_set-2-choice_text")

choiceText1.send_keys("Selenium")
choiceText2.send_keys("Python")
choiceText3.send_keys("Webpages")

choiceVotes = driver.find_element_by_name("choice_set-0-votes")
choiceVotes.clear()
choiceVotes.send_keys("3")

saveButton = driver.find_element_by_name("_save")
saveButton.click()


