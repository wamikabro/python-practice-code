# English to Pig Latin
print('Enter the English Message: ')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = [] # list of pig latin words

# if begins with vowel: add yay to end
# if begins with a consonant or cluster (ch gr), move it to the end + ay

# break the message into separate words
for word in message.split():
    # Separate non letters (Prefix)
    prefixNonLetters = ''
    '''
    ✅ Why len(word) > 0 is needed here?

    The loop removes characters from the front (word = word[1:]).
    If we don’t check len(word) > 0, and word becomes empty, 
    word[0] would cause an IndexError 
    (trying to access the first character of an empty string).
    '''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    # if after removing prefix, nothing is left, just add all those prefix
    # as a word and cotniue with for loop, don't go down
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    # Separate non letters (Suffix)
    suffixNonLetters = ''

    '''
    🚀  Why doesn’t it need len(word) > 0?

    We’re checking word[-1], but in Python, negative indexing 
    automatically handles empty strings safely.
    If word becomes empty, word[-1] will never be accessed 
    because the loop condition will fail before that happens.
    '''
    while not word[-1].isalpha():
        # always keep new suffix non letter before other suffix non letters
        # because we're checking suffix in backwords and we don't want to
        # destroy the order of suffix 
        suffixNonLetters = word[-1] + suffixNonLetters 
        word = word[:-1]

    # remember the word is upper or title case
    wasUpper = word.isupper()
    wasTitle = word.istitle()


    # Separate Consonants from the start of the word
    prefixConsonants = ''

    # if word is greater than 0 and it's not from defined VOWELS
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # Add the Pig Latin ending to the word:
    
    # if we have prefix consonants
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'
    
    # Set the word back to Uppercase or title case:
    if wasUpper: 
        word = word.upper()
    if wasTitle:
        word = word.title()

    # add non letters back to the start or the end of the word
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# Join all the words back together into a single string
newString = ' '.join(pigLatin)

print(newString)


