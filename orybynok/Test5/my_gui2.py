from typing import List, Any
from appJar import gui
import json

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
        print("Фамилия:", usr, "Паспорт:", pwd)

        with open(str(testn), 'a') as f_obj:
            json.dump(testn,f_obj)



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