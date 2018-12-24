from appJar import gui
from ezalitsky.console_work_with_file.file_in_console import checkIsWinCorrectPath

def press(button):
    def Read():
        print(button)
        file = app.getEntry("file")
        result = checkIsWinCorrectPath(file)

        if result != 0:
            app.setEntryInvalid("file")
        else:
            with open(file, "r", encoding="utf-8") as f:
                f.readlines(app.getTextArea("text"))
        return print("read")

    def MakeFile():
        file = app.getEntry("file")
        result = checkIsWinCorrectPath(file)
        if result != 0:
            app.setEntryInvalid("file")
        else:
            with open(file, "w+", encoding="utf-8") as f:
                f.writelines(app.getTextArea("text"))

        return print("make")
    def Addfile():
        file = app.getEntry("file")
        result = checkIsWinCorrectPath(file)
        if result != 0:
            app.setEntryInvalid("file")
        else:
            with open(file, "a", encoding="utf-8") as f:
                f.writelines(app.getTextArea("text"))

    def Rewrite():
        file = app.getEntry("file")
        result = checkIsWinCorrectPath(file)
        if result != 0:
            app.setEntryInvalid("file")
        else:
            with open(file, "w", encoding="utf-8") as f:
                f.writelines(app.getTextArea("text"))

    def Savefile():
        pass

    switcher = {
        "Чтение файла": Read,
        "Создать файл": MakeFile,
        "Дополнить файл": Addfile,
        "Перезаписать файл": Rewrite,
        "Сохранить содержимое": Savefile
    }
    def switch(act):
        return switcher.get(act)
    switch(button)




app = gui("Программа работы с файлами: чтение, создание нового файла, запись, перезапись.", "900x400")
app.setBg("light green")
app.addValidationEntry("file")
app.setEntryDefault("file", "Полный путь с именем файла")
app.addTextArea("text", text=None)
app.setTextArea("text", "Введите текст", end=False, callFunction=False)
app.addButtons(["Чтение файла", "Создать файл", "Дополнить файл", "Перезаписать файл"], press)
app.addButtons(["Сохранить содержимое"], press)
app.go()
