import random

guesses = ''
turns = 12

words = ['python', 'java', 'ruby', 'javascript', 'php', 'csharp', 'swift', 'html', 'css', 'cplus']
word = random.choice(words)

print("Guess the programming language challenge.")
name = str(input("What's your name: "))

print('Best of luck with the game', name)


while turns > 0:
    
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=" ")
        elif char not in guesses: # or we could say else: simply
            print("_", end=" ")
            failed += 1
    print('\n') # two lines gap
    
    if failed == 0:
        print(f'You Win!\nThe word is {word}.')
        break

    character = input('Guess the Character: ')[:1]

    if character in word:
        guesses+= character
    else: 
        turns -= 1
        if turns > 0:
            print(f"Wrong Character\nYou've {turns} turns left.")
        else:
            print(f"You Lost.\nThe word was {word}.")
    
    