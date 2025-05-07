from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

browser = webdriver.Chrome()

browser.get('https://www.facebook.com/')

try:
    # enter email
    userElement = browser.find_element(By.ID, 'email')    
    userElement.send_keys('wamik.abro212@gmail.com')

    # enter password
    passwordElement = browser.find_element(By.ID, 'pass')
    passwordElement.send_keys(sys.argv[1])

    # click login 
    loginButton = browser.find_element(By.NAME, 'login')
    loginButton.click()
except: 
    print("didn't find")

input("Press Enter to close the browser...")
