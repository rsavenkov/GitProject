import postgresql

db = postgresql.open("pq://postgres:040692@127.0.0.1:5432/Database")

# select_teachers=db.prepare('''SELECT teachers.first_name, teacher.id, count(students.*)''')

group_by = db.prepare('''
select  teachers.first_name, teachers.id, count(students.*)
  from student join teachers on students.teachers_id = teachers.id
group by teachers.id, teachers.first_name;

''')

for row in group_by:
    print(row)