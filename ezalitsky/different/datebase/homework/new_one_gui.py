from appJar import gui
import postgresql

app = gui('Add datebase', '500x300')

db = postgresql.open("pq://egor:1236@127.0.0.1:5432/mytestdb")

# def menuPress():
#     pass
#
# fileMenus = ["Open", "Save", "Save as...", "-", "Export", "Print", "-", "Close"]
# app.addMenuList("File", fileMenus, menuPress)

def press(btn):

    if btn == 'Cancel':
        app.stop()
        print( 'Finish')
    elif btn == 'Add database':
        name = app.getEntry('name1')
        surname = app.getEntry('SurName1')
        age = int(app.getEntry('Age'))

        ochered = db.prepare('''

        insert into ochered
        values ($1, $2, $3)

        ''')
        ochered(name, surname, age)
    elif btn == 'Show':
        table = db.prepare('''
                           select  *
                           from ochered; 
                           ''')
        for row in table:
            print(row)
            app.addMessage(row)

app.addLabel( 'title', '        Hello please add values datebase ' )
app.setLabelFg( "title", "#00FA9A" )

tools = ["ABOUT", "REFRESH", "OPEN", "CLOSE", "SAVE",
        "NEW", "SETTINGS", "PRINT", "SEARCH", "UNDO",
        "REDO", "PREFERENCES", "HOME", "HELP", "CALENDAR",
        "WEB", "OFF"]

app.addToolbar(tools, press, findIcon=True)

app.addEntry( 'name1', column=0, row=0 )
app.setEntryDefault("name1", "Name")

app.addEntry( 'SurName1', column=0, row=1 )
app.setEntryDefault("SurName1", "Surname")

app.addEntry( 'Age', column=0, row=2 )
app.setEntryDefault("Age", "Age")

app.buttons(["Add database", "Show", "Cancel"], press)

# a = 'wqe'
# def changeLabel(btn,*args):
#     pass
#
#
# app.addLabel("l1", "Simple Demo")
# app.addEntry("text")
# app.addButton("OK", changeLabel)
# app.addEmptyLabel("l2")
# app.addStatusbar(fields=3)
# app.setStatusbar("Line: 20", 0)
# app.setStatusbar("Column: 4", 1)
# app.setStatusbar("Mode: Edit", 2)
# app.go()
#
# app.setBg('green')
# app.setFont(15)

app.go()

