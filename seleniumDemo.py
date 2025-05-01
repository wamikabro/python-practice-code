from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()

browser.get('https://inventwithpython.com')

try:
    elem = browser.find_element(By.LINK_TEXT, 'Read Online for Free')
    print(type(elem))
    elem.click()
except:
    print('Was not able to find an element with that name.')