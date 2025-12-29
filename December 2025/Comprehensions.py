# List comprehensions examples
squares = [x**2 for x in range(10)] # List of squares from 0 to 9
print("List of squares from 0 to 9:", squares)

# list comprehension from existing list
original_list = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in original_list] # Doubling each element
print("Doubled list:", doubled)

# list comprehension with condition
even_squares = [x**2 for x in range(10) if x % 2 == 0] # Squares of even numbers only
print("Squares of even numbers from 0 to 9:", even_squares)

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row] # Flattening a 2D matrix
print("Flattened matrix:", flattened)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Set comprehension
unique_squares = {x**2 for x in range(-5, 6)} # Set of unique squares from -5 to 5
print("Set of unique squares from -5 to 5:", unique_squares)

# Dictionary comprehension
square_dict = {x: x**2 for x in range(6)} # Dictionary of numbers and their squares
print("Dictionary of numbers and their squares:", square_dict)

# Mapping without map()
nums = [1, 2, 3, 4, 5]
cubed = [x**3 for x in nums] # Cubing each element
print("Cubed list:", cubed)

# Mapping with map function
cubed_map = list(map(lambda x: x**3, nums))
print("Cubed list using map():", cubed_map)

# length of all strings in a list using comprehension
strings = ["apple", "banana", "cherry"]
lengths = [len(x) for x in strings]
print("Lengths of strings:", lengths)

# length of all strings in a list using map
lengths_map = list(map(len, strings))
print("Lengths of strings using map():", lengths_map)

# location mapping using comprehension and enumerate
locations = ["New York", "Los Angeles", "Chicago"]
location_dict = {index: city for index, city in enumerate(locations)}
print("Location mapping using comprehension:", location_dict)