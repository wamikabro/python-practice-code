# in sequenced files e.g. spam001.txt, spam002.txt, create place for the file to add
# if file to add is e.g. spam002.txt, then rename files from spam002.txt
# increment all them by 1. And then add your desired file i.e. spam002.txt

from pathlib import Path
import os, shutil, re

def gapAdder(path):
    # make sure path is absolute
    path = Path.absolute(path)

    # what file to add
    fileToAddName = 'spam002.txt'

    # regex to accept all these kind of files
    endingWithThreeNumbers = re.compile(r'^(.*?)(\d{3})(\.txt)$')

    # file to add name regex match object
    # group(2) has the number of the file e.g. 002
    moOfFileToAdd = endingWithThreeNumbers.match(fileToAddName)
    
    os.mkdir(Path.cwd()/'projects'/'GapsFolder'/'tempDir')
    tempDirPath = Path.cwd()/'projects'/'GapsFolder'/'tempDir'
    print(tempDirPath)
    
    for file in path.glob('*.txt'):
        if endingWithThreeNumbers.match(file.name):
            
            matchedFile = endingWithThreeNumbers.match(file.name)

            if int(matchedFile.group(2)) < int(moOfFileToAdd.group(2)):
                shutil.move(file, tempDirPath)

            elif int(matchedFile.group(2)) >= int(moOfFileToAdd.group(2)):
                change = str(int(matchedFile.group(2)) + 1)
                # if length of correct number is 1,2 or 3
                length = len(change)
                # remove last number regarding length of difference from stem, 
                # add corrected number
                newNameForFile = matchedFile.group(1) + matchedFile.group(2)[:-length] + change + matchedFile.group(3)
                
                # rename the file to new name
                shutil.move(file, tempDirPath/str(newNameForFile))

    # Create the user's demanded file in GapsFolder            
    newFile = open(Path.cwd()/'projects'/'GapsFolder'/fileToAddName, 'w')
    newFile.write('Hello')

    # now move everyting from tempDir to the parent GapsFolder back
    source = Path.cwd()/'projects'/'GapsFolder'/'tempDir'
    destination =  Path.cwd()/'projects'/'GapsFolder'
    for item in source.iterdir():
        shutil.move(str(item), str(destination))
    
    # delete tempDir because it's empoty now
    os.rmdir(Path.cwd()/'projects'/'GapsFolder'/'tempDir')

gapAdder(Path(Path.cwd()/'projects'/'GapsFolder'))