# Creating Sets
# Demonstrating the creation of sets in Python

# Creating a set from a list with duplicate elements
my_list = [1, 2, 2, 3, 4, 4, 5]
my_set = set(my_list)
print("Set created from list (duplicates removed):", my_set)

# Creating a set using curly braces
another_set = {5, 6, 7, 8, 8, 9} # it looks like a dictionary but without key-value pairs it's a set
print("Set created using curly braces (duplicates removed):", another_set)

# Creating an empty set
empty_set = set()
print("Empty set:", empty_set)

# Creating a set from a string
string_set = set("hello")
print("Set created from string (unique characters):", string_set)
# Output: Set created from string (unique characters): {'h', 'e', 'l', 'o'}

# Creating a set from a tuple
tuple_set = set((1, 2, 3, 3, 4))
print("Set created from tuple (duplicates removed):", tuple_set)
# Output:
'''
Set created from list (duplicates removed): {1, 2, 3, 4, 5}
Set created using curly braces (duplicates removed): {5, 6, 7, 8, 9}
Empty set: set()
Set created from string (unique characters): {'h', 'e', 'l', 'o'}
Set created from tuple (duplicates removed): {1, 2, 3, 4}
'''