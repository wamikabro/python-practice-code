all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'],
             ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]

namesOfInterest = [name for sublist in all_data for name in sublist if name.count('e') > 1] # Nested list comprehension to find names with more than one 'e'
print(namesOfInterest)
# Output:
'''
['Steven']
'''