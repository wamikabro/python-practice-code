import pprint

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]

# returns us the whole thing but in str and pretiffied at the same time
formatedText = pprint.pformat(cats)

# storing a variable in it
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + formatedText + '\n' )

fileObj.close()

# the program that we just created by opening
# and had stored the variable in it
import myCats
print(myCats.cats)