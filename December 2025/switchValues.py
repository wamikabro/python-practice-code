a = 10
b = 23

print("Before switching:")
print("a:", a)
print("b:", b)

# switching values without using a temporary variable
a, b = b, a # it is called unpacking because right side is a tuple (b, a)

# After switching
print("After switching:")
print("a:", a)
print("b:", b)

# Explanation:
# it is same as 
a, b = (b, a) # right? Yes, it is. 
# so first (b, a) is evaluated to a tuple with current values of b and a
# then unpacked to a and b respectively
print("After switching again:")
print("a:", a)
print("b:", b)