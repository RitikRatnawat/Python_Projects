from random import randrange

def DisplayBoard(board):
    #
    # the function accepts one parameter containing the board's current status
    # and prints it out to the console
    #
    print("+", "-" * 7, "+", "-" * 7, "+", "-" * 7, "+", end="\n")
    print("|", " " * 7, "|", " " * 7, "|", " " * 7, "|", end="\n")
    print("|", " " * 2, board[0][0], " " * 2, "|", " " * 2, board[0][1], " " * 2, "|", " " * 2, board[0][2], " " * 2,
          "|", end="\n")
    print("|", " " * 7, "|", " " * 7, "|", " " * 7, "|", end="\n")
    print("+", "-" * 7, "+", "-" * 7, "+", "-" * 7, "+", end="\n")
    print("|", " " * 7, "|", " " * 7, "|", " " * 7, "|", end="\n")
    print("|", " " * 2, board[1][0], " " * 2, "|", " " * 2, board[1][1], " " * 2, "|", " " * 2, board[1][2], " " * 2,
          "|", end="\n")
    print("|", " " * 7, "|", " " * 7, "|", " " * 7, "|", end="\n")
    print("+", "-" * 7, "+", "-" * 7, "+", "-" * 7, "+", end="\n")
    print("|", " " * 7, "|", " " * 7, "|", " " * 7, "|", end="\n")
    print("|", " " * 2, board[2][0], " " * 2, "|", " " * 2, board[2][1], " " * 2, "|", " " * 2, board[2][2], " " * 2,
          "|", end="\n")
    print("|", " " * 7, "|", " " * 7, "|", " " * 7, "|", end="\n")
    print("+", "-" * 7, "+", "-" * 7, "+", "-" * 7, "+", end="\n")


def EnterMove(board):
    #
    # the function accepts the board current status, asks the user about their move,
    # checks the input and updates the board according to the user's decision
    #
    move = int(input("Enter Your Move : "))
    lst = MakeListOfFreeFields(board)

    if move < 3 and (0, move - 1) in lst:
        board[0][move - 1] = 'O'
    elif move > 3 and move < 7 and (1, move - 4) in lst:
        board[1][move - 4] = 'O'
    elif move < 10 and (2, move - 7) in lst:
        board[2][move - 7] = 'O'


def MakeListOfFreeFields(board):
    #
    # the function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers
    #
    frlst = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != 'O' and board[i][j] != 'X':
                frlst.append((i, j))

    return frlst


def VictoryFor(board, sign):
    #
    # the function analyzes the board status in order to check if
    # the player using 'O's or 'X's has won the game
    #
    for i in range(2):
        if (board[i][0] == sign and board[i][1] == sign and board[i][2] == sign):
            return True

    for i in range(2):
        if (board[0][i] == sign and board[1][i] == sign and board[2][i] == sign):
            return True

    if (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign):
        return True
    elif (board[0][2] == sign and board[1][1] == sign and board[2][1] == sign):
        return True
    else:
        return False


def DrawMove(board):
    #
    # the function draws the computer's move and updates the board

    lst = MakeListOfFreeFields(board)
    while True:
        move = randrange(1, 9)
        if move < 4 and (0, move - 1) in lst:
            board[0][move - 1] = 'X'
            return
        elif move > 3 and move < 7 and (1, move - 4) in lst:
            board[1][move - 4] = 'X'
            return
        elif move < 10 and (2, move - 7) in lst:
            board[2][move - 7] = 'X'
            return


board = [[i + 1 for i in range(3)], [i for i in range(4, 7)], [i for i in range(7, 10)]]
while True:
    if VictoryFor(board, 'O'):
        win = 'O'
        print("You Won")
        break
    elif VictoryFor(board, 'X'):
        win = 'X'
        print("Computer Won")
        break
    elif len(MakeListOfFreeFields(board)) == 0:
        print("Game Ties")
        break

    DrawMove(board)
    DisplayBoard(board)
    EnterMove(board)
    DisplayBoard(board)
