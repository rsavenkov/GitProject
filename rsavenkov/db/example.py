# импортим в код библиотеку postgresql для работы с базой данных postgresql
import postgresql

# создаем соединение с базой данной my_db по адресу хост 127.0.0.1, порт 5432, логин postgres, пароль G24O02d24230303
db = postgresql.open("pq://postgres:G24O02d24230303@127.0.0.1:5432/my_db")
# выполяем ddl sql который создает табличку emp с полями emp_name и emp_salary
db.execute("CREATE TABLE emp (emp_name text PRIMARY KEY, emp_salary numeric)")

# готовим dml sql добавления записи в табличку emp
make_emp = db.prepare("INSERT INTO emp VALUES ($1, $2)")
# готовим dml sql обновления записи в табличке emp
raise_emp = db.prepare("UPDATE emp SET emp_salary = emp_salary + $2 WHERE emp_name = $1")
# готовим dml sql выбора записей из таблички emp
get_emp_with_salary_lt = db.prepare("SELECT emp_name FROM emp WHERE emp_salary < $1")

# в транзакции 4 раза выполняем INSERT в таличку emp со значениями
with db.xact():
    make_emp("John Doe", 150)
    make_emp("Jane Doe", 150)
    make_emp("Andrew Doe", 55)
    make_emp("Susan Doe", 60)

# в транзакции в цикле извлекаем из таблички emp записи по условию зарплата < 125
# при извлечении каждой строчки печатаем имя сотрудника и выполняем обновление данных по зп этого сотрудника на 10
with db.xact():
    for row in get_emp_with_salary_lt(125):
        print(row["emp_name"])
        raise_emp(row["emp_name"], 10)