import postgresql

db = postgresql.open('pq://egor:123@127.0.0.1:5432/mytestdb')
get_emp_with_salary_lt = db.prepare("SELECT * FROM mytestdb.probe.comp_shop INNER JOIN mytestdb.probe.assembly ON (mytestdb.probe.comp_shop.identifire = mytestdb.probe.assembly.identifire);")

with db.xact():
    with open(
            r'C:\Users\Xiaomi\Documents\Exploit_directories\Python\PycharmProjects\GitProject\ezalitsky\different\datebase\my_db_table2',
            "w+", encoding="utf-8") as f:
        for row in get_emp_with_salary_lt:
                f.writelines(str(row))
                f.writelines('\n')


