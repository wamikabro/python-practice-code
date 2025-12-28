# sorting lists 
list = ["hi", "apple", "banana", "cherry","bye"]
print("Original list:", list)

# Sort by length of the string using sorted() function
sorted_by_length = sorted(list, key=len)
print("Sorted by length:", sorted_by_length)

# by using .sort() method
list.sort(key=len)
print("List sorted in place by length:", list)

# sorting in reverse order
list.sort(key=len, reverse=True)
print("List sorted in place by length (reverse):", list)

# using lambda function as key
list.sort(key=lambda x: x[0])  # sort by first character
print("List sorted in place by first character:", list)