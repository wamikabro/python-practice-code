# tuple
a = (1, 2, 3, 4, 5)
print("Tuple a:", a)

# unpacking tuple
x, y, z, p, q = a
print("Unpacked values:", x, y, z, p, q)

# tuple in tuple
b = (1, 2, (3, 4), 5)
print("Tuple b:", b)

# unpacking tuple in tuples too
m, n, (o, r), s = b # missing brackets around (o, r) will give error
print("Unpacked values from b:", m, n, o, r, s)