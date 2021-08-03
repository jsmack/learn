import dbm


with dbm.open('cache', 'c') as db:
    db['key1'] = 'value1'
    db['key2'] = 'value2'

    # TypeError: dbm mappings have byte or string elements only
    # db['key3'] = 1

with dbm.open('cache', 'r') as db:
    print(db.get('key1'))