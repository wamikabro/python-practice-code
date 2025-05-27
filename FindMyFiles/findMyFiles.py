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
def scanAndCollectForMove(sourcePath, fileType): # In this case, sourcePath and destinationPath are same
    # count all files, matched files, possible to move, impossible to move
    counters = {
        'numberOfFoundFiles': 0,
        'numberOfMatchedFiles': 0,
        'potentialFilesNo': 0,
        'rejectedFilesNo': 0
    }

    # Find free drive space
    freeDriveSpaceInGB = shutil.disk_usage(sourcePath.drive).free / (1024 ** 3)

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
    # returning calling functiopn to get generator object, that's how they work                    
    # returning counters, so counters are incremented when generator used
    # Still not memory efficient!
    return generator(), counters


# Generator function for Different Destination to determine how many files can be moved or copied
def scanAndCollectForDifferentDestination(sourcePath, destinationPath, fileType):
    counters = {
        'numberOfFoundFiles': 0,
        'numberOfMatchedFiles': 0,
        'sumOfFilesSize': 0 # bytes
    }

    # Find free drive space in Destination drive
    freeDriveSpaceInGB = shutil.disk_usage(destinationPath.drive).free / (1024 ** 3)

    def generator():
        for foldername, subfolders, filenames in os.walk(sourcePath):
            for filename in filenames:
                counters['numberOfFoundFiles'] += 1
                file_path = Path(foldername) / filename
                if file_path.suffix[1:] == fileType and file_path.is_file():
                    file_size = os.path.getsize(file_path)
                    counters['sumOfFilesSize'] += file_size
                    counters['numberOfMatchedFiles'] += 1
                    yield (file_path, file_size)

    return  generator(), counters, freeDriveSpaceInGB



# If Source and Destination Drive is same, and user wants to Move: 
if sourcePath.drive == destinationPath.drive and copyOrMove == 'move':
    
    # Use your generator-based function
    potentialFilesGen, stats = scanAndCollectForMove(sourcePath, fileTypes[0])
    
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
            # TODO: Create folder, following some naming scheme, checking if name already exists etc
            # shutil.move(filePath, destinationPath / filePath.name)
            print(f'Moving: {filePath.name}')
    else:
        print('You chose not to Move. See You.')


#TODO: Else if destination is different for Move or it's Copy, then do    
# Calculate sum of all the file sizes, and check if the drive has capacity to hold all those files
else:
    gen, counters, freeGB = scanAndCollectForDifferentDestination(sourcePath, destinationPath, fileTypes[0])

    # Force the generator to run (consume all items)
    file_list = list(gen)

    foundFiles = counters['numberOfFoundFiles']
    matchedFiles = counters['numberOfMatchedFiles']
    sumOfFilesSizeInGB = counters['sumOfFilesSize'] / (1024 ** 3)

    # Print summary
    print(f"🔍 Total files scanned: {foundFiles}")
    print(f"✅ Matched files (.{fileTypes[0]}): {matchedFiles}")
    print(f"💾 Total size of matched files: {sumOfFilesSizeInGB:.2f} GB")
    print(f"📂 Free space on destination drive: {freeGB:.2f} GB")


    #if sumOfFilesSizeInGB > freeDriveSpaceInGB:
        #print("❌ Not enough space to", copyOrMove)
        
        # If the destination drive has no enough capacity, then look how much capacity it has
        # based on that tell the user They can't move/copy all files, 
        # But they can move/copy if they want to move/copy smallest files, ## out of ## files will be moved/copied
        # If they want to move/copy large files, ## out of ## files will be moved/copied
        # if they want to cancel it just tap cancel
    #else:
        #TODO: copy or move as suggested
        #pass