# Will hold our game board data
board = ["-" for x in range(10)]

# if the game is over yet
game_still_going = True

# who the winner is
winner = None

# who the current player is (X goes first)
current_player = "X"

# Display the game board to the screen
def printBoard():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
 
# Handle a turn for an arbitrary player
def handle_turn(player):

    print(player + "'s turn")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9: ")
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else: print("You can't go here. Try again!")
    board[position] = player
    printBoard()

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False

def check_colums():
    global game_still_going
    colum1 = board[0] == board[1] == board[2] != "-"
    colum2 = board[3] == board[4] == board[5] != "-" 
    colum3 = board[6] == board[7] == board[8] != "-" 
    if colum1 or colum2 or colum3:
        game_still_going = False
    if colum1:
        return board[0]
    elif colum2:
        return board[3]
    elif colum3:
        return board[6]

def check_columns():
    global game_still_going
    colum1 = board[0] == board[3] == board[6] != "-"
    colum2 = board[1] == board[4] == board[7] != "-" 
    colum3 = board[2] == board[5] == board[8] != "-" 
    if colum1 or colum2 or colum3:
        game_still_going = False
    if colum1:
        return board[0]
    elif colum2:
        return board[1]
    elif colum3:
        return board[4]

def check_diagnals():
    global game_still_going
    diagnal1 = board[0] == board[4] == board[8] != "-"
    diagnal2 = board[2] == board[4] == board[6] != "-"
    if diagnal1 or diagnal2:
        game_still_going = False
    if diagnal1:
        return board[0]
    elif diagnal2:
        return board[2]

def check_for_winner():
    global winner
    colums_winner = check_colums()
    columns_winner = check_columns()
    diagnals_winner = check_diagnals()
    if colums_winner:
        winner = colums_winner
    elif columns_winner:
        winner = columns_winner
    elif diagnals_winner: 
        winner = diagnals_winner
    else: winner = None

def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def check_if_game_over():
    check_for_winner()
    check_if_tie()

# Play a game of tic tac toe
def playGame():
    printBoard()
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

    # the game has ended
    if winner == "X" or winner == "O":
        print(winner + " won !!!")
    else: print("TIEEEE")

playGame()