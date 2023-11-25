from guizero import App,Text,PushButton

app = App("top secret")
title = Text(app,"Push the red button to find your spy name ")
button = PushButton(app,text="tell me !")

app.display()