import postgresql


db = postgresql.open("pq://egor:1236@127.0.0.1:5432/mytestdb")


db.prepare('''
INSERT into public.students (ident, first_name, middle_name, last_name, male, birthday, description, teacher_id)
VALUES (14, 'XXX', 'AAAA', 'CCCC', false, '2001-03-31 18:00:54.508000', 'ddddd', 1);
''')

db.prepare('''
INSERT into public.students (ident, first_name, middle_name, last_name, male, birthday, description, teacher_id)
VALUES (22, 'bbb', 'AAdd', 'CaddasCCC', true , '2001-03-31 18:00:54.508000', 'ddddasddadasddd', 2);
''')

db.prepare("""
INSERT INTO public.teacher (id, first_name, last_name, birthday_date, gender, description) 
VALUES (5, 'Ruslan2', 'Savenkov', '1987-04-24 00:00:00.000000', true, 'teaches python');
""")

