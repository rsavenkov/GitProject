from appJar import gui

app = gui('')
app.setFont(20)
app.setBg('#00ff55')

app.addLabel('l11', 'Move me around')
app.addGrip(0, 1)
app.addSeparator(1, 0, 2, colour='red')
app.go()