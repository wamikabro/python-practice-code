def collatz(number):
    if number % 2 == 0:
        value = number//2
        print(value)
        return value
    else:
        value = 3 * number + 1
        print(value)
        return value
try:
    collatz(int('fsdf'))
except TypeError: # if we didn't convert to int by using int() and the exception caused by if statement while trying to take out % of non integer
    print("Value Passed must be an Integer")
except ValueError: # error returned by int() on getting non integer
    print('Value Passed must be an Integer')