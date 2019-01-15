from appJar import gui


app = gui('Hello')

app.setBg('lightblue')
app.addHorizontalSeparator(0, 0, 4, colour='red')
app.addVerticalSeparator(1, 0, colour='#8585e0')
app.addVerticalSeparator(1, 1, colour='#d6d6f5')
app.addVerticalSeparator(1, 2, colour='#1f1f7a')
app.addVerticalSeparator(1, 3, colour='#ff33bb')
app.addHorizontalSeparator(2, 0, 4, colour='#00e64d')
app.go()