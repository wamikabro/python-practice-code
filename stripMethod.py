spam = '     Hello          '

stripLeft = spam.lstrip()
print(stripLeft)

stripRight = spam.rstrip() # we can not see the differfence in terminal
print(stripRight)

stripBothSides = spam.strip()
print(stripBothSides)

# all the occurences of o from the start and end removed
newString = 'ooooooooooHelloooooooo'
stripOutOFromBothSides = spam.strip('o')
print(stripOutOFromBothSides)
