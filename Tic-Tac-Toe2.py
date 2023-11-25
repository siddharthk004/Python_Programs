
from guizero import App,Box,PushButton

def Clear_board():
    new_board = [[None,None,None],[None,None,None],[None,None,None]]
    for x in range(3):
        for y in range(3):
            button = PushButton(
                board,text="",grid=[x,y],width=3
            )
            new_board[x][y] = button
    return new_board


app = App("Tic Tac Toe")

board = Box(app,layout="grid")
board_squares = Clear_board()    
app.display()