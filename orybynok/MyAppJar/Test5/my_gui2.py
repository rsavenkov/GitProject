from typing import List, Any
from appJar import gui
import json
file_name = 'registration.txt'

testn = []
# handle button events

def press(button):
    if button == 'Очистить':
        app.stop()
    else:
        fileN = app.getEntry("Имя файла")
        testn.append(fileN)
        usr = app.getEntry("Фамилия")
        testn.append(usr)
        pwd = app.getEntry('Паспорт')
        testn.append(pwd)

        with open(file_name, 'a', encoding="utf-8") as f:
            f.write(str(testn))

        with open(file_name, 'r', encoding='utf-8') as f:
            contents = f.read()
            x = contents.count('Test')
            # content = f.read()
            print(contents)
            print(x)



# create a GUI variable called app
app = gui("Login Window", "400x400")
app.setBg("lightyellow")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Welcome to appJar")
app.setLabelBg("title", "lightblue")
app.setLabelFg("title", "lightyellow")

app.addLabelEntry("Имя файла")
app.addLabelEntry("Фамилия")
app.addLabelSecretEntry('Паспорт')
app.addScrolledTextArea(str(testn))
# link the buttons to the function called press


app.addButtons(["Ввод", 'Очистить',], press)

app.setFocus("Имя файла")


# start the GUI
app.go()