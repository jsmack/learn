print('s')
print((str('s')))
print(repr('s'))
print(type(repr('s')))

import datetime
d = datetime.datetime.now()
print(d)
print(str(d))
print(repr(d))

print('{!r} {} {!s}'.format('test1', 'test2', 'test3'))

class Point(object):
    def __init__(self,x ,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point<object>'
    def __str__(self):
        return 'Point ({}, {})'.format(self.x, self.y)


p = Point(100, 200)
print('{0!r}'.format(p))
print('{0}'.format(p))
print('{0!s}'.format(p))
