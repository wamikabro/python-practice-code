import pyinputplus as pyip

def addsUpToTen(numbers):
    numbersList = list(numbers)

    # convert all elements to integer one by one
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)

    # sum all the elements and check if they're equal to 10
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.' %(sum(numbersList)))
    
    return int(numbers) # Return an int form of numbers.

# no parantheses after addsUpToTen, because we don't want to call, but pass the function
response = pyip.inputCustom(addsUpToTen) 
