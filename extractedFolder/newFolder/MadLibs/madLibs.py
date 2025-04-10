from pathlib import Path
import re
p = Path(Path.cwd(), 'projects', 'MadLibs')

findAdjectiveNounOrVerb = re.compile(r'ADJECTIVE|NOUN|VERB')

for textFilePathObj in p.glob('*.txt'):
    file = open(textFilePathObj, 'r')
    text = file.read()
    file.close()

    def askToChangeWhatMatched(match):
        wordToReplace = match.group(0) # Anything from ADJECTIVE NOUN or VERB
        return input(f'Enter a {wordToReplace}: ')
    # askToChangeWhatMatched function is implictly called by .sub()
    # on each iteration
    # and since it takes an argument 'match' as we saw above,
    # .sub will automatically pass the match to it
    # match is an object itself having the information of matched word

    # btw re.sub is an iterator within itself.
    # it will check and replace whole text before letting the loop continue
    newText = findAdjectiveNounOrVerb.sub(askToChangeWhatMatched, text)
    # this line will run after whole text has been checked and replaced

    # .name means name of file with extension
    newFileName = 'new' + textFilePathObj.name
    newFilePath = Path(p,"NewText",newFileName)

    newFileHandle = open(newFilePath, 'w')
    newFileHandle.write(newText)
    newFileHandle.close()
 
    