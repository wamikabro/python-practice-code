spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)

print()

for k in spam.keys():
    print(k)

print()

for i in spam.items():
    print(i)

print()

# both key and value variables in single for
for k, v in spam.items():
    print('Key: ' + k + 'Value: ' + str(v))


# check if a key or a value exists in dictionary
if 'color' in spam.keys():
    print('Color is in keys')

if 'red' in spam.values():
    print('Yes, Red color is in values')

if 'color' in spam:
    print("Yes color is in spam")