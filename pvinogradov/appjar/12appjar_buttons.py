from appJar import gui


def press(btn):



app = gui('function', '500x500')


app.addNamedButton('hello', '123', press, row=3, column=0)
app.addButton('Enter', press, rowspan=10, column=6, row=0)
app.addScrolledTextArea("t2", text='', row=0)
app.addButtons([1, 2, 3, 4, '+', '-'], press, row=1)
app.addButtons([5, 6, 7, 8, '=', '%'], press, row=2)
app.addButtons([9, 0, '*', '/', '//'], press, row=3)

app.go()
