a = 10
b = 10

print(id(a) == id(b))  # True, because same ints get stored in same instance

c = None

print(c is None)  # True, because None is a singleton instance