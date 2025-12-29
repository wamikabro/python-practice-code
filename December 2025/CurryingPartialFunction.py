# function currying and partial functions
# without partial 
def add(x, y):
    return x + y

def add_five(y):
    return add(5, y)

print("Adding 5 to 10 without partial:", add_five(10))  # Output: 15

# without partial but with lambda
add_five_lambda = lambda y: add(5, y)
print("Adding 5 to 10 with lambda:", add_five_lambda(10))
# Output: 15

# with partial
from functools import partial
add_five_partial = partial(add, 5)
print("Adding 5 to 10 with partial:", add_five_partial(10))
# Output: 15