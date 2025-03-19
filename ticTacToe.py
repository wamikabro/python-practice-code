theBoard = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'middle-L': ' ', 'middle-M': ' ', 'middle-R': ' ',
    'bottom-L': ' ', 'bottom-M': ' ', 'bottom-R': ' '
}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['middle-L'] + '|' + board['middle-M'] + '|' + board['middle-R'])
    print('-+-+-')
    print(board['bottom-L'] + '|' + board['bottom-M'] + '|' + board['bottom-R'])

turn = 'X' # whose turn is this?

i = 0
while i<9:
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space? ')
    move = input()

    if move not in theBoard.keys():
        print('Invalid Move. Try again!')
        continue

    if theBoard[move] != ' ':
        print('Position already reserved, try something else.')
        continue

    theBoard[move] = turn

    if theBoard['top-L'] == turn and theBoard['top-M'] == turn and theBoard['top-R'] == turn\
    or theBoard['middle-L'] == turn and theBoard['middle-M'] == turn and theBoard['middle-R'] == turn\
    or theBoard['bottom-L'] == turn and theBoard['bottom-M'] == turn and theBoard['bottom-R'] == turn\
    or theBoard['top-L'] == turn and theBoard['middle-L'] == turn and theBoard['bottom-L'] == turn\
    or theBoard['top-M'] == turn and theBoard['middle-M'] == turn and theBoard['bottom-M'] == turn\
    or theBoard['top-R'] == turn and theBoard['middle-R'] == turn and theBoard['bottom-R'] == turn\
    or theBoard['top-L'] == turn and theBoard['middle-M'] == turn and theBoard['bottom-R'] == turn\
    or theBoard['top-R'] == turn and theBoard['middle-M'] == turn and theBoard['bottom-L'] == turn:
        print(turn + " won!")
        break

    if i == 8:
        print('Draw!')
        break

    i += 1

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    
printBoard(theBoard)