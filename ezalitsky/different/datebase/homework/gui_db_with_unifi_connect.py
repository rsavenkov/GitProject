from appJar import gui
import postgresql

app = gui('Add datebase', '500x300')

def connect():
    global db
    name = input("Input data base user : ")
    password = input("Input date base user password : ")
    db_name = input("Write your date base name")
    db =  postgresql.open('pq://' + name + ':' + '@' + connection + '/' + db_name)
    return db

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
            app.message(row)

# made unifi connection to db

choice = input(" Your data base is local (127.0.0.1:5432) ? (yes/no) \n")
if choice == "yes":
    connection = "127.0.0.1:5432"
    connect()
elif choice == "no":
    connection = input("Input your data base host connection. Format: [ip:port] (example: 8.8.8.8:5432) :")
    connect()
else:
    print(" Your choise incorrect !")


# gui construckt

app.addEntry( 'name1', column=0, row=0 )
app.setEntryDefault("name1", "Name")

app.addEntry( 'SurName1', column=0, row=1 )
app.setEntryDefault("SurName1", "Surname")

app.addEntry( 'Age', column=0, row=2 )
app.setEntryDefault("Age", "Age")

app.buttons(["Add database", "Show", "Cancel"], press)

app.go()