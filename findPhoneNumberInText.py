def isPhoneNumber(text):
    if len(text) != 12:
        return False
    
    for i in range (0, 12):

        if i == 3 or i == 7:
            if text[i] == '-':
                continue
            else: 
                return False

        if not text[i].isdecimal():
            return False

    return True   


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
