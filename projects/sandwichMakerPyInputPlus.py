import pyinputplus as pyip
from tabulate import tabulate


print("Thanks for using Sandwich Maker\
    \nGet your custom sandwich")

breadTypePrompt = "Choose Type of Bread\n"
breadChoices = ['Wheat', 'White', 'Sourdough']

proteinTypePrompt = 'Choose Type of Protein\n'
proteinChoices = ['Chicken', 'Turkey', 'Ham', 'Tofu']

cheesePrompt = 'Want Cheese? Yes/No: '
cheeseTypePrompt = "Choose Type of Cheese\n"
cheeseChoices = ['Cheddar', 'Swiss', 'Mozzarella']

mayoPrompt = 'Do you want Mayo? Yes/No: '
mustardPrompt = 'Do you want Mustard? Yes/No: '
lettucePrompt = 'Do you want Lettuce? Yes/No: '
tomatoPrompt = 'Do you want Tomato? Yes/No: '

numberOfSandwichesPrompt = 'How many Sandwiches do you want: '


# inputMenu(choices, prompt='_default', default=None, blank=False, timeout=None, limit=None, strip=None, allowRegexes=None, blockRegexes=None, applyFunc=None, postValidateApplyFunc=None, numbered=False, lettered=False, caseSensitive=False)

breadChoice = pyip.inputMenu(breadChoices, breadTypePrompt, numbered= True)
proteinChoice = pyip.inputMenu(proteinChoices, proteinTypePrompt, numbered= True )

cheeseYesNo = pyip.inputYesNo(cheesePrompt)

if cheeseYesNo:
    cheeseChoice = pyip.inputMenu(cheeseChoices, cheeseTypePrompt, numbered=True)

mayoYesNo = pyip.inputYesNo(mayoPrompt)
mustardYesNo = pyip.inputYesNo(mustardPrompt)
lettuceYesNo = pyip.inputYesNo(lettucePrompt)
tomatoYesNo = pyip.inputYesNo(tomatoPrompt)



# Organizing the data for display
sandwich_summary = [
    ["Bread Type", breadChoice],
    ["Protein", proteinChoice],
    ["Cheese", cheeseChoice],
    ["Mayo", mayoYesNo],
    ["Mustard", mustardYesNo],
    ["Lettuce", lettuceYesNo],
    ["Tomato", tomatoYesNo]
]

# Displaying in a beautifully formatted table
print("\nYour Sandwich Order Summary:\n")
print(tabulate(sandwich_summary, tablefmt="fancy_grid"))