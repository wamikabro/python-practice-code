import re, pyperclip

# DD/MM/YYYY
dateDetect = re.compile(r'''(
# independent either 01 to 09
    # or 1 or 2 with 0 to 9
        # or 3 with 0 or 1
(\b0[1-9]|[12][0-9]|[3][01]) # 01 - 31
(/)
(0[1-9]|1[0-2]) # 01 - 12
(/)
([12]([0-9]{3})) # 1000 - 2999
)
''', re.VERBOSE)

copiedText = pyperclip.paste()

rawDates = []
datesTuple = dateDetect.findall(copiedText)

for dateTupleIndex in range(len(datesTuple)):
    rawDates.append(datesTuple[dateTupleIndex][0])

def leapYearValidator(year):
      return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def dateValidator(givenDateAsList): # [DD,MM,YYYY]
    day = int(givenDateAsList[0])
    month = int(givenDateAsList[1])
    year = int(givenDateAsList[2])

    match month:
        case 4|6|9|11:
            if not day <= 30:
                return False
        case 2:
            if leapYearValidator(year):
                if not day <= 29:
                    return False
            else:
                if not day <= 28:
                    return False    
        case _: # default case 1,3,5,7,8,10,12
            if not day <= 31:
                return False
    return True

validatedDates = []
for rawDate in rawDates:
    tempDateAsList = rawDate.split('/')
    if dateValidator(tempDateAsList):
        validatedDates.append(rawDate)
    
finalText = '''List of Validated Dates'''
for index in range(len(validatedDates)):
    finalText += '\nDate ' + str(index+1) + ": " + validatedDates[index]

pyperclip.copy(finalText)
