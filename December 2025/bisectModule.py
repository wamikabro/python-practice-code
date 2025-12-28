import bisect 

list = [1, 3, 4, 4, 4, 4, 6, 7]

# Finding the insertion point for 5 to maintain sorted order
insertion_point = bisect.bisect(list, 5)

print("Insertion point for 5 in the list:", insertion_point)

# Inserting 5 into the list at the found insertion point
bisect.insort(list, 5)
print("List after inserting 5:", list)

# Unsorted list example
unsorted_list = [7, 2, 5, 3, 1, 4, 6]
# trying without sorting 
insertion_point_unsorted = bisect.bisect(unsorted_list, 5)
print("Insertion point for 5 in the unsorted list:", insertion_point_unsorted)
bisect.insort(unsorted_list, 5)
print("Unsorted list after inserting 5:", unsorted_list)