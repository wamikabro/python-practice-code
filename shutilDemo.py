import shutil, os
from pathlib import Path
import time

p = Path.cwd()

# copy spam.txt to projects folder
#shutil.copy(p / 'spam.txt', p / 'projects')

# duplicate spam.txt but rename it
#shutil.copy(p / 'spam.txt', 'newSpam.txt')

# duplicate spam.txt, rename it and place it inside projects folder
#shutil.copy(p / 'spam.txt', 'projects/newSpam.txt')

# duplicate whole folder with everything inside it and save with new name
# only if the new given name already exists the error will be thrown
#shutil.copytree(p/'projects', p/'newFolder')

# copy spam.txt to the given folder, and return new address
# give error if file already exists in the folder with same name.
#newAddress = shutil.move(p / 'spam.txt', p /'newFolder')

# rename the spam.txt to here.txt
# shutil.move(p / 'spam.txt', p / 'here.txt')


# if no folder name as, then there without extension will hold here.txt
#shutil.move(p / 'here.txt', p / 'there')

# move there to the projects folder and name it as thereYouGo.txt (extension)
# shutil.move(p / 'there', p / 'projects' / 'thereYouGo.txt')


# it will throw an exception because folder where we are moving to doesn't exist
# shutil.move(p/'newSpam.txt',p/'thisFolderDoesntExist/here.txt')

# create dir
os.mkdir(p/'uselessDirectory')
time.sleep(2)

# create a file inside uselessDirectory
uselessFile = open(p/'uselessDirectory'/'newFile.txt', 'w')
uselessFile.write("Hello")

# create another file inside uselessDirectory
uselessFile2 = open(p/'uselessDirectory'/'newFile2.txt', 'w')
uselessFile2.write('Hello')

time.sleep(5)

# remove a file from the uselessDirectory
# it doesn't workh here because things are 
# being mixed, and its being accessed by 2 things at the same time
#os.unlink(p/'uselessDirectory'/'newFile2.txt')

time.sleep(5)


# remove dir if it's empty
try : 
    os.rmdir(p/'uselessDirectory')
# otherwise remove directory if its not empty
except:
    shutil.rmtree(p/'uselessDirectory')



