from guizero import App,Text,PushButton
from random import choice


def choose_name():
    # print("Button was pressed")
    First_name = ["Barbara","Woody","tiberius","smokey","jennifer","ruby"]
    last_name = ["SpindleShankes","Mysterioso","dungeon","catseye","Darkmeyer","Flamingobreath"]
    
    spy_name = choice(First_name)+" "+choice(last_name)
    
    print(spy_name)
        
app = App("top secret")

title = Text(app,"Push the red button to find your spy name ")
button = PushButton(app,choose_name,text="tell me !")
button.bg = "red"
button.text_size = 8

app.display()