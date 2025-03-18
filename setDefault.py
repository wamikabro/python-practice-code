# spam = {'name': 'Pooka', 'age': 5}
# if 'color' not in spam:
#    spam['color'] = 'black'

# vs

spam = {'name': 'Pooka', 'age': 5}
valueReturned = spam.setdefault('color', 'black') # what to check for, what to set if doesn't exist

print(valueReturned)
print(spam)

