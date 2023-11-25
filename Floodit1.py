# ---------------------------------
# imports
# ---------------------------------

from guizero import App,Waffle,Text,PushButton,info
import random

# ---------------------------------
# variables
# ---------------------------------
colours = ["red","blue","green","yellow","magenta","purple"]
board_size = 14
moves_limit = 25
moves_taken = 0

# ---------------------------------
# functions
# ---------------------------------
# Recursively floods adjacent squares
def flood(x,y,target,replacement):
    # Algorithm from https://en.eikipedia.org/wiki/flood_fill
    if target == replacement:
        return False
    
    if board.get_pixel(x,y) != target:
        return False
    board.set_pixel(x,y,replacement)
    if y+1 <= board_size-1:  # South
        flood(x,y+1,target,replacement)
    if y-1 >= 0:             # North
        flood(x,y-1,target,replacement)
    if x+1 <= board_size-1:  # East
        flood(x+1,y,target,replacement)
    if x-1 >= 0:             # West
        flood(x-1,y,target,replacement)
            
            
# Cheak Whether all squares are the same
def all_squares_are_the_same():
    squares = board.get_all()
    if all(colours == squares[0] for color in squares):
        return True
    else:
        return False

def Win_cheak():
    global moves_taken
    moves_taken += 1
    if moves_taken <= moves_limit:
        if all_squares_are_the_same():
            win_text.value = "you win !"
    else:
        win_text.value = "you lost :("

def fill_board():
    for x in range(board_size):
        for y in range(board_size):
            board.set_pixel(x,y,random.choice(colours))

def init_palette():
    for colour in colours:
        palette.set_pixel(colours.index(colour),0,colour)

def start_flood(x,y):
    flood_color = palette.get_pixel(x,y)
    target = board.get_pixel(0,0)
    flood(0,0,target,flood_color)
    Win_cheak()
    
# --------------------------------------
# App
# --------------------------------------

app = App("Flood it")

board = Waffle(app,width=board_size,height=board_size,pad=0)
palette = Waffle(app,width=6,height=1,dotty=True,
                 command=start_flood)

win_text = Text(app)

fill_board()
init_palette()

app.display()