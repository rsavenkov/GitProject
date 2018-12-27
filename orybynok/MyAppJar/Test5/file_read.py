file_name = 'registration.txt'


with open(file_name, 'r', encoding='utf-8') as f:
    contents = f.read()
    print(contents)


    if 'Test1'and'Oleg'and'0209' in contents:
        print('True')
    else:
        print('False')

from appJar import gui

app=gui()
app.setFont(20)
app.addLabelOptionBox("Options", ["- Fruits -", "Apple", "Orange",
                        "Pear", "kiwi", "- Pets -", "Dogs", "Cats",
                        "Fish", "Hamsters"])
app.go()