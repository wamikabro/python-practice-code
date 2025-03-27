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

'''
    if len(text) != 12:
        return False
    
    for i in range (0, 3):
        if not text[i].isdecimal():
            return False
        
    if text[3] != '-':
        return False
    
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    
    if text[7] != '-':
        return False
    
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
'''    


print(isPhoneNumber('413-555-4242'))

print(isPhoneNumber('4-325552-242'))
