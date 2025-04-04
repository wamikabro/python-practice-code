import pyinputplus as pyip

# default value be returned if timeout, or if you set limit then limit crossed
# but it isn't automatically printed like other things eg. 
# not a number, or blank isn't accepted
# you must print the response to print the default response
# which is obvious at some point
#response = pyip.inputNum("Enter num in 2 sec: ", timeout=2, default='You entered after 2 seconds lol.')
#print(response)

#response = pyip.inputNum("Enter number within 2 tries: ", limit=2)

# if you enter after the timeout limit, then the exception TimeOutExcpetion() occurs
#response = pyip.inputNum("Enter number within 2 seconds:", timeout=2)

# allow romans tp be accepted as numbers
# by using list of allowRegexes 
# it is allowing all the capital romans and zero
response = pyip.inputNum(allowRegexes=[r'\s+'])


