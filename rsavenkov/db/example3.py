import postgresql

db = postgresql.open("pq://postgres:123456@localhost:5432/postgres")

print('Before')
students = db.prepare("SELECT * FROM student")

for row in students:
    print(row)

sql_delete = db.prepare("DELETE FROM student WHERE first_name = $1")

try:
    with db.xact():
        sql_delete("Иван")
        raise Exception('Because we do raise in transaction, changes will not applied!')
except Exception:
    pass

print('After')
for row in students:
    print(row)