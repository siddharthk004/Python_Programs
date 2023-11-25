

# imports
from guizero import App,Text,Waffle
from random import randint


# variables
GRID_SIZE = 5
score = 0

# functions
def add_dot():
    x,y = randint(0,GRID_SIZE-1),randint(0,GRID_SIZE-1)
    while board[x,y].dotty == True:
        x,y = randint(0,GRID_SIZE-1),randint(0,GRID_SIZE-1)
    board[x,y].dotty = True
    board.set_pixel(x,y,"red")
    
    speed = 1000
    if score > 10:
        speed = 500
    if score > 20:
        speed = 400
    if score > 30:
        speed = 200
    
    board.after(1000,add_dot)

def destroy_dot(x,y):
    global score
    if board[x,y].dotty == True:
        board[x,y].dotty = False
        board.set_pixel(x,y,"white")
        score += 1
        score_display.value = "your score is "+str(score)

# App
app = App("Destroy the Dots")

instructions = Text(app,text="click the dot to destroy them")
board = Waffle(app,width=GRID_SIZE,height=GRID_SIZE,
               command=destroy_dot)
board.after(1000,add_dot)
score_display = Text(app,text="your score is "+str(score))

app.display()