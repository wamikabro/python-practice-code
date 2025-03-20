sentence = 'My name is lagan'

partitionedSentence = sentence.partition('is')

print(sentence) # my name is lagan
print(partitionedSentence)  # ('My name ', 'is', ' lagan')


# multiple assignment trick
before, separator, after = partitionedSentence 

print(before)
print(separator)
print(after)

# works on first occurence of separator

# if separator wasn't found then whole string will endup in first 
# element of the list, and 2nd and 3rd elements will stay empty
noSeparatorFound = 'Hello, world!'.partition('XYZ')
print(noSeparatorFound) # ('Hello, world!', '', '')