import postgresql
import random

# egor 123 mytestdb


connection = ''
table_name_people = ""
table_name_departments = ""
name_list = ["Frank", "John", "Bobby", "Rick", "Kim", "Lee", "Joe",
             "Andrew", "Pavel", "Alex", "George", "Martin"]
middle_name_list = ["Alex", "George", "Frank", "John", "Andrew", "Pavel",
                    "Martin" , "Bobby", "Rick", "Kim", "Lee", "Joe"]
last_name_list = ["Kunt", "Barbatos", "Putzer", "Milter", "Romanov", "Colter",
                  "Strabs", "Rodes", "Stephanson", "Wang", "Bucks", "Melliot"]
firm_list = ["GM", "Safe IT", "Miltown Technology", "Moto1 Co.", "Slikes Power Mashine", "Robot Company"]
specialisation_list = ["engineer", "programmer", "logistician", "developer", "erector", "tester"]
department_list = [1203, 2240, 512, 1044, 874, 579, 610, 93, 12, 2100, 45, 14]
city_list = ["New York", "Boston", "Seattle", "Chicago", "Denver", "Portland", "Milwaukee"]
description_list = ["Closed", "reorganized", "is moving", "perspective", "profitable"]


def create_new_table_people():
    id = 1
    point = input("Table with index or not ? yes/no \n")
    if point == "yes":
        db.prepare('''
            CREATE TABLE table_name_people (
                id integer, 
                first_name VARCHAR(100),
                last_name VARCHAR(100), 
                middle_name   VARCHAR(100), 
                firm VARCHAR(100), 
                specialisation VARCHAR(100))
            );      
              
            ALTER TABLE table_name_people ADD CONSTRAINT table_name_people_pk PRIMARY KEY (id);
            ''')
        while id < quantity:
            db.prepare('''
                INSERT INTO table_name_people VALUES (
                id, 
                random.choice(name_list), 
                random.choice(last_name_list), 
                random.choice(middle_name_list), 
                random.choice(firm_list), 
                random.choice(specialisation_list)
                )
            ''')
            id =+ 1
    elif point == "no":
        db.prepare('''CREATE TABLE table_name_people (
                   id integer, 
                   first_name VARCHAR(100), 
                   last_name VARCHAR(100), 
                   middle_name   VARCHAR(100), 
                   firm VARCHAR(100), 
                   specialisation VARCHAR(100)
                   )
                   ''')
        while id < quantity:
            db.prepare('''
                INSERT INTO table_name_people VALUES (
                id, 
                random.choice(name_list), 
                random.choice(last_name_list), 
                random.choice(middle_name_list), 
                random.choice(firm_list), 
                random.choice(specialisation_list)
                )
            ''')
            id = + 1
    else:
        print("Something went wrong )")

def create_new_table_departments():
    id = 1
    point = input("Table with index or not ? yes/no \n")
    if point == "yes":
        db.prepare('''
            CREATE TABLE table_name_departments (
                id integer, 
                department INTEGER, 
                city VARCHAR(255),
                description VARCHAR(600)
                );
            ALTER TABLE table_name_departments ADD CONSTRAINT table_name_departments_pk PRIMARY KEY (id);
        ''')

        while id < quantity:
            db.prepare('''
                       INSERT INTO table_name_people VALUES (
                       id, 
                       random.choice(department_list), 
                       random.choice(city_list), 
                       random.choice(description_list)
                       )
                       ''')
            id =+ 1
    elif point == "no":
        db.prepare('''
            CREATE TABLE table_name_departments (
                id integer, 
                department INTEGER, 
                city VARCHAR(255),
                description VARCHAR(600)
                );
        ''')
        while id < quantity:
            db.prepare('''
                       INSERT INTO table_name_people VALUES (
                       id, 
                       random.choice(department_list), 
                       random.choice(city_list), 
                       random.choice(description_list)
                       )
                       ''')
    else:
        print("Something went wrong )")

def connect():
    global db
    name = input("Input data base user : ")
    password = input("Input date base user password : ")
    db_name = input("Write your date base name")
    db =  postgresql.open('pq://' + name + ':' + '@' + connection + '/' + db_name)


choice = input(" Your data base is local (127.0.0.1:5432) ? (yes/no) \n")
if choice == "yes":
    connection = "127.0.0.1:5432"
    connect()
elif choice == "no":
    connection = input("Input your data base host connection. Format: [ip:port] (example: 8.8.8.8:5432).")
    connect()
else:
    print(" Your choise incorrect !")

flag = input("Would you like to create new table for people ? yes/no \n")
if flag == "yes":
    table_name_people = input("Write table name: ")
    quantity = int(input("Input quantity of items in people table (number):"))
    create_new_table_people()
elif flag == "no":
    flag = input("Would you like to create new table for department ? yes/no \n")
    if flag == "yes":
        table_name_departments = input("Write table name: ")
        quantity = int(input("Input quantity of items in department table (number):"))
        create_new_table_departments()
    elif flag == "no":
        print("Any new tables not created use old.")
    else:
        print("Incorrect input !")
else:
    print("Incorrect input !")




