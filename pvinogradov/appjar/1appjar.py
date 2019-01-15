from appJar import gui

count = 0


def press(btn):
    global count
    count += 1
    app.setLabel('title', btn + ' count' + str(count))
    if btn == 'Press me':
        app.setFg('#008ae6')
    elif btn == 'Helo':
        app.setFg('#1aff66')
    elif btn == 'Press me as well':
        app.setFg('#ffb3b3  ')
    if count == 10:
        app.infoBox('You', 'You got the counter to 10')
        app.stop()


app = gui('Demo GUI', '1000x1000')

app.setBg('#bfff00')  # цет фона
app.setFg('#00bfff')  # цвет букв
app.setFont(50)  # размер букв

app.addLabel('title', 'Hello World')
app.addMessage('info', 'this is a simple of appJar')

app.addButton('Press me', press)
app.addButton('Helo', press)
app.addButton('Press me as well', press)

app.go()
