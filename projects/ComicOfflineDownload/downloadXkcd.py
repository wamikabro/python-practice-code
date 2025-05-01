import webbrowser, requests, bs4, os
from pathlib import Path

# url
url = 'https://xkcd.com/'

(Path.cwd()/'projects'/'ComicOfflineDownload'/'xkcd').mkdir(exist_ok=True)

while not url.endswith('#'):
    # download web page
    response = requests.get(url)
    # throw if any exception
    response.raise_for_status()

    # Find the URL of the comic image.
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    comicImageObjectList = soup.select('div#comic > img')

    # if empty
    if comicImageObjectList == []:
        print("Couldn't find comic image.")
    else:
        imageUrl = 'https:' + comicImageObjectList[0].get('src')
    
        # Download the image.
        imageDownloadResponse = requests.get(imageUrl)
        imageDownloadResponse.raise_for_status()
   
        # Save the image to ./xkcd.
        imageFile = open(Path.cwd()/'projects'/'ComicOfflineDownload'/'xkcd'/Path(imageUrl).name, 'wb')

        for chunk in imageDownloadResponse.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    print(prevLink)

    url = 'https://xkcd.com' + prevLink.get('href')