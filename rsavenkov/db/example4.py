# импортим в код библиотеку postgresql для работы с базой данных postgresql
import postgresql
# импортим библиотеку time для работы со временем
from time import time

# создаем соединение с базой данной с указанием хоста, порта, логина и пароля
db = postgresql.open("pq://postgres:123456@localhost:5432/postgres")

'''
Функция которая инсертит в базу в различные таблички по параметру
'''
def insert_into_table(table_name):
    # объявляем параметризированную строку-insert которую потом будем готовить в качестве sql на выполнение
    insert = 'INSERT INTO table_with{}_index VALUES ($1, $2, $3, $4)'.format(table_name)
    # готовим ее как sql на выполнение
    insert_into_table = db.prepare(insert)

    # в цикле 10000 раз добавляем строку в таблицу с различными значениями
    i = 1
    while i < 10 * 1000:
        insert_into_table(i, 'some text - ' + str(i), 'some text -- ' + str(i), 'some text --- ' + str(i))
        # не забываем про инкремент счетчика чтобы выйти из цикла!
        i += 1

# создаем в транзации две таблички и наполняем их данными
# одна табличка с индексом по полю id, другая без
# последний ddl ALTER как раз создает индекс
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

    # вызываем нашу функцию для добавления записей в табличку с индексом
    insert_into_table('')
    # вызываем нашу функцию для добавления записей в табличку без индексом
    insert_into_table('out')

# засекаем время выполнения select по полю id по табличке с индексом
start = time()
db.prepare('SELECT * FROM table_without_index WHERE id = 5678;')
end = time()
print('Select from table without index by id is: ' + str(end - start))

# засекаем время выполнения select по полю id по табличке без индексом
start = time()
db.prepare('SELECT * FROM table_with_index WHERE id = 5678;')
end = time()
print('Select from table without index by id is: ' + str(end - start))

# пример показывает насколько разнИца время выполнения select-ов по табличкам с индексом и без индекса. РАзница огромная, несколько порядков
# При этом разница увеличивается с увеличением количества строк в таблицах