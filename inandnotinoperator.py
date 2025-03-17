myPets = ['Sufi', 'Puki', 'Fattu']

print('Enter a pet name: ')
name = input()

# print(name in myPets) # it will return true of false

if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')