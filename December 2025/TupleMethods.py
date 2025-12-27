# tuple methods
a = (5, 2, 3, 2, 4, 2, 1)
print("Original tuple a:", a)
# count method
count_of_2 = a.count(2)
print("Count of 2 in a:", count_of_2)
# index method
index_of_4 = a.index(4)
print("Index of 4 in a:", index_of_4)
# trying to find index of an element not in tuple will raise ValueError
# index_of_10 = a.index(10)  # Uncommenting this line will raise an error
