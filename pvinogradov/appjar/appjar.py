from tkinter import *  #
from tkinter import messagebox  #
from tkinter import ttk  #

import postgresql
from appJar import gui

app = gui( 'Add datebase', '710x300' )

db = postgresql.open( "pq://postgres:123@127.0.0.1:5432/paveldb" )


def menuPress(btn):
    if btn == 'Calculator':
        root = Tk()
        root.title( 'Calculiator' )

        def calc(key):
            if key == "=":
                str1 = "//%-+1234567890./*"
                if calc_entry.get()[0] not in str1:
                    calc_entry.insert( END, " The first character is not a number" )
                    messagebox.showerror( "Mistake!!! you entered not a number" )

                try:
                    result = eval( calc_entry.get() )
                    calc_entry.delete( 0, END )
                    calc_entry.insert( END, str( result ) )
                except:
                    calc_entry.insert( END, " Mistake!" )
                    messagebox.showerror( 'Error ', ' check data validity' )

            elif key == "c":
                calc_entry.delete( 0, END )

            elif key == '-/+':
                if '=' in calc_entry.get():
                    calc_entry.delete( 0, END )
                try:
                    if calc_entry.get()[0] == '-':
                        calc_entry.delete( 0 )
                    else:
                        calc_entry.insert( 0, '-' )
                except IndexError:
                    pass
            else:
                if '=' in calc_entry.get():
                    calc_entry.delete( 0, END )
                calc_entry.insert( END, key )

        bttn_list = [
            '7', '8', '9', '+', '-',
            '4', '5', '6', '*', '/',
            '1', '2', '3', '-/+', '=',
            '0', '.', 'c', '//', '%',
        ]
        r = 1
        c = 0
        for i in bttn_list:
            cmd = lambda x=i: calc( x )
            ttk.Button( root, text=i, command=cmd ).grid( row=r, column=c, sticky=E )
            c += 1

            if c > 4:
                c = 0
                r += 1

        calc_entry = Entry( root, width=50, borderwidth=5 )

        calc_entry.grid( row=0, column=0, columnspan=5 )
        root.mainloop()



#     app.setBg("green")
#     app.setFont(18)



def press1(btn):
    if btn == "OFF":
        app.stop()
        print('The End')


def press(btn):
    if btn == 'Cancel':
        app.stop()
        print( 'Finish' )
    elif btn == 'Add database':
        name = app.getEntry( 'name1' )
        surname = app.getEntry( 'SurName1' )
        age = int( app.getEntry( 'Age' ) )

        ochered = db.prepare( '''

        insert into ochered
        values ($1, $2, $3)

        ''' )
        ochered( name, surname, age )
    elif btn == 'Show':
        app.setFg( '#ff0066' )
        table = db.prepare( '''
                           select  *
                           from ochered; 
                           ''' )
        # a = []

        for row in table:
            # a.append( row )
            print( row )
            app.addMessage( row )
    elif btn == 'NUMBER OF PEOPLE':
        print('123')
        app.setFg( '#ff0066' )
        table1 = db.prepare( '''
                                   select  COUNT ("age")
                                   from ochered; 
                                   ''' )
        for i in table1:
            app.addMessage('Total number of people' + str(i))

    elif btn == 'Reset':
        a1.delete( [0], END )
        a2.delete( [0], END )
        a3.delete( [0], END )
        # menu()



# this is a pop-up


app.addLabel( 'title', '        Hello please add values datebase ' )
app.setLabelFg( "title", "#00FA9A" )

tools = ["ABOUT", "REFRESH", "OPEN", "CLOSE", "SAVE",
         "NEW", "SETTINGS", "PRINT", "SEARCH", "UNDO",
         "REDO", "PREFERENCES", "HOME", "HELP", "CALENDAR",
         "WEB", "OFF"]

app.addToolbar( tools, press1, findIcon=True )

a1 = app.addEntry( 'name1', column=0, row=0 )
app.setEntryDefault( "name1", "Name" )

a2 = app.addEntry( 'SurName1', column=0, row=1 )
app.setEntryDefault( "SurName1", "Surname" )

a3 = app.addEntry( 'Age', column=0, row=2 )
app.setEntryDefault( "Age", "Age" )

app.buttons( ["Add database", "Show", "Cancel", "Reset",'NUMBER OF PEOPLE'], press )

# def menu():

fileMenus = ["Open", "Save", "Save as...", "-", "Export", "Print", "-", "Close"]
app.addMenuList( "File", fileMenus, menuPress )
fileMenus1 = ['Calculator']
app.addMenuList( "Tools", fileMenus1, menuPress )
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
app.setBg('#0000ff')
app.setFont(14)

app.go()
