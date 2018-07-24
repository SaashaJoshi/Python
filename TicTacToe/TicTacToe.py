def displayBoard(board):
    print('  |       |')
    print('' + board[7] + ' |' + '   ' + board[8] + '   | ' + ' ' + board[9])
    print('  |       |')
    print('-------------')
    print('  |       |')
    print('' + board[4] + ' |' + '   ' + board[5] + '   | ' + ' ' + board[6])
    print('  |       |')
    print('-------------')
    print('  |       |')
    print('' + board[1] + ' |' + '   ' + board[2] + '   | ' + ' ' + board[3])
    print('  |       |')

def playerInput():
    marker=input('Player 1 chose marker: X or O: ').upper()
    if marker=='X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def placeMarker(board, position, marker):
    board[position] = marker

def win(board, marker):

    return ((board[7] == marker and board[8] == marker and board[9] == marker) or  # across the top
    (board[4] == marker and board[5] == marker and board[6] == marker) or  # across the middle
    (board[1] == marker and board[2] == marker and board[3] == marker) or  # across the bottom
    (board[7] == marker and board[4] == marker and board[1] == marker) or  # down the left side
    (board[8] == marker and board[5] == marker and board[2] == marker) or  # down the middle
    (board[9] == marker and board[6] == marker and board[3] == marker) or  # down the right side
    (board[7] == marker and board[5] == marker and board[3] == marker) or  # diagonal
    (board[9] == marker and board[5] == marker and board[1] == marker))  # diagonal

def space(board, position):
    return board[position]==' '

def check(board):
    for i  in range(1, 10):
        if space(board, i):
            return False
    return True

def choice(board):
    position=0
    if not check(board) or position not in [1,2,3,4,5,6,7,8,9]:
        position=int(input('Enter your move: '))
    return position


def play():
    board = [' '] * 10
    player= playerInput()
    print('Player 1: ', player[0])
    print('Player 2: ', player[1])

    flag=1
    game=0

    while flag:
        if not game:
            displayBoard(board)
            position = choice(board)
            placeMarker(board, position, player[0])

            if win(board, player[0]):
                displayBoard(board)
                print('Congratulations! Player 1 won the game!')
                flag=0
            else:
                if(check(board)):
                    displayBoard(board)
                    print('The game is a draw!')
                    flag=0
                else:
                    game=1

        if game:
            displayBoard(board)
            position = choice(board)
            placeMarker(board, position, player[1])

            if win(board, player[1]):
                displayBoard(board)
                print('Congratulations! Player 2 won the game!')
                flag=0
            else:
                if (check(board)):
                    displayBoard(board)
                    print('The game is a draw!')
                    flag=0
                else:
                    game = 0

play()
