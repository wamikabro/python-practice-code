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
    number = 1 # start naming files from 1
    while True:
        zipFilename = folderPath.stem + '_' + str(number) + '.zip'
        
        if not folderPath.exists:
            break

        number = number + 1

        # TODO: Create the ZIP file.
        print(f'Creating {zipFilename}')
        backupZip = zipfile.ZipFile(zipFilename, 'w')

        # TODO: Walk the entire folder tree and compress the files in each folder.
        print('Done.')    


backupToZip(Path('projects'))