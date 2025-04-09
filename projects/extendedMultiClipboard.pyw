# extendedMultiClipboard.pyw - Saves, loads and deletes the pieces of text to and from the clipboard.
# extendedMultiClipboard save <keyword> - to save what's in clipboard with given keyword
# extendedMultiClipboard list - to get the list of all the available keywords copied to the clipboard
# extendedMultiClipboard <keyword> - to get the value saved on the given keyword copied to the clipboard
# extendedMultiClipboard delete <keyword> - to delete the given keyword from the list
# extendedMultiClipboard deleteAll - to delete all the stored keywords from the list

import shelve, pyperclip, sys

mcbShelf = shelve.open('extendedMultiClipboard') # mcb = multi-clipboard


if len(sys.argv) == 3:
    # Save clipboard content to shelf.
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    # delete a content from shelf
    elif sys.argv[1].lower() == 'delete' and sys.argv[2] in mcbShelf:
        mcbShelf.pop(sys.argv[2])

elif len(sys.argv) == 2:
    # List keywords, load content or deleteall.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    # check if argv[i] is in mcbShelf (keys)
    # because mcbShelf is Shelve database and it acts like a dictionary
    # and if we use 'in' on dictionary, its keys are checked 
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    # delete all
    elif sys.argv[1].lower() == 'deleteall':
        mcbShelf.clear()

mcbShelf.close()
