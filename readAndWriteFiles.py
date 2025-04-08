from pathlib import Path

p = Path('spam.txt')

print(p.write_text('Hello, world!')) # number of characters written

print(p.read_text()) # read from the written file

# open() can take strings or path object
helloFile = open('spam.txt') # open spam.txt from THIS folder

# read file
helloContent = helloFile.read()
print(helloContent)

# read lines 
sonnetFile = open('sonnet29.txt')
# or sonnetFile = open('sonnet29.txt', 'r') 
# r (read) 
print(sonnetFile.readlines()) # list of lines

# write mode
# will be created if doesn't exist 
# because it's w (write) or a (append) mode
baconFile = open('bacon.txt', 'w')
baconFile.write('Hello, world!\n')
baconFile.close()

baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')

baconFile.close()

baconFile = open('bacon.txt')
print(baconFile.read())
baconFile.close()

