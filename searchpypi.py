#! python3
# searchpypi.py  - Opens several search results.

import requests, sys, webbrowser, bs4

print('Searching...') # display text while downloading the search result page
res = requests.get('https://github.com/search?q='+ ' '.join(sys.argv[1:]))

res.raise_for_status()


# change data to html DOM
soup = bs4.BeautifulSoup(res.text, 'html.parser')



# Step 1: Select all elements that have the class (even if not alone)
all_matches = soup.select('.prc-Link-Link-85e08')

# Step 2: Filter only those that have exactly that class and no others
# If less matches found than 10, then less will be stored
results = [el for el in all_matches if el.get('class') == ['prc-Link-Link-85e08']][:10]


for objectNumber in range(len(results)):
    url = "github.com" + results[objectNumber].get('href')
    print("Opening: " + url)
    # Open a browser tab for each result.
    webbrowser.open(url)