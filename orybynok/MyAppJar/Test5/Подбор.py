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
        app.getLabelOptionBox("-Время-",["10-12", "12-14", "14-16", "16-18", "18-20", "20-22"], press)
        app.getLabelOptionBox("-Место-", ["Полянка", "Тверская", "Митино", "Другое"], press)
        inf = app.getAllOptionBoxes()
        testn.append(inf)
        pl = app.getEntry("Ваш адрес")
        testn.append(pl)



        with open(file_name, 'a', encoding="utf-8") as f:
            f.write(str(testn)+'\n\n')

# content = f.read()

        with open(file_name, 'r', encoding='utf-8') as f:
            contents = f.read()
            lines = contents.splitlines()
            num_lines = int(len(lines))/3
            print(contents)
            print(num_lines)
            with open(number, 'w', encoding="utf-8") as f:
                f.write(str(num_lines))
            if  num_lines *3 %3 != 0:
                print("Вы не записались, повторите запись!")
            else:
                print("Спасибо, что Вы обратились к нам. Мы Вас ждём!")

# create a GUI variable called app
app = gui("Галина Рыбынок", "270x400")
app.setBg("yellow")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Добро пожаловать !!")
app.setLabelBg("title", "blue")
app.setLabelFg("title", "yellow")

app.addLabelOptionBox("-Месяц-",["Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"])
app.addLabelOptionBox("-Дата- ",["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"])
app.addLabelOptionBox("-Время-",["10-12", "12-14", "14-16", "16-18", "18-20", "20-22"])
app.addLabelOptionBox("-Место-",["Полянка", "Тверская", "Митино", "Другое"])
app.addEntry("Ваш адрес")
# link the buttons to the function called press


app.addButtons(["Отправить", 'Очистить',], press)



# start the GUI
app.go()