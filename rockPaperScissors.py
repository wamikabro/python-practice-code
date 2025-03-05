import random, sys

print("ROCK, PAPER, SCISSORS")

wins = losses = ties = 0

while True:
    print(wins, "Wins", losses, "Losses", ties, "Ties")
    choice = input('Enter your move:\n(r)ock (p)aper (s)cissors or (q)uit: ')
    computerChoice = random.choice(('r','p','s'))
    
    if choice not in ('r', 'p', 's', 'q'):
        pass # do nothing
    elif computerChoice == choice:
        ties += 1
    elif computerChoice == 'r' and choice == 'p' or computerChoice == 'p' and choice == 's' or computerChoice == 's' and choice == 'r':
        wins += 1
        print('You Win!')
    elif computerChoice == 'p' and choice == 'r' or computerChoice == 's' and choice == 'p' or computerChoice == 'r' and choice == 's':
        losses += 1
        print('You Lost :(')
    else:
        print('You Quit.')
        sys.exit()

    
    