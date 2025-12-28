# concatinate lists with + and .extends

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Using + operator
concatenated_list = list1 + list2
print("Concatenated list using + operator:", concatenated_list)

# Using extend() method
list1.extend(list2)
print("List1 after extending with List2:", list1)