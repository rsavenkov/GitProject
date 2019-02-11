# импортим в код библиотеку postgresql для работы с базой данных postgresql
import postgresql

# создаем соединение с базой данной с указанием хоста, порта, логина и пароля
db = postgresql.open("pq://egor:1236@127.0.0.1:5432/mytestdb")

# готовим sql для добавления в табличку учителей запись
insert_teacher = db.prepare('''
INSERT INTO teacher
VALUES ($1, $2, $3, $4, $5, $6);
''')

# добавлем учителя в табличку
insert_teacher(2, 'new teacher 2', 'new teacher 2', None, True, 'New student for teacher 2' )

# готовим sql для добавления в табличку студентов запись
insert_student = db.prepare('''
INSERT INTO student
VALUES ($1, $2, $3, $4, $5, $6, $7, $8);
 ''')

# добавляем 3-х студентов
i = 1
while 1 <= 3:
    insert_student(16 + i, 's'+ str(i), "s" + str(i), None, True, 'New student for teacher 2', 100, 2)
    i += 1

# готовим sql с group by для того чтобы вывести id учителя и кол-во студентов привязанных к нему
group_by = db.prepare('''
SELECT teacher_id, count(*)
from student  
group by teacher_id;
''')

# выводим результаты предыдущего sql
for row in group_by:
    print(row)