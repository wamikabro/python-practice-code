import copy

nestedList1 = [1,2]
nestedList2 = [3,4]

list1 = [nestedList1, nestedList2] # 2D List

shallowCopy = copy.copy(list1) # only copied 1D, and using same nestedLists.
deepCopy = copy.deepcopy(list1) # even made copy of nested lists.

print("list1: ", list1)
print("NestedList1: ", nestedList1)
print('NestedList2: ', nestedList2)
print("shallowCopy: ", shallowCopy)
print("deepCopy: ", deepCopy)


nestedList1[0] = 'changed'

print('\n')
print('After making changes to the nestedList1')
print('\n')


print("list1: ", list1)
print("NestedList1: ", nestedList1)
print('NestedList2: ', nestedList2)
print("shallowCopy: ", shallowCopy)
print("deepCopy: ", deepCopy)