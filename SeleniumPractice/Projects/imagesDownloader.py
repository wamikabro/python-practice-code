from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from pathlib import Path

searchQuery = input('What images to download: ')

browser = webdriver.Chrome()
browser.get('https://stocksnap.io/')

searchBar = browser.find_element(By.NAME, 'main-search')
searchBar.send_keys(searchQuery)

submitButton = browser.find_element(By.CSS_SELECTOR, "form[id='main-search-form'] button[type='submit']")
submitButton.click()

foundImagesDriver = browser.find_elements(By.CSS_SELECTOR, 'div.photo-grid-item img')

number = 1
for imageElement in foundImagesDriver:
    potentialImage = imageElement.get_attribute('src')
    if Path(potentialImage).suffix == 'jpg':
        imageBinary = requests.get(imageElement.get_attribute('src'))
        nameForImage = 'image' + str(number) + '.jpg' # image1

        imageFile = open(Path.cwd() / 'SeleniumPractice' / 'Projects' / nameForImage, 'wb')
        for chink in imageBinary.iter_content(100000):
            imageFile.write(chink)

        number+=1
        

input()