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

        app.getLabelOptionBox("-Месяц-",["Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"], press)
        app.getLabelOptionBox("-Дата- ",["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"], press)
        app.getLabelOptionBox("-Время-",["10-12", "12-14", "14-16", "16-18", "18-20", "20-22", "Июль", "Август", "Сентябрь"], press)
        inf2 = app.getAllOptionBoxes()
        testn.append(inf2)
        inf1 = app.getTextArea("Дополнительные сведения о своих желаниях")
        testn.append(inf1)

        with open(file_name, 'a', encoding="utf-8") as f:
            f.write(str(testn)+'\n')

# content = f.read()

        with open(file_name, 'r', encoding='utf-8') as f:
            contents = f.read()
            print(contents)
        with open(number, 'r', encoding="utf-8") as f:
            y = f.read()
            print(y)

# create a GUI variable called app
app = gui("Login Window", "270x400")
app.setBg("yellow")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Welcome to appJar")
app.setLabelBg("title", "blue")
app.setLabelFg("title", "yellow")

app.addLabelOptionBox("-Месяц-",["Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"])
app.addLabelOptionBox("-Дата- ",["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"])
app.addLabelOptionBox("-Время-",["10-12", "12-14", "14-16", "16-18", "18-20", "20-22"])
app.addScrolledTextArea("Дополнительные сведения о своих желаниях")
# link the buttons to the function called press


app.addButtons(["Отправить", 'Очистить',], press)



# start the GUI
app.go()