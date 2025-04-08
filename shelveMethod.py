import shelve

cats = ['Zophie', 'Pooka', 'Simon']

# can't pass in Path to shelve.open(), only str
shelfFile = shelve.open('mydata')
shelfFile['cats'] = cats

# shelve.open('myData')['cats'] = ['Zophie', 'Pooka', 'Simon']

shelfFile.close()

# read from shelve
shelfFile = shelve.open('myData')
print(shelfFile['cats'])
shelfFile.close()

# we get view instead of lists, that's why we convert it to the list
# as we know we've views in databases
shelfFile = shelve.open('myData')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))


