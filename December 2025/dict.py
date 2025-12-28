# dict keys values and update
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Original dictionary:", my_dict)

# Getting keys
keys = my_dict.keys()
print("Dictionary keys:", keys)

# Getting values
values = my_dict.values()
print("Dictionary values:", values)

# Updating dictionary
my_dict.update({'d': 4, 'e': 5})
print("Updated dictionary:", my_dict)
# Output:
'''
Original dictionary: {'a': 1, 'b': 2, 'c': 3}
Dictionary keys: dict_keys(['a', 'b', 'c'])
Dictionary values: dict_values([1, 2, 3])
Updated dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
'''
