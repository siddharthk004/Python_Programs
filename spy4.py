# Imports 
from guizero import App,Text,PushButton
from random import choice

# functions
def choose_name():
    First_name = ["Barbara","Woody","tiberius","smokey","jennifer","ruby"]
    last_name = ["SpindleShankes","Mysterioso","dungeon","catseye","Darkmeyer","Flamingobreath"]
    
    spy_name = choice(First_name)+" "+choice(last_name)
    
    name.value = spy_name
    
# App
app = App("top secret")

# Widgets
title = Text(app,"Push the red button to find your spy name ")
button = PushButton(app,choose_name,text="tell me !")
button.bg = "red"
button.text_size = 8
name = Text(app,text="")

# Display
app.display()