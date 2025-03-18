picnicItems = {'apples': 5, 'cups': 2}

statement1 = 'I am bringing ' + str(picnicItems.get('apples',0)) + ' apples to the picnic.'
statement2 = 'I am bringing ' + str(picnicItems.get('eggs',0)) + " eggs to the picnic."

print(statement1)
print(statement2)