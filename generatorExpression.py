# Generator expression to produce squares of numbers from 0 to 9
squares = (x**2 for x in range(10))


print(squares)

# yielding an element from the generator expression by consuming it using next() 
firstElement = next(squares)
print(firstElement)


listOfSquares = list(squares)

print(listOfSquares)