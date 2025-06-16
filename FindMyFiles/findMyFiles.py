from pathlib import Path
import os, shutil
import pyinputplus as pyip
from datetime import datetime

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
:''', allowRegexes=[r'(?i)^(copy|move)$'], blockRegexes=[(r'.*', "Please enter 'copy' or 'move' only. Retry.")]).lower()

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



# Define generator and counter logic before your main if-block
def scanAndCollectForMove(sourcePath, fileType):
    counters = {
        'numberOfFoundFiles': 0,
        'numberOfMatchedFiles': 0,
        'potentialFilesNo': 0,
        'rejectedFilesNo': 0
    }
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
                    else:
                        counters['rejectedFilesNo'] += 1
    return generator(), counters

def scanAndCollectForDifferentDestination(sourcePath, destinationPath, fileType):
    counters = {
        'numberOfFoundFiles': 0,
        'numberOfMatchedFiles': 0,
        'sumOfFilesSize': 0
    }
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

    return generator(), counters, freeDriveSpaceInGB

if sourcePath.drive == destinationPath.drive and copyOrMove == 'move':
    potentialFilesGen, stats = scanAndCollectForMove(sourcePath, fileTypes[0])
    potentialFiles = list(potentialFilesGen)
    print(f"""------------------------------------
{stats['numberOfMatchedFiles']}/{stats['numberOfFoundFiles']} are {fileTypes[0]} files.
{stats['potentialFilesNo']}/{stats['numberOfMatchedFiles']} can be Moved, while 
{stats['rejectedFilesNo']}/{stats['numberOfMatchedFiles']} are over sized hence rejected.
------------------------------------""")

    yesOrNo = pyip.inputYesNo('Do you want to continue the Moving process (yes/no): ')
    if yesOrNo == 'yes':
        print('Moving...')
        # Create timestamped subfolder in destination
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        fileTypesStr = "_".join(fileTypes)
        operationFolderName = f"{copyOrMove}_{fileTypesStr}_{timestamp}"
        finalDestinationPath = destinationPath / operationFolderName
        finalDestinationPath.mkdir(parents=True, exist_ok=True)
        for filePath in potentialFiles:
            destFile = finalDestinationPath / filePath.name
            try:
                shutil.move(filePath, destFile)
                print(f'Moved: {filePath.name}')
            except Exception as e:
                print(f"❌ Failed to move {filePath.name}: {e}")
    else:
        print('You chose not to Move. See You.')
else:
    gen, counters, freeDriveSpaceInGB = scanAndCollectForDifferentDestination(sourcePath, destinationPath, fileTypes[0])
    file_list = list(gen)
    foundFiles = counters['numberOfFoundFiles']
    matchedFiles = counters['numberOfMatchedFiles']
    sumOfFilesSizeInGB = counters['sumOfFilesSize'] / (1024 ** 3)

    print(f"🔍 Total files scanned: {foundFiles}")
    print(f"✅ Matched files (.{fileTypes[0]}): {matchedFiles}")
    print(f"💾 Total size of matched files: {sumOfFilesSizeInGB:.2f} GB")
    print(f"📂 Free space on destination drive: {freeDriveSpaceInGB:.2f} GB")

    if sumOfFilesSizeInGB > freeDriveSpaceInGB:
        print(f"❌ Not enough space to {copyOrMove}")

        filesWithSizes = file_list
        biggerFirst = sorted(filesWithSizes, key=lambda x: x[1], reverse=True)
        smallerFirst = sorted(filesWithSizes, key=lambda x: x[1])
        defaultOrder = filesWithSizes

        def calculateHowManyCanFit(sortedList):
            count = 0
            totalSize = 0
            for path, size in sortedList:
                sizeInGB = size / (1024 ** 3)
                if totalSize + sizeInGB <= freeDriveSpaceInGB:
                    totalSize += sizeInGB
                    count += 1
                else:
                    break
            return count, totalSize

        countBig, sizeBig = calculateHowManyCanFit(biggerFirst)
        countSmall, sizeSmall = calculateHowManyCanFit(smallerFirst)
        countDefault, sizeDefault = calculateHowManyCanFit(defaultOrder)

        print(f"\n📊 {copyOrMove.title()} Options Based on Space:")
        print(f"1️⃣ Bigger Files First: {countBig} files ({sizeBig:.2f} GB)")
        print(f"2️⃣ Smaller Files First: {countSmall} files ({sizeSmall:.2f} GB)")
        print(f"3️⃣ Default Order: {countDefault} files ({sizeDefault:.2f} GB)")

        userChoice = pyip.inputMenu(['1', '2', '3'], numbered=False, prompt="\nHow would you like to proceed?\n")

        if userChoice == '1':
            selectedList = biggerFirst[:countBig]
        elif userChoice == '2':
            selectedList = smallerFirst[:countSmall]
        else:
            selectedList = defaultOrder[:countDefault]

        print(f"\n⚙️  You selected to {copyOrMove} {len(selectedList)} file(s).\n")

        yesOrNo = pyip.inputYesNo(f"Do you want to continue the {copyOrMove} process (yes/no): ")
        if yesOrNo == 'yes':
            print(f"{copyOrMove.title()}ing {len(selectedList)} file(s)...\n")
            # Create timestamped subfolder in destination
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            fileTypesStr = "_".join(fileTypes)
            operationFolderName = f"{copyOrMove}_{fileTypesStr}_{timestamp}"
            finalDestinationPath = destinationPath / operationFolderName
            finalDestinationPath.mkdir(parents=True, exist_ok=True)

            for filePath, size in selectedList:
                destFile = finalDestinationPath / filePath.name
                try:
                    if copyOrMove == 'copy':
                        shutil.copy2(filePath, destFile)
                        print(f"✅ Copied: {filePath.name}")
                    else:
                        shutil.move(filePath, destFile)
                        print(f"✅ Moved: {filePath.name}")
                except Exception as e:
                    print(f"❌ Failed to {copyOrMove} {filePath.name}: {e}")
        else:
            print("❌ Operation cancelled by user.")
    else:
        print(f"\n✅ Enough space. {copyOrMove.title()}ing all matched files...\n")
        # Create timestamped subfolder in destination
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        fileTypesStr = "_".join(fileTypes)
        operationFolderName = f"{copyOrMove}_{fileTypesStr}_{timestamp}"
        finalDestinationPath = destinationPath / operationFolderName
        finalDestinationPath.mkdir(parents=True, exist_ok=True)
        
        for filePath, size in file_list:
            destFile = finalDestinationPath / filePath.name
            try:
                if copyOrMove == 'copy':
                    shutil.copy2(filePath, destFile)
                    print(f"✅ Copied: {filePath.name}")
                else:
                    shutil.move(filePath, destFile)
                    print(f"✅ Moved: {filePath.name}")
            except Exception as e:
                print(f"❌ Failed to {copyOrMove} {filePath.name}: {e}")