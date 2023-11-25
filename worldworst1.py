
# Imports
from guizero import App,Text

# functions
def flash_text():
    if title.visible:
        title.hide()
    else:
        title.show()

# App
app = App("Its all gone wrong",bg="dark green")

title = Text(app,text="some hard to read text",size="14",font="Cosmic Sans",color = "green")

app.repeat(1000,flash_text)

app.display()
