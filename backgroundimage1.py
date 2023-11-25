
from guizero import App,Text,Picture

app = App("Hello World")
app.bg = "#DA8977"
wanted_text = Text(app,"--WANTED--")
wanted_text.size = 50
wanted_text.font = "Times New Roman"

cat = Picture(app,image="tabitha.png")
app.display()