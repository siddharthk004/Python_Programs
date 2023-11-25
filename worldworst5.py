from guizero import App,PushButton

def are_you_sure():
    if app.yesno("confirmation","are you sure ?"):
        app.info("thanks","button pressed")
    else:
        app.error("ok","Cancelling")
        
app = App(title="pointless pop-ups")

button = PushButton(app,command=are_you_sure)

app.info("application started","well done you started the application")

app.display()