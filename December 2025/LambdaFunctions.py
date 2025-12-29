# Basic exmple of Lambda Function
square = lambda x: x * x
print("Square of 5 using lambda function:", square(5)) # it's in variable but it doesn't have a name with def
# Output: 25

# Lambda function with multiple arguments
add = lambda x, y: x + y
print("Sum of 3 and 7 using lambda function:", add(3, 7))
# Output: 10

# Lambda function used as an argument to another function
def apply_function(func, value):
    return func(value)
result = apply_function(lambda x: x + 10, 5)
print("Result of applying lambda function to 5:", result)
# Output: 15

# Lambda function with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers from the list using filter and lambda:", even_numbers)
# Output: [2, 4, 6, 8, 10]

# Lambda function with reduce()
# what will be the product of all numbers in the list
# what will the reduce do? It will apply the lambda function cumulatively to the items of the iterable, from left to right, so as to reduce the iterable to a single value.
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print("Product of all numbers in the list using reduce and lambda:", product)
# Output: 3628800

# Reduce above is just like (without reduce)
product_manual = 1
for num in numbers:
    product_manual *= num
    print("Product of all numbers in the list without reduce:", product_manual)
# Output: 3628800

# Or simply
import math
product_math = math.prod(numbers)
print("Product of all numbers in the list using math.prod():", product_math)
# Output: 3628800
