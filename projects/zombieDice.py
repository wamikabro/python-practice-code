import random
import sys
import time

# list or cup of all the dice available
# like: ['green', 'green', 'green', 'green', 'green', 'green', 'red', ... ]
diceCup = ['green'] * 6 + ['yellow'] * 4 + ['red'] * 3

# probability of choosen dice
greenDice = ['brain', 'brain', 'brain', 'footstep', 'footstep', 'shotgun']
yellowDice = ['brain', 'brain', 'footstep', 'footstep', 'shotgun', 'shotgun']
redDice = ['brain', 'brain', 'footstep', 'footstep', 'shotgun', 'shotgun', 'shotgun']

def drawDice(diceCup, noOfDiceToDraw=3):
    # shuffle the list each time before drawing
    random.shuffle(diceCup)

    # draw and remove the dice 
    # you can't directly use diceCup.pop(dice) because pop() expects an index, not a value.
    drawnDice = [diceCup.pop(diceCup.index(dice)) for dice in random.sample(diceCup, noOfDiceToDraw)]
    print('Drawn Dice: ', drawnDice)

    return drawnDice

def rollThreeDice(drawnDice):
    result = []

    for dice in drawnDice:
        if dice == 'green':
            result.append((random.choice(greenDice), 'green'))

        elif dice == 'yellow':
          result.append((random.choice(yellowDice), 'yellow'))

        else: 
            result.append((random.choice(redDice), 'red'))

    print('Rolled Dice: ', result)
    return result

noOfDiceToDraw = 3
brainList = []
shotgunList = []
drawnDice = drawDice(diceCup)
while True:
    # add some delay and line space after each iteration 
    time.sleep(1)
    print()

    def playGame(brainList, shotgunList, drawnDice):
        result = rollThreeDice(drawnDice)

        tempListOfFootstepDice = []
        for diceResult in result:
            if diceResult[0] == 'brain':
                brainList.append(diceResult)
            elif diceResult[0] == 'shotgun':
                shotgunList.append(diceResult)
                # footstepgreen, footstepred, footstepyellow
            elif diceResult[0] == 'footstep':
                # store the color of the dice with footsteps
                tempListOfFootstepDice.append(diceResult)

        if len(shotgunList) >= 3:
            print("Alas! You've lost every Brain, because you're dead of 3 shotguns.")
            sys.exit()

        # wanna continue or not? True = Wanna Continue
        # 90% chances that bot will choose yes, because there are 9 True and 1 False
        if random.choice([True] * 9 + [False]) == True:
            # if dice in cup is less than needed 
            # basically if we have footstep, we reroll it with other dice
            # and we draw dice only to make our dice 3 so we can roll
            if len(diceCup) < (3 - len(tempListOfFootstepDice)):
                # put back all the dice that show brain in the cup so we can reuse them
                # but we will keep our counter of eaten brains for sure
                for brain in brainList:
                    # add color of dice back to the cup
                    diceCup.append(brain[1])
                print('All brain dice added back to the cup.')
                print('Because 13 dice were already used.')
            
            # return new newDiceToRoll to the caller so it rewrite the drawnDice 
            # so in the next iteration these new dices are used 
            newDiceToRoll = drawDice(diceCup, 3-len(tempListOfFootstepDice))
            for footstep in tempListOfFootstepDice:
                newDiceToRoll.append(footstep[1])
            
            print('New Dice To Roll: ', newDiceToRoll)
            return newDiceToRoll
                

        else:
            print("Bot doesn't want to continue")
            print("Brain eaten by you are: ", len(brainList))
            sys.exit()

    # rerun the whole execution but each time with new drawn dice.
    drawnDice = playGame(brainList, shotgunList, drawnDice)
            







'''

dicesInCup = {
    'green': 6,
    'yellow': 4,
    'red': 3
} 

# probability of a dice getting picked from a cup
SingleDiceDrawingProbability = {
    # green are 6, yellow are 4 and red are 3 totals to 13
    'green' : 6/13, 'yellow': 4/13, 'red': 3/13
}

# probabability of drawing 3 dice of specific combination from the cup


# probability of getting this result 
ThreeDiceRollingProbability = {
        # 6 sides (3 brains, 2 footsteps, 1 shotguns)
        'green': {'brain': 3/6, 'footsteps': 2/6, 'shotguns': 1/6},
        # 6 sides (1 brains, 2 footsteps, 3 shotguns)
        'red': { 'brain': 1/6, 'footsteps': 2/6, 'shotguns': 3/6},  
        # 6 sides (2 brains, 2 footsteps, 2 shotguns)
        'yellow': {'brain': 2/6, 'footsteps': 2/6, 'shotguns': 2/6}
        }

'''