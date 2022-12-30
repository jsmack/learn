import re

#s = 'My name is Mike'
s = 'My name is ... Mike'

print(s.split())

p = re.compile(r'\W+')
print(p.split(s))

p1 = re.compile('(blue|white|red)')
print(p1.sub('color', 'blue socks and red shoes'))
print(p1.sub('color', 'blue socks and red shoes', count=1))
print(p1.subn('color', 'blue socks and red shoes'))

def hexrepl(match):
    value = int(match.group())
    return hex(value)

p2 = re.compile(r'\d')
print(p2.sub(hexrepl, '12345 55 11 test hoge3 2390'))