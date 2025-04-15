import requests, bs4

# returning the response object containing HTML of the web page
res = requests.get('https://nostarch.com')

res.raise_for_status()

# passing HTML of the web page to BeautifulSoup to parse
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')

# beautiful soup object
print(type(noStarchSoup))

# It will return list of Tag object containing all matches
elems = noStarchSoup.select('h2')

# how many elements
print(len(elems))

# print first tag object that contain child elements inside it if exists
print(elems[0])

# print text of first tag object
print(elems[0].getText()) 

# print attributes of first tag object
# dictionary containing separate lists of class and id attributes 
print(elems[0].attrs)