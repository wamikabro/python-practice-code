# adds bullet points to the start

import pyperclip
text = pyperclip.paste()


lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i] # add asterisk and then whole line

text = '\n'.join(lines)

pyperclip.copy(text)

print("Bullet points have been added!")