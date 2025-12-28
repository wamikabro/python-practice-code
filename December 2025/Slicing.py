seq = [7, 2, 3, 7, 5, 6, 0, 1]
print("Original list:", seq)

# Slicing example
print("Elements from index 2 to 5:", seq[2:6])  # from index 2 to 5
# Output: [3, 7, 5, 6]

# assigning with slicing
# changning elements from index 2 to 4
seq[2:5] = [8, 9, 10]
print("List after assigning [8, 9, 10] to indices 2 to 4:", seq)
# Output: [7, 2, 8, 9, 10, 6, 0, 1]

# either start of end defined
print("Elements from start to index 4:", seq[:5])  # from start to index 4
# Output: [7, 2, 8, 9, 10]

# double collon means step (jump) 
print("Elements from index 1 to 6 with step 2:", seq[1:7:2])  # from index 1 to 6 with step 2
# Output: [2, 9, 6]

# only step defined
print("Elements with step 3:", seq[::3])  # every 3rd element
# Output: [7, 9, 0]

# negative indexing
print("Last three elements using negative indexing:", seq[-3:])  # last three elements
# Output: [6, 0, 1]