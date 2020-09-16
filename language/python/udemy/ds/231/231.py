import collections


od = collections.OrderedDict(
    {'banana': 3, 'apple': 4, 'peer': 1, 'orange': 2}
)
od2 = collections.OrderedDict(
    {'banana': 3, 'apple': 4, 'orange': 1, 'peer': 2}
)

d = {'banana': 3, 'apple': 4, 'peer': 1, 'orange': 2}
print(d)
print(d == od)
print(od == od2)


odd = collections.OrderedDict(
    sorted(d.items(), key=lambda t: t[0])
)

print(odd)


odd2 = collections.OrderedDict(
    sorted(d.items(), key=lambda t: t[1])
)
print(odd2)

odd3 = collections.OrderedDict(
    sorted(d.items(), key=lambda t: len(t[0]))
)
print(odd3)


od['cc'] = 100
print(od)

od = collections.OrderedDict(
    sorted(od.items(), key=lambda t: t[0])
)
print(od)