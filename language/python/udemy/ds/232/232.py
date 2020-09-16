import re

m = re.match('a.c', 'abc')
print(m)
print(m.group())

s = re.search('a.c', 'test abc')
print(s)
print(s.span())
print(s.group())


fa = re.findall('a.c', 'test abc test abc')
print(fa)
fi = re.finditer('a.c', 'test abc test abc')
print([w.group() for w in fi])

print(re.match('a{2,4}', 'aaa'))
print(re.match('[a-zA-Z0-9_]', 'x'))
print(re.match('[^a-zA-Z0-9_]', 'x')) # not alphanumeric
print(re.match('\w', 'x'))   # alphanumeric and _
print(re.match('\W', '@'))   # not alphanumeric

print(re.match('[0-9]', '1'))
print(re.match('\d', '1'))
print(re.match('\D', '1'))
print(re.match('a|b', 'a')) # or
print(re.match('(abc)+', 'abc')) # () grouping
print(re.match('\s', ' '))

