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
    marker=['X', 'O']
    marker1=input('Player 1 chose marker: X or O: ').upper()
    if marker1.upper()==marker[0]:
        return marker
    else:
        return marker.reverse()

def placeMarker(board, position, marker):
    board[position] = marker

def checkPosition():
    return int(input('Enter your move: '))

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


def play():
    board = [' '] * 10
    player= playerInput()
    print('Player 1: ', player[0])
    print('Player 2: ', player[1])

    flag=1
    player=0

    while flag:
        while not player:
            displayBoard(board)
            position = checkPosition()
            placeMarker(board, position, player[0])

            if win(board, player[0]):
                displayBoard(board)
                print('Congratulations! Player 1 won the game!')
                flag=0
            elif(check(board)):
                displayBoard(board)
                print('The game is a draw!')
            else:
                player=1

            print('\n' * 100)

        while player:
            displayBoard(board)
            position = checkPosition()
            placeMarker(board, position, player[1])

            if win(board, player[1]):
                displayBoard(board)
                print('Congratulations! Player 2 won the game!')
                flag=0
            elif (check(board)):
                displayBoard(board)
                print('The game is a draw!')
            else:
                player = 0

play()
