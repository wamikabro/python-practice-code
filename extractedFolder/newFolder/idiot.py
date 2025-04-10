import pyinputplus as pyip

while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    # we can pass our own yes and no values to get in response
    # otherwise the default values will be yes or no
    # when we set our own yesVal and noVal, yes and no, no longer works
    
    # but when it was yes, user could enter y too.
    # now it's han, and user can enter just h too
    response = pyip.inputYesNo(prompt, yesVal='han', noVal='nahi')

    if response == 'nahi':
        break

print('Thank you. Have a nice day.')
