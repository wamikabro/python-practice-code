#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os
from pathlib import Path

def backupToZip(folderPath):
    # back up the entire contents of "folder" into a zip file

    folderPath = Path.absolute(folderPath) # make sure the path is absolute
    
    # figure out the filename this code should use based on
    # what files already exist
    number = 1 # start searching from 1 if zip file exists
    while True:
        print('1')
        zipFilename = os.path.basename(folderPath) + '_' + str(number) + '.zip'

        # causing issue on str etc
        #zipFilename = folderPath.stem + '_' + str(number) + '.zip'
        
        # if it doesn't exist, break the loop, because we've
        # new name for our zip file
        # time to store new snapshot in it!
        #if not zipFilename.exists():
        if not os.path.exists(zipFilename):
            break

        print('2')
        number = number + 1
        print('3')
    #Create the ZIP file.
    print(f'Creating {zipFilename}')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folderPath):
        print(f'Adding files in {foldername}')
        # add the current folder to the zip file.
        backupZip.write(foldername)

        # add all the files in this folder to the ZIP File
        for filename in filenames:
            newBase = os.path.basename(folderPath) + "_"
            # if it's folder_N.zip itself, don't backup it
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            # otherwise just add files of the folder into the folder in ZIP
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()

backupToZip(Path('projects'))