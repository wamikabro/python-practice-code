import zipfile, os
from pathlib import Path

# open zip file
exampleZip = zipfile.ZipFile('zipFolder.zip')

print(exampleZip.namelist())

for file in exampleZip.namelist():
    print("Size: " + str(exampleZip.getinfo(file).file_size))
    print("Compressed Size: " + str(exampleZip.getinfo(file).compress_size))
    try:
        print(f'Compressed file is {round(exampleZip.getinfo(file).file_size / exampleZip.getinfo(file).compress_size, 2)}x smaller!')
    except:
        pass    


# extract everything from the archive
# will create folder if given destination folder doesn't exist
# if passed nothing, it will be exracted to cwd.
# it doesn't extract the main folder that was zipped, only files inside it
exampleZip.extractall("extractedFolder")

# extract single file 
# must give folder name too even if it was inside main folder, 
# optional: 2nd parameter is destination folder. will be created if doesn't exist
# exampleZip.extract('newFolder/bulletPointAdder.py', 'folderFolder')

exampleZip.close()


# compress a file 
# create a zip file with write mode
# pass a if you don't want to overwrite
newZip = zipfile.ZipFile('new.zip', 'w')
# tell file to zip, and the algorithm to be used to zip
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
#verify
newZip = zipfile.ZipFile('new.zip')
print(newZip.namelist())

