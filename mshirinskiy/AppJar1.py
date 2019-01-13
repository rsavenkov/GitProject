from appJar import gui

count = 0

def press(btn):
    global count
    count += 1
    app.setLabel('title', 'Count' + str(count))

    #app.setLabel('title', btn)

    if btn == 'PRESS THIS BUTTON!':
        app.setFg('red')
    elif btn == 'PRESS ANOTHER BUTTON!':
        app.setFg('green')
    elif btn == 'PRESS THIS KIND OF BUTTON!':
        app.setFg('cyan')


    if count >=5:
        app.infoBox('You win!', 'You got the counter to 5!')

app = gui('Demo')

app.setBg('Orange')
app.setFg('White')
app.setFont(20)

app.addLabel('title','Hello world!')
app.addMessage('info', 'This is a simple demo of appJar capabilities.')

app.addButton('PRESS THIS BUTTON!', press)
app.addButton('PRESS ANOTHER BUTTON!', press)
app.addButton('PRESS THIS KIND OF BUTTON!', press)

app.go()