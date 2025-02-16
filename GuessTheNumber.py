import random


guess = random.randint(1, 100) # generate a random number between 1 to 100
number = 0

while guess != number:
    number = int(input("I am thinking about a number.\nGuess it from 1 to 100: "))
    if number < guess:
        print("lesser than the number")
    elif number > guess:
        print("greater than the number")
    else:
        print("you got it!")    