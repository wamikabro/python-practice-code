from pathlib import Path
import re

p = Path(Path.cwd())

findRegex = re.compile(input("What to Find: "))

for textFile in p.glob('*.txt'):
    file = open(textFile, 'r')
    text = file.read()

    try:
        textFound = findRegex.findall(text)
        if textFound:
            print(textFile.name + ":")
            print(textFound)
    except:
        pass