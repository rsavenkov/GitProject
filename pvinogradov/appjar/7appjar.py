from appJar import gui


def press(btn):
    if btn == 'Draw':
        a = app.getTurtleScreen('t1')
        b = app.getTurtle('t1')
        a.bgcolor('blue')
        b.pencolor('red')
        for i in range(20):
            b.forward(i * 10)
            b.left(144)
    elif btn == 'Out':
        app.stop()


app = gui('Label', '500x500')
app.addTurtle('t1')
app.addButtons(['Draw', 'Out'], press)
app.go()
