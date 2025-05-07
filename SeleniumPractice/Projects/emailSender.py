import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyinputplus as pyip

email = pyip.inputEmail('Enter Your Email: ')

browser = webdriver.Chrome()

browser.get('https://mail.google.com/')

emailBox = browser.find_element(By.NAME, 'identifier')
emailBox.send_keys(email)

nextButton = browser.find_element(By.CSS_SELECTOR, '#identifierNext button')
nextButton.click()

input()
