from appJar import gui
from PIL import Image, ImageTk

app = gui()
photo = ImageTk.PhotoImage(Image.open("images.jpg"))
app.addImageData("pic", photo, fmt="PhotoImage")
app.go()