def tryingGlobalStatement():
    global name # to effect global variable name
    name = "wamik"

name = "basit"

tryingGlobalStatement() # it effected the global variable becauuse of that statement
print(name)