# This program ssays hello n asks name
print('Hello, world!')

print('What is your name?')
name = input()

print('It is good to meet you, ' + name)

print('The length of your name is:')
print(len(name))

print('What is your age?')
age = input()

print('You will be ' + str(int(age) + 1)  + ' in a year.')

if name == 'Alice': # if name is
    print('Hi, Alice.')
elif age < 12: # if age is less than 12 and name is not Alice
    print('You are not Alice, kiddo.')