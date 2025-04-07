from pathlib import Path

import os

print(Path.cwd()) # cwd: current working directory


# there's no way to change directory using pathlib (modern lib) because 
# its dangerous to change directory while program is running
os.chdir('C:\\Windows\\System32') # chdir: change directory

print(Path.cwd())
print(os.getcwd()) # older way


print(Path.home()) # get home folder of user


# create waffles folder inside walnut
# if walnut doesn't exist, create it too, 
# same for delicious
# os.makedirs('C:\\delicious\\walnut\\waffles')


print(Path.cwd().is_absolute())
print(Path('spam/bacon/eggs').is_absolute())

# relative path
print(Path('my/relative/path'))
# make relative path absolute
print(Path.cwd() / Path('my/relative/path')) # / used for Path concatination here

# or use this way 
print(os.path.abspath('my/relative/path')) # or print(os.path.abspath(Path('my/relative/path')))
print(os.path.isabs('my/relative/path')) # check if absolute

# get related path from the 'start': which is supposed to be second argument
# we haven't passed start, that means it will use cwd as start path
# which is the same position where we're stanidng. 
# so it will show single dot '.'
print(os.path.relpath(Path.cwd())) 