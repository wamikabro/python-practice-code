tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    # list to store max width of each column
    colWidths = [0] * len(tableData) # [0,0,0]

    # find longest string in each column and add in colWidths
    for i in range(len(tableData)): # 0, 1, 2
    #   colWidths 0 = 8
    #   colWidths 1 = 5
    #   colWidths 2 = 5
        colWidths[i] = max(len(word) for word in tableData[i])
        











'''
for i, innerList in enumerate(tableData): # 0, ['apples', 'oranges', 'cherries', 'banana']
    lengthOfWord = 0
    for word in tableData[i]: 
        if len(word) > lengthOfWord:
            lengthOfWord = len(word)

'''

    



