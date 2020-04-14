s = """\
AAA
BBB
CCC
DDD
"""

#with open('test.txt', 'w') as ff:
#    ff.write(s)

with open('test.txt', 'r') as f:
    print(f.tell())
    print(f.read(1))
    f.seek(5)
    print(f.read(1))