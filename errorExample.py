import traceback
def spam():
    bacon()

def bacon():
    raise Exception('This is the error message.')

try: 
    spam()
except: 
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc()) # store traceback of the exception in file
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')

