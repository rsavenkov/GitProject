from appJar import gui

def press(button):
    if button == 'Выход':
        app.stop()
    elif button == 'Ввести':
        f = open('file.txt', "w+", encoding="utf-8")
        f.writelines(app.getEntry('Введите текст'))
        print(f)
        f.close()

app = gui("Текстовая программа", '1000x500')

app.addLabel('title', "Добро пожаловать в программу")
app.setLabelBg('title', 'green')

app.addLabelEntry('Введите текст')
app.addButtons(['Выход', 'Ввести'], press)

app.go()

