# Generator expression to produce squares of numbers from 0 to 9
squares = (x**2 for x in range(10))


print(squares)


listOfSquares = list(squares)

print(listOfSquares)