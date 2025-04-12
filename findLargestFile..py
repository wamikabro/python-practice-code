# find greatest file by size in the given drive or folder
from pathlib import Path
import os

def findLargestFile(path):
    print('Please be patient, calculations may take a while...')
    # Make sure its the absolute path
    path = Path.absolute(path)
    
    # greatest file by size's path
    greatestFile = ''

    #TODO: use os.walk to walk through all the files
    # keep first file in greitestFile in starting
    # to find the greatest file by size, keep on comparing
    # each file with the greatest file's size, if file size is greater
    # greatest fiie name gets updated to new files name, otherwise continue
    for foldername, subfolders, filenames in os.walk(path):
        for file in filenames:
            if greatestFile == '':
                greatestFile = Path(Path(foldername)/file)
                continue
            
            currentFile = Path(os.path.join(foldername, file))
            # if current file size is greater than greatestFile's size
            if os.path.getsize(currentFile) > os.path.getsize(greatestFile):
                # set current file as new greatestFile
                greatestFile = currentFile
                
    file_size_in_gbs = os.path.getsize(greatestFile) / 1024 / 1024 / 1024
    print(f"Greatist File in {path}: {greatestFile}")
    print('Its size is: %d gbs' %file_size_in_gbs)

findLargestFile(Path('D:/'))