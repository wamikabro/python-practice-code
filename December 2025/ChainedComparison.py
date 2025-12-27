

a = 10
b = 11
c = 12

if a < b < c: # this condition is called chained comparison
    print("a is less than b and b is less than c")

if a < b and b < c: # with and operator
    print("a is less than b and b is less than c")

if a < b or b > c: # with or operator
    print("Either a is less than b or b is greater than c")