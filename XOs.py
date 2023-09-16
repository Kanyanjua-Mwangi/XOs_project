board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

''

currentplayer = "X"
winner = 0
gameRunning = True

def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

printBoard(board)

def playerInput(board): 
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentplayer
    else:
        print("Spot played")

playerInput(board)

def checkhorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkvertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkdiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board != "-":
        winner == board
        return True
    elif board[2] == board[4] == board[6] and board != "-":
        winner == board
        return True

def checktie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("Tie!")
        gameRunning = False

def Checkwin():
    global gameRunning
    if checkdiagonal(board) or checkvertical(board) or checkhorizontal(board):
        print(f"The winner is {winner}")

def Swithplayer():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"

    else:
        currentplayer = "X"

    
while gameRunning:
    printBoard(board)
    playerInput(board)
    checktie(board)
    Checkwin()
    Swithplayer()
