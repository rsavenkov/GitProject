import sqlite3

conn = sqlite3.connect( 'employee12.db' )
#
c = conn.cursor()
# c.execute( """CREATE table employees(
#             first text,
#             last text,
#             pay integer)""" )
# c.execute("INSERT INTO employee12 VALUES ('C1orey', 'Shqfer', 50000)")
# conn.commit()
# c.execute("SELECT * FROM employees WHERE  last='Shafer'")
# print(c.fetchall() )
conn.commit()
conn.close()
