from appJar import gui

def press(button):
    if button == 'Cancel':
        app.stop()
    else:
        usr = app.getEntry('Username')
        pwd = app.getEntry('Password')
        print('User', usr, 'Pass', pwd)


app = gui('Login Window', '400x200')
app.setBg('orange')
app.setFont(18)

app.addLabel('title', 'Welcome to appJar')
app.setLabel('title', 'blue')
app.setLabel('title', 'orange')

app.addLabelEntry('Username')
app.addLabelSecretEntry('Password')

app.addButtons(['Sumbit', 'Cancel'], press)
app.setFocus('Username')

app.go()