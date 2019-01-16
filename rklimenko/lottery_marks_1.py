from appJar import gui
from random import randint

def press(button):
    app.clearLabel('title')
    app.setSize('fullscreen')
    a = randint(1, 17)
    app.setMessage('title', 'И оценку "5" получает учащийся под номером ' + str(a))



def press1(button):
    app.stop()
    print('Кажется, вы испугались')


app = gui('Лотерея', '800x400')

app.setFont(20)
app.addLabel("title", "Лотерея оценок по информатике для 11Т")
#app.setLabelBg('title', 'orange')
app.addEmptyMessage('title')
app.addButton('Вперёд!', press)
app.addButton('Назад', press1)


app.go()
