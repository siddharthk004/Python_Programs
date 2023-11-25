
# imports
from guizero import App,Box,PushButton,Text

# function
def Clear_board():
    new_board = [[None,None,None],[None,None,None],[None,None,None]]
    for x in range(3):
        for y in range(3):
            button = PushButton(
                board,text="",grid=[x,y],width=3,
                command=choose_square,args=[x,y]
            )
            new_board[x][y] = button
    return new_board

def choose_square(x,y):
    board_squares[x][y].text = turn
    board_squares[x][y].disable()
    toggle_player()
    cheak_win()
    
def toggle_player():
    global turn
    if turn == "x":
        turn = "o"
    else:
        turn = "x"
    
    message.value = "it is your turn, "+turn

def cheak_win():
    winner = None
    
    # vertical lines
    if(
        board_squares[0][0].text == board_squares[0][1].text == board_squares[0][2].text
    )and board_squares[0][2].text in ["x","o"]:
        winner = board_squares[0][0]
    
    elif(
        board_squares[1][0].text == board_squares[1][1].text == board_squares[1][2].text
    )and board_squares[1][2].text in ["x","o"]:
        winner = board_squares[1][0]

    elif(
        board_squares[2][0].text == board_squares[2][1].text == board_squares[2][2].text
    )and board_squares[2][2].text in ["x","o"]:
        winner = board_squares[2][0]
        
    # horizontal lines
    elif(
        board_squares[0][0].text == board_squares[1][0].text == board_squares[2][0].text
    )and board_squares[2][0].text in ["x","o"]:
        winner = board_squares[0][0]
    
    elif(
        board_squares[0][1].text == board_squares[1][1].text == board_squares[2][1].text
    )and board_squares[2][1].text in ["x","o"]:
        winner = board_squares[0][1]

    elif(
        board_squares[0][2].text == board_squares[1][2].text == board_squares[2][2].text
    )and board_squares[2][2].text in ["x","o"]:
        winner = board_squares[0][2]
        
    # diagonals
    elif(
        board_squares[0][0].text == board_squares[1][1].text == board_squares[2][2].text
    )and board_squares[2][0].text in ["x","o"]:
        winner = board_squares[0][0]
    
    elif(
        board_squares[2][0].text == board_squares[1][1].text == board_squares[0][2].text
    )and board_squares[0][2].text in ["x","o"]:
        winner = board_squares[0][2]

    if winner is not None:
        message.value = winner.text+"Wins !"
    elif moves_taken() == 9:
        message.value = "it`s a draw"
    
def moves_taken():
    moves = 0
    for row in board_squares:
        for col in row:
            if col.text == "x" or col.text == "o":
                moves = moves+1
    return moves        
        
# variables
turn = "x"

# App
app = App("Tic Tac Toe")

board = Box(app,layout="grid")
board_squares = Clear_board()    
message = Text(app,text="It is your turn, "+turn)

app.display()