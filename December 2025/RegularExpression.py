# All about regular expressions in Python

import re

# Sample text to search
text = "The rain in Spain stays mainly in the plain."
# Regular expression pattern to find all words ending with 'ain'
pattern = r'\b\w*ain\b'
# Finding all occurrences of the pattern
matches = re.findall(pattern, text)
print("Words ending with 'ain':", matches)
# Output:
# Words ending with 'ain': ['rain', 'Spain', 'plain']

# Using re.sub to replace 'ain' with 'ane'
replaced_text = re.sub(r'ain', 'ane', text)
print("Text after replacement:", replaced_text)
# Output:
# Text after replacement: The rane in Spane stays manely in the plane.

# Using re.search to find the first occurrence of 'mainly'
search_result = re.search(r'mainly', text)
if search_result:
    print("Found 'mainly' at position:", search_result.start())
# Output:
# Found 'mainly' at position:  twenty-two

# Using re.match to check if the text starts with 'The'
match_result = re.match(r'The', text)
if match_result:
    print("The text starts with 'The'")

# Output:
# The text starts with 'The'

# Using re.split to split the text at spaces
split_text = re.split(r'\s+', text)
print("Text split into words:", split_text)
# Output:
# Text split into words: ['The', 'rain', 'in', 'Spain', 'stays', 'mainly', 'in', 'the', 'plain.']

# Using re.compile to create a regex object for finding vowels
vowel_pattern = re.compile(r'[aeiou]')
vowel_matches = vowel_pattern.findall(text)
print("Vowels in the text:", vowel_matches)

# Output:
# Vowels in the text: ['e', 'a', 'i', 'i', 'a', 'i', 'a', 'e', 'a', 'i', 'i', 'e', 'a', 'i']

# Using re.finditer to find all occurrences of 'in'
finditer_results = re.finditer(r'in', text)
print("Occurrences of 'in':")
for match in finditer_results:
    print(f"'in' found at position: {match.start()} to {match.end()}")
# Output:
# Occurrences of 'in':
# 'in' found at position: 5 to 7
# 'in' found at position: 14 to 16
# 'in' found at position: 33 to 35

# Using re.fullmatch to check if the entire text matches a pattern
fullmatch_result = re.fullmatch(r'The rain in Spain stays mainly in the plain\.', text)
if fullmatch_result:
    print("The entire text matches the pattern.")
# Output:
# The entire text matches the pattern.

# Using re.escape to escape special characters in a string
special_string = "Hello. How are you? (I hope you're well!)"
escaped_string = re.escape(special_string)
print("Escaped string:", escaped_string)
# Output:
# Escaped string: Hello\. How are you\? \(I hope you\'re well!\)

# Using re.VERBOSE to create a more readable regex pattern
verbose_pattern = re.compile(r'''
    \b          # word boundary
    \w+         # one or more word characters
    @           # at symbol
    \w+         # one or more word characters
    \.          # dot
    \w{2,3}     # two to three word characters (domain)
    \b          # word boundary
''', re.VERBOSE)
email_text = "Please contact us at info@example.com or support@company.org for more information."

email_matches = verbose_pattern.findall(email_text)
print("Email addresses found:", email_matches)
# Output:
# Email addresses found: ['info@example.com', 'support@company.org']

# Using re.IGNORECASE to perform case-insensitive matching
ignorecase_pattern = re.compile(r'python', re.IGNORECASE)
ignorecase_matches = ignorecase_pattern.findall("I love Python. python is great. PYTHON!")
print("Case-insensitive matches for 'python':", ignorecase_matches)
# Output:
# Case-insensitive matches for 'python': ['Python', 'python', 'PYTHON']

# Using re.MULTILINE to match patterns at the start of each line
multiline_text = """First line
Second line
Third line"""
multiline_pattern = re.compile(r'^(\w+)', re.MULTILINE)
multiline_matches = multiline_pattern.findall(multiline_text)
print("First words of each line:", multiline_matches)
# Output:
# First words of each line: ['First', 'Second', 'Third']

# Using re.DOTALL to make '.' match newline characters
dotall_text = "First line.\nSecond line.\nThird line."
dotall_pattern = re.compile(r'First.*Third', re.DOTALL)
dotall_match = dotall_pattern.search(dotall_text)
if dotall_match:
    print("DOTALL match found:", dotall_match.group())
# Output:
# DOTALL match found: First line.
#Second line.
#Third line.