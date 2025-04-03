import re
# number at least once, space, word character at least once
xmasRegex = re.compile(r'\d+\s\w+')

# in our given string there are multiple word characters
# don't confuse them as single word
# word 'drumers' will be missed because 
# 'dang' is 4 word characters, and then there's space character
# the next pattern match is on 11 then 

'''
['12 dang', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', 
'6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']
'''
print(xmasRegex.findall('12 dang drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 \
swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))


# Custom Character Class
# Vowels 
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))


# negative class
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))


# starts with
beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello, world!').group()) # Hello

# ends with
endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 2').group()) # 2


# starts and ends with
wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890').group())
# it fails because xyz is breaking the given pattern
# Unlike other regex searches, where a match can be found anywhere in the string,
# the ^ and $ force the entire string to be a match.
print(wholeStringIsNum.search('12345xyz67890') == None) # True


# wildcard '.' (dot) character
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))


# anything
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
 
print(mo.group(1)) # AI
print(mo.group(2)) # Sweigart

# non greedy everything vs greedy everything
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
# stops at first stop
print(mo.group()) # <To serve man>

# greedy 
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group()) # goes on an on until last stop


# New Line Accepted
newlineRegex = re.compile('<.*>', re.DOTALL)
mo = newlineRegex.search('<Hello Honey\nI am on new line!> it is not included.')
print(mo.group())

# Case Insensitive Matching
robocop = re.compile(r'robocop', re.I) # or re.IGNORECASE
rc = robocop.search('RoboCop is part man, part Machine, all Cop.')
print(rc.group())

# string substituting (replacement) using regex
# replace Agent + (1 or more characters available until space)
namesRegex = re.compile(r'Agent \w+')
# if used (r'Agent' \w+?') then only single character will 
# be replaced after Alice, because it will become non greedy
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

# secret CENSORING 
agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent \
Eve knew Agent Bob was a double agent.'))

# combination of re.IGNORECASE and re.DOTALL
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
result = someRegexValue.search('''
    So there we go foO # this is line 1
    Yeah how are you?
''')
print(result.group())