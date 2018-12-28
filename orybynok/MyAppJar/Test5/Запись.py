from typing import List, Any
from appJar import gui
file_name = 'registration3.txt'
number = 'number3.txt'

testn = []
# handle button events

def press(button):
    if button == 'Очистить':
        app.stop()
    else:
        usr = app.getEntry("Фамилия")
        testn.append(usr)
        name = app.getEntry("Имя")
        testn.append(name)
        app.getLabelOptionBox("- Ваш Возраст -",["18-25","26-35","36-45","46-55+"], press)
        app.getLabelOptionBox("- Цель Визита -", ["Консультация",
                                     "Классический массаж", "СПА", "Медитация"], press)
        pwd = app.getAllOptionBoxes()
        testn.append(pwd)
        inf = app.getTextArea("Дополнительные сведения о себе")
        testn.append(inf)


        with open(file_name, 'a', encoding="utf-8") as f:
            f.write(str(testn)+'\n')

# content = f.read()

        with open(file_name, 'r', encoding='utf-8') as f:
            contents = f.read()
            print(contents)
            print("Подберите удобное для Вас время и место!")

# create a GUI variable called app
app = gui("Login Window", "380x400")
app.setBg("yellow")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Welcome to appJar")
app.setLabelBg("title", "blue")
app.setLabelFg("title", "yellow")

app.addLabelEntry("Фамилия")
app.addLabelEntry("Имя")
app.addLabelOptionBox("- Ваш Возраст -",["18-25","26-35","36-45","46-55+"])
app.addLabelOptionBox("- Цель Визита -", ["Консультация",
                                     "Классический массаж", "СПА", "Медитация"])
app.addScrolledTextArea("Дополнительные сведения о себе")

# link the buttons to the function called press


app.addButtons(["Ввод", 'Очистить',], press)

app.setFocus("Фамилия")


# start the GUI
app.go()