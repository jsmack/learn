import memcache
import sqlite3
import time

db = memcache.Client(['127.0.0.1:11211'])

# time = cache alive time
db.set('web_page', 'value1', time=1)
#time.sleep(2)
print(db.get('web_page'))

db.set('counter', 0)
db.incr('counter',1)
db.incr('counter',1)
db.incr('counter',1)

print(db.get('counter'))

conn = sqlite3.connect('test_sqlite2.db')
curs = conn.cursor()
#curs.execute(
#             'create table persons('
#             'employ_id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')
#curs.execute('INSERT INTO persons(name) values("Mike")')
#conn.commit()
#conn.close()

def get_employ_id(name):
    employ_id = db.get(name)
    if employ_id:
        return employ_id
    else:
        curs.execute(
            'SELECT * from persons where name = "{}"'.format(name)
        )
        person = curs.fetchone()
        if not person:
            raise Exception('No employ')
        employ_id, name = person
        db.set(name, employ_id, time=60)
        return employ_id

print(get_employ_id("Mike"))