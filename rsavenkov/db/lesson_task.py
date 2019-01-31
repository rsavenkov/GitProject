import postgresql

db = postgresql.open("pq://egor:1236@127.0.0.1:5432/mytestdb")

insert_teacher = db.prepare ('''
INSERT INTO teacher
VALUES ($1, $2, $3, $4, $5, $6);

''')

insert_teacher(2, 'new teacher 2', 'new teacher 2', None, True, 'New student for teacher 2' )

insert_student = db.prepare('''
INSERT INTO student
VALUES ($1, $2, $3, $4, $5, $6, $7, $8);
 ''')

i = 1
while 1 <= 3:
    insert_student(16 + i, 's'+ str(i), "s" + str(i), None, True, 'New student for teacher 2', 100, 2)
    i += 1

group_by = db.prepare('''
SELECT teacher_id, count(*)
from student  
group by teacher_id;

''')
for row in group_by:
    print(row)