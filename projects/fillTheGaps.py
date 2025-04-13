# program to fill the gaps by sorting the numbering in the file names in a folder
from pathlib import Path
import os, shutil, re

def fillTheGaps(path):
    # make sure path is absolute
    path = Path.absolute(path)
    # regex to find specifically the file names ending with 3 digits
    # capturing whole name in 3 groups
    endingWithThreeNumbers = re.compile(r'^(.*?)(\d{3})(\.txt)$')
    
    previousMatchedFile = ''
    for file in path.glob('*.txt'):
        if endingWithThreeNumbers.match(file.name):
            matchedFile = endingWithThreeNumbers.match(file.name)
            # if previous path empty, put first found file in it
            if previousMatchedFile == '':
                previousMatchedFile = matchedFile
                # don't run this iteration further
                continue
            
            # otherwise compare last 3 letters of name (stem/capture group 2) of the file
            # with last 3 letters of the name (stem/capture group 2) of the previous file
            # by converting both to int, file's answer - previous File's answer
            # if the difference is of 1, everything alright, just put matchedFile to previousMatchedFile
            # if difference of more than 1, then int(previous)+1 or minus difference + 1 from file
            # if new answer of file is 1 in length, replace last, if 2, then replace last 2, if 3 then replace last 3.
            
            # if matchedFile last 3 number - previousMatchedFile last 3 numbers is 1
            # that means everything is okay. We need to move on
            if int(matchedFile.group(2)) - int(previousMatchedFile.group(2)) == 1:
                previousMatchedFile = matchedFile
            # difference is greater than 1
            elif int(matchedFile.group(2)) - int(previousMatchedFile.group(2)) > 1: 
                # correct numbering
                differenceCorrection = str(int(previousMatchedFile.group(2)) + 1)
                # if length of correct number is 1,2 or 3
                lengthOfDifference = len(differenceCorrection)
                # remove last number regarding length of difference from stem, 
                # add corrected number
                newNameForFile = matchedFile.group(1) + matchedFile.group(2)[:-lengthOfDifference] + differenceCorrection + matchedFile.group(3)
                # rename the file to new name
                shutil.move(file, path/newNameForFile)
                # but we lost our regex groups. we cant store
                # new name to previousMatchedFile now
                # beacause next iteration will cause error
                # because it will try to use it using group()

                # that's why we need to convert it into groups() again
                # by simply rematching it. and we already know
                # that it will definitly match, that's why we are 
                # inside here
                previousMatchedFile = endingWithThreeNumbers.match(newNameForFile)
               


fillTheGaps(Path(Path.cwd()/'projects'/'GapsFolder'))