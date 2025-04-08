from pathlib import Path
import os

p = Path('C:/Users/AI/spam.txt')

print(p.anchor) # C:\

print(p.parent) # C:\Users\AI it's just changed to str, otherwise its obj
# proff
print(type(p.parent))

print(p.name) # spam.txt

print(p.stem) # spam

print(p.suffix) # .txt

print(p.drive) # C: available only for windows


# Parents vs Parent
print(Path.cwd()) # D:\Coding\Other Codes\python-practice-code
print(Path.cwd().parents[0]) # D:\Coding\Other Codes
print(Path.cwd().parents[1]) # D:\Coding
print(Path.cwd().parents[2]) # D:\


# vs old os module
calcFilePath = 'C:\\Windows\\System32\\calc.exe'
print(os.path.abspath(calcFilePath)) # C:\Windows\System32\calc.exe
print(os.path.basename(calcFilePath)) # calc.exe
print(os.path.dirname(calcFilePath)) # C:\\Windows\\System32
# to get both in a tuple 
print(os.path.split(calcFilePath)) # ('C:\\Windows\\System32', 'calc.exe')

# just a string to separate folders but according to
# the correct rules defined in os.sep, it will be telling 
# the string split() method, where to put splits 
# os.sep take care of whether it has to return / or \\ based on operating system
# because windows path has \ so \\ (with escape character) and / on linux and ios
# on ios, drive element will be empty ''
print(calcFilePath.split(os.sep)) # ['C:', 'Windows', 'System32', 'calc.exe']

# get size of this file
print(os.path.getsize(str(Path.cwd()) + '\\extractPathAttributes.py' ) / 1024) # Result in Kbs
# btw instead of converting to str, and using + and \\,
# we could simply use / and concatinate the paths
print(os.path.getsize(Path.cwd() / 'extractPathAttributes.py' ) / 1024) # Result in Kbs


# files in projects folder 
print(os.listdir(Path.cwd() / 'projects'))

print()

# use glob() from Path to get list of files instead
# we got a generator object from glob, and converted it to a list
# then we have path to each file.
print(list((Path.cwd() / 'projects').glob('*'))) # * means everything. 
# *.txt would've meant all txt files.

#......................................
# Check if path exists
winDir = Path('C:/Windows')
print(winDir.exists()) # True

# If it exists and is a directory
print(winDir.is_dir()) # True
# If it exists and is a file
print(winDir.is_file()) # False

print(Path('D:/').exists()) # only checking drive

# using os we can use similar methods 
# os.path.isdir(), .isfile(), .exists()