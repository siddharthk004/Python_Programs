
# imports
from guizero import App,Text,Waffle
from random import randint


# variables
GRID_SIZE = 5

# functions
def add_dot():
    x,y = randint(0,GRID_SIZE-1),randint(0,GRID_SIZE-1)
    while board[x,y].dotty == True:
        x,y = randint(0,GRID_SIZE-1),randint(0,GRID_SIZE-1)
    board[x,y].dotty = True
    board.set_pixel(x,y,"red")


# App
app = App("Destroy the Dots")

instructions = Text(app,text="click the dot to destroy them")
board = Waffle(app,width=5,height=5)
add_dot()

app.display()