import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# type of res is response object just like promises in js
print(type(res))
# to check if response was successful
print(res.status_code == requests.codes.ok)
# length of text received in response
print(len(res.text))

print(res.text[:251])

# to check if there was any exception. If none then None!
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))