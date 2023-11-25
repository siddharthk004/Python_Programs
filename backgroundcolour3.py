
from guizero import App,Text

app = App("Hello World")
app.bg = "#DA8977"
wanted_text = Text(app,"--WANTED--")
wanted_text.size = 50
app.display()
