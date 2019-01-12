from appJar import gui

def press(button):
    if button == 'Выход':
        app.stop()
    elif button == 'ВВести':
        f = open('file.txt', "w+", encoding="utf-8")
        print(f)
app = gui("Текстовая программа", '1000x500')

app.addLabel('title', "Добро пожаловать в программу")
app.setLabelBg('title', 'green')

app.addLabelEntry('Введите текст')

app.addButtons(['Выход', 'ВВести'], press)

app.go()
f.close()
