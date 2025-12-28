# Without using enumerate
seq = ['a', 'b', 'c', 'd', 'e']
i = 0
for item in seq:
    print(i, item)
    i += 1

# Output:
'''
0 a
1 b
2 c
3 d
4 e
'''

print() #----------------------------------------------------

# Using enumerate
for index, item in enumerate(seq):
    print(index, item)

# Output:
'''
0 a
1 b
2 c
3 d
4 e
'''