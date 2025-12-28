# Using Reversed Object
sequence = ['p', 'y', 't', 'h', 'o', 'n']
reversed_seq = reversed(sequence)
print("Reversed object:", reversed_seq)
# Output: Reversed object: <reversed object at 0x...>
# Converting reversed object to a list
reversed_list = list(reversed_seq)
print("List from reversed object:", reversed_list)