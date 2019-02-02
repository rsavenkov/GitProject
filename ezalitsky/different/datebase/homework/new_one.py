import postgresql


db = postgresql.open("pq://egor:1236@127.0.0.1:5432/mytestdb")

insert_table = db.prepare( '''

insert into test_table
values ($1, $2, $3, $4, $5, $6)

''')

param1 = 0
param2 = 0
param3 = 0
param4 = ""
param5 = ""
param6 = ""
i = 0
print("vvesti znacheniya")
count = int(input("vvedite scolko znacheniy (chislo): "))
while i < count:
    param1 = int(input("vvesti chislo 1:"))
    param2 = int(input("vvesti chislo 2:"))
    param3 = int(input("vvesti chislo 3:"))
    param4 = input("vvesti stroku 4:")
    param5 = input("vvesti stroku 5:")
    param6 = input("vvesti stroku 6:")
    print("---------------------------", i)
    i += 1
    with db.xact():
        insert_table(param1, param2, param3, param4, param5, param6)





