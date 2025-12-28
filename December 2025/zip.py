sequence1 = ['a', 'b', 'c']
sequence2 = [1, 2, 3]

# Using zip to combine sequences
zipped = zip(sequence1, sequence2)
print("Zipped object:", zipped)
# Output: Zipped object: <zip object at 0x...>

# Converting zipped object to a list of tuples
zipped_list = list(zipped)
print("List of tuples from zipped object:", zipped_list)
# Output: List of tuples from zipped object: [('a', 1), ('b', 2), ('c', 3)]

# Unzipping the list of tuples back into individual sequences
# Using the asterisk (*) operator to unzip
unzipped = zip(*zipped_list) 
unzipped_list1, unzipped_list2 = list(unzipped)
print("Unzipped sequence 1:", unzipped_list1)
print("Unzipped sequence 2:", unzipped_list2)
# Output: Unzipped sequence 1: ['a', 'b', 'c']
# Output: Unzipped sequence 2: [1, 2, 3]
# Note: The unzipping step works because we first converted the zipped object to a list of tuples.