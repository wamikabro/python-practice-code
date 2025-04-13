from pathlib import Path
import os, shutil

def findAllPdfs(path):
    # make sure the path is absolute
    path = Path.absolute(path)
    # create directory in current working directory 
    pathToFolder = Path.cwd()/'projects/AllPdfs'
    os.mkdir(pathToFolder)    
    
    # walk thorugh all files using os.walk
    #for foldername, subfolders, filenames in os.walk(path):
    #    for file in filenames:
    #        if Path(file).suffix == '.pdf':
    #            print(file)
    
    # or we could've simply used .rglob (recursive glob) to find all the .pdf 
    for file in path.rglob('*.pdf'):
        shutil.copy(file,pathToFolder)
        


findAllPdfs(Path('D:/'))