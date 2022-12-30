
t = (1, 2, 3)
print('{0[0]}'.format(t))
print('{0[2]}'.format(t))
print('{t[2]}'.format(t=t))
print('{0}'.format(*t))

d = {'hoge': 'fuga', 'foo':'bar'}

print('{0[hoge]}'.format(d))

print('{:<30}'.format('left'))
print('{:>30}'.format('right'))
print('{:^30}'.format('center'))
print('{0:*^30}'.format('center'))
print('{name:*^30}'.format(name='center'))
print('{name:{fill}{align}{width}}'.format(name='center', fill='*', align='^', width=30))

print('{:,}'.format(123456789))
print('{:+f} {:+f}'.format(3.14, -3.14))

print('{:.2%}'.format(19/22))
print('{}'.format(19/22))

print(int(100), hex(100), oct(100), bin(100))
print('{0:d}, {0:x}, {0:o}, {0:b}'.format(100))
print('{0:d}, {0:#x}, {0:#o}, {0:#b}'.format(100))

for i in range(20):
    for base in 'bdx':
        print('{0:5{base}}'.format(i, base=base), end=' ')
    print('')
