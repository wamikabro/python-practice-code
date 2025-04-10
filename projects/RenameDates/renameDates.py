import shutil, os, re
from pathlib import Path

datePattern = re.compile(r'''^(.*?)
((0|1)?\d-) # Month (MM): optional 0 or 1, and then a digit, and -
((0|1|2|3)?\d-) # Day (DD): optional 1,2,3,4, and then a digit, and -
((19|20)\d{2}) # Year (YYYY): either 19  or 20, then 2 more digits
(.*?)$''', re.VERBOSE)

# Loop over the files in the working directory.
for amerFilename in os.listdir('projects/RenameDates/Files'):
    mo = datePattern.search(amerFilename)

    # Skip files without a date.
    if mo == None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)
    
    # Form the European-style filename.
    euroFilename = beforePart + dayPart + monthPart + yearPart + afterPart
    # Get the full, absolute file paths.
    amerPathPlusFileName = Path(Path.cwd() / 'projects/RenameDates/Files' / amerFilename) # path+filename
    euroPathPlusFileName = Path(Path.cwd() / 'projects/RenameDates/Files' / euroFilename) # path+new File name
    print(amerPathPlusFileName)
    print(euroPathPlusFileName)

    # Rename the files.
    shutil.move(amerPathPlusFileName, euroPathPlusFileName)