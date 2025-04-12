import re, os
from pathlib import Path

deleteZipFiles = re.compile(r'projects_\d+')

for file in Path.cwd().glob('*zip'):
    if deleteZipFiles.fullmatch(file.stem):
        os.remove(file)
