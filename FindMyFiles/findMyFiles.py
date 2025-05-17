from pathlib import Path
import os, shutil
import pyinputplus as pyip

# Ask File Types
fileTypes = input('''Select File Type/s to Search For
    mp3
    mp4
    png 
    jpg
    gif
    pdf
    xls
    xlsx
    doc
    docx
    or any other file extension...
    note: you can type multiple file types with space in between
    e.g. mp3 mp4 pdf
      : ''').split(' ')
print()

# Ask Source Folder/Drive
while True:
    try:
        sourcePath = Path.absolute(Path(input('''What Drive/Folder to go through?
            (e.g. type 'D:/' or 'D:/Folder/SubFolder')
            note: please must add : after drive letter or else it will be mistaken to folder
            :''')))
    
        if not Path.exists(sourcePath):
            raise FileNotFoundError('\nError: Folder/Drive not found. Try Again.\n')
    
        break
    except FileNotFoundError as ex:
        print(ex)


# Ask if Copy or Move?
copyOrMove = pyip.inputStr('''You wanna Copy or Move?
(type 'copy' or 'move')
WARNING: Move will delete files from the Source. It's Risky.
:''',allowRegexes=[r'(?i)^(copy|move)$'],
blockRegexes=[(r'.*', "Please enter 'copy' or 'move' only. Retry.")]).lower()

# Ask Destination Folder/Drive
while True:
    try:
        destinationPath = Path.absolute(Path(input(f'''What Drive/Folder to {copyOrMove} found files in?
            (e.g. type 'D:/' or 'D:/Folder/SubFolder')
            :''')))
    
        if not Path.exists(destinationPath):
            raise FileNotFoundError('\nError: Folder/Drive not found. Try Again.\n')
    
        break
    except FileNotFoundError as ex:
        print(ex)

# Note: Use Iterators to keep track of file sizes, and know what to yield based on file sizes

# If Source and Destination Drive is same, and user wants to Move: 
if sourcePath.drive == destinationPath.drive and copyOrMove == 'move':
    numberOfFoundFiles = 0
    numberOfMatchedFiles = 0
    potentialFilesNo = 0
    rejectedFilesNo = 0
    
    # First go through all the files ONE BY ONE just checking that drive has enough space 
    freeDriveSpaceInGB = shutil.disk_usage(sourcePath.drive).free / (1024 ** 3)
    for foldername, subfolders, filenames in os.walk(sourcePath):
        for filename in filenames:
            numberOfFoundFiles += 1 
            fileSizeInGB = os.path.getsize(Path(foldername) / filename) / (1024 ** 3)
            # if file is of type that we're trying to find
            # and file is lesser or equal in to the available size of drive
            if Path(filename).suffix[1:] == fileTypes[0]:
                numberOfMatchedFiles += 1
                if freeDriveSpaceInGB >= fileSizeInGB: 
                    # to hold that single file copy by checking size of the file and remaining storage in drive
                    potentialFilesNo += 1
                elif freeDriveSpaceInGB < fileSizeInGB:
                    # count the files that can not be moved because they're heavier than the space available
                    rejectedFilesNo += 1
    print(f'''------------------------------------
{numberOfMatchedFiles}/{numberOfFoundFiles} are {fileTypes[0]} files.
{potentialFilesNo}/{numberOfMatchedFiles} can be Moved, while 
{rejectedFilesNo}/{numberOfMatchedFiles} are over sized hens rejected.
------------------------------------''')                
    # and ask the user if they wanna proceed with other files or cancel
    yesOrNo = pyip.inputYesNo('Do you want to continue the Moving process (yes/no): ')
    if yesOrNo == 'yes':
        #TODO: Move 
        print('Moving...')
    else:
        print('You chose not to Move. See You.')
        

#TODO: Else do    
# Calculate sum of all the file sizes, and check if the drive has capacity to hold all those files
# during that create an iterator that store list of file sizes and destinations, 
# If the destination drive has no enough capacity, then look how much capacity it has
# based on that tell the user They can't move/copy all files, 
# But they can move/copy if they want to move/copy smallest files, ## out of ## files will be moved/copied
# If they want to move/copy large files, ## out of ## files will be moved/copied
# if they want to cancel it just tap cancel


