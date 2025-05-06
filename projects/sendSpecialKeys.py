from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome()

browser.get('https://nostarch.com')

htmlElem = browser.find_element(By.TAG_NAME, 'html')

# End button of Keyboard
htmlElem.send_keys(Keys.END) # scroll to the bottom

time.sleep(3)

# Home button of keyboard
htmlElem.send_keys(Keys.HOME) # scroll to the top

input()