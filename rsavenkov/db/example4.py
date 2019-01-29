import postgresql
from time import time

db = postgresql.open("pq://postgres:123456@localhost:5432/postgres")

'''
Функция которая инсертит в базу в различные таблички по параметру
'''
def insert_into_table(table_name):
    insert = 'INSERT INTO table_with{}_index VALUES ($1, $2, $3, $4)'.format(table_name)
    insert_into_table = db.prepare(insert)

    i = 1
    while i < 10 * 1000:
        insert_into_table(i, 'some text - ' + str(i), 'some text -- ' + str(i), 'some text --- ' + str(i))
        i += 1

# создаем в транзации две таблички и наполняем их данными
with db.xact():
    no_index = db.execute('''
CREATE TABLE table_without_index (
    id integer,
    some_field1 VARCHAR,
    some_field2 VARCHAR,
    some_field3 VARCHAR
);
''')

    yes_index = db.execute('''
CREATE TABLE table_with_index (
    id integer,
    some_field1 VARCHAR,
    some_field2 VARCHAR,
    some_field3 VARCHAR
);

ALTER TABLE table_with_index ADD CONSTRAINT table_with_index_pk PRIMARY KEY (id);
''')

    # для таблички с индексом
    insert_into_table('')
    # для таблички без индексом
    insert_into_table('out')

start = time()
db.prepare('SELECT * FROM table_without_index WHERE id = 5678;')
end = time()
print('Select from table without index by id is: ' + str(end - start))

start = time()
db.prepare('SELECT * FROM table_with_index WHERE id = 5678;')
end = time()
print('Select from table without index by id is: ' + str(end - start))
