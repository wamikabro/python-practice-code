# mcb.pyw - Saves and loads pieces of text to the clipboard.

# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard text to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword text to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb') # mcb = multi-clipboard

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    # check if argv[i] is in mcbShelf (keys)
    # because mcbShelf is Shelve database and it acts like a dictionary
    # and if we use 'in' on dictionary, its keys are checked 
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
