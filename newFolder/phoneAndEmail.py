import pyperclip, re

# US Based Phone Number
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # either 123 or (123) but optional
    (\s|-|.)? # either space, - or . but optional
    (\d{3}) # 3 digits 
    (\s|-|.) # separator
    (\d{4}) # 4 digits
    
    # This pattern is often used for phone number extensions in formats like:
    # 📞 555-123-4567 ext 987
    # 📞 555-123-4567 x1234
    # 📞 555-123-4567 ext. 99
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
                                            
    )''', re.VERBOSE)

# Email
# wamik.abro212@gmail.com
emailRegex = re.compile(r'''(
    (?<=\s) # Lookbehind assertion to ensure there's space before the email, but don't capture the space
    ([\w]+(?:\.[\w]+)*) # word + (. and words optional) 
    (@)
    ([A-Za-z]+)
    (.)
    ([A-Za-z]+)
    )''', re.VERBOSE)

copiedText = pyperclip.paste()

finalText = ""

phoneNumbersFound = phoneRegex.findall(copiedText)
for index in range(len(phoneNumbersFound)):
    finalText += "Phone Number " + str(index + 1) + ": " + str(phoneNumbersFound[index][0]) + '\n'

emailsFound = emailRegex.findall(copiedText)

for index in range(len(emailsFound)):
    finalText += "Email" + str(index+1) + ": " + str(emailsFound[index][0]) +'\n'


pyperclip.copy(finalText)
