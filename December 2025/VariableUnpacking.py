# A common use of variable unpacking is iterating over sequences of tuples or lists:
data = [(1,2,3), (4,5,6), (7,8,9)]

# using f-strings 
for x, y, z in data:
    print(f"x: {x}, y: {y}, z: {z}")

print()  # line break

# or by using format
for x, y, z in data:
    print("x: {0}, y: {1}, z: {2}".format(x, y, z))
