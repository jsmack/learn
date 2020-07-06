import sqlite3

#conn = sqlite3.connect('test_sqlite.db')

## in memory
conn = sqlite3.connect(':memory:')

curs = conn.cursor()

curs.execute(
    'create table persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)'
)
conn.commit()

curs.execute(
    'INSERT INTO persons(name) values("Mike")'
)
conn.commit()

curs.execute('select * from persons')
print(curs.fetchall())

curs.execute(
    'INSERT INTO persons(name) values("Nancy")'
)
curs.execute(
    'INSERT INTO persons(name) values("Jun")'
)
conn.commit()

curs.execute('UPDATE persons set name = "Michel" where name = "Mike"')
conn.commit()

curs.execute('DELETE FROM persons where name ="Michel"')
conn.commit()

curs.execute('select * from persons')
print(curs.fetchall())
curs.close()
conn.close()

