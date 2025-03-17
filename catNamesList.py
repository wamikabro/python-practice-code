catNames = []

while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()

    if name == '':
        break

    catNames.append(name)
    # catNames = catNames + [name] # concatinating single name list to old list
print('The cat names are:')

for name in catNames:
    print(name)