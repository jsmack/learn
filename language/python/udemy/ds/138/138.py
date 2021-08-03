import mysql.connector


#conn = mysql.connector.connect(host='127.0.0.1',user='root',password='')
#cur = conn.cursor()


#cur.execute(
#    'Create database test_mysql_database'
#)


conn = mysql.connector.connect(host='127.0.0.1', database='test_mysql_database')
cur = conn.cursor()

#cur.execute('create table person('
#            'id int not null auto_increment,'
#            'name varchar(14) not null,'
#            'PRIMARY key(id))')

#conn.commit()

cur.execute('insert into person(name) values("Mike")')
#conn.commit()
cur.execute('select * from person')
for row in cur:
    print(row)
print("###################")

cur.execute('update person set name = "Michel" where name ="Mike"')
cur.execute('select * from person')
for row in cur:
    print(row)
print("###################")
cur.execute('delete from person where name = "Michel"')
cur.execute('select * from person')

for row in cur:
    print(row)
print("###################")

cur.close()

cur.close()
conn.close()
