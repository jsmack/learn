import happybase

con = happybase.Connection('localhost')

con.open()

con.create_table(b'sns2', {'blog': dict()})
table = con.table(b'sns2')

table.put(
    b'user1', {
        b'blog:bitcoin': b'user1 about bitcoin',
        b'blog:soccer': b'user1 about soccer'
    }
)

table.put(
    b'user2', {
        b'blog:soccer': b'user2 about soccer'
    }
)

print(list(table.scan()))
print("#######")
print(list(table.scan(row_prefix=b'user1')))
print("#######")
print(list(table.scan(columns=[b'blog:soccer'])))

con.disable_table(b'sns')
con.delete_table(b'sns')