from guizero import App,Text,PushButton

def choose_name():
    print("Button was pressed")
    
app = App("top secret")

title = Text(app,"Push the red button to find your spy name ")
button = PushButton(app,choose_name,text="tell me !")

app.display()