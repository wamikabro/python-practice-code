from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()

browser.get('https://inventwithpython.com')

try:
    linkElem = browser.find_element(By.LINK_TEXT, 'Python Programming Exercises, Gently Explained')

    linkElem.click()
except Exception as e:  
    print(e)


input()