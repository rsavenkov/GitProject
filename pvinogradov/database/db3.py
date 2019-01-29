import postgresql.driver as pg_driver

db = pg_driver.connect( user='postgres', password='123', host='127.0.0.1', database='paveldb', port=5432 )
for Films in db.prepare( "SELECT films FROM public.films " ):
    print(Films)