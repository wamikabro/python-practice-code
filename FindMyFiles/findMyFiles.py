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
# Define generator and counter logic before your main if-block
def scanAndCollectForMove(sourcePath, fileType, freeDriveSpaceInGB):
    counters = {
        'numberOfFoundFiles': 0,
        'numberOfMatchedFiles': 0,
        'potentialFilesNo': 0,
        'rejectedFilesNo': 0
    }

    def generator():
        for foldername, subfolders, filenames in os.walk(sourcePath):
            for filename in filenames:
                counters['numberOfFoundFiles'] += 1 
                filePath = Path(foldername) / filename
                fileSizeInGB = os.path.getsize(filePath) / (1024 ** 3)
                if Path(filename).suffix[1:] == fileType:
                    counters['numberOfMatchedFiles'] += 1
                    if freeDriveSpaceInGB >= fileSizeInGB: 
                        counters['potentialFilesNo'] += 1
                        yield filePath
                    elif freeDriveSpaceInGB < fileSizeInGB:
                        counters['rejectedFilesNo'] += 1
    return generator(), counters


# If Source and Destination Drive is same, and user wants to Move: 
if sourcePath.drive == destinationPath.drive and copyOrMove == 'move':
    
    freeDriveSpaceInGB = shutil.disk_usage(sourcePath.drive).free / (1024 ** 3)
    
    # Use your generator-based function
    potentialFilesGen, stats = scanAndCollectForMove(sourcePath, fileTypes[0], freeDriveSpaceInGB)
    
    # Convert generator to list so we can reuse it after asking user
    potentialFiles = list(potentialFilesGen)

    # Unpack counters
    numberOfFoundFiles = stats['numberOfFoundFiles']
    numberOfMatchedFiles = stats['numberOfMatchedFiles']
    potentialFilesNo = stats['potentialFilesNo']
    rejectedFilesNo = stats['rejectedFilesNo']

    print(f'''------------------------------------
{numberOfMatchedFiles}/{numberOfFoundFiles} are {fileTypes[0]} files.
{potentialFilesNo}/{numberOfMatchedFiles} can be Moved, while 
{rejectedFilesNo}/{numberOfMatchedFiles} are over sized hens rejected.
------------------------------------''')

    yesOrNo = pyip.inputYesNo('Do you want to continue the Moving process (yes/no): ')
    if yesOrNo == 'yes':
        print('Moving...')
        for filePath in potentialFiles:
            #shutil.move(filePath, destinationPath / filePath.name)
            print(f'Moveding: {filePath.name}')
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


