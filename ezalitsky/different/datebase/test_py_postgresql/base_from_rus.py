import postgresql

db = postgresql.open('pq://egor:123@127.0.0.1:5432/mytestdb')
db.execute("CREATE TABLE emp (emp_name text PRIMARY KEY, emp_salary numeric)")

make_emp = db.prepare("INSERT INTO emp VALUES ($1, $2)")
raise_emp = db.prepare("UPDATE emp SET emp_salary = emp_salary + $2 WHERE emp_name = $1")
get_emp_with_salary_lt = db.prepare("SELECT emp_name FROM emp WHERE emp_salary < $1")

with db.xact():
    make_emp("Jone Doe", 150)
    make_emp("Jane Doe", 65)
    make_emp("Andrew Doe", 78)
    make_emp("Susan Doe", 22)
    make_emp("Mary Doe", 38)
    make_emp("Alex Doe", 89)

with db.xact():
    for row in get_emp_with_salary_lt(125):
        print(row["emp_name"])
        raise_emp(row["emp_name"], 10)