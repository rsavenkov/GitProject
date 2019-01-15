from appJar import gui
from rsavenkov.console import checkIsWinCorrectPath

def press1(button):
    file = app1.getEntry("file")
    with open(file, "w+", encoding="utf-8") as f:
        f.writelines(app1.getTextArea("text"))
    app.stop()

def press(button):
    file = app.getEntry("file")
    result = checkIsWinCorrectPath(file)
    if result != 0:
        app.setEntryInvalid("file")
    else:
        print("Попробуйте ещё раз")
        app.go()
    app.stop()
    #exit(-1)

app = gui("Оконная программа", "500x300")

app.addValidationEntry("file")
app.setEntryDefault("file", "Путь к файлу")
app.setFocus("file")
app.addButton("Сохранить имя файла", press)

app.go()

app1 = gui("Оконная программа", "700x400")

app1.addTextArea("text")
app1.addButton("Создать файл", press1)

app1.go()