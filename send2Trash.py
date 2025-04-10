import time
import send2trash

baconFile = open('bacon.txt', 'a') # created a file
baconFile.write('Bacon is not a vegetable.')

baconFile.close()

time.sleep(2)

send2trash.send2trash('bacon.txt')