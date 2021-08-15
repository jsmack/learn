# "is"  is equal object

a = 1
b = 1
print(f'1:{id(1)}, a:{id(a)}, b:{id(b)}')
print(f'a is b = {a is b}')
c = 2 -1
d = a
print(f'c is d = {c is d}')
b = 2
print(f'1:{id(1)}, a:{id(a)}, b:{id(b)}')

he = "he"
he2 = "h" + "e"

print(he is he2)


nothing = None

print(f'nothing is {nothing}')
print(f'nothing is None?=> {nothing is None}')