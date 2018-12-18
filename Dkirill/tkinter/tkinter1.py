from tkinter import *

root = Tk()

topFrame = Frame()
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Москва ",fg="red")
button2 = Button(topFrame, text="Архангельск",fg="blue")
button3 = Button(topFrame, text="Ухта",fg="green")
button4 = Button(bottomFrame, text="Питер",fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)
root.mainloop()
