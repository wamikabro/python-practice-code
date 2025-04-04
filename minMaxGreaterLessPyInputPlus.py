import pyinputplus as pyip

response = pyip.inputNum('Enter num: ', blank=True)

print("You entered: ", response) if response else print("You didn't enter anything.")
# print("You entered:", response if response else "No input provided")



# pyip.inputNum('Enter num minimum 4: ', min=4)

# pyip.inputNum('Enter num greater than 4: ', greaterThan=4)

# pyip.inputNum('minimum 4, less than 6 345>', min=4, lessThan=6)

