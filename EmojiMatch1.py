# -----------------------------------
# Imports
# -----------------------------------
import os
from random import shuffle
from guizero import App,Box,Picture,PushButton


# -----------------------------------
# Variables
# -----------------------------------
# set the path to the emoji folder on your computere
emojis_dir = "emojis"
emojis = [os.path.join(emojis_dir,f) for f in os.listdir(emojis_dir)]
shuffle(emojis)

# -----------------------------------
# Functions
# -----------------------------------
def setup_round():
    for picture in Pictures:
        picture.image = emojis.pop()
        
    for button in buttons:
        button.image = emojis.pop()
        
        
# -----------------------------------
# App
# -----------------------------------
app = App("emoji match")

Picture_box = Box(app,layout="grid")
button_box = Box(app,layout="grid")

Pictures = []
buttons = []

for x in range(0,3):
    for y in range(0,3):
        Picture = Picture(Picture_box,grid=[x,y])
        Pictures.append(Picture)
        
        button = PushButton(button_box,grid=[x,y])
        buttons.append(button)
        
        
setup_round()

app.display()