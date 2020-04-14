s = """\
AAA
BBB
CCC
DDD
"""

#with open('test.txt', 'w') as ff:
#    ff.write(s)

with open('test.txt', 'r') as f:
    #print(f.read())
    while True:
        chunk = 2
        #line = f.readline()
        line = f.read(chunk)
        #print(line, end='')
        print(line)
        if not line:
            break
