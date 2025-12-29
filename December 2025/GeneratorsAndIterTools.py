import itertools 

first_letter = lambda x: x[0] # lambda function to get first letter of a string

# Using itertools.groupby() to group items based on the first letter
words = ['apple', 'banana', 'apricot', 'blueberry', 'cherry', 'avocado']
grouped_words = itertools.groupby(words, first_letter)
for key, group in grouped_words:
    print(f"{key}: {list(group)}")
# Output:
'''
a: ['apple', 'apricot', 'avocado']
b: ['banana', 'blueberry']
c: ['cherry']
'''
