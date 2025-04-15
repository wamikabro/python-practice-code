import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

res.raise_for_status()

playFile = open('RomeoAndJuliet.txt', 'wb') # wb: write binary

for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()