# def g_hello():
#     yield 'hello 1'
#     yield 'hello 2'
#     yield 'hello 3'

def g_hello():
    while True:
        r = yield  'hello'
        yield r


g = g_hello()
print(next(g))
print(g.send('plus'))
print(next(g))
print(g.send('plus'))
print(g.send('plus'))
print(next(g))
