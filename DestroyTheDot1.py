
# imports
from guizero import App,Text,Waffle

# variables

# functions

# App
app = App("Destroy the Dots")

instructions = Text(app,text="click the dot to destroy them")
board = Waffle(app,width=5,height=5)

app.display()
