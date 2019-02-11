# импортим в код библиотеку postgresql для работы с базой данных postgresql
import postgresql

# создаем соединение с базой данной с указанием хоста, порта, логина и пароля
db = postgresql.open("pq://postgres:123456@localhost:5432/postgres")

print('Before')
# готовим select по табличке студенты
students = db.prepare("SELECT * FROM student")

# извлекаем студентов из бд и печатаем в консоль
for row in students:
    print(row)

# готовим DELETE по табличке студенты с условием по имени
sql_delete = db.prepare("DELETE FROM student WHERE first_name = $1")

# в транзакции удаляем из бд студентов с именем Иван и бросаем ошибку с собственным пояснением
# перехватываем ошибку и ничего не делаем.
# Этот код показывает работу в транзакии, изменения не зафиксируются пока весь код в транзакции не будет завершен без ошибок
try:
    with db.xact():
        sql_delete("Иван")
        raise Exception('Because we do raise in transaction, changes will not applied!')
except Exception:
    pass

# печатаем студентов. Список будет тот же что и выводом раньше, таким образом показываем что изменения не принялись, транзакция работает
print('After')
for row in students:
    print(row)