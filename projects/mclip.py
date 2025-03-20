# A multi clipboard program
import sys, pyperclip

Text = {'agree': """ Yes, I agree. That sounds fine to me.""",
        'busy': """ Sorry, I am busy at the moment.""",
        'upsell': """Would you consider making this a monthly donation?"""
        }

# to make sure that we've got at least 2 arguments 
# # because 1st thing in argument is the name of program
# so we will access second later
if len(sys.argv) < 2:
    print('Usage: Please pass an argument.')
    sys.exit()


keyphrase = sys.argv[1]

if keyphrase in Text.keys(): # or simply Text
    pyperclip.copy(Text[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)    