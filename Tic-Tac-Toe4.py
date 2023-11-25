
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
    
def toggle_player():
    global turn
    if turn == "x":
        turn = "o"
    else:
        turn = "x"
    
    message.value = "it is your turn, "+turn

# variables
turn = "x"

# App
app = App("Tic Tac Toe")

board = Box(app,layout="grid")
board_squares = Clear_board()    
message = Text(app,text="It is your turn, "+turn)

app.display()