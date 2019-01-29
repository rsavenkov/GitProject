

import postgresql

db = postgresql.open( "pq://paveldb:123@127.0.0.1:5432/paveldb" )

# db.execute("CREATE TABLE my_test (my_test_name text PRIMARY KEY, my_test_salary numeric)")
#
# make_my_test = db.prepare("INSERT INTO my_test VALUES ($1, $2)")
# raise_my_test = db.prepare("UPDATE my_test SET my_test_salary = my_test_salary + $2 WHERE my_test_name = $1")
lis = db.prepare( "SELECT * FROM students " )

# with db.xact():
# make_my_test("John Doe", 150)
# make_my_test("Jane Doe", 150)
# make_my_test("Andrew Doe", 55)
# make_my_test("Susan Doe", 60)
# make_my_test("Japhar Doe", 150)
# make_my_test("Kory Doe", 55)
# make_my_test("Samuel Doe", 60)

with db.xact():
    for row in lis:
        a = []
        for i in row:
            a.append( i )
        a = ''.join( map( str, [(a)] ) )
        print( a )

with open( 'C:/svn/untitled1/trunk/pvinogradov/database/23.txt', 'w+' )as f:
    for i in a:
        f.write( "%s/n" % i )
        # raise_my(row["my_test_name"], 10)

a = make_emp('  ')