word = 'Hello'

# Hello with 10 length of String by adding 
# spaces on the right to justify the text to left
lJustWord = word.ljust(10) 
print(lJustWord)

# Hello with 10 length of String by adding 
# spaces on the LEFT to justify the text to RIGHT
rJustWord = word.rjust(10) 
print(rJustWord)

# justify text to left by adding asterisks
# to right on remaining length of string from 10
lJustWord2 = word.ljust(10, '*') 
print(lJustWord2)

# if you put string lenght less than or equal to 
# your string itself, nothing will change
lJustWord3 = word.ljust(3, '*') 
print(lJustWord3)

# it centers the text and given things on both sides
CenteredWord = word.center(10, '-')
print(CenteredWord)