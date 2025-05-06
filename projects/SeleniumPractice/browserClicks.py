from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://automatetheboringstuff.com/2e/chapter12/')

browser.back()
input()