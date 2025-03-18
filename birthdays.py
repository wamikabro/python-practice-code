birthdays = {'moazzam': 'June 5', 'sarim': 'March 17', 'wasik': 'April 17'}

while True: 
    print('Enter a name: (blank to quit)')
    name = input().lower()

    if name == '':
        break

    if name in birthdays: 
        print(birthdays[name] + ' is the birthday of ' + name)

    else: 
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()

        birthdays[name] = bday
        print('Birthday database updated.')