from appJar import gui
from random import randint

def press(button)
    app.clearLabel('title')
    app.setSize('fullscreen')
    a = randint(1, 17)
    app.setMessage('title', '� ������ "5" �������� �������� ��� ������� ' + str(a))



def press1(button):
    app.stop()
    print('�������, �� ����������')


app = gui('�������', '800x400')

app.setFont(20)
app.addLabel("title", "������� ������ �� ����������� ��� 11�")
#app.setLabelBg('title', 'orange')
app.addEmptyMessage('title')
app.addButton('�����!', press)
app.addButton('�����', press1)


app.go()
