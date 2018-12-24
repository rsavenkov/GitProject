from appJar import gui
from ezalitsky.console_work_with_file.file_in_console import checkIsWinCorrectPath

def press(button):
    def Read():
        file = app.getEntry("file")
        result = checkIsWinCorrectPath(file)

        if result != 0:
           return app.setEntryInvalid("file")
        else:
            with open(file, "r", encoding="utf-8") as f:
                f.read(app.show("file"))
                # f.readlines(app.TextArea("text"))

    def MakeFile():
        file = app.getEntry("file")
        result = checkIsWinCorrectPath(file)
        if result != 0:
            app.setEntryInvalid("file")
        else:
            with open(file, "w", encoding="utf-8") as f:
                f.writelines(app.getTextArea("text"))

    def Addfile():
        file = app.getEntry("file")
        result = checkIsWinCorrectPath(file)
        if result != 0:
            app.setEntryInvalid("file")
        else:
            with open(file, "a", encoding="utf-8") as f:
                f.writelines(app.getTextArea("text"))

    def Quit():
        app.stop()

    switcher = {
        "Чтение файла": Read,
        "Создать/перезаписать файл": MakeFile,
        "Дополнить файл": Addfile,
        "Выход": Quit
    }
    def switch(act):
        return switcher.get(act)
    switch(button)()


app = gui("Программа работы с файлами: чтение, создание нового файла, запись, перезапись.", "900x400")
app.setBg("green")
app.addValidationEntry("file")
app.setEntryDefault("file", "Полный путь с именем файла")
app.addTextArea("text")
app.setTextArea("text", "Введите текст")
app.addButtons(["Чтение файла", "Создать/перезаписать файл", "Дополнить файл"], press)
app.addButtons(["Выход"], press)
app.go()
