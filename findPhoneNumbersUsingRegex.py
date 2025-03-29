import re

# regex object created. 
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# printing an object calls repr() and passing the object to it
# it then tries to print in a good manner
# its just like toString in other languages
print(phoneNumberRegex)

# match object
mo = phoneNumberRegex.search('My 415-555-4241 number is 415-555-4242.')

# call group() on match object to return the match
print('Phone number found: ' + mo.group())

