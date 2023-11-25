# simple paint app,just draw dots

# ----------------------------------
# imports
# ----------------------------------
from guizero import App,Drawing

# ----------------------------------
# functions
# ----------------------------------
def draw(event):
    painting.oval(
        event.x - 1,event.y - 1,
        event.x + 1,event.y + 1,
        color = "black")
    
# ----------------------------------
# App
# ----------------------------------

app = App("paint")

painting = Drawing(app,width="fill",height="fill")

app.display()