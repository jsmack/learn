import sqlite3
from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask import Response

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database',None)
    if db is None:
        db = g._database = sqlite3.connect('testsqlite.db')
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/employee', methods=['POST', 'PUT', 'DELETE'])
@app.route('/employee/<name>', methods=['GET'])
def employee(name=None):
    db = get_db()
    curs = db.cursor()
    curs.execute(
        'CREATE TABLE if NOT EXISTS persons( '
        'id integer primary key autoincrement, name string)'
    )
    db.commit()

    name = request.values.get('username', name)
    if request.method == 'GET':
        print('SELECT * from persons where name = "{}"'.format(name))
        curs.execute('SELECT * from persons where name = {}'.format(name))
        person = curs.fetchone()
        if not person:
            return "No", 404
        user_id, name = person
        return '{}:{}'.format(user_id,name), 200

    if request.method == 'POST':
        curs.execute('insert into persons(name) values("{}")'.format(name))
        db.commit()
        return 'Created {}'.format(name), 201

    if request.method == 'PUT':
        new_name = request.values['new_name']
        curs.execute('update persons set name = "{}" where name = "{}"'.format(
            new_name, name
        ))
        db.commit()
        return "updated {} {}".format(name,new_name) , 200

    if request.method == 'DELETE':
        curs.execute('DELETE from persons where name ="{}"'.format(name))
        db.commit()
        return 'deleted {}'.format(name), 200



@app.route('/')
def hello_world():
    return 'top'

@app.route('/hello')
@app.route('/hello/<username>')
def hello_world2(username=None):
    #return 'hello world2 {}'.format(username)

    return render_template('hello.html', username=username)

@app.route('/post', methods=['POST', 'PUT', 'DELETE'])
def show_post():
    return str(request.values['username'])


def main():
    app.debug =True
    app.run()
    #app.run(host='127.0.0.1', port=5000)

if __name__ == '__main__':
    main()