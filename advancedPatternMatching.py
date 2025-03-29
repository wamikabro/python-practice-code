import re

# () create different groups
# keep in these groups if whole pattern matches
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search('My number is 415-555-4242.')

print(mo.group(1)) # 415
print(mo.group(2)) # 555-4242
# group() is returning a tuple of multiple values
print(mo.group()) # 415-555-4242

# multiple assignment trick 
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

# pipeline / or 
# wamique or wasique
findOr = re.compile(r'Wamique|Wasique')

findWamique = findOr.search('My name is Wamique')
print(findWamique.group())
findWasique = findOr.search('My name is Wasique')
print(findWasique.group())

findFirstOccurance = findOr.search("Our names are Wamique and Wasique.")
print(findFirstOccurance.group())

# to find all use findall instead of search
findAllOccurances = findOr.findall('Our names are Wamique and Wasique.')
# no group anymore
print(findAllOccurances)


# bat + any of the following
# has 2 groups
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
batObj = batRegex.search('Batmobile lost a wheel')
print(batObj.group())


# Optional Matching ?
# Don't Match or match once
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group()) # Batman

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group()) # Batwoman
print(mo2.group(1)) # wo


# matching zero or more with asterisk
batRegex = re.compile(r'Bat(wo)*man')

mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group()) # Batman

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group()) # Batwoman

mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())


# matching once or more 
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())


mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None)


# matching specific repetitions with braces
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group()) # HaHaHa

mo2 = haRegex.search('Ha')
print(mo2 == None) # True

# greedy vs non greedy search
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group()) # 'HaHaHaHaHa'


nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHa')
print(mo2.group()) # HaHaHa

# non greedy better example
regex = re.compile(r'(Ha){3,5}?-xyz')
mo = regex.search('HaHaHaHaHa-xyz')

# it wasn't possible for even lazy to take 3 Ha only
# because technically it would've changed the word
print(mo.group()) # HaHaHaHaHa-xyz


# findall with groups.
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
# [('415', '555', '9999'), ('212', '555', '0000')]
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))