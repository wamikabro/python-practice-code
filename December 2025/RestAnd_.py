# *rest example
a = (1, 2, 3, 4, 5)

# unpacking with rest
x, y, *z = a
print("x:", x)
print("y:", y)
print("z (rest):", z) # z will be a list of remaining values

print()  # line break

# rest can also be in middle
x, *y, z = a
print("x:", x)
print("y (rest):", y) # y will be a list of remaining values
print("z:", z)

print()  # line break

# *_ can be used to ignore certain values
x, y, *_ = a
print("x:", x)
print("y:", y)
# here, all values except first two are ignored: Kind of Haha
print(_) # _ will be a list of ignored values