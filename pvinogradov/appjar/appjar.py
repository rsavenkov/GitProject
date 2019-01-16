from appJar import gui

app = gui()
app.addTextArea("t1", text='Hello')
app.addScrolledTextArea("t2", text='World')
app.addScrolledTextArea("t3", text='courses')
app.setTextArea("t1", ' добавили текст', end=True, callFunction=True)
# app.clearTextArea("t1", callFunction=True)  # очистить ввод

app.go()
